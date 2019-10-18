from input import Input
from topic import Topic

class Ingestor:
    # Ingestor is a class which manages how we consume the data
    # Currently the system supports consuming the data from a file or the api

    def topic_proc(self, topic, country, epoch):
        """
        Every topic ingested needs to be added to the memory and to the expiration queue
        """
        new_topic = Topic(topic)
        self.memory.increase_counter(country, new_topic)
        self.queue.push(epoch, country, new_topic)

    def event_proc(self, topics, country, epoch):
        for topic in topics:
            self.topic_proc(topic, country, epoch)

    def __init__(self, memory, queue, source = 'file'):
        self.memory = memory
        self.queue = queue
        for line in Input(source).get():
            try:
                topics = line['group']['group_topics']
                country = line['group']['group_country']
                epoch = line['mtime']
                self.event_proc(topics, country, epoch)
            except KeyError:
                pass
