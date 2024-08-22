from Clase import *
import streamlit as st
def menu():
    
    st.title("Limpieza de Datos")
    
    uploaded_file = st.file_uploader("Carga tu archivo CSV", type=["csv"])
    
    if uploaded_file and 'data' not in st.session_state:
        BD = AnalisisDatos(uploaded_file)
        BD.load_data()

    if 'data' in st.session_state:
        BD = AnalisisDatos(None)
        with st.sidebar:
            st.header("Menú")
            
            
            opc = st.selectbox("Seleccione una opción", ["Base de datos", "Primeras Filas", "Últimas Filas"])
            if st.button("Ver Datos"):
                if opc == "Base de datos":
                    obtenerDatos(BD)
                elif opc == "Primeras Filas":
                    obtenerHead(BD)
                elif opc == "Últimas Filas":
                    obtenerTail(BD)
            
            st.divider()
            opc = st.selectbox("Seleccione una opción", [ "Descripción de la Base de Datos"])
            if st.button("Ver Información"):    
                
                if opc == "Descripción de la Base de Datos":
                    obtenerDescribe(BD)
                    
            st.divider()

            valoresNull(BD)
            
            
            st.divider()
            Cambio_tipo(BD)

            st.divider()
            cambioMoneda(BD)

            st.divider()
            MedidasTendencia(BD)

            st.divider()
            get_grafico(BD)
                
            
                


def obtenerDatos(BD):
    st.write("Base de Datos")
    st.write(BD.get_datos())

def obtenerHead(BD, n=20):
    st.write("Primeras Filas")
    st.write(BD.get_head(n))

def obtenerTail(BD, n=20):
    st.write("Últimas Filas")
    st.write(BD.get_tail(n))

def obtenerDescribe(BD):
    st.write("Descripción de la Base de Datos")
    st.write(BD.get_describe())
    # columnas = BD.get_columnas()
    # columna = st.selectbox("Seleccione una columna para realizar análisis descriptivo", columnas)
    # st.write(BD.get_AnalisisDescriptivo(columna))
    # st.write(BD.get_grafico())

def valoresNull(BD):
    st.write("Valores faltantes:")
    BD.get_column_null()
    
    column= st.session_state.data.columns
    column = st.selectbox("Selecciona columna a remplazar", column)
    if st.button("Ver valores nulos"):
        BD.get_valoresnull(column)
    valor = st.selectbox("Reemplaza datos faltantes con su media", ["Moda","Media","Mediana"])
    if st.button("Cambiar valores nulos"):
        BD.cambiarnulos(column,valor)
    
    

def Cambio_tipo(BD):
    st.write("Tipos de datos")
    st.write(BD.get_types())
    columns= st.session_state.data.columns
    column = st.selectbox("Seleccione una columna para modificar tipo de datos", columns)
    tipo = st.selectbox("Seleccione un tipo de datos", ["", "int", "float", "object", "datetime64[ns]"])
    if st.button("Cambiar tipo de dato"):
        BD.cambioTipo(column, tipo)

def cambioMoneda(BD):
    st.write("Cambio de Moneda")
    columns= st.session_state.data.columns
    column = st.selectbox("Seleccione una columna para cambiar moneda", columns)
    valores=st.selectbox("Seleccione moneda a cambiar",["","Usd-Clp","Clp-Usd","Eur-Usd","Eur-Clp","Usd-Eur","Clp-Eur"])
    if st.button("Cambiar moneda"):
        BD.set_moneda(column, valores)

def MedidasTendencia(BD):
    st.write("Medidas de Tendencia Central")
    columns= st.session_state.data.columns
    column = st.selectbox("Seleccione una columna para obtener medidas de tendencia central", columns)
    if st.button("Obtener medidas de tendencia central"):
        BD.get_AnalisisDescriptivo(column)

def get_grafico(BD):
    st.write("Gráfico")
    columns= st.session_state.data.columns
    column = st.selectbox("Seleccione una columna para graficar",columns)
    if st.button("Ver gráfico"):
        BD.get_grafico(column)
    