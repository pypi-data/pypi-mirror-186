import os
import numpy as np
from avenieca.utils import Config
from avenieca.utils import Signal
from avenieca.producers import Stream
from avenieca.producers import Event
from avenieca.consumer import Consumer


def consume(func, topic):
    Config["bootstrap_servers"] = os.environ["KAFKA_URL"]
    Config["topic"] = topic
    client = Consumer(config=Config)
    client.consume(func, True)


def test_stream_publish():
    def verify(data):
        valence = data["valence"]
        state = data["state"]
        assert valence == 10
        assert state == "[0.2, 0.3, 0.8]"

    def handler():
        Signal["valence"] = 10
        Signal["state"] = np.array([0.2, 0.3, 0.8])
        return Signal

    Config["bootstrap_servers"] = os.environ["KAFKA_URL"]
    Config["topic"] = "test_topic_1"
    stream = Stream(config=Config, sync_rate=1)
    stream.publish(handler, True)
    consume(verify, Config["topic"])


def test_event_publish():
    def verify(data):
        valence = data["valence"]
        state = data["state"]
        assert valence == 9
        assert state == "[0.1, 0.2, 0.1]"

    def handler():
        Signal["valence"] = 9
        Signal["state"] = "[0.1, 0.2, 0.1]"
        return Signal

    Config["bootstrap_servers"] = os.environ["KAFKA_URL"]
    Config["topic"] = "test_topic_2"
    event = Event(config=Config)
    event.publish(handler())
    consume(verify, Config["topic"])