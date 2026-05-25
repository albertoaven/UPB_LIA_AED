def quick_sort(arr, asc):
  """Ordena una lista usando quick sort y devuelve una nueva lista.

  Soporta listas de enteros o de objetos con atributo `priority`.

  Args:
    arr: Lista de elementos a ordenar.
    asc: `True` para orden ascendente, `False` para descendente.

  Returns:
    list: Nueva lista ordenada segun el criterio indicado.
  """
  if len(arr) <= 1:
    return arr
  
  if isinstance(arr[0], int):
    if asc:
      pivot = arr[len(arr) // 2]
      left = [x for x in arr if x < pivot]
      middle = [x for x in arr if x == pivot]
      right = [x for x in arr if x > pivot]

      return quick_sort(left, asc) + middle + quick_sort(right, asc)
    else:
      pivot = arr[len(arr) // 2]
      left = [x for x in arr if x > pivot]
      middle = [x for x in arr if x == pivot]
      right = [x for x in arr if x < pivot]

      return quick_sort(left, asc) + middle + quick_sort(right, asc)
  else:
    if asc:
      pivot = arr[len(arr) // 2].priority
      left = [x for x in arr if x.priority < pivot]
      middle = [x for x in arr if x.priority == pivot]
      right = [x for x in arr if x.priority > pivot]

      return quick_sort(left, asc) + middle + quick_sort(right, asc)
    else:
      pivot = arr[len(arr) // 2].priority
      left = [x for x in arr if x.priority > pivot]
      middle = [x for x in arr if x.priority == pivot]
      right = [x for x in arr if x.priority < pivot]

      return quick_sort(left, asc) + middle + quick_sort(right, asc)