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



# Add the project root to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import your modules
from models.menu_generator import generate_menu
from database.db import insert_menu, get_connection
from smolagents import CodeAgent, HfApiModel



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
    elif isinstance(menu, str):
        # Handle string format menu by trying to parse potential sections
        sections = re.split(r'\n\s*\n|\n(?=[A-Z][a-z]+:)', menu)
        for section in sections:
            if ':' in section:
                parts = section.split(':', 1)
                st.markdown(f"<div class='category-label'>{parts[0].strip()}</div>", unsafe_allow_html=True)
                items = parts[1].strip().split('\n')
                for item in items:
                    if item.strip():
                        st.write(f"• {item.strip()}")
            else:
                st.write(section)
    else:
        st.write(menu)