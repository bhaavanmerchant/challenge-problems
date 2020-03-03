import numpy
import unittest
import uuid

from Partitioner import FirstFitPartitioner

class TestFirstFitPartitioner(unittest.TestCase):
    def test_smallData(self):
        counts = [(6,'a'), (3, 'b'), (2, 'c'), (1, 'd'), (4,'f')]
        partitioner = FirstFitPartitioner(3, counts)
        partitionSize = partitioner.partitionSize
        partitionSize.sort()
        self.assertEqual(partitionSize, [5, 5, 6])

    def test_unbalancedData(self):
        counts = [(6,'a'), (6, 'b'), (6, 'c'), (6, 'd')]
        partitioner = FirstFitPartitioner(3, counts)
        partitionSize = partitioner.partitionSize
        partitionSize.sort()
        self.assertEqual(partitionSize, [6, 6, 12])

    def test_bigData(self):
        size_big = 1_000_000
        exp_dist = numpy.random.exponential(scale=100, size=size_big)
        ids = [''] * size_big
        for i in range(size_big):
            ids[i] = str(uuid.uuid4())[:8]
        counts = list(zip(exp_dist, ids))
        partitioner = FirstFitPartitioner(10_000, counts)
        self.assertGreaterEqual(partitioner.getLoadFactor(), 0.99)

    def test_known_getPartitionId(self):
        counts = [(5,'a'), (3, 'b'), (2, 'c'), (1, 'd'), (4,'f')]
        partitioner = FirstFitPartitioner(3, counts)
        # In a firstfit partitioner, the first element will be assigned to the 1st partition (which is 0 in this case)
        self.assertEqual(partitioner.getPartitionId('a'),0)

    def test_unknown_getPartitionId(self):
        counts = [(5,'a'), (3, 'b'), (2, 'c'), (1, 'd'), (4,'f')]
        partitioner = FirstFitPartitioner(3, counts)
        # For an unknown partition query we still return a partition id, within the given partition sizes
        self.assertLess(partitioner.getPartitionId('q'), len(partitioner.partitionSize))

    def test_balanced_getLoadFactor(self):
        counts = [(5,'a'), (3, 'b'), (2, 'c'), (1, 'd'), (4,'f')]
        partitioner = FirstFitPartitioner(3, counts)
        self.assertEqual(partitioner.getLoadFactor(), 1)

    def test_unbalanced_getLoadFactor(self):
        counts = [(6,'a'), (6, 'b'), (6, 'c'), (6, 'd')]
        partitioner = FirstFitPartitioner(3, counts)
        self.assertEqual(partitioner.getLoadFactor(), 2/3)
