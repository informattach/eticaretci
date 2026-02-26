import streamlit as st
import pandas as pd
import math
import io

def calculate_price(price_str):
    if pd.isna(price_str):
        return "SKU Bulunamadı"
    try:
        clean_str = str(price_str).replace('$', '').replace(' ', '').replace(chr(160), '').replace(',', '.')
        price = float(clean_str)
    except ValueError:
        return "Format Hatası"

st.title("Informattach Fiyat Otomasyonu")
st.write("Orijinal eBay ve EasyNC verilerini içeren Excel (.xlsx) dosyanızı yükleyin.")

uploaded_file = st.file_uploader("Excel Dosyası Seç (.xlsx)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
