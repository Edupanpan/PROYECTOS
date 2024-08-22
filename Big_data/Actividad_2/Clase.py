import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

class AnalisisDatos:
    def __init__(self, CsvUploud=None):
        self.data = None
        self.csv_upload = CsvUploud
    
    def load_data(self):
        if self.csv_upload and self.csv_upload.name.endswith('.csv'):
            self.data = pd.read_csv(self.csv_upload)
            st.session_state.data = self.data
        else:
            st.error("Formato de archivo no soportado.")

    def get_datos(self):
        st.dataframe(st.session_state.data)
    
    def get_head(self, n=20):
        st.dataframe(st.session_state.data.head(n))
    
    def get_tail(self, n=20):
        st.dataframe(st.session_state.data.tail(n))
    
    def get_describe(self):
        st.dataframe(st.session_state.data.describe())
    def get_column_null(self):
        st.dataframe(st.session_state.data.isnull().sum())
    def get_valoresnull(self,column):
        global ID_new
        ID_null=st.session_state.data[st.session_state.data[column].isnull()].index.tolist()
        ID_new=ID_null
        st.dataframe(st.session_state.data.loc[ID_null])  
         
    def cambiarnulos(self, column,valor):
            st.dataframe(st.session_state.data.isnull().sum()) 
            if valor == "Moda":
                mode=self.get_mode(column)
                st.session_state.data[column].fillna(mode, inplace=True)
            elif valor == "Media":
                mean=self.get_mean(column)
                st.session_state.data[column].fillna(mean, inplace=True)
            elif valor == "Mediana":
                median=self.get_median(column)
                st.session_state.data[column].fillna(median, inplace=True)
            st.dataframe(st.session_state.data.loc[ID_new])

    def get_columnas(self):
        st.dataframe(st.session_state.data.columns.values)
            
    
    

    def get_mean(self,column):
        return st.session_state.data[column].mean()
    def get_mode(self,column):
        return st.session_state.data[column].mode()
    def get_median(self,column):
        return st.session_state.data[column].median()
    def get_var(self,column):
        return st.session_state.data[column].var()
    def get_std(self,column):
        return st.session_state.data[column].std()
    def get_range(self,column):
        return st.session_state.data[column].quantile(0.75)-st.session_state.data[column].quantile(0.25)
        
    
    def get_types(self):
        st.dataframe(st.session_state.data.dtypes)
    
    def cambioTipo(self, column, tipo):#cambiar tipos de datos de columnas
            if tipo == "int":
                st.dataframe(st.session_state.data[column].astype(int))

            elif tipo == "float":
                st.dataframe(st.session_state.data[column].astype(float))
            elif tipo == "object":
                st.dataframe(st.session_state.data[column].astype(object))
            elif tipo == "datetime64[ns]":
                st.session_state.data[column] = pd.to_datetime(st.session_state.data[column], format='mixed')           
            st.dataframe(st.session_state.data)

    def set_moneda(self, column,valores):#funcion para cambiar moneda de alguna columna de salario si existe
            if valores=="Usd-Clp":
                st.session_state.data[column]=st.session_state.data[column]*924
                st.dataframe(st.session_state.data[column])
            elif valores=="Clp-Usd":
                st.session_state.data[column]=st.session_state.data[column]/924
                st.dataframe(st.session_state.data[column])
            elif valores=="Eur-Usd":
                st.session_state.data[column]=st.session_state.data[column]*1.11
                st.dataframe(st.session_state.data[column])
            elif valores=="Usd-Eur":
                st.session_state.data[column]=st.session_state.data[column]/1.11
                st.dataframe(st.session_state.data[column])
            elif valores=="Eur-Clp":
                st.session_state.data[column]=st.session_state.data[column]*1027
                st.dataframe(st.session_state.data[column])
            elif valores=="Clp-Eur":
                st.session_state.data[column]=st.session_state.data[column]/1027
                st.dataframe(st.session_state.data[column])
    
    #especifico del proyecto:
    def get_AnalisisDescriptivo(self, columna):

            if columna=="Age":
                st.write("Edad promedio: ",self.get_mean(columna))
                st.write("Edad mediana: ",self.get_median(columna))
                st.write("Edad moda: ",self.get_mode(columna))
                st.write("Edad varianza: ",self.get_var(columna))
                st.write("Edad desviación estándar: ",self.get_std(columna))
                st.write("Edad Rango intercuartil: ",self.get_range(columna))
            elif columna=="Salary":
                st.write("Salario promedio: ",self.get_mean(columna))
                st.write("Salario mediana: ",self.get_median(columna))
                st.write("Salario moda: ",self.get_mode(columna))
                st.write("Salario varianza: ",self.get_var(columna))
                st.write("Salario desviación estándar: ",self.get_std(columna))
                st.write("Salario Rango intercuartil: ",self.get_range(columna))
            else:
                st.write("No se puede realizar análisis descriptivo de esta columna")
    def get_grafico(self,column):
            
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
            if 'Salary' in column:
                ax1.bar(st.session_state.data['ID'], st.session_state.data['Salary'], alpha=0.7)
                ax1.set_xlabel('ID')
                ax1.set_ylabel('Salary')
                ax1.set_title('Gráfico de Barras de Salario')
                ax1.grid(True)
            else:
                ax1.set_visible(False)  # Ocultar el eje si no hay datos
            if 'Age' in column:
                ax2.bar(st.session_state.data['ID'], st.session_state.data['Age'], alpha=0.7)
                ax2.set_xlabel('ID')
                ax2.set_ylabel('Age')
                ax2.set_title('Gráfico de Barras de Edad')
                ax2.grid(True)
            else:
                ax2.set_visible(False)  # Ocultar el eje si no hay datos

            st.pyplot(fig)# Mostrar los gráficos en Streamlit
    def get_outlier(self,column):
        edad=st.session_state.data[column]
        Q1 = st.session_state.data[column].quantile(0.25)
        Q3 = st.session_state.data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        st.dataframe(st.session_state.data[(st.session_state.data[column] < lower_bound) | (st.session_state.data[column] > upper_bound)])
        fig, ax = plt.subplots()
        ax.boxplot(edad, vert=False)
        ax.set_title('Boxplot de edades')
        ax.set_xlabel('Edad')
        st.pyplot(fig)