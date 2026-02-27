import streamlit as st
import pandas as pd
import math

def calculate_price(price_str):
    if pd.isna(price_str):
        return None
    try:
        clean_str = str(price_str).replace('$', '').replace(' ', '').replace(chr(160), '').replace(',', '.')
        price = float(clean_str)
    except ValueError:
        return None

st.title("Informattach Fiyat Motoru")
st.write("İki ayrı CSV dosyasını yükle. Arka planda eşleşsin, eBay'in formatı bozulmadan fiyatlar güncellensin.")

col1, col2 = st.columns(2)
with col1:
    ebay_file = st.file_uploader("1. eBay CSV Dosyası", type=["csv"])
with col2:
    easync_file = st.file_uploader("2. EasyNC CSV Dosyası", type=["csv"])

if ebay_file and easync_file:
    try:
        df_ebay = pd.read_csv(ebay_file, low_memory=False, dtype=str)
        df_easync = pd.read_csv(easync_file, low_memory=False)
    except Exception as e:
        st.error(f"Dosya yüklenirken hata oluştu: {e}")
