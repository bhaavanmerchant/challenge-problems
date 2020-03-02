import unittest

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