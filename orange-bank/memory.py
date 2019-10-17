from collections import Counter

class Memory:

    def __init__(self):
        self.mem = {}

    def increase_counter(self, country, topic):
        if country not in self.mem:
            self.mem[country] = Counter()
        self.mem[country][topic] += 1

    def decrease_counter(self, country, topic):
        self.mem[country][topic] -= 1

    def print_memory(self, top_n = 10):
        for country in self.mem:
            print(country)
            print([(topic.topic_name, count) for (topic, count) in self.mem[country].most_common(top_n)])
