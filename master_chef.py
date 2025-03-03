import streamlit as st
import sys
import os
import json
from datetime import datetime
import pandas as pd
import base64
from fpdf import FPDF
import re
from tools.suggest_menu import suggest_menu
from utils.menus_operations import get_recent_menus, display_menu
from utils.pdf_operations import create_pdf
from models.generate_recipes import generate_recipes
from models.generate_shopping_list import generate_shopping_list
from models.suggest_drinks import suggest_drinks

# Add the project root to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import your modules
from models.menu_generator import generate_menu
from database.db import insert_menu, get_connection
from smolagents import CodeAgent, HfApiModel

# Initialize the agent for additional features
agent = CodeAgent(tools=[suggest_menu], model=HfApiModel())

# Set page configuration
st.set_page_config(
    page_title="Master Chef AI",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-family: 'Helvetica Neue', sans-serif;
        color: #1E1E1E;
        text-align: center;
        padding-bottom: 20px;
        border-bottom: 2px solid #FF5733;
        margin-bottom: 30px;
    }
    .subheader {
        font-family: 'Helvetica Neue', sans-serif;
        color: #FF5733;
        font-weight: 600;
    }
    .menu-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .sidebar-header {
        font-family: 'Helvetica Neue', sans-serif;
        color: #FF5733;
        text-align: center;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .generate-button {
        background-color: #FF5733;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        border: 1px solid #ddd;
        padding: 10px;
    }
    .info-box {
        background-color: #e8f4f8;
        border-left: 5px solid #4c92d3;
        padding: 15px;
        border-radius: 5px;
    }
    .category-label {
        font-weight: bold;
        color: #FF5733;
        margin-top: 10px;
    }
    .stDownloadButton {
        color: white;
        background-color: #4CAF50;
        padding: 10px 20px;
        border-radius: 5px;
        text-decoration: none;
        display: inline-block;
        margin: 4px 2px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)


def get_download_link(pdf_bytes, filename):
    """Generate a download link for the PDF"""
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}" class="stDownloadButton">📥 Download PDF</a>'
    return href

def main():
    # Initialize session state for storing data between reruns
    if 'menu' not in st.session_state:
        st.session_state.menu = None
    if 'occasion' not in st.session_state:
        st.session_state.occasion = ""
    if 'shopping_list' not in st.session_state:
        st.session_state.shopping_list = None
    if 'recipes' not in st.session_state:
        st.session_state.recipes = None
    if 'drinks' not in st.session_state:
        st.session_state.drinks = None
    
    # Sidebar content
    with st.sidebar:
        st.markdown("<h2 class='sidebar-header'>🧑‍🍳 Master Chef AI</h2>", unsafe_allow_html=True)
        st.markdown("---")
        
        st.markdown("### About")
        st.markdown("""
        Master Chef AI helps you plan perfect menus for any occasion. 
        Just enter your event type, and our AI will generate a customized menu.
        """)
        
        st.markdown("---")
        
        st.markdown("### Recent Menus")
        recent_menus = get_recent_menus()
        
        if recent_menus:
            for menu in recent_menus:
                with st.expander(f"{menu['occasion']} ({menu['created_at'][:10]})"):
                    display_menu(menu['menu'])
        else:
            st.write("No recent menus found.")
            
        st.markdown("---")
        st.markdown("### Tips")
        st.markdown("""
        - Be specific about your occasion
        - Mention dietary preferences
        - Include cultural preferences
        - Specify the number of guests
        """)

    # Main content area
    st.markdown("<h1 class='main-header'>🍽️ AI-Based Menu Designer</h1>", unsafe_allow_html=True)
    
    # Two-column layout for input
    col1, col2 = st.columns([3, 1])
    
    with col1:
        occasion = st.text_input("What's the occasion?", 
                                placeholder="e.g., Birthday dinner for 10 people, vegetarian options",
                                value=st.session_state.occasion)
    
    with col2:
        st.write("")
        st.write("")
        generate_button = st.button("Generate Menu 🧠", use_container_width=True)
    
    # Generate menu based on input
    if generate_button and occasion:
        with st.spinner("Chef is thinking... 🤔"):
            menu = generate_menu(occasion)
            st.session_state.menu = menu
            st.session_state.occasion = occasion
            # Reset additional features
            st.session_state.shopping_list = None
            st.session_state.recipes = None
            st.session_state.drinks = None
            
        # Save to database
        insert_menu(occasion, menu)
    
    # Display menu if available
    if st.session_state.menu:
        st.markdown("<h2 class='subheader'>Your Custom Menu</h2>", unsafe_allow_html=True)
        
        # Display the menu in a card
        st.markdown("<div class='menu-card'>", unsafe_allow_html=True)
        st.markdown(f"<h3>Menu for: {st.session_state.occasion}</h3>", unsafe_allow_html=True)
        display_menu(st.session_state.menu)
        
        # Generate PDF download link
        pdf_bytes = create_pdf(st.session_state.occasion, st.session_state.menu)
        st.markdown(get_download_link(pdf_bytes, f"menu_{st.session_state.occasion.replace(' ', '_')}.pdf"), unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Display save confirmation
        st.markdown("<div class='info-box'>", unsafe_allow_html=True)
        st.markdown("✅ Menu saved successfully! You can find it in your recent menus.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Additional features section
    if st.session_state.menu:
        st.markdown("<h2 class='subheader'>Additional Features</h2>", unsafe_allow_html=True)
        
        # Feature tiles in three columns
        feat_col1, feat_col2, feat_col3 = st.columns(3)
        
        with feat_col1:
            st.markdown("<div class='menu-card'>", unsafe_allow_html=True)
            st.markdown("### 🛒 Shopping List")
            st.markdown("Generate a shopping list for your menu.")
            if st.button("Create List", key="shop_list", use_container_width=True):
                with st.spinner("Generating shopping list..."):
                    st.session_state.shopping_list = generate_shopping_list(st.session_state.menu)
            
            if st.session_state.shopping_list:
                st.markdown("#### Your Shopping List")
                st.write(st.session_state.shopping_list)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with feat_col2:
            st.markdown("<div class='menu-card'>", unsafe_allow_html=True)
            st.markdown("### 📋 Recipes")
            st.markdown("Get detailed recipes for menu items.")
            
            # Modify the logic here
            if st.button("View Recipes", key="recipes", use_container_width=True):
                with st.spinner("Generating recipes..."):
                    # Generate recipes and store them in session_state
                    st.session_state.recipes = generate_recipes(st.session_state.menu)
            
            if "recipes" in st.session_state and st.session_state.recipes:
                st.markdown("#### Recipes")
                st.write(st.session_state.recipes)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with feat_col3:
            st.markdown("<div class='menu-card'>", unsafe_allow_html=True)
            st.markdown("### 🍷 Drink Pairings")
            st.markdown("Get beverage recommendations.")
            if st.button("Suggest Drinks", key="drinks", use_container_width=True):
                with st.spinner("Suggesting drink pairings..."):
                    st.session_state.drinks = suggest_drinks(st.session_state.menu)
            
            if st.session_state.drinks:
                st.markdown("#### Recommended Drinks")
                st.write(st.session_state.drinks)
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "Developed with ❤️ by Master Chef AI Team | © 2025"
    )

if __name__ == "__main__":
    main()