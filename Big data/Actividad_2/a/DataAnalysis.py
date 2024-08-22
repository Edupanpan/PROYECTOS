import pandas as pd
import streamlit as st
from io import StringIO

class CSV:
    def __init__(self, file=None):
        self.file = file

    def CargarCSv(self):
        if self.file and self.file.name.endswith('.csv'):
            st.session_state.data = pd.read_csv(self.file)
        else:
            st.error("Formato de archivo no soportado.")

    def datos_faltantes(self, column):
        if not isinstance(self.data, pd.DataFrame):
            raise ValueError("self.data no es un DataFrame válido.")
        
        if column not in self.data.columns:
            raise ValueError(f"La columna '{column}' no existe en el DataFrame.")
        
        self.data[column].fillna(self.data[column].mean(), inplace=True)
        return self.data


    def cambiar_tipo(self, column, new_dtype):
        self.data[column] = self.data[column].astype(new_dtype)
        return self.data

    def convertir_moneda(self, column, conversion_option):
        if conversion_option == 'USD a CLP':
            self.data[column] = self.data[column] * 850  # Ejemplo de tasa de cambio
        elif conversion_option == 'CLP a USD':
            self.data[column] = self.data[column] / 850  # Ejemplo de tasa de cambio
        return self.data

    def limitar_edad(self, column, min_age, max_age):
        self.data = self.data[(self.data[column] >= min_age) & (self.data[column] <= max_age)]
        return self.data


    def obtener_info_df(self):
        buffer = StringIO()
        st.session_state.data.info(buf=buffer)
        info_str = buffer.getvalue()
        buffer.close()
        return info_str