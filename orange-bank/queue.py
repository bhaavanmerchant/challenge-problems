

class Queue:
    # Queue is a bounded list of topics that have been obeserved at a given epoch.
    # In the actual system, I would use something like kafka, as a backend for this
    def __init__(self, timeout_limit):
        self.q = []
        self.timeout_limit = timeout_limit

    def push(self, epoch, country, topic):
        self.q.append((epoch, country, topic))

    def housekeeping(self, now, memory):
        """
        This function clears from memory data older than timeout_limit
        """
        if len(self.q) > 0 and self.q[0][0] < (now - self.timeout_limit):
            _, country, expired_topic = self.q.pop(0)
            memory.decrease_counter(country, expired_topic)

    def _get_queue_length(self):
        return len(self.q)

    def _get_queue_state(self):
        return [(epoch, country, topic.topic_name) for (epoch, country, topic) in self.q]
