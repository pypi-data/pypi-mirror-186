from avenieca.producer import Producer
from avenieca.utils.signal import verify_signal


class Event(Producer):
    """
    Event producer class for syncing from an event driven source.
    Use this class if you want to handle the outer syncing logic, then pass the
    signal to the publish method to publish.

    :param config: configuration dictionary
    """
    def __init__(self, config: dict):
        super().__init__(config)
        self.config = config
        self.sync = True

    def publish(self, signal: dict):
        """
        call this method with the signal dictionary to publish once to a digital twin

        :param signal: signal data
        :return: None
        """
        if self.sync:
            verify_signal(signal)
            return self.send(signal)

    @property
    def config(self):
        return self.config

    @config.setter
    def config(self, value):
        self._config = value
