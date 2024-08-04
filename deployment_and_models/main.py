import streamlit as st
import klasifikasi_penyakit
import klasifikasi_nutrisi

st.set_page_config(
    page_title = ' Final Project - Deteksi Nutrisi dan Penyakit Pada Tanaman Padi',
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state = 'expanded'
)

# st.markdown("![Alt Text](https://giffiles.alphacoders.com/107/107600.gif)")
PAGES = {
    'Aplikasi 1 - Deteksi Penyakit' : klasifikasi_penyakit,
    'Aplikasi 2 - Deteksi Nutrisi': klasifikasi_nutrisi,

}

st.sidebar.title('Menu')
selection = st.sidebar.selectbox('Pilih Aplikasi', list(PAGES.keys()))
page = PAGES [selection]
page.app()