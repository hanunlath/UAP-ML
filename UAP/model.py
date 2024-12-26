import streamlit as st
import joblib
import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Membuat path absolut ke file model
model_path = os.path.join(current_dir, 'model', 'RFmodel.pkl')
scaler_path = os.path.join(current_dir, 'model', 'scaler2.pkl')
state = os.path.join(current_dir, 'model', 'state_label_encoder.pkl')
categories = os.path.join(current_dir, 'model', 'categories_label_encoder.pkl')
name_path= os.path.join(current_dir, 'model', 'feature_names.pkl')

# Memuat model dan scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
label_encoder_state = joblib.load(state)
label_encoder_categories = joblib.load(categories)
feature_names = joblib.load(name_path)

# Daftar negara bagian di AS berdasarkan wilayah geografis
states_west = ['California', 'Oregon', 'Washington', 'Nevada', 'Arizona', 'Utah', 'Colorado', 'New Mexico', 'Idaho', 'Montana', 'Wyoming', 'Hawaii', 'Alaska']
states_east = ['Maine', 'Vermont', 'New Hampshire', 'Massachusetts', 'Rhode Island', 'Connecticut', 'New York', 'New Jersey', 'Pennsylvania', 'Delaware', 'Maryland', 'Virginia', 'North Carolina', 'South Carolina', 'Georgia', 'Florida', 'Ohio', 'Michigan', 'Indiana', 'Kentucky', 'Tennessee', 'West Virginia', 'Missouri', 'Arkansas', 'Louisiana', 'Alabama', 'Mississippi', 'North Dakota', 'South Dakota', 'Nebraska', 'Kansas', 'Iowa', 'Wisconsin']
states_north = ['Maine', 'New Hampshire', 'Vermont', 'Michigan', 'Minnesota', 'Wisconsin', 'Montana', 'North Dakota', 'South Dakota', 'Wyoming']
states_south = ['Texas', 'Florida', 'Georgia', 'North Carolina', 'South Carolina', 'Tennessee', 'Alabama', 'Louisiana', 'Kentucky', 'Mississippi', 'Arkansas']

region_states = {
    "West": states_west,
    "East": states_east,
    "South": states_south,
    "North": states_north,
    "Other": ["Other"]
}

# Judul aplikasi
st.title("Prediksi Tempat Wisata di USA")

# Input user
st.header("Masukkan Data Prediksi")
state = st.selectbox("Region of state", ['East', 'West', 'South', 'North', 'Other'])

# Tampilkan daftar state berdasarkan region yang dipilih
st.write("Daftar negara bagian dalam region ini:")
st.write(", ".join(region_states[state]))

latitude = st.number_input("Latitude", step=0.01)
longitude = st.number_input("Longitude", step=0.01)
month = st.selectbox("Bulan Kunjungan", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

# Tombol prediksi
if st.button("Prediksi"):
    # Encode input
    state_encoded = label_encoder_state.transform([state])[0]
    
    # Buat DataFrame input
    input_data = pd.DataFrame({
        'Region_enc': [state_encoded],
        'Latitude': [latitude],
        'Longitude': [longitude],
        'Month': [month]
    })

    # Pastikan urutan kolom sesuai dengan fitur yang digunakan saat training
    input_data = input_data[feature_names]

    # Scaling data input
    input_data_scaled = scaler.transform(input_data)

    # Prediksi
    prediction = model.predict(input_data_scaled)
    prediction_label = label_encoder_categories.inverse_transform(prediction)

    # Tampilkan hasil prediksi
    st.subheader("Hasil Prediksi")
    st.write(f"Kategori Prediksi: {prediction_label[0]}")