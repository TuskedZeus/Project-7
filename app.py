import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')

st.header('Análisis de datos de vehículos')


if st.button('Construir histograma'):
    fig = px.histogram(df, x='price')
    st.write('Histograma de precios de vehículos')
    st.plotly_chart(fig)


if st.button('Construir gráfico de dispersión'):
    fig = px.scatter(df, x='model_year', y='price')
    st.write('Gráfico de dispersión de precios de vehículos vs. año')
    st.plotly_chart(fig)
