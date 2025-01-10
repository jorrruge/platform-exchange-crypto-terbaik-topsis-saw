import streamlit as st
import pandas as pd

# Load the CSV file
file_path = "AHP TOPSIS SAW.csv"
data = pd.read_csv(file_path)

# Streamlit App
st.title("Visualisasi Data AHP, TOPSIS, SAW, dan AHP TOPSIS SAW")

# Bagian 1: AHP Pembobotan
st.header("1. AHP Pembobotan")
bobot_df = data[data['Sheet'] == 'AHP Pembobotan'].drop(columns=['Sheet'])

if not bobot_df.empty:
    st.write("### Data Bobot")
    st.dataframe(bobot_df)

# Bagian 2: TOPSIS
st.header("2. Perhitungan TOPSIS")
topsis_df = data[data['Sheet'] == 'TOPSIS'].drop(columns=['Sheet'])

if not topsis_df.empty:
    st.write("### Data TOPSIS")
    st.dataframe(topsis_df)

    # Alternatif nilai tertinggi dan terendah
    highest_alternative = topsis_df.iloc[topsis_df.iloc[:, 1].idxmax()]
    lowest_alternative = topsis_df.iloc[topsis_df.iloc[:, 1].idxmin()]

    st.write(f"### Alternatif dengan Nilai Tertinggi:")
    st.write(highest_alternative)

    st.write(f"### Alternatif dengan Nilai Terendah:")
    st.write(lowest_alternative)

# Bagian 3: SAW
st.header("3. Peringkat SAW")
saw_df = data[data['Sheet'] == 'SAW'].drop(columns=['Sheet'])

if not saw_df.empty:
    st.write("### Data Peringkat")
    st.dataframe(saw_df)

# Bagian 4: AHP TOPSIS SAW
st.header("4. Peringkat Berdasarkan AHP TOPSIS SAW")
average_df = data[data['Sheet'] == 'AHP TOPSIS SAW'].drop(columns=['Sheet'])

if not average_df.empty:
    st.write("### Data AHP TOPSIS SAW")
    st.dataframe(average_df)

    # Dropdown untuk memilih kriteria
    selected_kriteria = st.selectbox("Pilih Kriteria untuk Penilaian:", average_df.columns[1:])

    if selected_kriteria:
        # Menghitung nilai akhir berdasarkan kriteria
        average_df["Nilai Akhir"] = average_df[selected_kriteria]
        sorted_average_df = average_df.sort_values(by="Nilai Akhir", ascending=False)

        st.write(f"### Peringkat Alternatif Berdasarkan: {selected_kriteria}")
        st.dataframe(sorted_average_df[[average_df.columns[0], "Nilai Akhir"]])
