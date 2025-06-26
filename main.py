import streamlit as st
from easybuy_styles import inject_custom_css
from easybuy_ui import run_easybuy_ui

def main():
    inject_custom_css()
    run_easybuy_ui()

if __name__ == "__main__":
    main()
