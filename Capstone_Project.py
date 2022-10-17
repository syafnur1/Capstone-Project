import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(layout="wide")
image = Image.open("Barantum.png")
st.image(image, use_column_width='auto', caption = "Sumber : barantum.com")

'''
    # Analisis Pemulihan sektor Pariwisata pasca Pandemi di Indonesia
    Capstone Project with **streamlit** by Zulfikri Syafnur
    
    ---
'''

'''
## Kesiapan *Stakeholder* dalam membangkitkan kembali Pariwisata
[Pariwisata](https://id.wikipedia.org/wiki/Pariwisata) merupakan cara suatu negara mempromosikan negara tersebut sehingga dapat dikinjungi oleh banyak orang. Di Indonesia, contoh pariwisata yang menjadi tujuan wisata yang terkenal di dunia adalah [Bali](https://bali.com/). Bali terkenal dengan berbagai objek wisatanya seperti wisata alam, wisata budaya, dan wisata bahari
'''

st.subheader("Jumlah Wisatawan Asing Masuk ke Indonesia")
df = pd.DataFrame([[13514963], [16106954], [4052923], [1557530], [202823]],
                    index=['2018', '2019', '2020', '2021', '2022'],
                    columns=['Jumlah Turis'])
st.line_chart(data=df, use_container_width=True) 
st.caption('Sumber : Badan Pusat Statistik')

col1, col2 = st.columns(2)

st.subheader("Hubungan Jumlah Turis dengan Pandemi")

with col1:
   st.header("Jumlah Turis per Pintu Masuk")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("Kasus Positif Harian Covid di Indoneai")
   st.image("https://static.streamlit.io/examples/dog.jpg")


# Deklarasi dataset
#df1 = pd.read_excel('/content/Data Gabungan Turis.xlsx', sheet_name='Sheet2')

# Data prep

# End of Data Prep

# Image / can change with interactive DB
#image = Image.open("TurisTahun.png")
#st.image(image, use_column_width='auto', caption = "Sumber : Badan Pusat Statistik")

'''Menurut Badan Pusat Statistik, tingkat wisatawan mancanegara (wisman) yang datang ke Indonesia dari hingga tahun 2019 mengalami kenaikan sebanyak **2 juta** wisman, hal ini dapat dilihat pada grafik diatas. Namun saat tingkat wisman yang datang sedang tinggi, terjadi pandemi covid-19 di seluruh dunia termasuk Indonesia pada awal tahun 2020. Hal ini memberikan dampak negatif dengan menurun drastisnya wisman ke Indonesia mencapai **1000%** di tahun 2020.'''

# CHart
#df1= df.iloc[0:10]
#st.line_chart(data=df1, x = 'Ship Date', y = 'Profit', width=0, height=0, use_container_width=True)

#st.bar_chart(data=df1, x = 'Ship Date', y = 'Profit')

''' ### Hubungan Jumlah Turis dengan Pandemi'''

# Grafik jumlah turis pintu masuk dan covid harian
# Grafik korelasi
''' Dari kedua grafik diatas dapat diambil kesimpulan bahwa kasus Covid-19 yang muncul di tahun 2020 mempengaruhi jumlah wisman 
yang masuk ke Indonesia dari berbagai Pintu Masuk. Menjadi sangat sedikit ketika kasus positif harian mencapai puncaknya di tahun 2021. '''

# top 5 negara terbanyak ke indonesia

''' Dapat dilihat bahwa wisman yang banyak berpariwisata ke indonesia adalah negara-negara tetangga,
mayoritas berasal dari benua Asia dan Australia yang jaraknya tidak jauh dari Indonesia. '''

# Machine Learning + grafiknya

'''
# Daftar Pustaka
[BPS](https://www.bps.go.id/indicator/16/1150/1/jumlah-kunjungan-wisatawan-mancanegara-per-bulan-ke-indonesia-menurut-pintu-masuk-2017---sekarang.html)

[Kawal Covid 19](https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/htmlview)

[Model Decision Tree untuk Prediksi Jadwal Kerja menggunakan Scikit-Learn](https://jurnal.umj.ac.id/index.php/semnastek/article/view/5239/3517)

[barantum.com](https://www.barantum.com/blog/wp-content/uploads/2019/01/Wisata-Indonesia-Mempunyai-Peluang-Bisnis.jpg)
'''   
