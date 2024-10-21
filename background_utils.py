# background_utils.py
import base64
import streamlit as st

# Fungsi untuk memuat latar belakang dari file lokal
def load_background_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Fungsi untuk menambahkan latar belakang
def add_bg_from_local(bg_image):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bg_image}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
