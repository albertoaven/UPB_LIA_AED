# algorithms/kmp.py

def build_lps(pattern):
  """
  Construye el arreglo LPS (Longest Prefix Suffix).

  lps[i] almacena la longitud del prefijo propio más largo
  que también es sufijo para el substring pattern[0:i+1].

  Ejemplo:
    pattern = "ABABC"

    índice:   0 1 2 3 4
    patrón:   A B A B C
    lps:      0 0 1 2 0
  """

  # Inicialmente todos los valores son 0
  lps = [0] * len(pattern)

  # Longitud del prefijo-sufijo actual
  length = 0

  # El primer elemento siempre es 0, por eso empezamos en 1
  i = 1

  while i < len(pattern):

    # Si los caracteres coinciden,
    # extendemos el prefijo-sufijo actual
    if pattern[i] == pattern[length]:

      length += 1
      lps[i] = length

      i += 1

    else:

      # Si había un prefijo previo,
      # intentamos con el siguiente más corto
      if length != 0:

        length = lps[length - 1]

      else:
        # Si no existe ningún prefijo-sufijo válido
        lps[i] = 0
        i += 1

  return lps


def kmp_search(text, pattern):
  """
  Busca todas las ocurrencias de pattern dentro de text.

  Retorna una lista con las posiciones de inicio
  de cada coincidencia encontrada.
  """

  # Si el patrón está vacío no buscamos nada
  if len(pattern) == 0:
    return []

  # Preprocesamos el patrón
  lps = build_lps(pattern)

  positions = []

  # i -> índice del texto
  # j -> índice del patrón
  i = 0
  j = 0

  while i < len(text):

    # Si los caracteres coinciden,
    # avanzamos en ambos strings
    if text[i] == pattern[j]:
      i += 1
      j += 1

    # Si recorrimos completamente el patrón,
    # encontramos una ocurrencia
    if j == len(pattern):

      # La posición inicial es:
      # posición actual del texto - tamaño del patrón
      positions.append(i - j)

      # Continuamos buscando coincidencias solapadas
      # usando la información del LPS
      j = lps[j - 1]

    # Si hay un mismatch
    elif i < len(text) and text[i] != pattern[j]:

      # Si ya habíamos avanzado en el patrón,
      # no volvemos al inicio, sino al prefijo válido
      # más largo conocido
      if j != 0:
        j = lps[j - 1]

      # Si estábamos al principio del patrón,
      # simplemente avanzamos en el texto
      else:
        i += 1

  return positions