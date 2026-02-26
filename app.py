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
st.write("Sütun başlıkları 'eBay_SKU', 'EasyNC_SKU' ve 'EasyNC_Price' olan Excel dosyanı yükle.")

uploaded_file = st.file_uploader("Excel Dosyası Seç (.xlsx)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df['eBay_SKU_Temiz'] = df['eBay_SKU'].astype(str).str.strip()
    df['EasyNC_SKU_Temiz'] = df['EasyNC_SKU'].astype(str).str.strip()
