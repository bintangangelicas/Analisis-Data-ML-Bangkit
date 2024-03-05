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

st.markdown('''**Conclusion Pertanyaan 1 (Apakah ada musim/cuaca tertentu angka peminjaman/penyewaan sepeda meningkat? Jika ada, musim apa?)**

1: Clear, Few clouds, Partly cloudy, Partly cloudy

2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist

3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds

4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog

Angka 1-3 merepresentasikan cuaca, di mana telah dijelaskan keterangan dari angka-angka tersebut.
Dapat disimpulkan bahwa pada cuaca (1) di mana cuaca bersih dan berawan angka penyewaan sepeda meningkat lalu diikuti oleh cuaca (2) dan (3). Sedangkan di cuaca (4) tidak terdapat record peminjaman sepeda sama sekali.''')

jumlah_pinjam = load_data1().groupby('hr')['cnt'].mean()

plt.bar(jumlah_pinjam.index, jumlah_pinjam.values, color='brown')

plt.title('Rata - Rata Penyewaan Berdasarkan Jam')
plt.xlabel('Waktu')
plt.ylabel('Mean Penyewaan')

st.pyplot()
