

class Queue:
    def __init__(self, timeout_limit):
        self.q = []
        self.timeout_limit = timeout_limit

    def push(self, epoch, country, topic):
        self.q.append((epoch, country, topic))

    def housekeeping(self, now, memory):
        if len(self.q) > 0 and self.q[0][0] < (now - self.timeout_limit):
            _, country, expired_topic = self.q.pop(0)
            memory.decrease_counter(country, expired_topic)
            print('decreasing!' + str(len(self.q)))

    def print_q(self):
        # print([(epoch, country, topic.topic_name) for (epoch, country, topic) in self.q])
        print(len(self.q))