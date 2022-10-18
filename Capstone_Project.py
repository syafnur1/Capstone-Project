import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import lorem
import altair as alt
from vega_datasets import data
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium
import plotly.graph_objects as go
import plotly.express as px
import plost

st.set_page_config(layout="wide")
image = Image.open("Barantum.png")
st.image(image, use_column_width='auto', caption = "Sumber : barantum.com")

'''
    # Analisis Pemulihan Sektor Pariwisata Pasca Pandemi di Indonesia
    Capstone Project with **streamlit** by Zulfikri Syafnur
    
    ---
'''

'''
## Kesiapan *Stakeholder* dalam membangkitkan kembali Pariwisata
[Pariwisata](https://id.wikipedia.org/wiki/Pariwisata) merupakan cara suatu negara mempromosikan negara tersebut sehingga dapat dikinjungi oleh banyak orang. Di Indonesia, contoh pariwisata yang menjadi tujuan wisata yang terkenal di dunia adalah [Bali](https://bali.com/). Bali terkenal dengan berbagai objek wisatanya seperti wisata alam, wisata budaya, dan wisata bahari
'''

st.subheader("Jumlah Turis Asing Masuk ke Indonesia")
d = {'Tahun': ['2018','2019', '2020', '2021', '2022'], 
       'Jumlah Turis': [13514963, 16106954, 4052923, 1557530, 202823]}
df = pd.DataFrame(data = d)

plost.line_chart(df, x='Tahun', y='Jumlah Turis', color='red', legend='top', pan_zoom='both', title='Jumlah Turis Asing Masuk ke Indonesia', x_annot={'2020': "Ini ketika Pandemi Covid melanda Indonesia"},)
#base = alt.Chart(df, title="Jumlah Turis Asing Masuk ke Indonesia", height=300, width=700).encode(alt.X('Tahun', axis=alt.Axis(title='Tahun'))
#line = base.mark_line(stroke='#5276A7', interpolate='monotone', point=alt.OverlayMarkDef(color="blue")).encode(x = 'Tahun', y = alt.Y('Jumlah Turis', axis=alt.Axis(title='Jumlah Turis (Juta)', titleColor='#5276A7'),scale=alt.Scale(domain=[0, 20]))
#pb = alt.layer(line).resolve_scale( y = 'independent')
#st.line_chart(data = df, use_container_width=True)

st.caption("""<a style='display: block; text-align: center;color: black;' 
href="https://www.bps.go.id/indicator/16/1150/1/jumlah-kunjungan-wisatawan-mancanegara-per-bulan-ke-indonesia-menurut-pintu-masuk-2017---sekarang.html">
Sumber: Badan Pusat Statistik</a>""",unsafe_allow_html=True)

"""Menurut Badan Pusat Statistik, tingkat turis (wisatawan mancanegara) yang datang ke Indonesia hingga tahun 2019 mengalami kenaikan sebanyak **2 juta** turis, hal ini dapat dilihat pada grafik diatas. Namun saat tingkat turis yang datang sedang tinggi, terjadi pandemi covid-19 di seluruh dunia termasuk Indonesia pada awal tahun 2020 hingga sekarang. Hal ini memberikan dampak negatif dengan menurun drastisnya turis ke Indonesia mencapai **75 %** di tahun 2020."""

# Grafik jumlah turis pintu masuk dan covid harian
st.subheader("Hubungan Jumlah Turis dengan Pandemi")

col1, col2 = st.columns(2)
with col1:
   st.subheader("Jumlah Turis per Pintu Masuk")
   image = Image.open("Pinturis.png")
   st.image(image, use_column_width='auto', caption ='Sumber : Badan Pusat Statistik')

with col2:
   st.subheader("Kasus Positif Harian Covid di Indonesia")
   image = Image.open("Positif.png")
   st.image(image, use_column_width='auto', caption ='Sumber : kawalcovid19.id')

''' Dari kedua grafik diatas dapat diambil kesimpulan bahwa kasus Covid-19 yang muncul di tahun 2020 mempengaruhi jumlah turis yang masuk ke Indonesia dari berbagai Pintu Masuk. Sehingga menjadi sangat sedikit turis yang masuk ketika kasus positif harian mencapai puncaknya di tahun 2021.'''
# Grafik korelasi
''' **Apakah terdapat hubungan antara Jumlah Turis dengan Pandemi Covid?**

- H0 : Tidak terdapat hubungan antara Jumlah Turis dengan Pandemi Covid

- H1 : Terdapat hubungan antara Jumlah Turis dengan Pandemi Covid
'''

code = '''r = nΣxy–(Σx)(Σy) / √{nΣx²–(Σx)²}{nΣy² – (Σy)²}'''
st.code(code, language = 'python')

'''Dari hasil korelasi diatas, didapatkan bahwa **r = -0,42** . Hal ini berarti kita dapat mereject **H0**. Dengan demikian Pandemi Covid **mempengaruhi secara signifikan** terhadap Jumlah Turis yang memasuki Indonesia.'''

# Turis yang masuk per Negara Asal
st.subheader("Kunjungan Turis berdasarkan Negara Asal")

# Deklarasi dataset
country = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTXspAWpKN-lhLVzwafiDNnwXAUf_l_I-xsdO3AVT0bDzTsgS5NyMnaOQRB865eBscEt9NKka4cJ-pw/pub?gid=0&single=true&output=csv')

st.dataframe(country.style.highlight_max(axis=0), use_container_width=True)
# Data prep

# End of Data Prep

# Image / can change with interactive DB
#image = Image.open("TurisTahun.png")
#st.image(image, use_column_width='auto', caption = "Sumber : Badan Pusat Statistik")

# Chart
#df1= df.iloc[0:10]
#st.line_chart(data=df1, x = 'Ship Date', y = 'Profit', width=0, height=0, use_container_width=True)

#st.bar_chart(data=df1, x = 'Ship Date', y = 'Profit')


# top 5 negara terbanyak ke indonesia

''' Dapat dilihat bahwa **Top 5** Turis yang banyak berkunjung ke Indonesia adalah negara-negara tetangga, dan mayoritas negara tersebut berasal dari benua Asia yang jaraknya tidak jauh dari Indonesia.'''

# Machine Learning + grafiknya

'''
## Penutup
Kesimpulan dan saran yang dapat ditarik dari grafik-grafik diatas adalah sebagai berikut :

•	Terdapat korelasi negatif antara Jumlah Turis yang masuk ke Indonesia dengan Pandemi Covid. Semakin tinggi Covid maka semakin rendah Turis yang masuk.

•	Agar pariwisata dapat segera pulih di Indonesia, berdasarkan *Grafik : Jumlah Turis per Pintu Masuk* dapat dilihat bahwa pintu masuk via Udara adalah pintu masuk yang sangat sering digunakan Turis dibandingan via Darat dan via Laut, maka Pemerintah harus mempercepat membuka kembali penerbangan yang masuk ke Indonesia. 

•	Kementrian Pariwisata juga harus memiliki inovasi-inovasi terbaik untuk mempromosikan Indonesia ke mancanegara agar Turis asing berminat untuk datang ke Indonesia.
'''

'''
## Daftar Pustaka
[BPS](https://www.bps.go.id/indicator/16/1150/1/jumlah-kunjungan-wisatawan-mancanegara-per-bulan-ke-indonesia-menurut-pintu-masuk-2017---sekarang.html)

[Kawal Covid 19](https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/htmlview)

[Model Decision Tree untuk Prediksi Jadwal Kerja menggunakan Scikit-Learn](https://jurnal.umj.ac.id/index.php/semnastek/article/view/5239/3517)

[barantum.com](https://www.barantum.com/blog/wp-content/uploads/2019/01/Wisata-Indonesia-Mempunyai-Peluang-Bisnis.jpg)

[Statistika Non-Parametrik Analisis Jalur](https://slideplayer.info/slide/3099519)


## Contacts
[![MAIL Badge](https://img.shields.io/badge/-z26syafnur@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:z26syafnur@gmail.com)](mailto:z26syafnur@gmail.com)

[![LinkedIn](https://img.shields.io/badge/syafnur-zulfikri-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/syafnur-zulfikri/)](https://www.linkedin.com/in/syafnur-zulfikri/)


(C) Zulfikri Syafnur, 2022

CP10-22
'''
