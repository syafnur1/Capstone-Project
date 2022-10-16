import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(layout="wide")

'''
    # Analisis Pemulihan sektor Pariwisata pasca Pandemi di Indonesia
    Capstone Project with **streamlit** by Zulfikri Syafnur
    
    ---
'''

'''
## Kesiapan Stakeholder dalam membangkitkan kembali Pariwisata
[Pariwisata](https://id.wikipedia.org/wiki/Pariwisata) merupakan cara suatu negara mempromosikan negara tersebut sehingga dapat dikinjungi oleh banyak orang. 
Di Indonesia, contoh pariwisata yang menjadi tujuan wisata yang terkenal di dunia adalah [Bali](https://bali.com/). 
Bali terkenal dengan berbagai objek wisatanya seperti wisata alam, wisata budaya, dan wisata bahari
'''

# Deklarasi dataset

# Data prep

# End of Data Prep

# Image / can change with interactive DB
image = Image.open("TurisTahun.png")
st.image(image, use_column_width='auto', caption = "Sumber : Badan Pusat Statistik")

'''Menurut Badan Pusat Statistik, tingkat wisatawan mancanegara (wisman) yang datang ke Indonesia dari hingga tahun 2019 
mengalami kenaikan sebanyak **2 juta** wisman, hal ini dapat dilihat pada grafik diatas. Namun saat tingkat wisman yang datang sedang tinggi, 
terjadi pandemi covid-19 di seluruh dunia termasuk Indonesia pada awal tahun 2020. Hal ini memberikan dampak negatif dengan menurun drastisnya 
wisman ke Indonesia mencapai **1000%** di tahun 2020.'''

# CHart
#df1= df.iloc[0:10]
#st.line_chart(data=df1, x = 'Ship Date', y = 'Profit', width=0, height=0, use_container_width=True)

#st.bar_chart(data=df1, x = 'Ship Date', y = 'Profit')

'''
# Daftar Pustaka
[BPS](https://www.bps.go.id/indicator/16/1150/1/jumlah-kunjungan-wisatawan-mancanegara-per-bulan-ke-indonesia-menurut-pintu-masuk-2017---sekarang.html)

[Kawal Covid 19](https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/htmlview)

[Model Decision Tree untuk Prediksi Jadwal Kerja menggunakan Scikit-Learn](https://jurnal.umj.ac.id/index.php/semnastek/article/view/5239/3517)
'''   
