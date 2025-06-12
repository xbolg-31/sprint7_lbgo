import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Proyecto 7')
hist_check = st.checkbox('Construir histograma') # check histograma
disp_check = st.checkbox('Grafico de Dispersion') # check Dispersion
barr_check = st.checkbox('Grafico de Barras') # check barras

if hist_check: # al seleccionar check histograma
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_check: # al seleccionar check dispersion
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion')
    
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if barr_check: # al seleccionar check barras

    ylist = car_data['model_year'].unique()
    ylist = ylist[~np.isnan(ylist)].astype(int)
    options = st.multiselect(
    "Que año quieres ver?",
    ylist,
    accept_new_options=False,
    )
    #st.write("You selected:", options)
    gen_bar = st.checkbox('Generar') # check barras
    if gen_bar:
        # escribir un mensaje
        st.write('Creación de un grafico de barras')
        
        price_type = car_data.query(f"model_year.isin({options})")
        
        fig = px.bar(price_type, x='model_year', y='price', color='type')

        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)