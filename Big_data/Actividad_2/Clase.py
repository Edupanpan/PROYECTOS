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
        null_columns = st.session_state.data.columns[st.session_state.data.isnull().any()]
        return null_columns
    
    def get_cantidad_column_null(self):
        null_counts = st.session_state.data.isnull().sum()
        st.dataframe(null_counts[null_counts > 0])
    
    def get_valores_null(self,column):
        ID_null=st.session_state.data[st.session_state.data[column].isnull()].index.tolist()
        st.dataframe(st.session_state.data.loc[ID_null])
        
    
    def evaluar_edades(self):
        edades = st.session_state.data[(st.session_state.data['Age'] >= 18) & (st.session_state.data['Age'] <= 80)]
        st.session_state.data = edades
    
    def cambiarnulos(self, valor,column):
            if valor == "Moda":
                mode=self.get_mode(column)
                st.session_state.data[column].fillna(mode, inplace=True)
                
            elif valor == "Media":
                mean=self.get_mean(column)
                st.session_state.data[column].fillna(mean, inplace=True)
                
            elif valor == "Mediana":
                median=self.get_median(column)
                st.session_state.data[column].fillna(median, inplace=True)
            
            
            

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
    
    def get_grafico(self, column):
        if st.session_state.data[column].dtype == 'int64' or st.session_state.data[column].dtype == 'float64':
            plt.hist(st.session_state.data[column], bins='auto')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.title(f'Histogram of {column}')
            st.pyplot()
        elif st.session_state.data[column].dtype == 'object':
            
            value_counts = st.session_state.data[column].value_counts()
            plt.bar(value_counts.index, value_counts.values)
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.title(f'Bar Chart of {column}')
            plt.xticks(rotation=90)
            st.pyplot()
        else:
            st.write("Cannot plot histogram for non-numeric column.")
            
            
    def get_boxplot_or_frequency(self, column):
        if st.session_state.data[column].dtype == 'int64':
            data = st.session_state.data.dropna(subset=[column, 'Age'])
            plt.boxplot(data[column])
            plt.xlabel(column)
            plt.ylabel('Value')
            plt.title(f'Boxplot of {column}')
            st.pyplot()
        else:
            st.write("Cannot generate boxplot for this column.")
