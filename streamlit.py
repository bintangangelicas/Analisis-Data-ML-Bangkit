import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import ssl 
sns.set(style='dark')

ssl._create_default_https_context = ssl._create_unverified_context 
                                                                                   
#Judul Dashboard
st.title('Dashboard Penyewaan Sepeda')

#Baca Dataset
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/bintangangelicas/Analisis-Data-ML-Bangkit/main/day.csv',delimiter=',')
    return data

def load_data1():
    data1 = pd.read_csv('https://raw.githubusercontent.com/bintangangelicas/Analisis-Data-ML-Bangkit/main/hour.csv')
    return data1

st.subheader('Rata - Rata Penyewaan Berdasarkan Cuaca')

jumlah_pinjam = load_data().groupby('weathersit')['cnt'].mean()

plt.bar(jumlah_pinjam.index, jumlah_pinjam.values, color='green')

plt.title('Rata - Rata Penyewaan Berdasarkan Cuaca')
plt.xlabel('Cuaca')
plt.ylabel('Mean Penyewaan')

st.pyplot()


jumlah_pinjam = load_data1().groupby('hr')['cnt'].mean()

plt.bar(jumlah_pinjam.index, jumlah_pinjam.values, color='brown')

plt.title('Rata - Rata Penyewaan Berdasarkan Jam')
plt.xlabel('Waktu')
plt.ylabel('Mean Penyewaan')

st.pyplot()
