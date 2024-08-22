import streamlit as st
from a.funciones_ import cargar_csv, mostrar_dataframe
from a.menu_ import Principal

st.title("Limpieza de Datos")

uploaded_file = st.file_uploader("Carga tu archivo CSV", type=["csv"])

cargar_csv(uploaded_file)
Principal()
mostrar_dataframe()