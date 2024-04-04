import faker
from faker import Faker
import random
import string
import bcrypt

# Inicializar el generador de datos aleatorios
fake = Faker()

# Generar 1000 nombres aleatorios
nombres = [fake.name() for _ in range(5)]

# Generar 1000 correos electrónicos aleatorios
correos = [fake.email() for _ in range(5)]

# Generar 1000 contraseñas aleatorias
def generar_contraseña():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(12))

contraseñas = [generar_contraseña() for _ in range(5)]

# Encriptar las contraseñas utilizando bcrypt
contraseñas_encriptadas = [bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt()) for contraseña in contraseñas]

