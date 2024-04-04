import os
import requests

# Crear una carpeta para almacenar las imágenes descargadas
carpeta_imagenes = 'imagenes_descargadas'
if not os.path.exists(carpeta_imagenes):
    os.makedirs(carpeta_imagenes)

# Descargar 1000 imágenes
for i in range(5):
    # URL de la imagen a descargar
    url_imagen = 'https://thispersondoesnotexist.com/'
    # Realizar la solicitud GET para descargar la imagen
    respuesta = requests.get(url_imagen)
    # Ruta completa del archivo
    ruta_archivo = os.path.join(carpeta_imagenes, f"imagen_{i}.jpg")
    # Guardar la imagen en la carpeta
    with open(ruta_archivo, 'wb') as archivo:
        archivo.write(respuesta.content)

print("Descarga de imágenes completada.")
