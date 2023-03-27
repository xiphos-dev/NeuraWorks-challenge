# NeuralWorks challenge

## Análisis de modelo predictivo e implementación de API

1. Análisis de modelo y propuestas de mejora: `notebook/to_expose.ipynb`
2. Modelo guardado AUC 0.587: `api/modelo_datos_adicionales.json`
3. API: `api/api.py`
4. Cliente API: `cliente/cliente.py`

### Requerimientos
* `Python 3.8`
* Librerías: `pip install -r requirements.txt`


### Consideraciones

1. Para mantener el tiempo de ejecución reducido, se realizó un 5-fold nested cross validation. El espacio de búsqueda para los hiper-parámetros fue reducido, y solo unos pocos fueron considerados. La intención era demostrar una prueba de concepto: que este método puede aportar a mejorar los resultados obtenidos, sin necesariamente pagar el costo de tiempo de entrenamiento que tomaría aplicarlo de manera exhaustiva (con un N mayor y/o con un espacio de búqueda más grande para cada parámetro).

2. El modelo rescatado a partir del Inciso 2 fue guardado en formato json (`api/modelo_datos_adicionales.json`) en lugar de ser serializado, por ejemplo, en formato binario. Esto es debido a que los modelos de la librería XGBoost no son "estables ni portables" al ser serializados con librerías como pickle: leer más aquí https://xgboost.readthedocs.io/en/latest/tutorials/saving_model.html

3. Inciso 4: Para automatizar el proceso de build y deployment se puede recurrir a GitHub Actions, Kubernetes para la creación de la imagen de contenedor, y GCP para hospedar la API como un servicio en la nube. GCP permite tomar ventaja de la integración con elementos como Google Kubernetes Engine. El archivo `api/deploy.yaml` contiene un ejemplo de archivo de workflow para este proceso.

4. Inciso 5: el archivo `api/stats.png` contiene los resultados de la prueba realizada sobre la API. Dado que el servidor se encuentra montado sobre un equipo de uso personal, no cuenta con los recursos necesarios para asegurar la disponibilidad de la API frente al volumen de solicitudes de la prueba. Para mejorar estos resultados es posible escalar el backend horizontalmente, y también hacer uso de un load balancer para mitigar el riesgo que uno de los servidores se sature con solicitudes. La latencia de las respuestas esta asociada al hardware del servidor, dado que es un indicio del tiempo que este tarda en procesar la solicitud y responder con el resultado. Es trivial que el escalamiento vertical ayudará a mejorar este parámetro. Por otra parte, dependiendo del contexto en que la API será usada, una manera de reducir este lapso es solicitar a los usuarios enviar una versión pre-procesada de los datos, para así dimisnuir la carga de trabajo en el servidor. El módulo de API fue construido asumiendo que los usuarios enviarán solicitudes con el formato en que los datos se encuentran dentro del archivo `dataset_SCL.csv`.