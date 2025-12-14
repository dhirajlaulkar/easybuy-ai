import os
from groq import Groq
from PIL import Image
import base64
from io import BytesIO

class EcommerceAssistant:
    def __init__(self):
        # Ensure GROQ_API_KEY is available in environment
        self.client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )
        self.text_model = "llama-3.3-70b-versatile"
        self.vision_model = "llama-3.2-11b-vision-preview"

    def _get_completion(self, prompt, model=None):
        if model is None:
            model = self.text_model
            
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
        )
        return chat_completion.choices[0].message.content

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
        return self._get_completion(prompt)

    def analyze_product_image(self, image, context=""):
        # Convert PIL Image to base64
        buffered = BytesIO()
        # Convert to RGB if necessary (e.g. for PNG with alpha) to save as JPEG
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
        image.save(buffered, format="JPEG")
        base64_image = base64.b64encode(buffered.getvalue()).decode('utf-8')

        prompt_text = f"""
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

        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt_text},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            model=self.vision_model,
        )
        return chat_completion.choices[0].message.content

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
        return self._get_completion(prompt)

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
        return self._get_completion(prompt)
