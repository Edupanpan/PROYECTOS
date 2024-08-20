import streamlit as st
from Funciones import *
from Clase import *

try:
    st.set_page_config(page_title='Actividad 2 - Pandas', page_icon=":bar_chart:", layout="wide")#config pagina streamlit, nombre de arriba, icono,
    
    st.title("Analisis de Base de Datos con Pandas")#titulo de contenido
    uploaded_file = st.file_uploader("Cargar base de datos en formato CSV", type="csv")#seccion que perimte cargar archivos
    if uploaded_file is not None:
        analisis = crearObjeto(uploaded_file)
        
        menu(analisis)
except:
    st.write("Aún no se ha cargado un archivo CSV")