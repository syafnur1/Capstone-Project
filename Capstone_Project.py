import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Capstone Project",
                   page_icon=":airplane:",
)

header = st.container()
pendahuluan = st.container()
korelasi = st.container()
negara = st.container()
penutup = st.container()
pustaka = st.container()
kontak = st.container()

# Load Dataset

turis = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQY21pKyD2OqXjhrC2JpODETvSyfj8fS8dWE87smTC4JoxnJDZV_n7gcFtjHzYFpCZGtrfnfMl1CxVN/pub?gid=1602651423&single=true&output=csv")
country = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTXspAWpKN-lhLVzwafiDNnwXAUf_l_I-xsdO3AVT0bDzTsgS5NyMnaOQRB865eBscEt9NKka4cJ-pw/pub?gid=0&single=true&output=csv')
covid = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQY21pKyD2OqXjhrC2JpODETvSyfj8fS8dWE87smTC4JoxnJDZV_n7gcFtjHzYFpCZGtrfnfMl1CxVN/pub?gid=340714200&single=true&output=csv')
df3 = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQY21pKyD2OqXjhrC2JpODETvSyfj8fS8dWE87smTC4JoxnJDZV_n7gcFtjHzYFpCZGtrfnfMl1CxVN/pub?gid=0&single=true&output=csv')

with header:
    image = Image.open("Barantum.png")
    st.image(image, use_column_width='auto')
    st.caption("""<a style='display: block; text-align: center;color: black;' 
               href="https://www.barantum.com/blog/wp-content/uploads/2019/01/Wisata-Indonesia-Mempunyai-Peluang-Bisnis.jpg)">Sumber: barantum.com</a>""", 
               unsafe_allow_html=True)
    st.title('Analisis Pemulihan Sektor Pariwisata Pasca Pandemi di Indonesia')
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
         'Jumlah Turis': [13514963, 16106954, 4052923, 1557530, 202823]
        }
    
    df = pd.DataFrame(data = d)
    
    # grafik 1
    grafik_1 = px.line(df, 
                       x='Tahun', 
                       y='Jumlah Turis',
                       markers=True, 
                       template="plotly_white",
                       color_discrete_sequence =['#1F77B4']*len(covid),
    )
    grafik_1.update_layout(
                       title={
                         'text': "<b>Jumlah Turis per Tahun<b>",
                         'y':0.9,
                         'x':0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'},
                       xaxis_title='Tahun (Mar-18 sampai Mar-22)',
                       plot_bgcolor="white",
                       xaxis=(dict(showgrid=False)),
    )
    st.plotly_chart(grafik_1)      
      
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
    st.subheader("Jumlah Turis per Pintu Masuk")

    # Cleansing Dataset
    turis["Bulan Tahun"] = pd.to_datetime(turis["Bulan Tahun"])
    turis_bulan = turis[(turis["Bulan Tahun"] <= "3/31/2022")]
    turis_bulan = turis_bulan.groupby(['Bulan Tahun', 'Tipe Pintu Masuk']).agg({'Turis': 'sum'})
    
    pivot_tb = pd.pivot_table(data=turis_bulan, 
               values='Turis', 
               index='Bulan Tahun', 
               columns=['Tipe Pintu Masuk'])
    
    fig_turis_bulan = px.line(
                          pivot_tb,
                          y=["Darat", "Laut", "Udara"],
                          markers=True,
                          template="plotly_white",
                          labels={"variable" : "Pintu Masuk", 
                                 "value" : "Jumlah Turis"}
    )

    fig_turis_bulan.update_layout(
                   title={
                          'text': "<b>Turis per Pintu Masuk<b>",
                          'y':0.9,
                          'x':0.5,
                          'xanchor': 'center',
                          'yanchor': 'top'},
                   xaxis_title='Tahun (Mar-18 sampai Mar-22)',
                   yaxis_title='Jumlah Turis', 
                   plot_bgcolor="white",
                   legend_title="Pintu Masuk",
                   xaxis=(dict(showgrid=False)),
    )

    st.plotly_chart(fig_turis_bulan)
    
    st.caption("""<a style='display: block; text-align: center;color: black;' href="https://www.bps.go.id/indicator/16/1150/1/jumlah-kunjungan-wisatawan-mancanegara-per-bulan-ke-indonesia-menurut-pintu-masuk-2017---sekarang.html">Sumber: Badan Pusat Statistik</a>""",unsafe_allow_html=True)
    
    st.subheader("Kasus Positif Harian Covid di Indonesia")
    
    # Cleansing Dataset
    covid["Bulan Tahun"] = pd.to_datetime(covid["Bulan Tahun"])
    covid.rename(columns={'Bulan Tahun' : 'Bulan_Tahun'}, inplace=True)
    covid_bulan = covid[(covid["Bulan_Tahun"] <= "3/31/2022")]
    
    fig_covid_bulan = px.line(
                      covid, x="Bulan_Tahun",
                      y="Kasus harian",
                      template="plotly_white",
                      color_discrete_sequence =['#AF0038']*len(covid),
                      labels={"Kasus harian" : "Kasus Harian", 
                                 "Bulan_Tahun" : "Tanggal"}
    )
    
    fig_covid_bulan.update_layout(
                   title={
                          'text': "<b>Kasus Harian Covid<b>",
                          'y':0.9,
                          'x':0.5,
                          'xanchor': 'center',
                          'yanchor': 'top'},
                   xaxis_title='Tahun (Mar-20 sampai Mar-22)',
                   yaxis_title='Jumlah Positif', 
                   plot_bgcolor="white",
                   xaxis=(dict(showgrid=False)),
    )

    st.plotly_chart(fig_covid_bulan)
    
    st.caption("""<a style='display: block; text-align: center;color: black;' href="https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/htmlview">Sumber: Kawal Covid 19</a>""",unsafe_allow_html=True)
    
    st.markdown('''Dari kedua grafik diatas dapat diambil kesimpulan bahwa kasus Covid-19 yang muncul di tahun 2020 mempengaruhi jumlah turis yang 
                masuk ke Indonesia dari berbagai Pintu Masuk. Sehingga menjadi sangat sedikit turis yang masuk ketika kasus positif harian mencapai 
                puncaknya di tahun 2021.''')

    # korelasi
    df3 = df3.rename(columns = {'Harian': 'Positif Covid', 'Turis' : 'Jumlah Turis'})

    col3, col4= st.columns([1.55,2.5])

    with col3:
        correlation_matrix = round(df3[['Positif Covid', 'Jumlah Turis']].corr(), 2)
        correlation_matrix 

    with col4:
        st.markdown('''Dari hasil korelasi dua data diatas, didapatkan bahwa **r = -0,43** . Hal ini berarti kita dapat mereject **H0**. 
                    Dengan demikian Pandemi Covid **mempengaruhi secara signifikan** terhadap Jumlah Turis yang memasuki Indonesia.''')

# Turis yang masuk per Negara Asal
with negara:
    st.subheader("Kunjungan Turis berdasarkan Negara Asal")
    # Cleansing dataset
    country = country.drop(['Grand Total'], axis=1)
    country = country.set_index('Negara')
    
    groupby_column = st.radio(
      'Pilih Tahun : ',
      ['2018', '2019', '2020', '2021', '2022'], 
    horizontal=True)
    
    # -- Group Negara
    output_columns =['2018',  '2019', '2020', '2021',  '2022']
    country_grouped = country.sort_values(by = [groupby_column], ascending=False,)[output_columns].head(5)

    gra_country = px.bar(country_grouped,
                     x=groupby_column,
                     template="plotly_white",
                     color_discrete_sequence =['#1C8356']*len(country_grouped),
                    )
    
    gra_country.update_layout(
                title={
                          'text': "<b>Jumlah Turis berdasarkan Negara<b>",
                          'y':0.9,
                          'x':0.5,
                          'xanchor': 'center',
                          'yanchor': 'top'},
                plot_bgcolor="white",
                xaxis=dict(tickmode="auto",
                showgrid=False, 
                showline=False,
                showticklabels=True,
                domain=[0, 0.85],
                ),
                yaxis=dict(tickmode="auto",
                showgrid=False, 
                showline=False,
                showticklabels=True,
                domain=[0, 0.85],
                autorange="reversed"),
    )
    
    st.plotly_chart(gra_country)
  
    st.markdown('''Dapat dilihat bahwa Negara yang paling sering berkunjung ke Indonesia adalah negara-negara tetangga, dan mayoritas negara 
                tersebut berasal dari benua Asia yang jaraknya tidak jauh dari Indonesia.''')
    st.markdown('_________________')

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
    st.markdown('_________________')

with pustaka:
    st.subheader("Daftar Pustaka")
    st.markdown('''
                - [Badan Pusat Statistik](https://www.bps.go.id/indicator/16/1150/1/jumlah-kunjungan-wisatawan-mancanegara-per-bulan-ke-indonesia-menurut-pintu-masuk-2017---sekarang.html)
                - [Kawal Covid 19](https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/htmlview)
                - [Model Decision Tree untuk Prediksi Jadwal Kerja menggunakan Scikit-Learn](https://jurnal.umj.ac.id/index.php/semnastek/article/view/5239/3517)
                - [barantum.com](https://www.barantum.com/blog/wp-content/uploads/2019/01/Wisata-Indonesia-Mempunyai-Peluang-Bisnis.jpg)
                - [Statistika Non-Parametrik Analisis Jalur](https://slideplayer.info/slide/3099519)
                ''')
    st.markdown('_________________')

with kontak:
    st.subheader("Let's Connect with me")
    st.markdown('''
                [![MAIL Badge](https://img.shields.io/badge/-z26syafnur@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:z26syafnur@gmail.com)](mailto:z26syafnur@gmail.com)

                [![LinkedIn](https://img.shields.io/badge/syafnur-zulfikri-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/syafnur-zulfikri/)](https://www.linkedin.com/in/syafnur-zulfikri/)
                ''')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
    
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
