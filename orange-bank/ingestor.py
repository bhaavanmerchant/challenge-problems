from input import Input
from memory import Memory
from topic import Topic

class Ingestor:
    def topic_proc(self, topic, country, epoch):
        self.memory.increase_counter(country, Topic(topic))
        self.memory.print_memory()

    def event_proc(self, topics, country, epoch):
        for topic in topics:
            self.topic_proc(topic, country, epoch)

    def start(self):
        self.memory = Memory()
        for line in Input('file').get():
            try:
                topics = line['group']['group_topics']
                country = line['group']['group_country']
                epoch = line['mtime']
                self.event_proc(topics, country, epoch)
            except KeyError:
                pass


if __name__ == "__main__":
    Ingestor().start()