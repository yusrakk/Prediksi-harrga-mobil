# 🚗 Car Price Prediction Tool

Aplikasi web interaktif untuk memprediksi harga mobil berdasarkan spesifikasi teknis menggunakan Machine Learning.

## 📋 Daftar Isi
- [Fitur](#fitur)
- [Teknologi](#teknologi)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Deployment](#deployment)
- [Struktur Proyek](#struktur-proyek)
- [Penulis](#penulis)

## ✨ Fitur
- 🎯 Prediksi harga mobil dengan akurasi tinggi
- 🎨 Interface user-friendly dengan Streamlit
- 📊 Input parameter teknis (engine size, horsepower, dimensi, dll)
- 🏭 Filter berdasarkan merk dan tipe kendaraan
- 💾 Caching untuk performa optimal
- 🎬 Animasi Lottie untuk pengalaman visual yang menarik

## 🛠 Teknologi
- **Python 3.13**
- **Streamlit** - Web framework
- **Scikit-learn** - Machine Learning (Linear Regression)
- **Pandas** - Data processing
- **Joblib** - Model serialization
- **Streamlit Lottie** - Animasi

## 📦 Instalasi

### Prerequisites
- Python 3.8+
- pip atau conda

### Setup
```bash
# Clone repository
git clone https://github.com/yourusername/car-price-prediction.git
cd car-price-prediction

# Buat virtual environment
python -m venv .venv

# Aktifkan virtual environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Penggunaan

Jalankan aplikasi Streamlit:
```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser (`http://localhost:8501`).

### Langkah-langkah:
1. Pilih **Merk Mobil** dari sidebar
2. Pilih **Tipe Kendaraan** (Passenger atau Car/SUV)
3. Isi spesifikasi teknis:
   - Engine Size (L)
   - Horsepower (HP)
   - Wheelbase
   - Width
   - Length
   - Curb Weight (tons)
   - Fuel Capacity
   - Fuel Efficiency (MPG)
4. Klik tombol **"Hitung Estimasi Harga"**
5. Hasil prediksi akan ditampilkan

## ☁️ Deployment

### Deploy ke Streamlit Cloud

1. **Push ke GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Buka Streamlit Cloud:**
   - Pergi ke https://streamlit.io/cloud
   - Sign in dengan GitHub account
   - Klik "New app"
   - Pilih repository, branch, dan file (`app.py`)
   - Klik "Deploy"

3. **Aplikasi live!**
   - URL: `https://[app-name].streamlit.app`

## 📁 Struktur Proyek
```
car-price-prediction/
├── app.py                              # Main application
├── car_price_prediction_model.joblib   # Trained ML model
├── model_columns.pkl                   # Model feature names
├── requirements.txt                    # Dependencies
├── README.md                           # Project documentation
└── .venv/                              # Virtual environment
```

## 👤 Penulis
**Yusa Putra Rosdiana**  
NPM: 237006091

## 📝 Lisensi
MIT License - feel free to use this project for learning and development.

## 🙏 Terima Kasih
Terima kasih telah menggunakan Car Price Prediction Tool!
