from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve


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