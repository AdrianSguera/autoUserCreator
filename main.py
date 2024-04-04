import mysql.connector
from faker import Faker
import bcrypt
import os
import requests

cantidad_usuarios = 5

# Inicializar el generador de datos aleatorios
fake = Faker()

# Generar 1000 nombres aleatorios
nombres = [fake.name() for _ in range(cantidad_usuarios)]

# Generar 1000 correos electrónicos aleatorios
correos = [fake.email() for _ in range(cantidad_usuarios)]

contraseñas = ["1234" for _ in range(cantidad_usuarios)]

# Encriptar las contraseñas utilizando bcrypt
contraseñas_encriptadas = [bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt()) for contraseña in contraseñas]

# Crear una carpeta para almacenar las imágenes descargadas
carpeta_imagenes = 'imagenes_descargadas'  # Ruta absoluta
if not os.path.exists(carpeta_imagenes):
    os.makedirs(carpeta_imagenes)

# Descargar 1000 imágenes
i = 0  # Variable para mantener el número de la imagen
for _ in range(cantidad_usuarios):
    # URL de la imagen a descargar
    url_imagen = 'https://thispersondoesnotexist.com/'
    # Realizar la solicitud GET para descargar la imagen
    respuesta = requests.get(url_imagen)
    # Intentar guardar la imagen con un nombre único
    while True:
        # Ruta completa del archivo
        ruta_archivo = os.path.join(carpeta_imagenes, f"imagen_{i}.jpg")
        # Intentar guardar la imagen en la carpeta
        try:
            with open(ruta_archivo, 'xb') as archivo:  # 'xb' crea el archivo en modo binario, lanzará FileExistsError si ya existe
                archivo.write(respuesta.content)
            break  # Salir del bucle while si la imagen se guarda con éxito
        except FileExistsError:
            # Si el archivo ya existe, incrementar i y volver a intentar
            i += 1

# Conectarse a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234",
    database="usuarios_python"
)

# Verificar si la conexión fue exitosa
if conexion.is_connected():
    print("Conexión exitosa a la base de datos MySQL")

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Iterar sobre los datos y insertarlos en la tabla users
for i in range(cantidad_usuarios):
    nombre = nombres[i]
    correo = correos[i]
    contraseña = contraseñas_encriptadas[i]
    imagen = "imagen_{}.jpg".format(i)  # Ruta de la imagen
    # Consulta SQL para insertar un nuevo usuario en la tabla users
    consulta = "INSERT INTO users (name, email, password, image) VALUES (%s, %s, %s, %s)"
    valores = (nombre, correo, contraseña, imagen)
    cursor.execute(consulta, valores)

# Commit para guardar los cambios en la base de datos
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()

print("Datos insertados en la tabla users.")
