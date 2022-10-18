import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image

st.set_page_config(page_title="Capstone Project",
                   page_icon=":airplane:",
                   layout="wide")

header = st.container()
pendahuluan = st.container()
korelasi = st.container()
negara = st.container()
penutup = st.container()
pustaka = st.container()
kontak = st.container()

with header:
    image = Image.open("Barantum.png")
    st.image(image, use_column_width='auto')
    st.caption("""<a style='display: block; text-align: center;color: black;' 
               href="https://www.barantum.com/blog/wp-content/uploads/2019/01/Wisata-Indonesia-Mempunyai-Peluang-Bisnis.jpg)">Sumber: barantum.com</a>""", 
               unsafe_allow_html=True)
    st.title('Analisis Pemulihan Sektor :airplane: Pariwisata Pasca Pandemi di Indonesia')
    st.markdown('Capstone Project with **streamlit** by Zulfikri Syafnur')
    st.markdown('_________________')

with pendahuluan:
    st.header('Kesiapan *Stakeholder* dalam membangkitkan kembali Pariwisata')
    st.markdown('''[Pariwisata](https://id.wikipedia.org/wiki/Pariwisata) merupakan cara suatu negara mempromosikan negara tersebut 
                sehingga dapat dikinjungi oleh banyak orang. Di Indonesia, contoh pariwisata yang menjadi tujuan wisata yang terkenal 
                di dunia adalah [Bali](https://bali.com/). Bali terkenal dengan berbagai objek wisatanya seperti wisata alam, wisata budaya, 
                dan wisata bahari''')
    st.subheader("Jumlah Turis Asing Masuk ke Indonesia")
    
    d = {'Tahun': ['2018','2019', '2020', '2021', '2022'],
         'Jumlah Turis': [13514963, 16106954, 4052923, 1557530, 202823]}
    
    df = pd.DataFrame(data = d)
    # grafik 1
    plost.line_chart(df, x='Tahun', y='Jumlah Turis', color='red', legend='bottom', 
                     pan_zoom='both', title='Jumlah Turis per Tahun',
                     x_annot={'2020': "Ini ketika Pandemi Covid melanda Indonesia"},
                    )
    st.caption("""<a style='display: block; text-align: center;color: black;'
    href="https://www.bps.go.id/indicator/16/1150/1/jumlah-kunjungan-wisatawan-mancanegara-per-bulan-ke-indonesia-menurut-pintu-masuk-2017---sekarang.html">
    Sumber: Badan Pusat Statistik</a>""",unsafe_allow_html=True)
    st.markdown('''Menurut Badan Pusat Statistik, tingkat turis (wisatawan mancanegara) yang datang ke Indonesia hingga tahun 2019 mengalami kenaikan 
                sebanyak **2 juta** turis, hal ini dapat dilihat pada grafik diatas. Namun saat tingkat turis yang datang sedang tinggi, terjadi 
                pandemi covid-19 di seluruh dunia termasuk Indonesia pada awal tahun 2020 hingga sekarang. Hal ini memberikan dampak negatif dengan 
                menurun drastisnya turis ke Indonesia mencapai **75 %** di tahun 2020.''')

# Grafik 2 & 3
with korelasi:
    st.subheader("Hubungan Jumlah Turis dengan Pandemi")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Jumlah Turis per Pintu Masuk")
        image = Image.open("Pinturis.png")
        st.image(image, use_column_width='auto')
        st.caption("""<a style='display: block; text-align: center;color: black;' href="https://www.bps.go.id/indicator/16/1150/1/jumlah-kunjungan-wisatawan-mancanegara-per-bulan-ke-indonesia-menurut-pintu-masuk-2017---sekarang.html">Sumber: Badan Pusat Statistik</a>""",unsafe_allow_html=True)
    with col2:
        st.subheader("Kasus Positif Harian Covid di Indonesia")
        image = Image.open("Positif.png")
        st.image(image, use_column_width='auto')
        st.caption("""<a style='display: block; text-align: center;color: black;' href="https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/htmlview">Sumber: Kawal Covid 19</a>""",unsafe_allow_html=True)
    st.markdown('''Dari kedua grafik diatas dapat diambil kesimpulan bahwa kasus Covid-19 yang muncul di tahun 2020 mempengaruhi jumlah turis yang 
                masuk ke Indonesia dari berbagai Pintu Masuk. Sehingga menjadi sangat sedikit turis yang masuk ketika kasus positif harian mencapai 
                puncaknya di tahun 2021.''')

    # korelasi
    st.markdown('**Apakah terdapat hubungan antara Jumlah Turis dengan Pandemi Covid?**')
    st.markdown('> - H0 : Tidak terdapat hubungan antara Jumlah Turis dengan Pandemi Covid')
    st.markdown('> - H1 : Terdapat hubungan antara Jumlah Turis dengan Pandemi Covid')

    code = '''r = nΣxy–(Σx)(Σy) / √{nΣx²–(Σx)²}{nΣy² – (Σy)²}'''
    st.code(code, language = 'python')

    df3 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQY21pKyD2OqXjhrC2JpODETvSyfj8fS8dWE87smTC4JoxnJDZV_n7gcFtjHzYFpCZGtrfnfMl1CxVN/pub?gid=0&single=true&output=csv')
    df3 = df3.rename(columns = {'Harian': 'Positif per Bulan', 'Turis' : 'Jumlah Turis'})

    col3, col4= st.columns([1.5,2.5])

    with col3:
        correlation_matrix = df3[['Positif per Bulan', 'Jumlah Turis']].corr()
        correlation_matrix 

    with col4:
        st.markdown('''Dari hasil korelasi dua data diatas, didapatkan bahwa **r = -0,42** . Hal ini berarti kita dapat mereject **H0**. 
                    Dengan demikian Pandemi Covid **mempengaruhi secara signifikan** terhadap Jumlah Turis yang memasuki Indonesia.''')

# Turis yang masuk per Negara Asal
with negara:
    st.subheader("Kunjungan Turis berdasarkan Negara Asal")
    # Deklarasi dataset
    country = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTXspAWpKN-lhLVzwafiDNnwXAUf_l_I-xsdO3AVT0bDzTsgS5NyMnaOQRB865eBscEt9NKka4cJ-pw/pub?gid=0&single=true&output=csv')
    
    country = country.drop(['Grand Total'], axis=1)
    st.dataframe(country.style.highlight_max(axis=0), use_container_width=True)
    
    st.markdown('''Dapat dilihat bahwa **Top 5** Turis yang banyak berkunjung ke Indonesia adalah negara-negara tetangga, dan mayoritas negara 
                tersebut berasal dari benua Asia yang jaraknya tidak jauh dari Indonesia.''')

# Machine Learning + grafik

with penutup:
    st.subheader("Penutup")
    st.markdown('Kesimpulan dan saran yang dapat ditarik dari grafik-grafik diatas adalah sebagai berikut :')
    st.markdown('''- Terdapat korelasi negatif antara Jumlah Turis yang masuk ke Indonesia dengan Pandemi Covid. Semakin tinggi Covid maka semakin rendah 
                Turis yang masuk.''')
    st.markdown('''- Agar pariwisata dapat segera pulih di Indonesia, berdasarkan *Grafik : Jumlah Turis per Pintu Masuk* dapat dilihat bahwa pintu 
                masuk via Udara adalah pintu masuk yang sangat sering digunakan Turis dibandingan via Darat dan via Laut, maka Pemerintah harus 
                mempercepat membuka kembali penerbangan yang masuk ke Indonesia.''')
    st.markdown('''- Kementrian Pariwisata juga harus memiliki inovasi-inovasi terbaik untuk mempromosikan Indonesia ke mancanegara agar Turis asing 
                berminat untuk datang ke Indonesia.''')

with pustaka:
    st.subheader("Daftar Pustaka")
    st.markdown('''
                [BPS](https://www.bps.go.id/indicator/16/1150/1/jumlah-kunjungan-wisatawan-mancanegara-per-bulan-ke-indonesia-menurut-pintu-masuk-2017---sekarang.html)
                
                [Kawal Covid 19](https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/htmlview)
                
                [Model Decision Tree untuk Prediksi Jadwal Kerja menggunakan Scikit-Learn](https://jurnal.umj.ac.id/index.php/semnastek/article/view/5239/3517)

                [barantum.com](https://www.barantum.com/blog/wp-content/uploads/2019/01/Wisata-Indonesia-Mempunyai-Peluang-Bisnis.jpg)

                [Statistika Non-Parametrik Analisis Jalur](https://slideplayer.info/slide/3099519)
                ''')

with kontak:
    st.subheader("Contacts")
    st.markdown('''
                [![MAIL Badge](https://img.shields.io/badge/-z26syafnur@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:z26syafnur@gmail.com)](mailto:z26syafnur@gmail.com)

                [![LinkedIn](https://img.shields.io/badge/syafnur-zulfikri-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/syafnur-zulfikri/)](https://www.linkedin.com/in/syafnur-zulfikri/)
                ''')
    
#9EA25D:y, #615DA2:b
footer="""<style>
a:link , a:visited{
color: "green";
background-color: transparent;
text-decoration: none;
}
a:hover,  a:active {
color: black;
background-color: transparent;
text-decoration: none;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: none;
color: #9EA25D;
text-align: left;
}
</style>
<div class="footer">
<p>(C) by Zulfikri Syafnur, 2022<a style='display: block; text-align: left;' href="" target="_blank">CP10-22</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)


# Data prep

# End of Data Prep

# Image / can change with interactive DB
#image = Image.open("TurisTahun.png")
#st.image(image, use_column_width='auto', caption = "Sumber : Badan Pusat Statistik")

# Chart
#df1= df.iloc[0:10]
#st.line_chart(data=df1, x = 'Ship Date', y = 'Profit', width=0, height=0, use_container_width=True)

#st.bar_chart(data=df1, x = 'Ship Date', y = 'Profit')
