from typing import List, Tuple

import collections

class FirstFitPartitioner:
    def __init__(self, K: int, counts: List[Tuple[int, str]]):
        """
        Initializer for the FirstFitPartitioner, which constructs a map of partitioner strings, and assigns them a parition id

        Keyword argument:
        K: number of partitions available
        counts: A list of entries of counts of partitioning column string. When the column is user_id for example, it will be (counts_seen_of_a_user_id, user_id).
        """

        total_size = sum([c[0] for c in counts])
        avg_bin_size = total_size / K # Since we assume an exponential distribution, f(x) = lambda * e ** (- lambda * x), we can assume most values will be less that the average value

        self.partitionAssignment = {}
        partitionSize = [0] * K

        counts.sort(key=lambda k: k[0], reverse=True)
        i = 0                   # Counter to attempt to fit in the given number in a given partition id
        for count, partitionColumnStr in counts:
            jumps = 0
            while count + partitionSize[i] > avg_bin_size and jumps < K:
                i += 1
                jumps += 1      # Increment the total number of jumps made to fit in the given value
                i = i % K       # Once the i has exceeded the number of available partitions, we restart from the 1st partition
            self.partitionAssignment[partitionColumnStr] = i
            partitionSize[i] += count

        self.partitionSize = partitionSize

    def getPartitionId(self, partitionColumnStr: str) -> int:
        """
        At query time, this function will return a partition id for a partitioning column string. For example, user_id.
        """
        if partitionColumnStr in self.partitionAssignment: # Fetch an assigned partition number for the partitoner string value
            return self.partitionAssignment[partitionColumnStr]
        # Handle a case when we may be asked partition id for a partition string we haven't seen before.
        # This is a rare case, but may occur if there was a change in data between calling class constructor and the getPartitionId method
        # In this case, we naively return a random partition id.
        return hash(partitionColumnStr) % len(self.partitionSize)

    def getLoadFactor(self):
        """Get a measure of how populated the partitions are assigned, relative to the size of the maximum sized partition. If all partitions are exactly equal, this should be 1"""
        biggestBin = max(self.partitionSize)
        occupancyFactor = sum(self.partitionSize) / (biggestBin * len(self.partitionSize))
        return occupancyFactor
