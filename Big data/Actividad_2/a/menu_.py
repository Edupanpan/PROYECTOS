import streamlit as st
from a.DataAnalysis import CSV

def Principal():
    if 'data' in st.session_state:
        if 'step' not in st.session_state:
            st.session_state.step = 1
        analyzer = CSV(st.session_state.data)
        with st.sidebar:
            if st.session_state.step == 1:
                Paso1(analyzer)
            elif st.session_state.step == 2:
                Paso2(analyzer)
            elif st.session_state.step == 3:
                Paso3(analyzer)
            elif st.session_state.step == 4:
                Paso4(analyzer)

def avanzar_paso(paso):
    st.session_state.step = paso

def Paso1(analyzer):
    st.header("Paso 1: Reemplaza datos faltantes")
    column_num = st.session_state.data.select_dtypes(include=['number']).columns
    column = st.selectbox("Reemplaza datos faltantes con su media", column_num)
    if st.button("Corregir Datos"):
        # Modificación directa en st.session_state.data
        st.session_state.data = analyzer.datos_faltantes(column)
        st.success(f"Se reemplazaron los datos de la columna '{column}' por la media de sus datos.")
        avanzar_paso(2)

def Paso2(analyzer):
    st.header("Paso 2: Cambiar tipo de dato")
    st.divider()
    all_columns = st.session_state.data.columns
    column_to_change = st.selectbox("Selecciona una columna para cambiar su tipo de dato", all_columns)
    new_dtype = st.selectbox("Selecciona el nuevo tipo de dato", ['int64', 'float64', 'str', 'datetime'])
    if st.button("Cambiar Tipo de Dato"):
        # Modificación directa en st.session_state.data
        st.session_state.data = analyzer.cambiar_tipo(column_to_change, new_dtype)
        st.success(f"Se cambió el tipo de dato de la columna '{column_to_change}' a '{new_dtype}'.")
        avanzar_paso(3)

def Paso3(analyzer):
    st.header("Paso 3: Convertir moneda")
    st.divider()
    column_num = st.session_state.data.select_dtypes(include=['number']).columns
    column_to_convert = st.selectbox("Selecciona una columna para convertir moneda", column_num)
    conversion_option = st.selectbox("Selecciona la conversión", ['USD a CLP', 'CLP a USD'])
    if st.button("Convertir Moneda"):
        # Modificación directa en st.session_state.data
        st.session_state.data = analyzer.convertir_moneda(column_to_convert, conversion_option)
        st.success(f"Se realizó la conversión en la columna '{column_to_convert}'.")
        avanzar_paso(4)

def Paso4(analyzer):
    st.header("Paso 4: Limitar edad")
    st.divider()
    column_num = st.session_state.data.select_dtypes(include=['number']).columns
    column_age = st.selectbox("Selecciona una columna para limitar la edad", column_num)
    min_age = st.number_input("Edad mínima", min_value=0, value=18)
    max_age = st.number_input("Edad máxima", min_value=0, value=70)
    if st.button("Aplicar Límite de Edad"):
        # Modificación directa en st.session_state.data
        st.session_state.data = analyzer.limitar_edad(column_age, min_age, max_age)
        st.success(f"Se aplicó un límite de edad en la columna '{column_age}'.")

if __name__ == "__main__":
    Principal()
