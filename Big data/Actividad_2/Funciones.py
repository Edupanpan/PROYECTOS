from Clase import AnalisisDatos
import streamlit as st
import pandas as pd
def crearObjeto(uploaded_file):
    BD = AnalisisDatos(CsvUploud=uploaded_file)
    st.write("Datos cargados exitosamente")
    return BD


def menu(BD):
    metodo=st.selectbox("Seleccione una opción",["","Ver Datos","Ver Primeras Filas","Ver Últimas Filas","Ver Información","Ver Descripción","Valores Faltantes"])
    if metodo=="Ver Datos":
        obtenerDatos(BD)
    elif metodo=="Ver Primeras Filas": 
        obtenerHead(BD)
    elif metodo=="Ver Últimas Filas":
        obtenerTail(BD)
    elif metodo=="Ver Información":   
        obtenerInfo(BD)
    elif metodo=="Ver Descripción":
        obtenerDescribe(BD)
    elif metodo=="Valores Faltantes":
        valoresNull(BD)    
        



def obtenerDatos(BD):
    st.write("Base de Datos")  
    st.write(BD.get_datos())

def obtenerHead(BD, n=20):
        st.write("Primeras Filas")
        st.write(BD.get_head(n))

def obtenerTail(BD, n=20):
    st.write("Últimas Filas")
    st.write(BD.get_tail(n))

def obtenerInfo(BD):
    st.write("Información de la Base de Datos")
    st.write(BD.get_info())

def obtenerDescribe(BD):
    st.write("Descripción de la Base de Datos")
    st.write(BD.get_describe())

def valoresNull(BD):
    st.write("Valores faltantes:")
    st.write(BD.get_valoresnull())
    columnas=BD.get_columnas()
    texto_usuario = st.selectbox("Seleccione una columna para mostrar los valores nulos",columnas) 
    st.write(BD.mostrarnulos(texto_usuario))