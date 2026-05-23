import csv, json

datos = []

print("Abriendo archivo CSV")

with open("datos_empleo.csv", "r", newline="", encoding="UTF-8") as archivoCSV:
  datosCSV = csv.reader(archivoCSV)
  filas = list(datosCSV)

  for fila in filas:
    dic = {}

    dic["edad"] = fila[0]
    dic["pais"] = fila[1]
    dic["trabaja"] = True if fila[2] == "True" else False

    datos.append(dic)

print(f"Archivo abierto: \n {filas}")

with open("datos_empleo.json", "w", newline="", encoding="UTF-8") as archivoJSON:
  json.dump(datos, archivoJSON, indent=2)

print("Archivo JSON generado correctamente.")