from typing import Dict

import collections

class FirstFitPartitioner:
    EFFICIENCY_FACTOR = 0.8 # This is a NP hard problem. Given that we need to rely on heuristics, our final solution will not be fully efficienct, and therefore we need to accomodate inefficiency.

    def __init__(self, K: int, counts: Dict[str, int]):
        total_size = sum(counts.values())
        avg_bin_size = total_size / K # Since we assume an exponential distribution, f(x) = lambda * e ** (- lambda * x), we can assume most values will be less that the average value

        target_bin_size = avg_bin_size / FirstFitPartitioner.EFFICIENCY_FACTOR

        self.partitionAssignment = {}
        partitionSize = [0] * K

        for partitionStr in counts:
            i = 0
            while i < K and counts[partitionStr] + partitionSize[i] > target_bin_size:
                i += 1
            if i < K:
                self.partitionAssignment[partitionStr] = i
                partitionSize[i] += counts[partitionStr]

        self.partitionSize = partitionSize

    def getPartitionId(self, partitionStr: str) -> int:
        if partitionStr in self.partitionAssignment:
            return self.partitionAssignment[partitionStr]
        return hash(partitionStr) % len(self.partitionSize)

    def _getBinLoad(self):
        biggestBin = max(self.partitionSize)
        occupancyFactor = sum(self.partitionSize) / (biggestBin * len(self.partitionSize))
        return occupancyFactor
