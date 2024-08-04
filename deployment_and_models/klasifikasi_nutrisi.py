import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import os
from tensorflow import keras

def app():
    
    st.title("Deteksi Gejala Defisiensi Gizi pada Tanaman Padi")

    st.write("Defisiensi gizi pada tanaman padi sangat mempengaruhi kualitas padi tersebut. Terdapat tiga kandungan yang merupakan makronutrien utama dalam tanaman padi, yaitu Nitrogen (N), Fosfor (P), dan Kalium (K) (Shrestha dkk, 2020).")

    im = Image.open("pone.0113200.g001.tif")
    st.image(im, caption="Perbandingan antara daun padi yang sehat dengan yang mengalami defisiensi gizi (Chen L dkk, 2014).")

    st.markdown("***")

    st.header("Defisiensi Nitrogen (N)")
    st.write("""
             - Daun tua atau seluruh tanaman berwarna hijau kekuningan.
             """)
    n0 = Image.open("n0.JPG")
    st.image(n0, use_column_width="auto")
    with st.expander("Pencegahan"):
        st.subheader("Pencegahan:")
        st.write("""
                - Berikan lahan dengan drainase terbaik dan jangan terlalu sering menyiram tanaman.
                - Pastikan untuk menyirami tanaman secara teratur selama musim kering.
                - Pastikan untuk menambahkan bahan organik, misalnya kompos, pupuk kandang, atau mulsa.
                """)
    with st.expander("Penanganan"):
        st.subheader("Penanganan:")
        st.write("""
                - Pemakaian Pupuk N secara efisien, yaitu pupuk yang mengandung banyak unsur Nitrogen.
                """)

    st.markdown("***")

    st.header("Defisiensi Fosfor (P)")
    st.write("""
             - Ujung daun berwarna coklat kekuningan.
             - Daun cenderung kecil, pendek, dan memiliki warna hijau tua yang cukup gelap, dan terkadang muncul warna ungu kemerahan pada daun tersebut.
             """)
    p0 = Image.open("p0.JPG")
    st.image(p0, use_column_width="auto")   
    with st.expander("Pencegahan"):
        st.subheader("Pencegahan:")
        st.write("""
                - Gunakan varietas yang efisien dalam menyerap fosfor dari tanah.
                - Pastikan pemupukan tanaman yang seimbang dan efisien.
                - Kubur sisa-sisa tanaman ke dalam tanah setelah panen.
                - Gunakan pendekatan terpadu dengan pupuk mineral dan organik untuk menjaga keseimbangan unsur hara tanah.
                """)
    with st.expander("Penanganan"):
        st.subheader("Penanganan:")
        st.write("""
                - Pemakaian Pupuk P secara efisien, yaitu pupuk yang mengandung banyak unsur Fosfor.
                """)

    st.markdown("***")

    st.header("Defisiensi Kalium (K)")  
    st.write("""
             - Ujung daun berwarna coklat kekuningan.
             - Garis-garis kuning mungkin muncul di sepanjang sela-sela daun dan daun bagian bawah mungkin menekuk ke bawah.
            """)
    k0 = Image.open("k0.JPG")
    st.image(k0, use_column_width="auto")
    with st.expander("Pencegahan"):
        st.subheader("Pencegahan:")
        st.write("""
                - Tanam varietas yang lebih efisien dalam penyerapan kalium.
                - Pastikan penggunaan pupuk yang seimbang untuk menjamin pasokan unsur hara yang tepat untuk tanaman.
                - Tambahkan bahan organik ke tanah berupa pupuk kandang atau mulsa tanaman.
                - Siram tanaman secara teratur dan hindari menggenangi lahan.
                """)
    with st.expander("Penanganan"):
        st.subheader("Penanganan:")
        st.write("""
                - Pemakaian Pupuk K secara efisien, yaitu pupuk yang mengandung banyak unsur Kalium.
                """)

    st.markdown("***")

    st.header("Petunjuk Penggunaan Aplikasi:")
    st.write("Dalam menggunakan aplikasi, diharap agar pengguna menyiapkan gambar berformat JPG/PNG yang hanya mengandung satu helai daun padi dalam posisi vertikal atau horizontal.")

    st.subheader("Gambar Vertikal:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Defisiensi Nitrogen (N)")
        n1 = Image.open("n1.JPG")
        n1 = n1.resize((round(n1.size[0]*0.15), round(n1.size[1]*0.15)))
        st.image(n1)
    with col2:
        st.write("Defisiensi Fosfor (P)")
        p1 = Image.open("p1.JPG")
        p1 = p1.resize((round(p1.size[0]*0.15), round(p1.size[1]*0.15)))
        st.image(p1)
    with col3:
        st.write("Defisiensi Kalium (K)")
        k1 = Image.open("k1.JPG")
        k1 = k1.resize((round(k1.size[0]*0.15), round(k1.size[1]*0.15)))
        st.image(k1)
        
    st.subheader("Gambar Horizontal:")
    st.write("Defisiensi Nitrogen (N)")
    n2 = Image.open("n2.JPG")
    st.image(n2)
        
    st.write("Defisiensi Fosfor (P)")
    p2 = Image.open("p2.JPG")
    st.image(p2)

    st.write("Defisiensi Kalium (K)")
    k2 = Image.open("k2.JPG")
    st.image(k2)

    st.markdown("***")
    
    #@st.cache(allow_output_mutation=True)
    def load_model():
        # model_path = 'rice_nutrient_model.hdf5'
        model_path = os.path.join(os.path.dirname(__file__), 'rice_nutrient_model.hdf5')

        
        if os.path.exists(model_path):
            model = tf.keras.models.load_model(model_path)
            return model
        else:
            raise FileNotFoundError(f"Model file not found: {model_path}")
        
        return model
    #Load the model
    model = load_model()
    def import_and_predict(image_data, model):
        size = (224,224)
        image = ImageOps.fit(image_data, size, Image.LANCZOS) #resize image
        img = tf.keras.preprocessing.image.img_to_array(image)
        img = img/255.0
        img_reshape = np.array(img)
        img_reshape = np.expand_dims(img_reshape, axis = 0)
        prediction = model.predict(img_reshape) 

        return prediction

    uploaded_file = st.file_uploader("Tekan tombol Browse files dan arahkan ke lokasi gambar.", type=["jpg","png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded file', use_column_width="auto")
        st.write("")
        st.write("Mengklasifikasi...")
        predictions = import_and_predict(image, model)
        label = np.argmax(predictions)
        if label == 0:
            st.write("Defisiensi Nitrogen (N)")
            st.write("Penanganan:")
            st.write("""
                    - Pemakaian Pupuk N secara efisien, yaitu pupuk yang mengandung banyak unsur Nitrogen.
                    """)
        if label == 1:
            st.write("Defisiensi Fosfor (P)")
            st.write("Penanganan:")
            st.write("""
                    - Pemakaian Pupuk P secara efisien, yaitu pupuk yang mengandung banyak unsur Fosfor.
                    """)
        if label == 2:
            st.write("Defisiensi Kalium (K)")
            st.write("Penanganan:")
            st.write("""
                    - Pemakaian Pupuk K secara efisien, yaitu pupuk yang mengandung banyak unsur Kalium.
                    """)

    st.markdown("***")

    st.header("Referensi")
    st.subheader("Dataset yang dipakai:")
    st.write("""
             - Kaggle: https://www.kaggle.com/guy007/nutrientdeficiencysymptomsinrice
            """)
    st.subheader("Publikasi:")
    st.write("""
             - Shrestha, Jiban & Kandel, Manoj & Subedi, Subash & Shah, Kabita. (2020). Role of nutrients in rice (Oryza sativa L.): A review. Agrica. 9. 53-62. 10.5958/2394-448X.2020.00008.5.
             - Chen L, Lin L, Cai G, Sun Y, Huang T, et al. (2014) Identification of Nitrogen, Phosphorus, and Potassium Deficiencies in Rice Based on Static Scanning Technology and Hierarchical Identification Method. PLOS ONE 9(11): e113200. https://doi.org/10.1371/journal.pone.0113200
             - Dobermann, A. and Fairhurst, T. (2000) Rice: Nutrient Disorders & Nutrient Management. Handbook Series, Potash & Phosphate Institute (PPI), Potash & Phosphate Institute of Canada (PPIC) and International Rice Research Institute, Philippine, 191.
            """)
    st.subheader("Halaman Internet:")
    st.write("""
             - https://plantix.net/id/library/plant-diseases/700006/nitrogen-deficiency
             - https://plantix.net/id/library/plant-diseases/700005/phosphorus-deficiency
             - https://plantix.net/id/library/plant-diseases/700002/potassium-deficiency
            """)
