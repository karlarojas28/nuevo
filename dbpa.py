


import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Datos Aseguradora") # Nombre para configurar la pagina web
st.header('Datos clientes aseguradora') #Va a ser el titulo de la pagina
st.subheader('Que informacion se puede obtener de cada clente') #Subtitulo

excel_file = 'fraudes_con_na 2.xlsx' #Nombre archivo a importar  'xlsx' hace referencia a excel

df = pd.read_excel(excel_file, #importo el archivo excel
                   usecols = 'A:I', #aqui traigo las columnas que quiero usar
                   header =0) #desde que fila debe empezar a tomarme la informacion *Empieza a contar desde 0*
df
