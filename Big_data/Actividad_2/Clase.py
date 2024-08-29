import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

class AnalisisDatos:
    def __init__(self, CsvUploud=None):
        self.data = None
        self.csv_upload = CsvUploud
    
    def load_data(self):
        try:
            if self.csv_upload and self.csv_upload.name.endswith('.csv'):
                self.data = pd.read_csv(self.csv_upload)
                st.session_state.data = self.data
            else:
                st.error("Formato de archivo no soportado.")
        except Exception as e:
            st.error(f"Error al cargar los datos: {e}")

    def get_datos(self):
        try:
            st.dataframe(st.session_state.data)
        except Exception as e:
            st.error(f"Error al obtener los datos: {e}")
    
    def get_head(self, n=20):
        try:
            st.dataframe(st.session_state.data.head(n))
        except Exception as e:
            st.error(f"Error al obtener las primeras filas: {e}")
    
    def get_tail(self, n=20):
        try:
            st.dataframe(st.session_state.data.tail(n))
        except Exception as e:
            st.error(f"Error al obtener las últimas filas: {e}")
    
    def get_describe(self):
        try:
            st.dataframe(st.session_state.data.describe())
        except Exception as e:
            st.error(f"Error al obtener la descripción: {e}")

    def get_column_null(self):
        try:
            null_columns = st.session_state.data.columns[st.session_state.data.isnull().any()]
            return null_columns
        except Exception as e:
            st.error(f"Error al obtener columnas con valores nulos: {e}")
    
    def get_cantidad_column_null(self):
        try:
            null_counts = st.session_state.data.isnull().sum()
            st.dataframe(null_counts[null_counts > 0])
        except Exception as e:
            st.error(f"Error al obtener cantidad de valores nulos: {e}")
    
    def get_valores_null(self, column):
        try:
            ID_null = st.session_state.data[st.session_state.data[column].isnull()].index.tolist()
            st.dataframe(st.session_state.data.loc[ID_null])
        except Exception as e:
            st.error(f"Error al obtener valores nulos: {e}")
        
    def evaluar_edades(self):
        try:
            edades = st.session_state.data[(st.session_state.data['Age'] >= 18) & (st.session_state.data['Age'] <= 80)]
            st.session_state.data = edades
        except Exception as e:
            st.error(f"Error al evaluar edades: {e}")
    
    def cambiarnulos(self, valor, column):
        try:
            if valor == "Moda":
                mode = self.get_mode(column)
                st.session_state.data[column].fillna(mode, inplace=True)
            elif valor == "Media":
                mean = self.get_mean(column)
                st.session_state.data[column].fillna(mean, inplace=True)
            elif valor == "Mediana":
                median = self.get_median(column)
                st.session_state.data[column].fillna(median, inplace=True)
        except Exception as e:
            st.error(f"Error al cambiar valores nulos: {e}")

    def get_columnas(self):
        try:
            st.dataframe(st.session_state.data.columns.values)
        except Exception as e:
            st.error(f"Error al obtener columnas: {e}")

    def get_mean(self, column):
        return st.session_state.data[column].mean()
    
    def get_mode(self, column):
        return st.session_state.data[column].mode()
    
    def get_median(self, column):
        return st.session_state.data[column].median()
    
    def get_var(self, column):
        return st.session_state.data[column].var()
    
    def get_std(self, column):
        return st.session_state.data[column].std()
    
    def get_range(self, column):
        return st.session_state.data[column].quantile(0.75) - st.session_state.data[column].quantile(0.25)
    
    def get_types(self):
        try:
            st.dataframe(st.session_state.data.dtypes)
        except Exception as e:
            st.error(f"Error al obtener tipos de datos: {e}")
    
    def cambioTipo(self, column, tipo):
        try:
            if tipo == "int":
                st.dataframe(st.session_state.data[column].astype(int))
            elif tipo == "float":
                st.dataframe(st.session_state.data[column].astype(float))
            elif tipo == "object":
                st.dataframe(st.session_state.data[column].astype(object))
            elif tipo == "datetime64[ns]":
                st.session_state.data[column] = pd.to_datetime(st.session_state.data[column], format='mixed')
            st.dataframe(st.session_state.data)
        except Exception as e:
            st.error(f"Error al cambiar tipo de dato: {e}")

    def set_moneda(self, column, valores):
        try:
            if valores == "Usd-Clp":
                st.session_state.data[column] = st.session_state.data[column] * 924
            elif valores == "Clp-Usd":
                st.session_state.data[column] = st.session_state.data[column] / 924
            elif valores == "Eur-Usd":
                st.session_state.data[column] = st.session_state.data[column] * 1.11
            elif valores == "Usd-Eur":
                st.session_state.data[column] = st.session_state.data[column] / 1.11
            elif valores == "Eur-Clp":
                st.session_state.data[column] = st.session_state.data[column] * 1027
            elif valores == "Clp-Eur":
                st.session_state.data[column] = st.session_state.data[column] / 1027
            st.dataframe(st.session_state.data[column])
        except Exception as e:
            st.error(f"Error al cambiar moneda: {e}")

    def get_AnalisisDescriptivo(self, columna):
        try:
            if columna == "Age":
                st.write("Edad promedio: ", self.get_mean(columna))
                st.write("Edad mediana: ", self.get_median(columna))
                st.write("Edad moda: ", self.get_mode(columna))
                st.write("Edad varianza: ", self.get_var(columna))
                st.write("Edad desviación estándar: ", self.get_std(columna))
                st.write("Edad Rango intercuartil: ", self.get_range(columna))
            elif columna == "Salary":
                st.write("Salario promedio: ", self.get_mean(columna))
                st.write("Salario mediana: ", self.get_median(columna))
                st.write("Salario moda: ", self.get_mode(columna))
                st.write("Salario varianza: ", self.get_var(columna))
                st.write("Salario desviación estándar: ", self.get_std(columna))
                st.write("Salario Rango intercuartil: ", self.get_range(columna))
            else:
                st.write("No se puede realizar análisis descriptivo de esta columna")
        except Exception as e:
            st.error(f"Error al obtener análisis descriptivo: {e}")
    
    def get_grafico(self, column):
        try:
            if st.session_state.data[column].dtype == 'int64' or st.session_state.data[column].dtype == 'float64':
                plt.hist(st.session_state.data[column], bins='auto')
                plt.xlabel(column)
                plt.ylabel('Frequency')
                plt.title(f'Histogra {column}')
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
        except Exception as e:
            st.error(f"Error al generar gráfico: {e}")
            
    def get_boxplot_or_frequency(self, column):
        try:
            if st.session_state.data[column].dtype == 'int64':
                data = st.session_state.data.dropna(subset=[column, 'Age'])
                plt.boxplot(data[column])
                plt.xlabel(column)
                plt.ylabel('Value')
                plt.title(f'Boxplot of {column}')
                st.pyplot()
            else:
                st.write("Cannot generate boxplot for this column.")
        except Exception as e:
            st.error(f"Error al generar boxplot: {e}")
    def calcular_matriz_correlacion(self):
        try:
            if st.session_state.data is not None:
                numeric_columns = st.session_state.data.select_dtypes(include=['int64', 'float64']).columns
                return st.session_state.data[numeric_columns].corr()
            else:
                st.error("No se han cargado los datos.")
        except Exception as e:
            st.error(f"Error al calcular la matriz de correlación: {e}")

    def visualizar_matriz_correlacion(self):
        try:
            corr_matrix = self.calcular_matriz_correlacion()
            plt.figure(figsize=(10, 8))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
            st.pyplot(plt)
        except Exception as e:
            st.error(f"Error al visualizar la matriz de correlación: {e}")

    def graficar_dispersion(self, col1, col2):
        try:
            if st.session_state.data is not None:
                numeric_columns = st.session_state.data.select_dtypes(include=['int64', 'float64']).columns
                if col1 in numeric_columns and col2 in numeric_columns:
                    plt.figure(figsize=(10, 6))
                    sns.scatterplot(x=st.session_state.data[col1], y=st.session_state.data[col2])
                    plt.xlabel(col1)
                    plt.ylabel(col2)
                    plt.title(f'Dispersión entre {col1} y {col2}')
                    st.pyplot(plt)
                else:
                    st.error("Las columnas deben ser numéricas.")
            else:
                st.error("No se han cargado los datos.")
        except Exception as e:
            st.error(f"Error al graficar la dispersión: {e}")

    def prueba_correlacion(self, col1, col2, metodo='pearson'):
        try:
            if st.session_state.data is not None:
                numeric_columns = st.session_state.data.select_dtypes(include=['int64', 'float64']).columns
                if col1 in numeric_columns and col2 in numeric_columns:
                    if metodo == 'pearson':
                        corr, p_value = pearsonr(st.session_state.data[col1], st.session_state.data[col2])
                    elif metodo == 'spearman':
                        corr, p_value = spearmanr(st.session_state.data[col1], st.session_state.data[col2])
                    else:
                        raise ValueError("Método no soportado. Use 'pearson' o 'spearman'.")
                    
                    st.write(f"Coeficiente de correlación ({metodo}): {corr}")
                    st.write(f"Valor p: {p_value}")
                else:
                    st.error("Las columnas deben ser numéricas.")
            else:
                st.error("No se han cargado los datos.")
        except Exception as e:
            st.error(f"Error al realizar la prueba de correlación: {e}")