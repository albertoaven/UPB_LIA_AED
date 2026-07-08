def solve_resource_assignment():
  best_x = 0
  best_y = 0
  best_z = 0

  for x in range(21):
    for y in range(21):
      if (2 * x + 4 * y <= 20 and x + 2 * y <= 10):
        z = (10 * x + 15 * y)

        if z > best_z:
          best_z = z
          best_x = x
          best_y = y

  return (best_x, best_y, best_z)