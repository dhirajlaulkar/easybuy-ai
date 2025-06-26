import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
    :root {
      --bg: #0f172a;
      --surface: #1e293b;
      --primary: #3b82f6;
      --secondary: #fb923c;
      --accent: #22d3ee;
      --text: #e2e8f0;
      --muted: #94a3b8;
      --card-radius: 18px;
      --card-shadow: 0 4px 24px #0003;
      --border: 1px solid #334155;
      --font-header: 'Poppins', 'Inter', sans-serif;
      --font-body: 'Open Sans', sans-serif;
    }
    html, body, [class*="stApp"] {
      background: var(--bg) !important;
      color: var(--text) !important;
      font-family: var(--font-body) !important;
    }
    section[data-testid="stSidebar"] {
      background: var(--surface) !important;
      color: var(--text) !important;
      border-right: var(--border);
      min-width: 270px !important;
    }
    .hero {
      background: linear-gradient(90deg, var(--primary) 0%, var(--accent) 100%);
      border-radius: 24px;
      box-shadow: var(--card-shadow);
      padding: 2.5em 2em 2em 2em;
      margin-bottom: 2em;
      color: #fff;
      text-align: center;
    }
    .hero h1 {
      font-family: var(--font-header);
      font-size: 2.8rem;
      font-weight: 800;
      margin-bottom: 0.2em;
    }
    .hero p {
      font-size: 1.25rem;
      color: #e0e7ef;
      margin-bottom: 0.5em;
    }
    .hero .badge {
      background: var(--secondary);
      color: #fff;
      border-radius: 12px;
      padding: 0.3em 1em;
      font-size: 1rem;
      font-weight: 600;
      margin-bottom: 1em;
      display: inline-block;
    }
    .stCard, .main-card {
      background: var(--surface);
      border-radius: var(--card-radius);
      box-shadow: var(--card-shadow);
      padding: 2em 1.5em;
      margin-bottom: 2em;
      border: var(--border);
    }
    .stButton>button {
      background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%) !important;
      color: #fff !important;
      font-weight: 700 !important;
      border-radius: 8px !important;
      border: none !important;
      padding: 0.7em 2em !important;
      font-size: 1.1rem !important;
      box-shadow: 0 2px 8px #0002;
      transition: background 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
      background: linear-gradient(90deg, var(--secondary) 0%, var(--primary) 100%) !important;
      box-shadow: 0 4px 16px #0003;
    }
    input, textarea, .stTextInput>div>div>input {
      background: #0f172a !important;
      color: var(--text) !important;
      border-radius: 8px !important;
      border: 1px solid var(--muted) !important;
      font-size: 1rem !important;
      font-family: var(--font-body) !important;
    }
    .stTable th {background: var(--primary); color: #fff;}
    .stTable td {background: #1e293b; color: #e2e8f0;}
    .stTable tr:nth-child(even) td {background: #334155;}
    .stExpanderHeader {
      font-family: var(--font-header);
      font-size: 1.1rem;
      color: var(--primary);
    }
    .fade-in {
      animation: fadeIn 0.7s;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: none; }
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&family=Poppins:wght@600;800&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)
