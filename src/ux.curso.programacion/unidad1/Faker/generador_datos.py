#importar la libreria faker
from faker import Faker
faker= Faker("es_MX")
#python3 -m pip install Faker

print("Generando datos Dummy con Faker")

print(f"Nombre:{faker.name()}")
print(f"Direccion:{faker.address()}")
print(f"Telefono:{faker.phone_number()}")
print(f"Correo:{faker.email()}")