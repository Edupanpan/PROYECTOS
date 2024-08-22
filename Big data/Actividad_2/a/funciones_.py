import streamlit as st
from a.DataAnalysis import CSV

def cargar_csv(upload_file):
    if upload_file and 'data' not in st.session_state:
        analyzer = CSV(upload_file)
        analyzer.CargarCSv()

def mostrar_dataframe():
    if 'data' in st.session_state:
        st.write("### DataFrame")
        st.dataframe(st.session_state.data)

        st.write("Primeras Filas del DF")
        st.write(st.session_state.data.head())

        st.write('Ultimas Filas del DF')
        st.write(st.session_state.data.tail())

        st.write('Descripcion del DF')
        st.write(st.session_state.data.describe())

        st.write('Valores Nulos del DF')
        st.write(st.session_state.data.isnull().sum())

        st.write('Info del DF')
        analyzer = CSV(None)
        st.text(analyzer.obtener_info_df())

        csv = st.session_state.data.to_csv(index=False)
        st.download_button(
            label="Descargar DataFrame modificado",
            data=csv,
            file_name='df_modificado.csv',
            mime='text/csv',
        )