from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve


# Instalamos las librerías para conexión con MongoDB
import pymongo
import certifi


# Especificamos nuestra base de datos de MongoDB
ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://johnnlor:mperic82@cluster0.vamcmwn.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

baseDatos = client["async_team_data_base"]
print(baseDatos.list_collection_names())


# Cargar Servidor Inicial para Comprobar Funcionamiento
app=Flask(__name__)
cors = CORS(app)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


# Realizamos una prueba al Servidor
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running... We are OnLine!!!"
    return jsonify(json)


if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])