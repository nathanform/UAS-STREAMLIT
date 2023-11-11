import streamlit as st
import pandas as pd
import numpy as np


# Menu utama
menu_utama = st.sidebar.radio("Menu Utama", ["Beranda", "Data Grafik"])

if menu_utama == "Beranda":
    st.title('Aplikasi Streamlit Ujian Akhir Semester')
    st.write("Selamat datang di halaman beranda. Didalam aplikasi ini kami mempunyai 3 jenis data yang berbeda yang nanti nya dapat diakses dengan mudah, diantaranya:")
    image = st.image('hero.jpg')
    st.image('mpl.jpg')
    st.image('rice.jpg')

elif menu_utama == "Data Grafik":
    # Data Mlbb
    df_mlbb = pd.read_csv('Mlbb_Heroes.csv')
    st.title('Data Hero MLBB')
    st.write(df_mlbb)
    
    # Grafik Pie untuk Role Hero
    fig_mlbb_pie = px.pie(df_mlbb, names='Primary_Role', title='Role Hero')
    st.plotly_chart(fig_mlbb_pie)
    
    # Grafik Bar untuk Match Esport
    fig_mlbb_bar = px.bar(df_mlbb, x='Name', y='Esport_Wins', title='Match Esport')
    st.plotly_chart(fig_mlbb_bar)

    # Data MPL ID S10
    df_mpl = pd.read_csv('MPL_ID_S10.csv')
    st.title('DATA MPL ID S10')
    st.write(df_mpl)

    # Grafik Pie untuk Best Picked
    fig_mpl_pie = px.pie(df_mpl, names='Bs_picked', title='Best Picked')
    st.plotly_chart(fig_mpl_pie)

    # Grafik Bar untuk Win Rate of MPL Mobile Legends Heroes
    fig_mpl_bar = px.bar(df_mpl, x='Hero', y='T_winrate', title='Win Rate of MPL Mobile Legends Heroes')
    st.plotly_chart(fig_mpl_bar)

    # Data Rice Production Indonesia
    df_rice = pd.read_csv('rice.csv')

    # Mengelompokkan data berdasarkan provinsi dan menghitung produksi beras maksimum per provinsi
    data_grouped = df_rice.groupby('Provinsi')['Production.(ton)'].max()

    # Mengurutkan data dari terbanyak ke terkecil
    data_sorted = data_grouped.sort_values(ascending=False)

    # Menampilkan hasil
    st.title('Data Rice Production Indonesia')
    st.write(df_rice)
    st.write("Data Produksi Beras per Provinsi (Terbanyak ke Terkecil):")
    st.write(data_sorted)

    # Grafik Pie untuk Production.(ton)
    fig_rice_pie = px.pie(df_rice, names='Provinsi', title='Production.(ton)')
    st.plotly_chart(fig_rice_pie)
