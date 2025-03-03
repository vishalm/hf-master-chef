# Placeholder comment for suggest_menu.py
from smolagents import tool

@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    
    Args:
        occasion: The type of occasion for the event.
    
    Returns:
        A string representing the menu suggestion.
    """
    occasion_key = occasion.lower().strip()
    
    # Dictionary mapping for over 50 occasions
    menu_options = {
        "casual": "Pizza, snacks, and drinks.",
        "formal": "3-course dinner with wine and dessert.",
        "superhero": "Buffet with high-energy and healthy food.",
        "birthday": "Cake, finger foods, and festive treats.",
        "holiday": "Seasonal specialties with warm desserts.",
        "wedding": "Elegant multi-course meal with champagne.",
        "corporate": "Assorted sandwiches, salads, and gourmet bites.",
        "graduation": "A mix of celebratory appetizers and refreshing drinks.",
        "picnic": "Sandwiches, fresh fruits, and lemonade.",
        "brunch": "Eggs benedict, mimosas, and pastries.",
        "anniversary": "Romantic dinner with fine dining options.",
        "reunion": "Comfort food buffet with nostalgic dishes.",
        "barbecue": "Grilled meats, vegetables, and iced tea.",
        "baby shower": "Light bites, finger sandwiches, and mocktails.",
        "retirement": "Classic favorites with a touch of elegance.",
        "fundraiser": "Elegant hors d'oeuvres and signature cocktails.",
        "themed": "Custom menu based on your chosen theme.",
        "movie night": "Popcorn, nachos, and soft drinks.",
        "game night": "Finger foods, sliders, and craft beers.",
        "housewarming": "Variety of small bites and a welcome cocktail.",
        "networking": "Canapés, mini quiches, and professional cocktails.",
        "potluck": "Diverse dishes contributed by guests.",
        "cultural": "Ethnic specialties and traditional flavors.",
        "rock concert": "Quick bites, hot dogs, and sodas.",
        "sports event": "Tailgate food with burgers and beers.",
        "gala": "Exquisite multi-course meal with gourmet wines.",
        "cocktail party": "Stylish cocktails paired with chic appetizers.",
        "wine tasting": "Artisan cheeses, charcuterie, and select wines.",
        "health-focused": "Organic, low-calorie dishes and smoothies.",
        "vegan": "Plant-based dishes bursting with flavor.",
        "gluten-free": "Gluten-free gourmet selections.",
        "christmas": "Festive seasonal dishes with holiday treats.",
        "new year's": "Sparkling beverages and celebratory bites.",
        "st patrick's": "Irish classics with a modern twist.",
        "easter": "Spring-inspired dishes with fresh ingredients.",
        "halloween": "Spooky-themed snacks and eerie desserts.",
        "mardi gras": "Cajun and Creole delights with flair.",
        "summer party": "Refreshing salads, BBQ, and tropical drinks.",
        "winter party": "Hearty stews, roasts, and warm beverages.",
        "spring party": "Fresh, seasonal flavors with light dishes.",
        "autumn party": "Rustic comfort foods with pumpkin treats.",
        "casual dinner": "Comforting pasta dishes and cozy soups.",
        "dinner party": "Elegant entrees with curated wine pairings.",
        "fast food": "Burgers, fries, and milkshakes.",
        "food truck festival": "Variety of street foods and gourmet treats.",
        "buffet": "All-you-can-eat spread with diverse options.",
        "family gathering": "Homestyle cooking and shared family favorites.",
        "community event": "Large-scale catering with crowd-pleasing dishes.",
        "appreciation event": "Deluxe dishes with a touch of luxury.",
        "farewell party": "Memorable dishes that celebrate legacy.",
        "sports watch party": "Finger foods and energy-boosting snacks.",
        "art gallery opening": "Sophisticated hors d'oeuvres and artisan beverages.",
        "charity event": "Elegant yet approachable dishes to please a broad audience.",
        "religious event": "Respectful and traditional menu offerings.",
        "corporate retreat": "Healthy and satisfying meals to fuel productivity.",
        "seasonal festival": "Local flavors and seasonal specialties.",
        "potluck dinner": "A collaborative assortment of dishes.",
        "diy cooking class": "Interactive food stations with guided recipes."
    }
    
    # Return the matched menu or a custom suggestion if not found
    if occasion_key in menu_options:
        return menu_options[occasion_key]
    else:
        return (f"Custom menu suggestion: Consider a fusion of flavors, interactive food stations, "
                f"and signature dishes tailored for a '{occasion}' themed event.")
