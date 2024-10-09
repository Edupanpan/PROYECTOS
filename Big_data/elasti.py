from elasticsearch import Elasticsearch

# Crear una instancia del cliente de Elasticsearch
es = Elasticsearch(hosts=["http://localhost:9200"],basic_auth=("sebita","1234567"))

# Verificar la conexión

if es.ping():
    print("Conectado a Elasticsearch")
else:
    print("No se pudo conectar a Elasticsearch")
