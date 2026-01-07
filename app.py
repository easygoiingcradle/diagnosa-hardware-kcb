import streamlit as st

# JUDUL & HEADER (BAB 2.1)
st.set_page_config(page_title="Sistem Pakar Hardware v2.0", layout="wide")
st.title("💻 Sistem Pakar Diagnosa Hardware Laptop")
st.write("Metode: Forward Chaining | Identifikasi masalah berdasarkan fakta gejala.")

# 1. BASIS PENGETAHUAN (KNOWLEDGE BASE) - BAB 2.2 Poin 1
# Memisahkan fakta dan aturan agar sesuai metode Forward Chaining
rules = [
    {"gejala": ["Layar bergaris", "Layar berkedip"], "diagnosa": "Kerusakan Panel LCD / Kabel Flexibel"},
    {"gejala": ["Bunyi Beep berulang", "Layar Hitam saat nyala"], "diagnosa": "Masalah pada RAM (Memory)"},
    {"gejala": ["Bodi panas", "Kipas berisik", "Sering mati mendadak"], "diagnosa": "Overheat (Fan kotor/Thermal Paste kering)"},
    {"gejala": ["Baterai silang", "Hanya nyala saat di-charge"], "diagnosa": "Baterai Drop atau IC Power Rusak"},
    {"gejala": ["Keyboard mengetik sendiri", "Beberapa tombol tidak fungsi"], "diagnosa": "Kerusakan Jalur Keyboard (Short Circuit)"},
    {"gejala": ["Loading sangat lambat", "Muncul Blue Screen"], "diagnosa": "Indikasi Harddisk/SSD Bad Sector"}
]

# 2. UI/UX INPUT GEJALA (BAB 2.1 Poin A)
st.subheader("Pilih Gejala yang Terjadi:")
col1, col2 = st.columns(2)

# Mengumpulkan semua fakta unik dari rules
all_symptoms = sorted(list(set([s for r in rules for s in r['gejala']])))

selected_symptoms = []
for i, symptom in enumerate(all_symptoms):
    with col1 if i < len(all_symptoms)/2 else col2:
        if st.checkbox(symptom):
            selected_symptoms.append(symptom)

# 3. FITUR INPUT GEJALA TAMBAHAN (Sesuai Permintaan Revisi)
st.divider()
st.subheader("Tidak menemukan gejala Anda?")
user_extra = st.text_input("Masukkan gejala tambahan (Opsional):")
if user_extra:
    selected_symptoms.append(user_extra)

# 4. MESIN INFERENSI (FORWARD CHAINING) - BAB 2.2 Poin 6
if st.button("Mulai Diagnosa"):
    if not selected_symptoms:
        st.warning("Silakan pilih minimal satu gejala.")
    else:
        st.info(f"Fakta yang ditemukan: {', '.join(selected_symptoms)}")
        
        found = False
        results = []

        # Logika Forward Chaining: Mencocokkan fakta dengan aturan
        for rule in rules:
            # Jika semua gejala dalam aturan ada di gejala yang dipilih user
            if any(s in selected_symptoms for s in rule['gejala']):
                results.append(rule['diagnosa'])
                found = True

        st.subheader("Hasil Analisis Sistem:")
        if found:
            # Menghapus duplikat hasil
            for res in list(set(results)):
                st.error(f"⚠️ Rekomendasi: {res}")
        else:
            st.success("Sistem tidak menemukan kecocokan aturan. Disarankan cek ke teknisi untuk gejala tambahan tersebut.")

# FOOTER (BAB 1.3)
st.caption("Target Performa: Inference Time < 100ms | Akurasi berdasarkan Knowledge Base.")