def bs(list, key):
  """Realiza una busqueda binaria sobre enteros o eventos con atributo id.

  Args:
    list: Lista ordenada de enteros o de objetos con atributo `id`.
    key: Valor objetivo a buscar.

  Returns:
    tuple: Si la lista es de enteros, retorna (indice, comparaciones) o (-1, comparaciones).
      Si la lista es de objetos, retorna (objeto, comparaciones) o (None, comparaciones).
  """
  start = 0
  end = len(list) - 1
  comparisons = 0

  while start <= end:
    comparisons += 1
    middle = (start + end) // 2

    if isinstance(list[0], int):
      if list[middle] == key:
        return middle, comparisons
      elif list[middle] < key:
        start = middle + 1
      else:
        end = middle - 1

      return -1, comparisons
    
    else:
      if list[middle].id == key:
        return list[middle], comparisons
      elif list[middle].id < key:
        start = middle + 1
      else:
        end = middle - 1

  return None, comparisons