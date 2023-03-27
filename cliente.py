import requests
import pandas as pd

URL = 'http://127.0.0.1:5000/predecir/'
RUTA_DATOS = "dataset_SCL.csv"
N=10
datos = pd.read_csv(RUTA_DATOS, nrows=N).to_json()
HEADERS = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(URL, data=datos, headers=HEADERS)
print(r,r.text)
