import pandas as pd
from io import StringIO
import streamlit as st
import matplotlib.pyplot as plt

class AnalisisDatos:
    
    def __init__(self, CsvUploud=None):
        if CsvUploud:
            self.data = pd.read_csv(CsvUploud)
        else:
            self.data = None

    def get_datos(self):
        return self.data
    
    def get_head(self, n=20):
        if self.data is not None:
            return self.data.head(n)
    
    def get_tail(self, n=20):
        if self.data is not None:
            return self.data.tail(n) 

    def get_info(self):
        if self.data is not None:
            buffer = StringIO()#revisar blockde notas
            self.data.info(buf=buffer)
            return buffer.getvalue()
    
    def get_describe(self):
        if self.data is not None:
            return self.data.describe(include='all')

    def get_columnas(self):
        if self.data is not None:
            return self.data.columns.values
    
    def get_types(self):
        if self.data is not None:
            return self.data.dtypes
    
    def get_valoresnull(self):
        if self.data is not None:
            return self.data.isnull().sum()
    
   
    def cambiarnulos(self, columna, valor,valor_especifico):
        if self.data is not None:
            ids_nulos = self.data[self.data[columna].isnull()].index.tolist()
            filas_antes = self.data.loc[ids_nulos]
            if valor == "Moda":
                self.data[columna] = self.data[columna].fillna(self.data[columna].mode()[0])
            elif valor == "Media":
                self.data[columna] = self.data[columna].fillna(self.data[columna].mean())
            elif valor == "Mediana":
                self.data[columna] = self.data[columna].fillna(self.data[columna].median())
            elif valor == "Valor específico":
               
                self.data[columna] = self.data[columna].fillna(valor_especifico)
            filas_despues = self.data.loc[ids_nulos]
            return filas_despues

    
    def cambioTipo(self, columna, tipo):#cambiar tipos de datos de columnas
        if self.data is not None:
            if tipo == "int":
                self.data[columna] = self.data[columna].fillna(0)
                self.data[columna] = self.data[columna].astype(int)
                self.set_moneda(columna)

            elif tipo == "float":
                self.data[columna] = self.data[columna].fillna(0)   
                self.data[columna] = self.data[columna].astype(float)
                self.set_moneda(columna)
            elif tipo == "object":
                self.data[columna] = self.data[columna].fillna("Sin definir")
                self.data[columna] = self.data[columna].astype(str)
            elif tipo == "datetime64[ns]":
                self.data[columna] = self.data[columna].fillna("2021-01-01")
                self.data[columna] = pd.to_datetime(self.data[columna])            
            return self.data  

    def set_moneda(self, columna):#funcion para cambiar moneda de alguna columna de salario si existe
        if self.data is not None:
            valores=st.selectbox("Seleccione moneda a cambiar",["","Usd-Clp","Clp-Usd","Eur-Usd","Eur-Clp","Usd-Eur","Clp-Eur"])
            if valores=="Usd-Clp":
                self.data[columna]=self.data[columna]*924
            elif valores=="Clp-Usd":
                self.data[columna]=self.data[columna]/924
            elif valores=="Eur-Usd":
                self.data[columna]=self.data[columna]*1.11
            elif valores=="Usd-Eur":
                self.data[columna]=self.data[columna]/1.11
            elif valores=="Eur-Clp":
                self.data[columna]=self.data[columna]*1027
            elif valores=="Clp-Eur":
                self.data[columna]=self.data[columna]/1027
    
    #especifico del proyecto:
    def get_AnalisisDescriptivo(self, columna):
        if self.data is not None:
            if columna=="Age":
                st.write("Edad promedio: ",self.data[columna].mean())
                st.write("Edad mediana: ",self.data[columna].median())
                st.write("Edad moda: ",self.data[columna].mode()[0])
                st.write("Edad varianza: ",self.data[columna].var())
                st.write("Edad desviación estándar: ",self.data[columna].std())
                st.write("Edad Rango intercuartil: ",self.data[columna].quantile(0.75)-self.data[columna].quantile(0.25))
            elif columna=="Salary":
                st.write("Salario promedio: ",self.data[columna].mean())
                st.write("Salario mediana: ",self.data[columna].median())
                st.write("Salario moda: ",self.data[columna].mode()[0])
                st.write("Salario varianza: ",self.data[columna].var())
                st.write("Salario desviación estándar: ",self.data[columna].std())
                st.write("Salario Rango intercuartil: ",self.data[columna].quantile(0.75)-self.data[columna].quantile(0.25))
            elif columna=="Country":
                st.write("País con más registros: ",self.data[columna].mode()[0])
            else:
                st.write("No se puede realizar análisis descriptivo de esta columna")
    def get_grafico(self):
        if self.data is not None:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

            # Gráfico de barras para 'Salary'
            if 'Salary' in self.data.columns:
                ax1.bar(self.data['ID'], self.data['Salary'], alpha=0.7)
                ax1.set_xlabel('ID')
                ax1.set_ylabel('Salary')
                ax1.set_title('Gráfico de Barras de Salario')
                ax1.grid(True)
            else:
                ax1.set_visible(False)  # Ocultar el eje si no hay datos

            # Gráfico de barras para 'Age'
            if 'Age' in self.data.columns:
                ax2.bar(self.data['ID'], self.data['Age'], alpha=0.7)
                ax2.set_xlabel('ID')
                ax2.set_ylabel('Age')
                ax2.set_title('Gráfico de Barras de Edad')
                ax2.grid(True)
            else:
                ax2.set_visible(False)  # Ocultar el eje si no hay datos

            # Mostrar los gráficos en Streamlit
            st.pyplot(fig)