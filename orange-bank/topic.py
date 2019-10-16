class Topic:
    def __init__(self, topic_dict):
        self.urlkey = topic_dict['urlkey']
        self.topic_name = topic_dict['topic_name']

    def __hash__(self):
        return hash(self.urlkey)