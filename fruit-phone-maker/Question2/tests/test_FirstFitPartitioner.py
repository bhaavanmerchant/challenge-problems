import numpy
import unittest
import uuid

from Partitioner import FirstFitPartitioner

class TestFirstFitPartitioner(unittest.TestCase):
    def test_smallData(self):
        counts = {
            'a': 6,
            'b': 3,
            'c': 2,
            'd': 1,
            'f': 4
        }
        partitioner = FirstFitPartitioner(3, counts)
        self.assertGreaterEqual(partitioner._getBinLoad(), 0.8)

    def test_bigData(self):
        counts = {}
        for cnt in numpy.random.exponential(scale=100, size=50000000):
            counts[str(uuid.uuid4())[:8]] = cnt
        print("solving")
        partitioner = FirstFitPartitioner(10000, counts)
        print(partitioner._getBinLoad())
