import streamlit as st
from Funciones import *
from Clase import *

try:
    menu()
except Exception as e:
    st.error(f"Error en el menú: {e}")