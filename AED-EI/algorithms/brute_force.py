import time

def brute_force_search(text, pattern):
  """
  Busca todas las ocurrencias de un patrón
  dentro de un texto mediante fuerza bruta.

  Args:
    text (str): Texto donde buscar.
    pattern (str): Patrón a buscar.

  Returns:
    list[int]: Posiciones donde aparece el patrón.
  """

  # Lista donde guardaremos las posiciones encontradas
  positions = []

  # Longitud del texto
  n = len(text)

  # Longitud del patrón
  m = len(pattern)

  # Si el patrón está vacío no buscamos nada
  if m == 0:
    return positions

  # Recorremos todas las posiciones posibles donde
  # el patrón podría comenzar dentro del texto
  #
  # Ejemplo:
  # texto = "HOLA MUNDO" (9 caracteres)
  # patrón = "MUN" (3 caracteres)
  #
  # La última posición válida para empezar es:
  # 9 - 3 = 6
  for i in range(n - m + 1):

    # Suponemos inicialmente que hay coincidencia
    match = True

    # Comparamos carácter por carácter
    # el patrón con el texto
    for j in range(m):
      # Comparamos el carácter j del patrón
      # con el carácter correspondiente del texto
      if text[i + j] != pattern[j]:

        # Si alguno es distinto, descartamos
        # esta posición y salimos del bucle
        match = False
        break

    # Si nunca encontramos diferencias,
    # el patrón aparece en la posición i
    if match:
      positions.append(i)

  return positions