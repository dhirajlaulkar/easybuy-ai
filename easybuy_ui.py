import streamlit as st
from PIL import Image
from easybuy_core import EcommerceAssistant
from easybuy_styles import inject_custom_css
import os
from dotenv import load_dotenv
import google.generativeai as genai

# --- Load environment variables and configure Gemini ---
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def run_easybuy_ui():
    inject_custom_css()
    # --- Sidebar Branding ---
    st.sidebar.image("./carryall_13438458.png", width=90)
    st.sidebar.markdown("<div style='font-family:Poppins,sans-serif;font-size:1.3rem;font-weight:700;color:#87CEEB;margin-bottom:1em;'>EasyBuy Assistant</div>", unsafe_allow_html=True)

    # --- Hero Section ---
    with st.container():
        st.markdown("""
        <div class="hero fade-in">
            <div class="badge">AI-powered Shopping • Gemini 1.5 Flash</div>
            <h1>EasyBuy Assistant</h1>
            <p>Discover, compare, and analyze products with the power of Gemini AI.<br>Get personalized recommendations, image insights, and more!</p>
        </div>
        """, unsafe_allow_html=True)

    # --- Feature Navigation ---
    features = [
        {"name": "Product Recommendations", "icon": "", "desc": "Get tailored product suggestions based on your needs and budget."},
        {"name": "Image Analysis", "icon": "", "desc": "Analyze product images for details, quality, and price estimation."},
        {"name": "Review Analysis", "icon": "", "desc": "Summarize and score customer reviews for any product."},
        {"name": "Product Comparison", "icon": "", "desc": "Compare two products side-by-side and get a smart recommendation."}
    ]

    # --- Sidebar Feature Button Navigation ---
    if 'selected_feature' not in st.session_state:
        st.session_state['selected_feature'] = features[0]["name"]

    with st.sidebar:
        st.markdown("<div style='margin-bottom:1.5em;'><b></b></div>", unsafe_allow_html=True)
        for f in features:
            is_selected = st.session_state['selected_feature'] == f["name"]
            btn_label = f"{f['icon']} {f['name']}"
            btn_kwargs = {
                'key': f"feature_btn_{f['name']}",
                'help': f['desc']
            }
            if st.button(btn_label, **btn_kwargs):
                st.session_state['selected_feature'] = f["name"]
        st.markdown("<hr style='border:1px solid #334155;margin:1.5em 0;'>", unsafe_allow_html=True)

    feature = st.session_state['selected_feature']
    assistant = EcommerceAssistant()

    # --- Main Content ---
    with st.container():
        if feature == "Product Recommendations":
            with st.container():
                st.markdown('<div class="main-card fade-in">', unsafe_allow_html=True)
                st.markdown("<h2 style='font-family:Poppins,sans-serif;color:#22d3ee;'>Product Recommendations</h2>", unsafe_allow_html=True)
                st.write("<span style='color:#94a3b8;'>Get 5 personalized product picks, key features, and shopping tips.</span>", unsafe_allow_html=True)
                with st.form("rec_form"):
                    col1, col2 = st.columns(2)
                    with col1:
                        user_query = st.text_area("What are you looking for?", placeholder="E.g., Best laptop for gaming under ₹1000...")
                        budget = st.text_input("Budget (optional)", placeholder="₹500 - ₹1000")
                    with col2:
                        category = st.selectbox("Category (optional)", ["Any", "Electronics", "Clothing", "Home & Garden", "Sports", "Books", "Beauty"])
                    submitted = st.form_submit_button("Get Recommendations")
                if submitted:
                    with st.spinner("Generating recommendations..."):
                        recommendations = assistant.product_recommendation(user_query, budget, category)
                        st.markdown(f"<div class='stCard fade-in' style='background:#172554;border-left:6px solid #3b82f6;'><b>Recommendations:</b><br>{recommendations}</div>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

        elif feature == "Image Analysis":
            with st.container():
                st.markdown('<div class="main-card fade-in">', unsafe_allow_html=True)
                st.markdown("<h2 style='font-family:Poppins,sans-serif;color:#22d3ee;'>Product Image Analysis</h2>", unsafe_allow_html=True)
                st.write("<span style='color:#94a3b8;'>Upload a product image to get AI-powered insights and price estimation.</span>", unsafe_allow_html=True)
                with st.form("img_form"):
                    uploaded_image = st.file_uploader("Upload product image", type=['png', 'jpg', 'jpeg'])
                    context = st.text_input("Additional context (optional)", placeholder="E.g., This is a smartphone I'm considering...")
                    img_submitted = st.form_submit_button("Analyze Product")
                if uploaded_image and img_submitted:
                    image = Image.open(uploaded_image)
                    st.image(image, caption="Product Image", use_container_width=True)
                    with st.spinner("Analyzing product image..."):
                        analysis = assistant.analyze_product_image(image, context)
                        st.markdown(f"<div class='stCard fade-in' style='background:#172554;border-left:6px solid #fb923c;'><b>Product Analysis:</b><br>{analysis}</div>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

        elif feature == "Review Analysis":
            with st.container():
                st.markdown('<div class="main-card fade-in">', unsafe_allow_html=True)
                st.markdown("<h2 style='font-family:Poppins,sans-serif;color:#22d3ee;'>Customer Review Analysis</h2>", unsafe_allow_html=True)
                st.write("<span style='color:#94a3b8;'>Paste customer reviews to get sentiment, pros/cons, and a buy recommendation.</span>", unsafe_allow_html=True)
                with st.form("rev_form"):
                    reviews = st.text_area("Paste customer reviews here:", placeholder="Copy and paste multiple customer reviews...", height=200)
                    rev_submitted = st.form_submit_button("Analyze Reviews")
                if rev_submitted:
                    with st.spinner("Analyzing reviews..."):
                        sentiment_analysis = assistant.review_sentiment_analysis(reviews)
                        st.markdown(f"<div class='stCard fade-in' style='background:#172554;border-left:6px solid #22d3ee;'><b>Review Analysis:</b><br>{sentiment_analysis}</div>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

        elif feature == "Product Comparison":
            with st.container():
                st.markdown('<div class="main-card fade-in">', unsafe_allow_html=True)
                st.markdown("<h2 style='font-family:Poppins,sans-serif;color:#22d3ee;'>Product Comparison</h2>", unsafe_allow_html=True)
                st.write("<span style='color:#94a3b8;'>Compare two products side-by-side and get a smart recommendation.</span>", unsafe_allow_html=True)
                with st.form("cmp_form"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("Product 1")
                        product1 = st.text_area("Product 1 Details:", placeholder="Name, specifications, price, features...", height=150, key="prod1")
                    with col2:
                        st.subheader("Product 2")
                        product2 = st.text_area("Product 2 Details:", placeholder="Name, specifications, price, features...", height=150, key="prod2")
                    cmp_submitted = st.form_submit_button("Compare Products")
                if cmp_submitted and product1 and product2:
                    with st.spinner("Comparing products..."):
                        comparison = assistant.compare_products(product1, product2)
                        st.subheader("Product Comparison:")
                        import re
                        features = re.findall(r"\* (.+?): (.+?) vs (.+)", comparison)
                        if features:
                            st.markdown("<b>Feature Comparison Table:</b>", unsafe_allow_html=True)
                            table_md = "<table class='stTable'><thead><tr><th>Feature</th><th>Product 1</th><th>Product 2</th></tr></thead><tbody>"
                            for f in features:
                                table_md += f"<tr><td>{f[0]}</td><td>{f[1]}</td><td>{f[2]}</td></tr>"
                            table_md += "</tbody></table>"
                            st.markdown(table_md, unsafe_allow_html=True)
                        st.markdown(f"<div class='stCard fade-in' style='background:#172554;border-left:6px solid #22d3ee;'><b>Gemini's Recommendation:</b><br>{comparison}</div>", unsafe_allow_html=True)
                elif cmp_submitted:
                    st.warning("Please enter details for both products!")
                st.markdown('</div>', unsafe_allow_html=True)

    # --- Footer ---
    st.markdown("<hr style='border:1px solid #334155;margin:2em 0 1em 0;'>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; color:#94a3b8; font-size:1.1rem;'> This assistant uses Gemini AI.</div>", unsafe_allow_html=True)

# At the end of the file, add:
if __name__ == "__main__":
    run_easybuy_ui()
