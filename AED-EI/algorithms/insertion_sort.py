def insertion_sort(arr, asc):
  if isinstance(arr[0], int):
    for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1

      if asc == True:
        while j >= 0  and key < arr[j]:
          arr[j + 1] = arr[j]
          j -=1

        arr[j + 1] = key
      else:
        while j >= 0  and key > arr[j]:
          arr[j + 1] = arr[j]
          j -=1

        arr[j + 1] = key
  else:
    for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1

      if asc == True:
        while j >= 0  and key.age < arr[j].age:
          arr[j + 1] = arr[j]
          j -=1

        arr[j + 1] = key
      else:
        while j >= 0  and key.age > arr[j].age:
          arr[j + 1] = arr[j]
          j -=1

        arr[j + 1] = key        

  return arr