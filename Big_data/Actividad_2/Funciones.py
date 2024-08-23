from Clase import *
import streamlit as st
def menu():
    
    st.title("Activad Numero 2 Big Data") 
    
    uploaded_file = st.file_uploader("Carga tu archivo CSV", type=["csv"])
    
    if uploaded_file and 'data' not in st.session_state:
        BD = AnalisisDatos(uploaded_file)
        BD.load_data()

    if 'data' in st.session_state:
        BD = AnalisisDatos(None)
        
        st.title("MENU DE FUNCIONES")
        
        st.header("VIsualización de Datos")
        opc = st.selectbox("", ["Base de datos", "Primeras Filas", "Últimas Filas"])
        if st.button("Ver Datos"):
            if opc == "Base de datos":
                obtenerDatos(BD)
            elif opc == "Primeras Filas":
                obtenerHead(BD)
            elif opc == "Últimas Filas":
                obtenerTail(BD)
        
        st.divider()
        st.header("Información General")
        if st.button("Ver Información 'sucia'"):    
            obtenerDescribe(BD)
                
        st.divider()
        st.title("Limpieza de Datos")
        st.header("Paso 1: Valores Faltantes")
        valoresNull(BD)
        
        
        st.divider()
        st.header("Paso 2: Limpiar edades")
        if st.button("Limpiar edades"):
            st.write("modificado con exito") 
            BD.evaluar_edades()
        
        st.divider()
        st.header("Paso 3: Cambio de tipo de datos")
        Cambio_tipo(BD)

        st.divider()
        st.header("Paso opcional: Cambio de moneda")
        cambioMoneda(BD)

        st.divider()
        st.header("Paso 4: Medidas de Tendencia Central")
        MedidasTendencia(BD)

        st.divider()
        get_grafico(BD)
        
        st.divider()
        get_outliers(BD)
                
            
                


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
    BD.get_cantidad_column_null()
    
    columns= BD.get_column_null()
    column=st.selectbox("Selecciona columna a remplazar", columns)
    BD.get_valores_null(column)
    valor = st.selectbox("Reemplaza datos faltantes con su media", ["Moda","Media","Mediana"])
    if st.button("Cambiar valores nulos"):
        if column in st.session_state.data.columns:
            st.write("modificado con exito")
            BD.cambiarnulos(valor, column)
        else:
            st.error(f"La columna {column} no existe en el DataFrame.")
    

def Cambio_tipo(BD):
    st.write("Tipos de datos")
    st.write(BD.get_types())
    columns= st.session_state.data.columns
    column = st.selectbox("Seleccione una columna para modificar tipo de datos", columns)
    tipo = st.selectbox("Seleccione un tipo de datos", ["", "int", "float", "object", "datetime64[ns]"])
    if st.button("Cambiar tipo de dato"):
        BD.cambioTipo(column, tipo)
        st.write("Modificado con exito")

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
def get_outliers(BD):
    st.write("Outliers")
    columns= st.session_state.data.columns
    column = st.selectbox("Seleccione una columna para detectar outliers",columns)
    if st.button("Detectar Outliers"):
        BD.get_boxplot_or_frequency(column)
    