from Clase import *
import streamlit as st

def menu(BD):
    st.title("Limpieza de Datos")

    uploaded_file = st.file_uploader("Carga tu archivo CSV", type=["csv"])

    if uploaded_file and 'data' not in st.session_state:
        analyzer = AnalisisDatos(uploaded_file)
        analyzer.load_data()

    if 'data' in st.session_state:
        analyzer = AnalisisDatos(None)
        if 'metodo' not in st.session_state:
            st.session_state.metodo = 1
        with st.sidebar:
            st.header("Menú")
            if st.session_state.metodo == 1:
                opc = st.selectbox("Seleccione una opción", ["Base de datos", "Primeras Filas", "Últimas Filas"])
                if opc == "Base de datos":
                    obtenerDatos(BD)
                elif opc == "Primeras Filas":
                    obtenerHead(BD)
                elif opc == "Últimas Filas":
                    obtenerTail(BD)

                if st.button("Siguiente"):
                    st.session_state.metodo = 2
                    st.rerun()
        
            elif st.session_state.metodo == 2:
                # opc = st.selectbox("Seleccione una opción para modificar valores nulos", ["media", "moda", "mediana"])
                # if opc is not None:
                valoresNull(BD)
                if st.button("Guardar Datos"):
                    guardar_datos()
                if st.button("Anterior"):
                    st.session_state.metodo = 1
                    st.rerun()
                if st.button("Siguiente"):
                    st.session_state.metodo = 3
                    st.rerun()
        
            elif st.session_state.metodo == 3:
                Cambio_tipo(BD)
                if st.button("Guardar Datos"):
                    guardar_datos()
                if st.button("Anterior"):
                    st.session_state.metodo = 2
                    st.rerun()
                if st.button("Siguiente"):
                    st.session_state.metodo = 4
                    st.rerun()
            
            elif st.session_state.metodo == 4:
                opc = st.selectbox("Seleccione una opción", ["Información de la Base de Datos", "Descripción de la Base de Datos"])
                if opc == "Información de la Base de Datos":
                    obtenerInfo(BD)
                elif opc == "Descripción de la Base de Datos":
                    obtenerDescribe(BD)

                if st.button("Anterior"):
                    st.session_state.metodo = 3
                    st.rerun()
                if st.button("Siguiente"):
                    st.session_state.metodo = 5
                    st.rerun()

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
    columnas = BD.get_columnas()
    columna = st.selectbox("Seleccione una columna para realizar análisis descriptivo", columnas)
    st.write(BD.get_AnalisisDescriptivo(columna))
    st.write(BD.get_grafico())

def valoresNull(BD):
    # columnas = BD.get_columnas()
    # columna = st.selectbox("Seleccione una columna para modificar valores nulos", columnas)
    # st.write("Valores faltantes:")
    # st.write(BD.get_valoresnull())
    # st.write(BD.cambiarnulos(valor, columna))
    st.write("Valores faltantes:")
    st.write(BD.get_valoresnull())
    columnas=BD.get_columnas()
    texto_usuario = st.selectbox("Seleccione una columna para modificar valores nulos",columnas) 
    valor_modificar = st.selectbox("Seleccione un valor",["","Moda","Media","Mediana"]) 
    st.write(BD.cambiarnulos(texto_usuario, valor_modificar))

def Cambio_tipo(BD):
    st.write("Tipos de datos")
    st.write(BD.get_types())
    columnas = BD.get_columnas()
    columna = st.selectbox("Seleccione una columna para modificar tipo de datos", columnas)
    tipo = st.selectbox("Seleccione un tipo de datos", ["", "int", "float", "object", "datetime64[ns]"])
    st.write(BD.cambioTipo(columna, tipo))

def guardar_datos():
    # df = BD.get_datos()
    # df.to_csv(nombre_archivo, index=False)  
    # st.write(f"Datos guardados en {nombre_archivo}")
    # st.write(df)
    # BD=df
    # return BD
    st.write("Datos guardados")