
class Memory:

    def __init__(self):
        self.mem = {}

    def increase_counter(self, country, topic):
        if country not in self.mem:
            self.mem[country] = {}
        if topic not in self.mem[country]:
            self.mem[country][topic] = 1
        else:
            self.mem[country][topic] += 1

    def print_memory(self):
        for country in self.mem:
            for t in self.mem[country]:
                if self.mem[country][t] > 1:
                    print(self.mem[country][t])
