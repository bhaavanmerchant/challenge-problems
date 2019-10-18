from collections import Counter

class Memory:
    # Memory is an object which stores seen topics for all countries
    # I would use redis here in the actual system

    def __init__(self):
        self.mem = {}

    def increase_counter(self, country, topic):
        if country not in self.mem:
            self.mem[country] = Counter()
        self.mem[country][topic] += 1

    def decrease_counter(self, country, topic):
        self.mem[country][topic] -= 1

    def all_country_trends(self):
        result = {}
        for country in self.mem:
            result[country] = self.get_country_trends(country)
        return result

    def get_country_trends_with_counts(self, country, top_n = 10):
        return [(topic.topic_name, count) for (topic, count) in self.mem[country].most_common(top_n)]

    def get_country_trends(self, country, top_n = 10):
            return [topic.topic_name for (topic, count) in self.mem[country].most_common(top_n)]
