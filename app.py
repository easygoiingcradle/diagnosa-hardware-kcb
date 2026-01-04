import streamlit as st

# Bagian ini untuk BAB 2.1: DESAIN INTERFACE [cite: 28]
st.set_page_config(page_title="Sistem Pakar Diagnosa Laptop")
st.title("Aplikasi Diagnosa Kerusakan Hardware")
st.write("Identifikasi masalah laptop Anda berdasarkan gejala yang muncul.")

st.divider()

# FORM INPUT DATA [cite: 29]
st.subheader("Pilih Gejala yang Terdeteksi:")
gejala_1 = st.checkbox("Layar muncul garis warna-warni")
gejala_2 = st.checkbox("Terdengar bunyi 'Beep' saat dinyalakan")
gejala_3 = st.checkbox("Kipas sangat berisik dan bodi bawah panas")

# TAMPILAN OUTPUT / HASIL DIAGNOSA 
if st.button("Proses Diagnosa"):
    st.info("Hasil Analisis Sistem:")
    
    # Logika Model (BAB 2.2: PEMBAHASAN) [cite: 34, 42]
    if gejala_1:
        st.error("Rekomendasi: Periksa kabel flexibel atau ganti Panel LCD.")
    elif gejala_2:
        st.error("Rekomendasi: Bersihkan pin RAM menggunakan penghapus atau ganti RAM.")
    elif gejala_3:
        st.warning("Rekomendasi: Bersihkan debu pada fan dan ganti Thermal Paste.")
    else:
        st.success("Sistem tidak mendeteksi kerusakan pada hardware tersebut.")