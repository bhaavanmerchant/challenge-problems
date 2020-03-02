import numpy
import unittest
import uuid

from Partitioner import FirstFitPartitioner

class TestFirstFitPartitioner(unittest.TestCase):
    def test_smallData(self):
        counts = [(6,'a'), (3, 'b'), (2, 'c'), (1, 'd'), (4,'f')]
        partitioner = FirstFitPartitioner(3, counts)
        self.assertGreaterEqual(partitioner._getBinLoad(), 0.8)

    def test_unbalancedData(self):
        counts = [(6,'a'), (6, 'b'), (6, 'c'), (6, 'd')]
        partitioner = FirstFitPartitioner(3, counts)
        self.assertGreaterEqual(partitioner._getBinLoad(), 0.8)

    def test_bigData(self):
        size_big = 1_000_000
        exp_dist = numpy.random.exponential(scale=100, size=size_big)
        ids = [''] * size_big
        for i in range(size_big):
            ids[i] = str(uuid.uuid4())[:8]
        counts = list(zip(exp_dist, ids))
        print("solving")
        partitioner = FirstFitPartitioner(10000, counts)
        print(partitioner._getBinLoad())
