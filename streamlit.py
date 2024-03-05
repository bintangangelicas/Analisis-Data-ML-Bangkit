import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#Judul Dashboard
st.title('Dashboard Penyewaan Sepeda')

#Baca Dataset
@st.cache_data 
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/bintangangelicas/Analisis-Data-ML-Bangkit/96ea2a88a69f7873bcd44a9dfb30620fce1e5678/day.csv')
    return data

def load_data():
    data1 = pd.read_csv('https://raw.githubusercontent.com/bintangangelicas/Analisis-Data-ML-Bangkit/96ea2a88a69f7873bcd44a9dfb30620fce1e5678/hour.csv
')
    return data1

st.subheader('Rata - Rata Penyewaan Berdasarkan Cuaca')

jumlah_pinjam = data_day.groupby('weathersit')['cnt'].mean()

plt.bar(jumlah_pinjam.index, jumlah_pinjam.values, color='green')

plt.title('Rata - Rata Penyewaan Berdasarkan Cuaca')
plt.xlabel('Cuaca')
plt.ylabel('Mean Penyewaan')

st.pyplot()


jumlah_pinjam = data_hour.groupby('hr')['cnt'].mean()

plt.bar(jumlah_pinjam.index, jumlah_pinjam.values, color='brown')

plt.title('Rata - Rata Penyewaan Berdasarkan Jam')
plt.xlabel('Waktu')
plt.ylabel('Mean Penyewaan')

plt.show()


