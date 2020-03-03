# Partitioner

The goal of this problem is to pack records of users into evenly distributed partitions. We want to keep all records of a given user together.

This is a bin packing problem, and a NP-hard problem. I attempt to solve this, using the First Fit Decreasing algorithm. While this cannot guaruntee exact results, there is a strict upper bound (~1.22 times the best packing solution) of efficiency. Given the use case of spark partitioning, such an upper bound seems good enough.

## Algorithm

I try to sort the data by decreasing order of counts, and also compute the target size of each partition. I then assign each element to the next available bin / partition, where I can fit in the records within the required target size.
Since sorting is involved in this process, the average time complexity of this operation is O(n log n).

I loop through the data, to try to fit in a given record. However, in the worst case, if I am unable to fit a record after jumping over all K partitions, I assign it to any partition I can.

I maintain the running map of user_id (partitioningColumnString) and it's assigned partition id in a instance variable / hash map.

Whenever, someone queries the data, I can lookup this hash map `self.partitionAssignment` and return the assigned parition id in O(1) time.

The benefit of decoupling init and querying is that querying operation, which can be executed from different executors, is really fast.

Given the decoupling, while not desirable, it is still possible someone changes data between the call of init and the query. This may introduce new, and unknown user_ids into the data. We therefore also provide for a fallback by randomly allocating the new user_ids to a partition.

## Alternatives

Given that we know that the data is expoenentially distributed, we can also attempt a pure analytical solution to the problem. For an exponential distibution, I would divide the area under the curve into K areas (parallel to y-axis), once I receive the count data.
![exponential_pdf](https://i.imgur.com/zZDK1p5.png).
I'll keep a track of the corresponding y-cordinates of the function in a sorted array.

On query time, I can query the corresponding count of the user_id, and do a binary search on this array, to find which area this user_id belongs to. I can return the corresponding index of the element in the array, as the partition Id.

This solution prevents a massive computation at the initialization of the partitioner, and makes the initialization a quick operation. The query time is also an O(log K) operation which given the bound of K is a reasonably constant time operation.

However, given that strict assumption required, which may not be true for non-parametric data, I preferred to use the bin packing solution which is approximately correct.

## Scale
Given the requirements, this solution is able to produce results for millions of user ids and thousands of partition. However, given the choice of python as a language, a massive penalty is being incurred in serializing and deserializing nd_arrays to pyobjects, which slows down the computation a little bit. Given that this cost is a one time cost, this algorithm is still tractable. However, I would prefer to use Scala / Java which would allow the data to be accessed at minimal copying cost, and would integrate well with the Spark infrastructure, when building a production system. Ability to use vectorization (AVX), through these languages, will provide significant boost to performance.

Furthermore, I would consider dividng the data into as many cores / threads, and then ask each executor to bin pack a chunk of data into an equal fraction of bins.
Potentially, using GPU's multi cores (or similar hardware accelerators) is also an option, and we can write kernels to distribute work on them.

## Results
For large numpy generated data, spread over 10k partitions, we are able to achieve 99%+ packing efficiency.


## Requirements:
This program requires Python 3+, and has been developed and tested on Python 3.8.
Also this programs requires numpy to be installed for testing purposes. This library isused to simulate exponential sampled data.

## Usage
This can be used like, for K parititions:
```
from Partitioner import FirstFitPartitioner
counts = [(5,'a'), (3, 'b'), (2, 'c'), (1, 'd'), (4,'f')]
partitioner = FirstFitPartitioner(3, counts)
partitioner.getPartitionId('a')
```

The partitionId is an integer between 0 to K. We can hash it to get a corresponding spark partition if required.

## To test:
This can be unit tested using:
```
python -m unittest tests/test_FirstFitPartitioner.py
```
