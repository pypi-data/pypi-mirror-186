import json
from kafka import KafkaConsumer


class Consumer:
    """
    Base consumer for consuming messages (signals) from a digital twin.

    :param config: configuration dictionary
    """
    def __init__(self,
                 config: dict,
                 ):
        self.config = config
        self.topic = config["topic"]
        self.client = KafkaConsumer(
            self.topic,
            bootstrap_servers=config["bootstrap_servers"],
            auto_offset_reset=config["auto_offset_reset"]
        )

    def consume(self, func, sync_once=False):
        """
        :param func: handler to process received messages
        :param sync_once: run consume loop once
        :return: none
        """
        for msg in self.client:
            byte_val = msg.value
            data = json.loads(byte_val)
            func(data)
            if sync_once:
                break
