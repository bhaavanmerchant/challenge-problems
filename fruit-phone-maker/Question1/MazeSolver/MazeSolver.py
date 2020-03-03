from typing import List, Tuple

import heapq

class MazeSolver:
     def __init__(self, grid: List[List[bool]]):
          self.grid = grid
          self.grid_dims = self._compute_grid_dimensions()

     def nextPositions(self, node: Tuple[int, int]) -> List[Tuple[int, int]]:
          """Get possible positions you can traverse on the grid from position node"""
          (i, j) = node
          allPositions = [
               (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
          ]
          possiblePositions = []
          for position in allPositions:
               if position[0] >= 0 and position[0] < self.grid_dims[0] and position[1] >= 0 and position[1] < self.grid_dims[1]:
                    if self.grid[position[0]][position[1]] == False:
                         possiblePositions.append(position)
          return possiblePositions

     def _compute_grid_dimensions(self):
          """Compute the grid dimensions and store them in the instance variable self.grid_column_dims"""
          grid_row_dims = len(self.grid)
          grid_column_dims = 0
          if grid_row_dims > 0:
               grid_column_dims = len(self.grid[0])
          return (grid_row_dims, grid_column_dims)

     def _get_distance_heuristic(self, node1: Tuple[int, int], node2: Tuple[int, int]) -> int:
          """Get a heuristic of the distance between two node. For now we use Manhattan Distance."""
          return abs(node1[0]- node2[0]) + abs(node1[1]- node2[1])

     def isConnected(self, aX: int, aY: int, bX: int, bY: int) -> bool:
          """See if two points (aX, aY) and (bX, bY) are connected on the graph"""
          src, dst = (aX, aY), (bX, bY)

          to_visit = [(self._get_distance_heuristic(src, dst), src)]
          heapq.heapify(to_visit)
          visited_nodes = set()

          while len(to_visit) > 0:
               _, node = heapq.heappop(to_visit)

               if node == dst:
                    return True
               if node not in visited_nodes:
                    moves = self.nextPositions(node)
                    for move in moves:
                         heapq.heappush(to_visit, (self._get_distance_heuristic(move, dst), move))
                    visited_nodes.add(node)

          return False
