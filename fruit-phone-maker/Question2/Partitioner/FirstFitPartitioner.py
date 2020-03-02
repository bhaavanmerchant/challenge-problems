from typing import List, Tuple

import collections

class FirstFitPartitioner:
    def __init__(self, K: int, counts: List[Tuple[int, str]]):
        total_size = sum([c[0] for c in counts])
        avg_bin_size = total_size / K # Since we assume an exponential distribution, f(x) = lambda * e ** (- lambda * x), we can assume most values will be less that the average value

        target_bin_size = avg_bin_size * (1 + 1/K**1.2) # Applying a smoothening function, to allow misfitting for smaller K values

        self.partitionAssignment = {}
        partitionSize = [0] * K

        counts.sort(key=lambda k: k[0], reverse=True)
        i = 0
        for count, partitionStr in counts:
            jumps = 0
            while count + partitionSize[i] > target_bin_size and jumps < K:
                i += 1
                jumps += 1
                i = i % K
            self.partitionAssignment[partitionStr] = i
            partitionSize[i] += count

        self.partitionSize = partitionSize

    def getPartitionId(self, partitionStr: str) -> int:
        if partitionStr in self.partitionAssignment:
            return self.partitionAssignment[partitionStr]
        return hash(partitionStr) % len(self.partitionSize)

    def _getBinLoad(self):
        biggestBin = max(self.partitionSize)
        occupancyFactor = sum(self.partitionSize) / (biggestBin * len(self.partitionSize))

        return occupancyFactor
