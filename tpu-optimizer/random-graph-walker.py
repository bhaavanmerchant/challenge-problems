import sys

from random import randint

graph = {}
sequences = []

# Parse input
input_data = sys.stdin.read().split('\n')
L,N = input_data[0].split(',')
for line in input_data[1:]:
    if ' -> ' not in line:
        continue
    parsed_key, _, parsed_val = line.strip().split(' ')
    if parsed_key not in graph:
        graph[parsed_key] = [parsed_val]
    else:
        graph[parsed_key].append(parsed_val)

# Random traversal
n = int(N)
while n > 0:
    start_values = list(graph.keys())
    seq = []
    l = int(L)
    path_length_is_short = False
    while l > 0 and not path_length_is_short:
        selected_path = start_values[randint(0, len(start_values) - 1)]
        seq.append(selected_path)
        start_values = graph[selected_path]
        if start_values is None:
            path_length_is_short = True
        l -= 1
    if not path_length_is_short:
        sequences.append(seq)
        n -= 1

# Print output
for seq in sequences:
    print(", ".join(seq))
