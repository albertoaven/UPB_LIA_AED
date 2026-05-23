
# Prueba 1: LISTA
persona_lista = [35, 2500, "positivo"]
print("LISTA:", persona_lista)
print("Edad (índice 0):", persona_lista[0])

# Prueba 2: TUPLA
persona_tupla = (35, 2500, "positivo")
print("\nTUPLA:", persona_tupla)
print("Ingresos (índice 1):", persona_tupla[1])

# Prueba 3: DICCIONARIO
persona_dict = {
    "edad": 35,
    "ingresos": 2500,
    "etiqueta": "positivo"
}
print("\nDICCIONARIO:", persona_dict)
print("Etiqueta (clave):", persona_dict["etiqueta"])

# Prueba 4: CONJUNTO (para etiquetas únicas)
etiquetas = {"positivo", "negativo"}
print("\nCONJUNTO:", etiquetas)
print("¿Contiene 'positivo'?:", "positivo" in etiquetas)
