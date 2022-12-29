import json
import os
import urllib.request
from urllib.request import Request, urlopen


class_name = "cats"


#funcion descargar imagen dado un url y su destino
def download_image(url, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    req = Request(
            url=url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
    response = urlopen(req)
    file = open(dest + "/" + url.split("/")[-1]+".jpg", 'wb')
    file.write(response.read())
    file.close()
    print("Image successfully Downloaded: ",url.split("/")[-1])

#70% train, 15% test, 15% validation

with open(class_name+'.json') as json_file:
    data = json.load(json_file)["data"]
    
    for index, link in enumerate(data):
        print(link)
        #verificar si existe la imagen en el directorio
        folder = "train"
        if index > len(data)*0.7:
            folder = "test"
        elif index > len(data)*0.85:
            folder = "valid"
        
        
        if not os.path.exists("dataset/"+class_name+"/"+folder+"/" + link.split("/")[-1]):
            download_image(link, "dataset/"+class_name+"/"+folder)
