# MazeSolver

This is a program to identify if two points in a grid are connected or not.

A grid is a list of a list of integers where False represents free blocks, and True represents a block / wall.

## Requirements:
This program requires Python 3+, and has been developed and tested on Python 3.8.

## To run:
To use this module programatically, include the following line:
```
from MazeSolver import MazeSolver
```

The maze / grid can be initialized using:
```
grid = [
            [False,True,False],
            [False,True,False],
            [False,True,False]
        ]
maze = MazeSolver(grid)
```

Once the grid is initialized, we can query if two co-ordinates (aX, aY) and (bX, bY) are connected, by querying:
```
maze.isConnected(aX, aY, bX, bY)
```

## To test:
This can be unit tested using:
```
python -m unittest tests/test_MazeSolver.py
```

## Logic:
We do a breadth first search from the source to the destination co-ordinate. However, to guide our direction, to greedily move towards the destination, we use a heuristic, Manhattan Distance. This optimizes the problem space to reach the solution quicker.

At every node we visit, to move towards the node with the least distance from the destination, we maintain a priority queue of all possible nodes to travel, and choose the one which is the best.
