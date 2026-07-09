from functools import lru_cache
from typing import Dict, List

def count_paths_dag(adj: Dict[str, List[str]], start: str, goal: str) -> int:
  @lru_cache(maxsize=None)
  def dp(u: str) -> int:
    if u == goal:
      return 1
    
    return sum(dp(v) for v in adj.get(u, []))
  
  return dp(start)

if __name__ == "__main__":
  adj = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"], "E": []}

  assert count_paths_dag(adj, "A", "E") == 2