import pandas as pd
from io import StringIO

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
    
    def get_valoresnull(self):
        if self.data is not None:
            return self.data.isnull().sum()
    
    def mostrarnulos(self, columna):
        if self.data is not None:
            promedio=self.data[columna].mean()
            #return self.data[columna].fillna(promedio)
            return self.data[self.data[columna].isnull()]
    def get_columnas(self):
        if self.data is not None:
            return self.data.columns.values
            
#presentar variables que se pueden modificar en los valores nulos