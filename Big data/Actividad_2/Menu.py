import streamlit as st
from Funciones import *
from Clase import *

try:
    st.set_page_config(page_title='Actividad 2 - Pandas', page_icon=":bar_chart:", layout="wide")
    st.title("Analisis de Base de Datos con Pandas")
    uploaded_file = st.file_uploader("Cargar base de datos en formato CSV", type="csv")
    BD=AnalisisDatos(uploaded_file)
    menu(BD)

except Exception as e:
    st.write(e)