from sensor import Sensor
from threading import Thread
import time


class Pulse(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        self._thread = Thread(target=self._run)

    def _run(self):
        while self._running:
            time.sleep(1)
