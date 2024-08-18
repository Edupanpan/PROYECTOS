from Clase import AnalisisDatos

def crearObjeto(uploaded_file):
    BD = AnalisisDatos(CsvUploud=uploaded_file)
    return BD

def obtenerDatos(BD):
    return BD.get_datos()

def obtenerHead(BD, n=20):
    return BD.get_head(n)

def obtenerTail(BD, n=20):
    return BD.get_tail(n)

def obtenerInfo(BD):
    return BD.get_info()

def obtenerDescribe(BD):
    return BD.get_describe()

def valoresNull(BD):
    return BD.get_valoresnull()