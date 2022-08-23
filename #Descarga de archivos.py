#Descarga de archivos
#Importando bibliotecas
import os
import urllib.request
import datetime
import pandas as pd
import zipfile

# pwd
print(os.getcwd())

#  Estos son los datos que vamos a descargar y donde vamos a guardarlos
mineria_sonora_url = "https://www.inegi.org.mx/contenidos/masiva/indicadores/temas/mineria/mineria_26_xlsx.zip"
mineria_sonora_archivo = "mineriasonora.zip"
subdir = "./data/"

if not os.path.exists(mineria_sonora_archivo):
    if not os.path.exists(subdir):
        os.makedirs(subdir)
    urllib.request.urlretrieve(mineria_sonora_url, subdir + mineria_sonora_archivo)  
    with zipfile.ZipFile(subdir + mineria_sonora_archivo, "r") as zip_ref:
        zip_ref.extractall(subdir)

    with open(subdir + "info.txt", 'w') as f:
        f.write("Indicadores de minería en Sonora\n")
        info = """
        Indicadores de minería en Sonora.

        Los datos se obtuvieron de Dercarga masiva de INEGI con fecha de 23 de agosto de 2022 (la base de datos se actualiza constantemente) 

        """ 
        f.write(info + '\n')
        f.write("Descargado el " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write("Desde: " + mineria_sonora_url + "\n")
        f.write("Nombre: " + mineria_sonora_archivo + "\n")
