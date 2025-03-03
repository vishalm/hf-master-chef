# Placeholder comment for menu_generator.py
from tools.suggest_menu import suggest_menu
from smolagents import CodeAgent, HfApiModel

# Initialize the agent with our tool
agent = CodeAgent(tools=[suggest_menu], model=HfApiModel())

def generate_shopping_list(menu):
    """Generate a shopping list based on the menu"""
    # Use the agent to generate a shopping list
    if isinstance(menu, dict):
        menu_text = ""
        for category, items in menu.items():
            menu_text += f"{category}: "
            if isinstance(items, list):
                menu_text += ", ".join(items)
            else:
                menu_text += items
            menu_text += "\n"
    else:
        menu_text = str(menu)
    
    command = f"Create a shopping list for this menu: {menu_text}"
    shopping_list = agent.run(command)
    return shopping_list