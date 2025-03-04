# Placeholder comment for menu_generator.py
from tools.suggest_menu import suggest_menu
from smolagents import CodeAgent, HfApiModel
from models.agent import agent

# Initialize the agent with our tool
# agent = CodeAgent(tools=[suggest_menu], model=HfApiModel())

def generate_menu(occasion: str) -> str:
    """
    Generates a menu suggestion based on the provided occasion.
    
    Args:
        occasion: The occasion input from the user.
    
    Returns:
        A string containing the menu suggestion.
    """
    # Command format can be modified as needed
    command = f"Prepare a {occasion} menu for the party."
    result = agent.run(command)
    return result
