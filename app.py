import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('C:\\Users\\Ah-kin\\Python\\Project_7_Root\\Project-7\\vehicles_us.csv')

st.header('Análisis de datos de vehículos')


if st.button('Construir histograma'):
    fig = px.histogram(df, x='price')
    st.write('Histograma de precios de vehículos')
    st.plotly_chart(fig)


if st.button('Construir gráfico de dispersión'):
    fig = px.scatter(df, x='year', y='price')
    st.write('Gráfico de dispersión de precios de vehículos vs. año')
    st.plotly_chart(fig)