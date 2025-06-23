# populate_perfiles.py
import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practica.settings')  # Cambia 'tu_proyecto'
django.setup()

from perfil.models import Perfil  # Asegúrate que 'perfiles' es el nombre de tu app

fake = Faker()

TIPOS_PUESTO = ['remoto', 'presencial', 'hibrido']

def crear_perfiles(n=20):
    for _ in range(n):
        titulo = fake.job()
        empresa = fake.company()
        descripcion = fake.paragraph(nb_sentences=5)
        ubicacion = fake.city()
        tipo_puesto = random.choice(TIPOS_PUESTO)
        fecha_cierre = fake.date_between(start_date='+10d', end_date='+60d')
        link_aplicacion = fake.url()

        Perfil.objects.create(
            titulo=titulo,
            empresa=empresa,
            descripcion=descripcion,
            ubicacion=ubicacion,
            tipo_puesto=tipo_puesto,
            fecha_cierre=fecha_cierre,
            link_aplicacion=link_aplicacion
        )
    print(f"{n} perfiles creados exitosamente.")

if __name__ == '__main__':
    crear_perfiles(30)  # Puedes cambiar la cantidad
