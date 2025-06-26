import google.generativeai as genai
from PIL import Image

class EcommerceAssistant:
    def __init__(self):
        self.model = genai.GenerativeModel('models/gemini-1.5-flash')
        self.vision_model = genai.GenerativeModel('models/gemini-1.5-flash')
    def product_recommendation(self, user_query, budget=None, category=None):
        prompt = f"""
        You are an expert e-commerce assistant. Based on the user's query, provide personalized product recommendations.
        User Query: {user_query}
        Budget: {budget if budget else 'Not specified'} (in INR ₹)
        Category: {category if category else 'Any'}
        Please provide:
        1. 5 specific product recommendations with reasons
        2. Key features to look for
        3. Price range expectations (in INR ₹)
        4. Where to buy (online platforms)
        5. Things to avoid
        Format as a helpful shopping guide. All prices and budgets must be in INR (₹).
        """
        response = self.model.generate_content(prompt)
        return response.text
    def analyze_product_image(self, image, context=""):
        prompt = f"""
        Analyze this product image and provide:
        1. Product identification and category
        2. Key visual features and design elements
        3. Quality assessment based on appearance
        4. Suggested use cases
        5. Potential target audience
        6. Estimated price range (in INR ₹)
        Additional context: {context}
        All price estimates must be in INR (₹).
        """
        response = self.vision_model.generate_content([prompt, image])
        return response.text
    def review_sentiment_analysis(self, reviews_text):
        prompt = f"""
        Analyze the following customer reviews and provide:
        1. Overall sentiment score (1-10)
        2. Most common positive points
        3. Most common complaints
        4. Purchase recommendation (Buy/Don't Buy/Consider Alternatives)
        5. Summary of key insights
        Reviews:
        {reviews_text}
        """
        response = self.model.generate_content(prompt)
        return response.text
    def price_analysis(self, product_name, prices_data):
        prompt = f"""
        Analyze the pricing data for {product_name} and provide:
        1. Best value assessment
        2. Price trend analysis
        3. When to buy recommendations
        4. Platform comparison
        5. Potential savings opportunities
        Pricing Data (all prices in INR ₹):
        {prices_data}
        All price analysis and recommendations must be in INR (₹).
        """
        response = self.model.generate_content(prompt)
        return response.text
    def compare_products(self, product1_details, product2_details):
        prompt = f"""
        Compare these two products and provide a detailed analysis:
        Product 1: {product1_details}
        Product 2: {product2_details}
        Provide:
        1. Feature-by-feature comparison
        2. Value for money analysis
        3. Use case recommendations
        4. Final recommendation with reasoning
        5. Pros and cons of each
        """
        response = self.model.generate_content(prompt)
        return response.text
