import pickle
import xgboost
import pandas as pd
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/predecir/", methods=['POST'])
def predecir():

    datos = request.get_json()
    dataframe = pd.DataFrame.from_dict(datos)
    data = dataframe[['OPERA', 'MES', 'TIPOVUELO', 'SIGLADES', 'DIA']]
    dataframe = pd.DataFrame(0, index=np.arange(len(datos['MES'])), columns=columnas)
    res = {}
    predicciones = modelo.predict(dar_formato(data,dataframe))
    for contador, valor in enumerate(predicciones):
        res[int(contador)] = int(valor)

    return jsonify(res)


def dar_formato(datos, dataframe):
    for i in range(len(datos['MES'])):
        dataframe.loc[i,'MES_'+str(datos['MES'][i])] = 1
        dataframe.loc[i,'OPERA_'+datos['OPERA'][i]] = 1
        dataframe.loc[i,'TIPOVUELO_'+datos['TIPOVUELO'][i]] = 1
        dataframe.loc[i,'SIGLADES_'+datos['SIGLADES'][i]] = 1
    return dataframe


if __name__ == '__main__':
    ARCHIVO_MODELO = 'modelo_datos_adicionales.json'
    ARCHIVO_COLUMNAS = 'columnas_datos_adicionales.pkl'
    modelo = xgboost.XGBClassifier()
    modelo.load_model(ARCHIVO_MODELO)
    with open(ARCHIVO_COLUMNAS, 'rb') as archivo:
        columnas = pickle.load(archivo)
    app.run(debug=True)
