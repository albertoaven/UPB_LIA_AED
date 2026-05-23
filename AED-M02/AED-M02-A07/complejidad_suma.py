import timeit

def suma_iterativa(entrada):
    def funcion():
        resultado = 0

        for n in range(1, entrada + 1):
            resultado += n
        
        return resultado

    tiempo = timeit.timeit(funcion, number=1)
    
    return funcion(), tiempo

def suma_formula(entrada):
  def funcion():
    resultado = entrada * (entrada + 1) //2

    return resultado
  
  tiempo = timeit.timeit(funcion, number=1)

  return funcion(), tiempo

def main():
  while True:
    numero = input("Ingrese un número (X para salir): ")

    if numero.lower() == "x":
      print("Saliendo del programa.")
      print()
      break

    if int(numero):
      resultado, tiempo = suma_iterativa(int(numero))

      print(f"El resultado de la suma iterativa es: {resultado} y se logró en {tiempo} segundos.")
      print()

      resultado, tiempo = suma_formula(int(numero))

      print(f"El resultado de la suma fórmula es: {resultado} y se logró en {tiempo} segundos.")
      print()

main()