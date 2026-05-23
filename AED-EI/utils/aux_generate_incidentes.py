import random
from datetime import datetime, timedelta

categories = [
    "Accidente",
    "Clima",
    "Manifestación",
    "Obras",
    "Seguridad",
    "Incendio"
]

descriptions = [
    "Choque múltiple sobre ruta provincial con varios vehículos involucrados y demoras prolongadas.",
    "Fuertes lluvias redujeron considerablemente la visibilidad en toda la zona.",
    "Manifestantes realizaron corte parcial de calzada durante varias horas.",
    "Trabajos de mantenimiento generaron reducción de carriles y tránsito lento.",
    "Operativo policial preventivo con controles vehiculares intensivos.",
    "Incendio forestal cercano a la ruta afectó la circulación por presencia de humo.",
    "Vehículo de carga volcó en una curva peligrosa causando interrupciones.",
    "Caída de árboles sobre la carpeta asfáltica tras intensas ráfagas de viento.",
    "Accidente entre motocicleta y automóvil con asistencia médica en el lugar.",
    "Presencia de animales sueltos generó situaciones de riesgo para conductores."
]

start_date = datetime(2026, 5, 1, 6, 0, 0)

for i in range(200):
    timestamp = start_date + timedelta(minutes=random.randint(0, 50000))
    category = random.choice(categories)
    priority = random.randint(1, 5)
    description = random.choice(descriptions)
    origin_id = random.randint(1, 23)
    destination_id = random.randint(1, 23)

    while destination_id == origin_id:
        destination_id = random.randint(1, 23)

    print(
        f"('{timestamp.strftime('%Y-%m-%d %H:%M:%S')}', "
        f"'{category}', "
        f"{priority}, "
        f"'{description}', "
        f"{origin_id}, "
        f"{destination_id}),"
    )