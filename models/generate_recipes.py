
# Placeholder comment for menu_generator.py
from tools.suggest_menu import suggest_menu
from smolagents import CodeAgent, HfApiModel

# Initialize the agent with our tool
agent = CodeAgent(tools=[suggest_menu], model=HfApiModel())


def generate_recipes(menu):
    """Generate recipes for menu items"""
    # Use the agent to generate recipes
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
    
    command = f"Create simple recipes for the main dishes in this menu: {menu_text}"
    recipes = agent.run(command)
    return recipes