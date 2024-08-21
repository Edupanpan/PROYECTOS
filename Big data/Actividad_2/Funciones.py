from Clase import AnalisisDatos
import streamlit as st
import pandas as pd
def crearObjeto(uploaded_file):
    BD = AnalisisDatos(CsvUploud=uploaded_file)
    st.write("Datos cargados exitosamente")
    return BD


def menu(BD):
    metodo=st.selectbox("Seleccione una opción",["","Ver Datos","Ver Información","Valores Faltantes","Cambiar tipo de datos"])
    if metodo=="Ver Datos":
        opc=st.selectbox("Seleccione una opción",["","Base de datos","Primeras Filas","Últimas Filas"])
        if opc=="Base de datos":
            obtenerDatos(BD)
        elif opc=="Primeras Filas":
            obtenerHead(BD)
        elif opc=="Últimas Filas":
            obtenerTail(BD)
    elif metodo=="Ver Información": 
        opc=st.selectbox("Seleccione una opción",["","Información de la Base de Datos","Descripción de la Base de Datos"])  
        if opc=="Información de la Base de Datos":    
            obtenerInfo(BD)
        elif opc=="Descripción de la Base de Datos":
            obtenerDescribe(BD)
    elif metodo=="Valores Faltantes":
        valoresNull(BD)
    elif metodo=="Cambiar tipo de datos":
        Cambio_tipo(BD)   
        



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
    columnas=BD.get_columnas()
    columna=st.selectbox("Seleccione una columna para realizar análisis descriptivo",columnas)
    st.write(BD.get_AnalisisDescriptivo(columna))
    st.write(BD.get_grafico())


def valoresNull(BD):
    st.write("Valores faltantes:")
    st.write(BD.get_valoresnull())
    columnas=BD.get_columnas()
    texto_usuario = st.selectbox("Seleccione una columna para modificar valores nulos",columnas) 
    valor_modificar = st.selectbox("Seleccione un valor",["","Moda","Media","Mediana","Valor específico"])
    if valor_modificar=="Valor específico":
        valor_especifico=st.number_input("Ingrese el valor específico")  
    st.write(BD.cambiarnulos(texto_usuario, valor_modificar, valor_especifico))


def Cambio_tipo(BD):
    st.write("Tipos de datos")
    st.write(BD.get_types())
    columnas=BD.get_columnas()
    columna=st.selectbox("Seleccione una columna para modificar tipo de datos",columnas) 
    tipo=st.selectbox("Seleccione un tipo de datos",["","int","float","object", "datetime64[ns]"])
    st.write(BD.cambioTipo(columna,tipo))
