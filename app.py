import streamlit as st
import pandas as pd
import pickle
import numpy as np
import requests # Tambahan untuk load animasi
from streamlit_lottie import st_lottie # Library animasi
import joblib # Untuk load model .joblib

# Fungsi untuk memuat animasi Lottie
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_car = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

# Konfigurasi Halaman
st.set_page_config(
    page_title="Prediksi Harga Mobil by Yusa Putra Rosdiana",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007BFF;
        color: white;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        transform: scale(1.02);
    }
    h1 { color: #1E1E1E; font-family: 'Segoe UI', Tahoma, sans-serif; }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_assets():
    model = joblib.load('car_price_prediction_model.joblib')
    model_columns = pickle.load(open('model_columns.pkl', 'rb'))
    return model, model_columns

model, model_columns = load_assets()

# --- SIDEBAR ---
with st.sidebar:
    st.header("Konfigurasi Kendaraan")
    # Animasi kecil di sidebar
    st_lottie(lottie_car, speed=1, height=150, key="initial")
    st.info("Pilih merk dan tipe kendaraan Anda di sini.")
    
    manufacturers = sorted([col.replace('Manufacturer_', '') for col in model_columns if 'Manufacturer_' in col])
    selected_mfg = st.selectbox("Merk Mobil", manufacturers)
    selected_type = st.radio("Tipe Kendaraan", ["Passenger", "Car/SUV"])

# --- MAIN CONTENT ---
st.title("Car Price Prediction Tool")
st.write("Gunakan panel di bawah untuk memasukkan spesifikasi teknis mobil.")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Mesin & Tenaga")
    engine_size = st.number_input("Engine Size (L)", min_value=0.0, step=0.1, value=2.5)
    horsepower = st.number_input("Horsepower (HP)", min_value=0.0, step=1.0, value=150.0)

with col2:
    st.subheader("Dimensi Fisik")
    wheelbase = st.number_input("Wheelbase", min_value=0.0, value=100.0)
    width = st.number_input("Width", min_value=0.0, value=70.0)
    length = st.number_input("Length", min_value=0.0, value=180.0)
    curb_weight = st.number_input("Curb Weight (tons)", min_value=0.0, value=3.0)

with col3:
    st.subheader("Efisiensi")
    fuel_cap = st.number_input("Fuel Capacity", min_value=0.0, value=15.0)
    fuel_eff = st.number_input("Fuel Efficiency (MPG)", min_value=0.0, value=25.0)

st.divider()

@st.cache_data
def predict_price(engine_size, horsepower, wheelbase, width, length, curb_weight, fuel_cap, fuel_eff, mfg, vehicle_type):
    df_input = pd.DataFrame(0, index=[0], columns=model_columns)
    df_input['Engine_size'] = engine_size
    df_input['Horsepower'] = horsepower
    df_input['Wheelbase'] = wheelbase
    df_input['Width'] = width
    df_input['Length'] = length
    df_input['Curb_weight'] = curb_weight
    df_input['Fuel_capacity'] = fuel_cap
    df_input['Fuel_efficiency'] = fuel_eff
    
    if f"Manufacturer_{mfg}" in model_columns:
        df_input[f"Manufacturer_{mfg}"] = 1
    if f"Vehicle_type_{vehicle_type}" in model_columns:
        df_input[f"Vehicle_type_{vehicle_type}"] = 1
    
    return model.predict(df_input)[0]

if st.button("Hitung Estimasi Harga"):
    try:
        prediction = predict_price(engine_size, horsepower, wheelbase, width, length, curb_weight, fuel_cap, fuel_eff, selected_mfg, selected_type)
        
        # Animasi Berhasil
        st.balloons()
        
        # Layout Hasil dengan Animasi
        res_col1, res_col2 = st.columns([1, 2])
        with res_col1:
            # Menampilkan animasi mobil berjalan saat hasil muncul
            st_lottie(lottie_car, speed=1.5, height=200, key="success")
            
        with res_col2:
            st.markdown(f"""
                <div style="background-color: #f8f9fa; padding: 40px; border-radius: 10px; border-left: 5px solid #007BFF; margin-top: 20px;">
                    <h3 style="margin: 0; color: #555;">Estimasi Harga Jual:</h3>
                    <h1 style="margin: 10px 0; color: #007BFF; font-size: 3em;">${prediction:,.2f}</h1>
                    <p style="color: #888; font-size: 0.8em;">*Kalkulasi berdasarkan model Linear Regression.</p>
                </div>
            """, unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"Terjadi kesalahan saat prediksi: {e}")

# --- FOOTER ---
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #888888; padding: 20px;">
        <p style="margin-bottom: 5px;">Aplikasi Prediksi Harga Mobil v1.0</p>
        <strong style="color: #1E1E1E;">Nama: Yusa Putra Rosdiana</strong><br>
        <strong style="color: #1E1E1E;">NPM: 237006091</strong>
    </div>
""", unsafe_allow_html=True)