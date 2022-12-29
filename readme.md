# Clasificacion de imagenes usando redes neuronales convolucionales



## Carpetas y archivos

* `Models.ipynb`: Notebook donde se entrena los modelos vgg, inception y la cnn propia
* `SVM.ipynb`: Notebook donde se entrena el modelo SVM
* `dataset`: Carpeta donde se guardan los datos de entrenamiento, test y validacion por clases
* `data_clases`: Contiene los datos imagenes recolectadas por clases de lexica.art
* `recolector_donwload_imgs.py`: Script para descargar imagenes dado un json como los de data_clases
* `recolector_web.js`: Script para recolectar imagenes desde la web de lexica.art. copia en el portapapeles un json como los de data_clases
* `dockerfile`: Dockerfile para correr los notebooks usando una imagen de jupyter con tensorflow y gpu

