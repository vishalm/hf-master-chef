import streamlit as st
import sys
import os
import json
from datetime import datetime
import pandas as pd

# Add the project root to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import your modules
from models.menu_generator import generate_menu
from database.db import insert_menu, get_connection

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
</style>
""", unsafe_allow_html=True)

def get_recent_menus():
    """Fetch recent menus from the database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, occasion, menu, created_at 
        FROM menus 
        ORDER BY created_at DESC 
        LIMIT 5
    ''')
    results = cursor.fetchall()
    conn.close()
    
    menus = []
    for row in results:
        try:
            menu_data = json.loads(row[2]) if isinstance(row[2], str) else row[2]
            menus.append({
                'id': row[0],
                'occasion': row[1],
                'menu': menu_data,
                'created_at': row[3]
            })
        except json.JSONDecodeError:
            # Handle case where menu isn't valid JSON
            menus.append({
                'id': row[0],
                'occasion': row[1],
                'menu': row[2],
                'created_at': row[3]
            })
    
    return menus

def display_menu(menu):
    """Display a menu in a nicely formatted way"""
    if isinstance(menu, str):
        try:
            menu = json.loads(menu)
        except json.JSONDecodeError:
            st.write(menu)
            return
    
    if isinstance(menu, dict):
        for category, items in menu.items():
            st.markdown(f"<div class='category-label'>{category}</div>", unsafe_allow_html=True)
            if isinstance(items, list):
                for item in items:
                    st.write(f"• {item}")
            else:
                st.write(items)
            st.write("")
    else:
        st.write(menu)

def main():
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
                                placeholder="e.g., Birthday dinner for 10 people, vegetarian options")
    
    with col2:
        st.write("")
        st.write("")
        generate_button = st.button("Generate Menu 🧠", use_container_width=True)
    
    # Generate menu based on input
    if generate_button:
        if occasion:
            with st.spinner("Chef is thinking... 🤔"):
                menu = generate_menu(occasion)
            
            st.markdown("<h2 class='subheader'>Your Custom Menu</h2>", unsafe_allow_html=True)
            
            # Display the menu in a card
            st.markdown("<div class='menu-card'>", unsafe_allow_html=True)
            st.markdown(f"<h3>Menu for: {occasion}</h3>", unsafe_allow_html=True)
            display_menu(menu)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Save to database
            insert_menu(occasion, menu)
            
            # Display save confirmation
            st.markdown("<div class='info-box'>", unsafe_allow_html=True)
            st.markdown("✅ Menu saved successfully! You can find it in your recent menus.")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Export options
            export_col1, export_col2 = st.columns(2)
            with export_col1:
                if st.button("Export as PDF", use_container_width=True):
                    st.info("PDF export functionality would be implemented here.")
            with export_col2:
                if st.button("Share Menu", use_container_width=True):
                    st.info("Share functionality would be implemented here.")
        else:
            st.error("Please enter an occasion to generate a menu.")
    
    # Additional features section
    st.markdown("<h2 class='subheader'>Additional Features</h2>", unsafe_allow_html=True)
    
    # Feature tiles in three columns
    feat_col1, feat_col2, feat_col3 = st.columns(3)
    
    with feat_col1:
        st.markdown("<div class='menu-card'>", unsafe_allow_html=True)
        st.markdown("### 🛒 Shopping List")
        st.markdown("Generate a shopping list for your menu.")
        st.button("Create List", key="shop_list", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with feat_col2:
        st.markdown("<div class='menu-card'>", unsafe_allow_html=True)
        st.markdown("### 📋 Recipes")
        st.markdown("Get detailed recipes for menu items.")
        st.button("View Recipes", key="recipes", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with feat_col3:
        st.markdown("<div class='menu-card'>", unsafe_allow_html=True)
        st.markdown("### 🍷 Drink Pairings")
        st.markdown("Get beverage recommendations.")
        st.button("Suggest Drinks", key="drinks", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "Developed with ❤️ by Master Chef AI Team | © 2025"
    )

if __name__ == "__main__":
    main()