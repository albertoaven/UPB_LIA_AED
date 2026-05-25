def quick_sort(arr, asc):
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