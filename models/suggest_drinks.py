# Placeholder comment for menu_generator.py
from tools.suggest_menu import suggest_menu
from smolagents import CodeAgent, HfApiModel

# Initialize the agent with our tool
agent = CodeAgent(tools=[suggest_menu], model=HfApiModel())


def suggest_drinks(menu):
    """Suggest drink pairings for the menu"""
    # Use the agent to suggest drink pairings
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
    
    command = f"Suggest drink pairings (both alcoholic and non-alcoholic) for this menu: {menu_text}"
    drinks = agent.run(command)
    return drinks