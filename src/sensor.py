import time


class Sensor:
    def __init__(self):
        self._timestamp = time.time()
        self._running = False
        self._thread = None
        self._subscribers = list()

    def start(self):
        self._running = True
        self._thread.start()

    def stop(self):
        self._running = False
        self._thread.join()

    def subscribe(self, s):
        self._subscribers.append(s)

    def unsubscribe(self, s):
        self._subscribers.remove(s)


