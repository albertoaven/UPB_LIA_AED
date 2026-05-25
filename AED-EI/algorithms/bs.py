def bs(list, key):
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