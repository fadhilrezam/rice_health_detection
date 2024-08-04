import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
import numpy as np
from tensorflow import keras
import os

def app():
    #st.set_option('deprecation.showfileUploaderEncoding', False)
    #@st.cache(allow_output_mutation=True)

    def load_model():
        model_path = 'models/rice_disease_model.hdf5'
        if os.path.exists(model_path):
            model = tf.keras.models.load_model(model_path)
            return model
        else:
            raise FileNotFoundError(f"Model file not found: {model_path}")

    #Load the model
    model = load_model()
    
    st.title('Deteksi Penyakit (Blas, Blight, dan Tungro) pada Tanaman Padi')
    st.write("Penyakit pada tanaman padi sangat mempengaruhi kualitas padi tersebut. Terdapat tiga penyakit yang menjadi objek aplikasi ini, yaitu Blas, Blight, dan Tungro.")
    
    st.markdown("***")
    
    st.header("Penyakit Blas")
    st.write("""
             - Penyakit blas juga sering disebut sebagai busuk leher, patah leher, tekek (jawa Tengah), kecekik (Jawa Barat).
             - Penyakit blas disebabkan oleh jamur Pyricularia grisea.
             - Jamur ini dapat menginfeksi pada semua fase pertumbuhan tanaman padi, mulai dari fase pembibitan sampai pada fase generatif.
             - Daun terdapat becak coklat berbentuk belah ketupat dan memanjang searah dengan urat daun.
            """)
    b1 = Image.open("b1.jpg")
    b1 = b1.resize((round(b1.size[0]*0.15), round(b1.size[1]*0.15)))
    st.image(b1, use_column_width="auto")
    with st.expander("Pencegahan"):
        st.subheader("Pencegahan:")
        st.write("""
                - Sanitasi Lingkungan
                    - Menjaga kebersihan lingkungan sawah dari gulma yang mungkin menjadi inang alternatif dan membersihkan sisa-sisa tanaman yang terinfeksi merupakan usaha yang sangat dianjurkan mengingat patogen dapat bertahan pada inang alternatif dan sisa-sisa tanaman.
                - Pemberian Kompos Jerami
                    - Pemberian bahan organik berupa jerami sisa panen untuk penyehatan lahan harus dikomposkan lebih dulu. Pengkomposan jerami dapat menyebabkan miselia dan spora jamur mati, karena naiknya suhu selama proses dekoposisi.
                """)
    with st.expander("Penanganan"):
        st.subheader("Penanganan:")
        st.write("""
                - Gunakan varietas tahan sesuai dengan sebaran ras yang ada di daerah setempat.
                - Gunakan benih sehat.
                - Hindarkan penggunaan pupuk nitrogen diatas dosis anjuran.
                - Hindarkan tanam padi dengan varietas yang sama terus menerus sepanjang tahun.
                - Sanitasi lingkungan harus intensif karena inang alternatif patogen dapat berupa rerumputan.
                - Hindari tanam padi terlambat dari tanaman petani di sekitarnya.
                - Pengendalian secara dini dengan perlakuan benih sangat dianjurkan untuk menyelamatkan persemaian sampai umur 30 hari setelah sebar.
                - Penyemprotan fungisida sistemik sebaiknya 2 kali pada saat stadia tanaman anakan maksimum dan awal berbunga untuk mencegah penyakit blas daun dan blas leher terutama di daerah endemik.
                - Hindarkan jarak tanam rapat (sebar langsung).
                - Pemakaian kompos sebagai sumber bahan organik.
                """)

    st.markdown("***")
    
    st.header("Penyakit Blight")
    st.write("""
             - Penyakit blight juga sering disebut sebagai kresek, hawar daun, lodoh (Jawa).
             - Penyakit blight disebabkan oleh bakteri Xanthomonas oryzae pv. oryzae (Xoo).
                - Patogen ini dapat mengenfeksi tanaman padi pada semua fase pertumbuhan tanaman dari mulai pesemaian sampai menjelang panen.
             - Bila serangan terjadi pada awal pertumbuhan, tanaman menjadi layu dan mati, gejala ini disebut kresek.
                - Gejala kresek sangat mirip dengan gejala sundep yang timbul akibat serangan penggerek batang pada fase tenaman vegetatif.
             - Pada tanaman dewasa penyakit hawar daun bakteri menimbulkan gejala hawa (blight).
                - Baik gejala kresek maupun hawar, gejala dimulai dari tepi daun, berwarna keabu-abuan dan lama-lama daun menjadi kering.
            - Penyakit ini termasuk dalam kategori penyakit yang terbawa oleh benih (seed borne diseases). Penyakit akan berkembang dari benih padi yang terinfeksi oleh patogen.
            """)
    b2 = Image.open("b2.jpg")
    b2 = b2.resize((round(b2.size[0]*0.15), round(b2.size[1]*0.15)))
    st.image(b2, use_column_width="auto")
    with st.expander("Pencegahan"):
        st.subheader("Pencegahan:")
        st.write("""
                - Penanaman Benih dan Bibit Sehat
                    - Bibit yang sudah terinfeksi/bergejala penyakit hawar daun bakteri (HDB) sebaiknya tidak ditanam.
                - Pemupukan
                    - Perkembangan penyakit dapat ditekan dan diperoleh produksi yang tinggi disarankan menggunakan pupuk N dan K secara berimbang dengan menghindari pemupukan N terlalu tinggi.
                - Sanitasi Lingkungan
                    - Menjaga kebersihan lingkungan sawah dari gulma yang mungkin menjadi inang alternatif dan membersihkan sisa-sisa tanaman yang terinfeksi merupakan usaha yang sangat dianjurkan mengingat patogen dapat bertahan pada inang alternatif dan sisa-sisa tanaman.
                """)
    with st.expander("Penanganan"):
        st.subheader("Penanganan:")
        st.write("""
                - Bibit padi yang ditanam tidak dipotong pada bagian ujungnya.
                - Jarak tanam jangan terlalu rapat, disarankan dengan cara tanam jejer legowo.
                - Pengairan berselang (intermiten), hindari penggenangan yang terus-menerus.
                - Pemupukan berimbang, jangan terlalu banyak pupuk N.
                - Jika intensitas penyakit melebihi 20%, semprot dengan bakterisida.
                """)

    st.markdown("***")
    
    st.header("Penyakit Tungro")
    st.write("""
             - Terjadi perubahan warna daun terutama pada daun muda berwarna kuning oranye dimulai dari ujung daun.
             - Daun muda agak menggulung.
             - Penyakit tungro disebabkan oleh dua jenis virus yaitu virus yang berbentuk batang atau virus batang tungro padi Rice tungro bacilliform virus (RTBV) dan virus berbentuk bulat atau virus bulat tungro padi Rice tungro spherical virus (RTSV).
                - Kedua virus tersebut ditularkan oleh beberapa spesies wereng hijau dan wereng daun lainnya.
            """)
    t1 = Image.open("t1.jpg")
    t1 = t1.resize((round(t1.size[0]*0.15), round(t1.size[1]*0.15)))
    st.image(t1, use_column_width="auto")
    with st.expander("Pencegahan"):
        st.subheader("Pencegahan:")
        st.write("""
                - Tanam Serempak
                    - Penyakit tungro akan selalu ada pada daerah dengan pola tanam tidak serempak dan penanaman sepanjang tahun. Untuk mengurangi serangan penyakit tungro, dianjurkan tanam serempak minimal pada luasan 40 ha.
                - Mengatur Waktu Tanam yang Tepat
                    - Tanam pada saat yang tepat dimaksudkan agar supaya pada saat fase pertumbuhan tanaman padi peka dapat terhindar dari serangan penyakit tungro. Waktu tanam tepat diidentifikasi berdasarkan pola fluktuasi populasi wreng hijau, keberadaan virus tungro dan iklim terutama curah hujan.  Fase pertumbuhan tanaman padi peka terhadap serangan tungro adalah pada saat tanaman berumur kurang dari 45 hari setelah tanam.
                - Penanaman Benih yang Baik
                    - Menanam tanaman padi dengan varietas baik (tahan terhadap hama) adalah komponen penting dalam pengendalian penyakit tungro. Sekalipun varietas tersebut terserang penyakit, tanaman tidak akan menunjukkan kerusakan yang fatal sehingga dapat menghasilkan gabah yang normal.
                """)
    with st.expander("Penanganan"):
        st.subheader("Penanganan:")
        st.write("""
                - Waktu Tanam Tepat.
                - Tanam Serempak.
                - Penanaman Benih yang Baik.
                - Memusnahkan (eradikasi) tanaman terserang.
                - Penggunaan Pestisida.
                """)
    
    st.markdown("***")
    
    #upload image
    st.header("Petunjuk Penggunaan Aplikasi:")
    st.write("Dalam menggunakan aplikasi, diharap agar pengguna menyiapkan gambar berformat JPG/PNG yang hanya mengandung satu helai daun padi dalam posisi vertikal.")
    
    st.subheader("Gambar Vertikal:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Penyakit Blas")
        b11 = Image.open("b11.jpg")
        b11 = b11.resize((round(b11.size[0]*0.15), round(b11.size[1]*0.15)))
        st.image(b11)
    with col2:
        st.write("Penyakit Blight")
        b21 = Image.open("b21.jpg")
        b21 = b21.resize((round(b21.size[0]*0.15), round(b21.size[1]*0.15)))
        st.image(b21)
    with col3:
        st.write("Penyakit Tungro")
        t2 = Image.open("t2.jpg")
        t2 = t2.resize((round(t2.size[0]*0.15), round(t2.size[1]*0.15)))
        st.image(t2)
    
    file = st.file_uploader('Tekan tombol Browse files dan arahkan ke lokasi gambar.', type = ['jpg','png'])

    def import_and_predict(image_data, model):
        size = (224,224)
        image = ImageOps.fit(image_data, size, Image.LANCZOS) #resize image
        img = tf.keras.preprocessing.image.img_to_array(image)
        img = img/255.0
        img_reshape = np.array(img)
        img_reshape = np.expand_dims(img_reshape, axis = 0)
        prediction = model.predict(img_reshape) 

        return prediction

    if file is None:
        st.text('Silahkan unggah gambar terlebih dahulu untuk dapat memprediksi penyakit.')
    else:
        image = Image.open(file)
        col1, col2, col3= st.columns((0.5,1,0.5))
        with col1:
            st.write("")
        with col2:
            st.image(image, use_column_width = True)
        predictions = import_and_predict(image, model)
        class_names = ['Blas','Blight','Tungro']
        value = class_names[np.argmax(predictions)]
        st.header('Hasil Prediksi Penyakit: ')
        new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 35px;">Tanaman Padi ini memiliki penyakit {value}</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        with col3:
            st.write("")
        
        #Keterangan Penyakit Blas, cara mencegah dan mengendalikan penyakit
        if value == 'Blas':
            st.subheader("Penanganan:")
            st.write("""
                     - Gunakan varietas tahan sesuai dengan sebaran ras yang ada di daerah setempat.
                     - Gunakan benih sehat.
                     - Hindarkan penggunaan pupuk nitrogen diatas dosis anjuran.
                     - Hindarkan tanam padi dengan varietas yang sama terus menerus sepanjang tahun.
                     - Sanitasi lingkungan harus intensif karena inang alternatif patogen dapat berupa rerumputan.
                     - Hindari tanam padi terlambat dari tanaman petani di sekitarnya.
                     - Pengendalian secara dini dengan perlakuan benih sangat dianjurkan untuk menyelamatkan persemaian sampai umur 30 hari setelah sebar.
                     - Penyemprotan fungisida sistemik sebaiknya 2 kali pada saat stadia tanaman anakan maksimum dan awal berbunga untuk mencegah penyakit blas daun dan blas leher terutama di daerah endemik.
                     - Hindarkan jarak tanam rapat (sebar langsung).
                     - Pemakaian kompos sebagai sumber bahan organik.
                    """)
    
        #Keterangan Penyakit Blight, cara mencegah dan mengendalikan penyakit
        elif value == 'Blight':
            st.subheader('Penanganan:')
            st.write("""
                     - Bibit padi yang ditanam tidak dipotong pada bagian ujungnya.
                     - Jarak tanam jangan terlalu rapat, disarankan dengan cara tanam jejer legowo.
                     - Pengairan berselang (intermiten), hindari penggenangan yang terus-menerus.
                     - Pemupukan berimbang, jangan terlalu banyak pupuk N.
                     - Jika intensitas penyakit melebihi 20%, semprot dengan bakterisida.
                    """)

        #Keterangan Penyakit Tungro, cara mencegah dan mengendalikan penyakit
        elif value == 'Tungro':
            st.subheader('Keterangan Penyakit:')
            st.write('Penyakit Tungro merupakan penyakit padi yang disebabkan oleh dua jenis virus yaitu virus yang berbentuk batang atau virus batang tungro padi Rice tungro bacilliform virus (RTBV), dan virus berbentuk bulat atau virus bulat tungro padi Rice tungro spherical virus (RTSV). Kedua virus tersebut ditularkan oleh beberapa spesies wereng hijau dan wereng daun lainnya. ')
            st.write('Tanaman padi yang terinfeksi virus-virus tungro umumnya tampak kerdil dan daun berwarna kuning terutama pada daun muda.')
            st.write('\n')
            
            st.subheader("Penanganan:")
            st.write("""
                     - Waktu Tanam Tepat.
                     - Tanam Serempak.
                     - Penanaman Benih yang Baik.
                     - Memusnahkan (eradikasi) tanaman terserang.
                     - Penggunaan Pestisida.
                    """)
    
    st.markdown("***")
    
    st.header("Referensi")
    st.subheader("Dataset yang dipakai:")
    st.write("""
             - Kaggle: https://www.kaggle.com/tedisetiady/leaf-rice-disease-indonesia
            """)
    st.subheader("Halaman Internet:")
    st.write("""
             - https://bbpadi.litbang.pertanian.go.id/index.php/info-berita/info-teknologi/penyakit-blas-pada-tanaman-padi-dan-cara-pengendaliannya
             - https://tabloidsinartani.com/detail/indeks/agri-sarana/12779-Jangan-Sampai-Padi-Bablas-Kenali-dan-Kendalikan-Penyakit-Blas
             - https://bbpadi.litbang.pertanian.go.id/index.php/info-berita/info-teknologi/pengendalian-penyakit-kresek-dan-hawar-daun-bakteri
             - https://distan.bulelengkab.go.id/informasi/detail/artikel/penyakit-tungro-pada-tanaman-padi-dan-cara-pengendaliannya-44
            """)