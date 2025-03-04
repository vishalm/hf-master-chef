# Master Chef AI 🍽️

Master Chef AI is an intelligent AI-powered platform designed to generate customized menus for any occasion. This project is a work in progress, developed to showcase the concepts and capabilities learned from the **Hugging Face AI Agents** course. The app leverages the power of **smolagents** for intelligent task execution, demonstrating how AI agents can be used to create personalized experiences like menu planning, shopping list generation, recipe suggestions, and drink pairings.

![plot](/AI-Chef-Menu-Designer.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to **Master Chef AI**, your personal AI chef! This app leverages cutting-edge artificial intelligence to generate menus based on the occasion and dietary preferences. Whether you're looking for an elegant dinner menu, a casual barbecue, or a special event, our platform provides an intuitive and simple way to plan meals.

This project is currently a **work in progress**, developed to showcase the **Hugging Face AI Agents** course using **smolagents**. The goal is to demonstrate the potential of AI agents to assist in complex decision-making tasks, such as menu generation, shopping list creation, recipe generation, and drink pairing, all powered by AI.

### Key Features:
- **Custom Menu Generation**: AI creates personalized menus for different occasions like birthdays, weddings, or festive dinners.
- **Shopping List Generation**: Get a shopping list for all the ingredients in your menu.
- **Recipe Suggestions**: View detailed recipes for each menu item.
- **Drink Pairing Recommendations**: Find perfect drink pairings for your selected menu.

## Features

### 1. **Custom Menu Generator** 🧑‍🍳
- Enter the occasion details, such as the event type, dietary restrictions, and guest count.
- AI will generate a full menu tailored to your needs.

### 2. **Shopping List** 🛒
- Once a menu is generated, a shopping list is created with all necessary ingredients, making grocery shopping a breeze.

### 3. **Recipe Suggestions** 📋
- Get detailed instructions and ingredients for each menu item, ensuring you can prepare the dishes without missing a step.

### 4. **Drink Pairings** 🍷
- AI suggests drink pairings that complement your menu, elevating the overall dining experience.

## Tech Stack

- **Streamlit**: Framework for building interactive web applications.
- **Python**: Main programming language used for backend operations.
- **FPDF**: Library used for generating PDF files.
- **Hugging Face API**: Used for additional AI features like code generation and menu suggestions.
- **smolagents**: A key component for integrating AI agents in this project. The app demonstrates how **smolagents** can facilitate intelligent, automated task execution in the context of menu planning and related features.
- **SQLite/PostgreSQL**: Database used for storing recent menus.
- **Custom Models**:
  - **Menu Generator**: AI model that generates menu suggestions based on input.
  - **Recipe Generator**: AI model that provides detailed recipes for each menu item.
  - **Shopping List Generator**: AI tool to generate shopping lists.
  - **Drink Pairing Generator**: Recommender system for drink pairings based on the menu.

## Installation

### Prerequisites:
- Python 3.7 or higher
- Streamlit
- Hugging Face API key (for advanced AI features)
- smolagents library

### Step-by-Step Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/vishalm/hf-master-chef.git
   cd hf-master-chef
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run master_chef.py
   ```

4. Open your browser and go to `http://localhost:8501` to start using Master Chef AI.

## Usage

Once the app is running, follow these simple steps:

1. **Input Occasion**: Type in the occasion for which you need a menu, such as "Birthday dinner for 10 people" or "Wedding anniversary celebration."
2. **Generate Menu**: Click the "Generate Menu 🧠" button to create a customized menu.
3. **Explore Additional Features**: 
   - View and download the **shopping list** for the menu.
   - View **recipes** for each menu item.
   - Get suggested **drink pairings** for the dishes in your menu.

Once you're satisfied with the results, you can download the menu as a PDF or save it for future reference.

## Customization

You can customize the app further by modifying:
- **Menu Generator**: Adjust the logic in the `generate_menu` function to match your personal preferences.
- **Database Integration**: Modify the database connection to use other systems like PostgreSQL or MySQL if needed.
- **Styling**: Update the custom CSS to match your desired UI/UX preferences.


**Build the Docker image**:
   Run the following command in your terminal from the directory containing the `Dockerfile`:

```bash
docker build -t masterchef-ai . --no-cache
```

**Run the Docker container**:
   After the image is built, you can run it using:

```bash
docker run -p 8501:8501 masterchef-ai
```

This will run your Streamlit app on port 8501. You can access it by visiting `http://localhost:8501` in your web browser.



## Contributing

We welcome contributions to improve the app! If you'd like to contribute, feel free to fork the repository, make your changes, and create a pull request.

### Steps to Contribute:
1. Fork the repository.
2. Clone your forked repository:
   ```bash
   git clone https://github.com/vishalm/hf-master-chef.git
   ```
3. Make changes to the code.
4. Push your changes:
   ```bash
   git push origin your-branch-name
   ```
5. Open a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

