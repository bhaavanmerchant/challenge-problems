import unittest

from MazeSolver import MazeSolver

class TestMazeSolver(unittest.TestCase):
    def test_connected(self):
        grid = [
            [0,1,0],
            [0,0,0],
            [0,1,0]
        ]
        src = (0,0)
        dest = (2,2)
        self.assertTrue(MazeSolver().isConnected(grid, src[0], src[1], dest[0], dest[1]))

    def test_disconnected(self):
        grid = [
            [0,1,0],
            [0,1,0],
            [0,1,0]
        ]
        src = (0,0)
        dest = (2,2)
        self.assertFalse(MazeSolver().isConnected(grid, src[0], src[1], dest[0], dest[1]))


if __name__ == '__main__':
    unittest.main()