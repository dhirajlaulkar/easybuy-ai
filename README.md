# EasyBuy: Smart E-commerce Assistant

EasyBuy is a modern, Gemini-powered Streamlit app that helps users discover, compare, and analyze products with AI. It provides personalized recommendations, image analysis, review insights, and product comparisons—all in a beautiful, responsive UI.

## Features
- **Product Recommendations:** Get tailored product suggestions based on your needs and budget.
- **Image Analysis:** Upload a product image to get AI-powered insights and price estimation.
- **Review Analysis:** Summarize and score customer reviews for any product.
- **Product Comparison:** Compare two products side-by-side and get a smart recommendation.

## Project Structure
```
main.py                # Entry point for the Streamlit app
requirements.txt       # Python dependencies
.env                   # Environment variables (not committed)
easybuy_ui.py          # All Streamlit UI logic
 easybuy_core.py       # Gemini assistant logic
 easybuy_styles.py     # Custom CSS/styles
```

## Setup Instructions

1. **Clone the repository**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up your Gemini API key**
- Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

4. **Run the app**
```bash
streamlit run main.py
```

5. **Open in your browser**
- The app will open automatically, or visit [http://localhost:8501](http://localhost:8501)

## Notes
- Do **not** commit your `.env` file or API keys to version control.
- The app is fully responsive and works on desktop and mobile.

## License
MIT
