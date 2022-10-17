import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import altair as alt
import requests

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

st.subheader("Jumlah Turis Asing Masuk ke Indonesia")
df = pd.DataFrame([[13514963], [16106954], [4052923], [1557530], [202823]],
                    index=['2018', '2019', '2020', '2021', '2022'],
                    columns=['Jumlah Turis'])
st.line_chart(data=df, use_container_width=True) 
st.caption('Sumber : Badan Pusat Statistik')
'''Menurut Badan Pusat Statistik, tingkat turis (wisatawan mancanegara) yang datang ke Indonesia dari hingga tahun 2019 mengalami kenaikan sebanyak **2 juta** turis, hal ini dapat dilihat pada grafik diatas. Namun saat tingkat turis yang datang sedang tinggi, terjadi pandemi covid-19 di seluruh dunia termasuk Indonesia pada awal tahun 2020 hingga sekarang. Hal ini memberikan dampak negatif dengan menurun drastisnya turis ke Indonesia mencapai **1000%** di tahun 2020.'''

# Grafik jumlah turis pintu masuk dan covid harian
st.subheader("Hubungan Jumlah Turis dengan Pandemi")

col1, col2 = st.columns(2)
with col1:
   st.subheader("Jumlah Turis per Pintu Masuk")
   image = Image.open("Pinturis.png")
   st.image(image, use_column_width='auto', caption ='Sumber : Badan Pusat Statistik')

with col2:
   st.subheader("Kasus Positif Harian Covid di Indoneai")
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
#df1 = pd.read_excel('/content/Data Gabungan Turis.xlsx', sheet_name='Sheet2')

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

''' Dapat dilihat bahwa wisman yang banyak berpariwisata ke indonesia adalah negara-negara tetangga,
mayoritas berasal dari benua Asia dan Australia yang jaraknya tidak jauh dari Indonesia. '''

# Machine Learning + grafiknya

'''
# Daftar Pustaka
[BPS](https://www.bps.go.id/indicator/16/1150/1/jumlah-kunjungan-wisatawan-mancanegara-per-bulan-ke-indonesia-menurut-pintu-masuk-2017---sekarang.html)

[Kawal Covid 19](https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/htmlview)

[Model Decision Tree untuk Prediksi Jadwal Kerja menggunakan Scikit-Learn](https://jurnal.umj.ac.id/index.php/semnastek/article/view/5239/3517)

[barantum.com](https://www.barantum.com/blog/wp-content/uploads/2019/01/Wisata-Indonesia-Mempunyai-Peluang-Bisnis.jpg)

[Statistika Non-Parametrik Analisis Jalur](https://slideplayer.info/slide/3099519)
'''   

url_csv = "https://raw.githubusercontent.com/epogrebnyak/ssg-dataset/main/data/ssg.csv"
url_metadata = (
    "https://raw.githubusercontent.com/epogrebnyak/ssg-dataset/main/data/metadata.json"
)


@st.cache
def get_data():
    return pd.read_csv(url_csv, parse_dates=["created", "modified"])

@st.cache
def get_meta():
    return requests.get(url_metadata).json()

_df = get_data()
st.subheader("Kunjungan Turis berdasarkan Negara Asal")
all_langs = _df.lang.unique().tolist()

@st.cache
def palette(languages, default_color="#BEBEBE"):
    r = requests.get(
        "https://raw.githubusercontent.com/ozh/github-colors/master/colors.json"
    ).json()
    pal = {}
    for lang in languages:
        try:
            pal[lang] = r[lang]["color"]
        except KeyError:
            pal[lang] = default_color
    return list(pal.keys()), list(pal.values())


col_keys, col_values = palette(all_langs)
github_scale = alt.Scale(domain=col_keys, range=col_values)

selected_langs = st.multiselect(
    "Programming languages", options=all_langs, default=all_langs
)
plot_df = _df[_df.lang.isin(selected_langs)]
plot_df["stars"] = plot_df.stars.divide(1000).round(1)

# https://altair-viz.github.io/user_guide/customization.html#raw-color-values

chart = (
    alt.Chart(
        plot_df,
        title="Static site generators popularity",
    )
    .mark_bar()
    .encode(
        x=alt.X("stars", title="'000 stars on Github"),
        y=alt.Y(
            "name",
            sort=alt.EncodingSortField(field="stars", order="descending"),
            title="",
        ),
        color=alt.Color(
            "lang",
            legend=alt.Legend(title="Language"),
            scale=github_scale,
        ),
        tooltip=["name", "stars", "lang"],
    )
)


st.altair_chart(chart, use_container_width=True)
