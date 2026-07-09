import time

def knapsack(items, capacity):
  """
  Problema de la mochila 0/1.

  Args:
    items:
      [
        (event, cost, value),
        ...
      ]

    capacity:
      capacidad máxima.

  Returns:
    (
      valor_maximo,
      eventos_seleccionados
    )
  """
  start_time = time.perf_counter()
  evaluated_cells = 0
  decisions = 0

  n = len(items)

  dp = [
    [0 for _ in range(capacity + 1)]
    for _ in range(n + 1)
  ]

  for i in range(1, n + 1):
    _, cost, value = items[i - 1]

    for w in range(capacity + 1):
      if cost <= w:
        dp[i][w] = max(
          value +
          dp[i - 1][w - cost],

          dp[i - 1][w]
        )

      else:

        dp[i][w] = dp[i - 1][w]

  selected = []

  w = capacity

  for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
      event = items[i - 1]

      selected.append(event)

      w -= cost

  selected.reverse()

  return (
    dp[n][capacity],
    selected
  )