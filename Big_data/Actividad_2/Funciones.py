from Clase import AnalisisDatos
import streamlit as st

def menu():
    st.title("Actividad Número 2 Big Data")
    
    uploaded_file = st.file_uploader("Carga tu archivo CSV", type=["csv"])
    
    if uploaded_file and 'data' not in st.session_state:
        BD = AnalisisDatos(uploaded_file)
        BD.load_data()

    if 'data' in st.session_state:
        BD = AnalisisDatos(None)
        
        st.title("MENU DE FUNCIONES")
        
        st.header("Visualización de Datos")
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
            st.write("Modificado con éxito") 
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
    try:
        st.write("Base de Datos")
        st.write(BD.get_datos())
    except Exception as e:
        st.error(f"Error al obtener datos: {e}")

def obtenerHead(BD, n=20):
    try:
        st.write("Primeras Filas")
        st.write(BD.get_head(n))
    except Exception as e:
        st.error(f"Error al obtener primeras filas: {e}")

def obtenerTail(BD, n=20):
    try:
        st.write("Últimas Filas")
        st.write(BD.get_tail(n))
    except Exception as e:
        st.error(f"Error al obtener últimas filas: {e}")

def obtenerDescribe(BD):
    try:
        st.write("Descripción de la Base de Datos")
        st.write(BD.get_describe())
    except Exception as e:
        st.error(f"Error al obtener descripción: {e}")

def valoresNull(BD):
    if 'data' in st.session_state:
        BD = AnalisisDatos(None)
    try:
        
        st.write("Valores faltantes:")
        BD.get_cantidad_column_null()
        
        columns = BD.get_column_null()
        column = st.selectbox("Selecciona columna a reemplazar", columns)
        BD.get_valores_null(column)
        valor = st.selectbox("Reemplaza datos faltantes con su media", ["Moda", "Media", "Mediana"])
        if st.button("Cambiar valores nulos"):
            if column in st.session_state.data.columns:
                st.write("Modificado con éxito")
                BD.cambiarnulos(valor, column)
            else:
                st.error(f"La columna {column} no existe en el DataFrame.")
    except Exception as e:
        st.error(f"Error al manejar valores nulos: {e}")

def Cambio_tipo(BD):
    if 'data' in st.session_state:
        BD = AnalisisDatos(None)
    try:
        st.write("Tipos de datos")
        st.write(BD.get_types())
        columns = st.session_state.data.columns
        column = st.selectbox("Seleccione una columna para modificar tipo de datos", columns)
        tipo = st.selectbox("Seleccione un tipo de datos", ["", "int", "float", "object", "datetime64[ns]"])
        if st.button("Cambiar tipo de dato"):
            BD.cambioTipo(column, tipo)
            st.write("Modificado con éxito")
    except Exception as e:
        st.error(f"Error al cambiar tipo de dato: {e}")

def cambioMoneda(BD):
    if 'data' in st.session_state:
        BD = AnalisisDatos(None)
    try:
        st.write("Cambio de Moneda")
        columns = st.session_state.data.columns
        column = st.selectbox("Seleccione una columna para cambiar moneda", columns)
        valores = st.selectbox("Seleccione moneda a cambiar", ["", "Usd-Clp", "Clp-Usd", "Eur-Usd", "Eur-Clp", "Usd-Eur", "Clp-Eur"])
        if st.button("Cambiar moneda"):
            BD.set_moneda(column, valores)
    except Exception as e:
        st.error(f"Error al cambiar moneda: {e}")

def MedidasTendencia(BD):
    if 'data' in st.session_state:
        BD = AnalisisDatos(None)
    try:
        st.write("Medidas de Tendencia Central")
        columns = st.session_state.data.columns
        column = st.selectbox("Seleccione una columna para obtener medidas de tendencia central", columns)
        if st.button("Obtener medidas de tendencia central"):
            BD.get_AnalisisDescriptivo(column)
    except Exception as e:
        st.error(f"Error al obtener medidas de tendencia central: {e}")

def get_grafico(BD):
    if 'data' in st.session_state:
        BD = AnalisisDatos(None)
    try:
        st.write("Gráfico")
        columns = st.session_state.data.columns
        column = st.selectbox("Seleccione una columna para graficar", columns)
        if st.button("Ver gráfico"):
            BD.get_grafico(column)
    except Exception as e:
        st.error(f"Error al generar gráfico: {e}")

def get_outliers(BD):
    if 'data' in st.session_state:
        BD = AnalisisDatos(None)
    try:
        st.write("Outliers")
        columns = st.session_state.data.columns
        column = st.selectbox("Seleccione una columna para detectar outliers", columns)
        if st.button("Detectar Outliers"):
            BD.get_boxplot_or_frequency(column)
    except Exception as e:
        st.error(f"Error al detectar outliers: {e}")