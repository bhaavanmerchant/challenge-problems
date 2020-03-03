import unittest

from MazeSolver import MazeSolver

class TestMazeSolver(unittest.TestCase):
    def test_connected(self):
        grid = [
            [False,True,False],
            [False,False,False],
            [False,True,False]
        ]
        src = (0,0)
        dest = (2,2)
        self.assertTrue(MazeSolver(grid).isConnected(src[0], src[1], dest[0], dest[1]))

    def test_disconnected(self):
        grid = [
            [False,True,False],
            [False,True,False],
            [False,True,False]
        ]
        src = (0,0)
        dest = (2,2)
        self.assertFalse(MazeSolver(grid).isConnected(src[0], src[1], dest[0], dest[1]))

    def test_connected_big(self):
        SIZE = 9999
        grid = [ ]
        row_init = [False] * SIZE
        for i in range(SIZE):
            grid.append(row_init)
        src = (0,0)
        for i in range(SIZE):
            grid[i][875] = True
        grid[575][875] = False
        dest = (SIZE - 1, SIZE - 1)
        self.assertTrue(MazeSolver(grid).isConnected(src[0], src[1], dest[0], dest[1]))

    def test_disconnected_big(self):
        SIZE = 9999
        grid = [ ]
        row_init = [True] * SIZE
        for i in range(SIZE):
            grid.append(row_init)
        src = (0,0)
        dest = (SIZE - 1, SIZE - 1)
        grid[src[0]][src[1]] = False
        grid[dest[0]][dest[1]] = False
        self.assertFalse(MazeSolver(grid).isConnected(src[0], src[1], dest[0], dest[1]))

    def test_next_position(self):
        grid = [
            [True, True, False],
            [False, False, False],
            [True, False, True]
        ]
        res_centre = MazeSolver(grid).nextPositions((1,1))
        res_centre.sort()
        res_boundary = MazeSolver(grid).nextPositions((1,2))
        res_boundary.sort()
        self.assertEqual(res_centre, [(1, 0), (1, 2), (2, 1)])
        self.assertEqual(res_boundary, [(0, 2), (1, 1)])

    def test_grid_dims(self):
        grid = [
            [True, True, False],
            [False, False, False],
            [True, False, True]
        ]
        self.assertEqual(MazeSolver(grid)._compute_grid_dimensions(), (3,3))

    def test_distance_heuristics(self):
        grid = [
            [True, True, False],
            [False, False, False],
            [True, False, True]
        ]
        self.assertEqual(MazeSolver(grid)._get_distance_heuristic((0,0), (2,2)), 4)



if __name__ == '__main__':
    unittest.main()
