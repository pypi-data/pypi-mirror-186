import json
from kafka import KafkaProducer


class Producer:
    """
    Base producer for publishing messages.

    :param config: configuration dictionary
    """
    def __init__(self,
                 config: dict,
                 ):
        self.config = config
        self.topic = config["topic"]
        self.client = KafkaProducer(bootstrap_servers=config["bootstrap_servers"])

    def send(self, data: dict):
        """
        :param data: serialized signal dictionary
        :return: FutureRecordMetadata
        """
        json_object = json.dumps(data).encode("utf-8")
        result = self.client.send(self.topic, json_object)
        return result

