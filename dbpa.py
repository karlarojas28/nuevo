


import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Datos Aseguradora") # Nombre para configurar la pagina web
st.header('Datos clientes aseguradora') #Va a ser el titulo de la pagina
st.subheader('Que informacion se puede obtener de cada clente') #Subtitulo

excel_file = 'fraudes_con_na 2.xlsx' #Nombre archivo a importar  'xlsx' hace referencia a excel

