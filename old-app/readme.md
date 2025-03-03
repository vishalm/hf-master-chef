# AI-Based Food Menu Designer

This project is an AI-powered menu designer that generates custom menus based on user-provided occasions. The application features:

- **Streamlit Frontend:** A simple web interface where users can input an occasion and view the generated menu.
- **AI Integration:** Utilizes `smolagents` to generate menu suggestions from over 50 predefined options.
- **SQLite Database:** Stores generated menus for future reference.
- **Configurable Settings:** Centralized configuration for database paths and potential Supabase integration.

## Setup Instructions

1. **Clone the repository:**

```bash
   git clone https://your-repo-url/AI_Menu_Designer.git
   cd AI_Menu_Designer
```

2. **Install Dependencies:**

```bash
   pip install -r requirements.txt
```

3. **Run the Streamlit App:**

```bash
   streamlit run app/streamlit_app.py
```

4. **Configuration:**

   Update `config/config.py` with your specific settings (e.g., Supabase keys) if you plan to integrate further.

## How It Works

- **User Interface:** The Streamlit app prompts the user to enter an occasion.
- **Menu Generation:** The input is passed to the AI-based menu generator, which leverages the `smolagents` CodeAgent and a custom tool with 50+ menu options.
- **Data Storage:** The generated menu, along with the occasion, is saved to an SQLite database.
- **Extensibility:** The project is structured for easy updates and further integrations, such as Supabase for advanced data management.

## Future Improvements

- Enhanced error handling and validations.
- Integration with Supabase for real-time data sync.
- Extended AI capabilities for more dynamic menu creation.

Enjoy designing your custom menus!
