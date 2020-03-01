from typing import List, Tuple

import collections

class MazeSolver:
     def nextPositions(self, node: Tuple[int, int]) -> List[Tuple[int, int]]:
          (i, j) = node
          allPositions = [
               (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
          ]
          possiblePositions = []
          for position in allPositions:
               if position[0] >= 0 and position[0] < self.grid_dims[0] and position[1] >= 0 and position[1] < self.grid_dims[1]:
                    if self.grid[position[0]][position[1]] == 0:
                         possiblePositions.append(position)
          return possiblePositions

     def _compute_grid_dimensions(self):
          grid_row_dims = len(self.grid)
          grid_column_dims = 0
          if grid_row_dims > 0:
               grid_column_dims = len(self.grid[0])
          return (grid_row_dims, grid_column_dims)

     def isConnected(self, grid: List[List[int]], aX: int, aY: int, bX: int, bY: int) -> bool:
          src, dst = (aX, aY), (bX, bY)

          self.grid = grid
          self.grid_dims = self._compute_grid_dimensions()

          to_visit = collections.deque()
          to_visit.append(src)
          visited_nodes = set()

          while len(to_visit) > 0:
               node = to_visit.popleft()
               if node == dst:
                    return True
               if node not in visited_nodes:
                    moves = self.nextPositions(node)
                    to_visit += moves
                    visited_nodes.add(node)

          return False