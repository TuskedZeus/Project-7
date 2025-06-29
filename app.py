import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')


histograma_seleccionado = st.checkbox('Histograma de precios')
dispersion_seleccionado = st.checkbox('Gráfico de dispersión de precio vs año de modelo')


if histograma_seleccionado:
    fig = px.histogram(df, x='price', title='Distribución de Precios de Vehículos')
    st.plotly_chart(fig, use_container_width=True)

if dispersion_seleccionado:
    fig = px.scatter(df, x='model_year', y='price', title='Relación entre Precio y Año de Modelo')
    st.plotly_chart(fig, use_container_width=True)
