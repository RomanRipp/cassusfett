import RPi.GPIO as GPIO
from threading import Thread
import time
import logging


class Light:
    def __init__(self, pin, sleep=1):
        self._sleep = sleep
        self._pin = pin
        self._running = False
        self._light = False
        self._timestamp = time.time()
        GPIO.setup(self._pin, GPIO.IN)
        self._thread = Thread(target=self._run)

    def _run(self):
        while self._running:
            self._light = (GPIO.input(self._pin) == 0)
            self._timestamp = time.time()
            logging.debug("light: {}".format(self._light))
            time.sleep(self._sleep)

    def start(self):
        self._running = True
        self._thread.start()
        logging.info("light sensor started")

    def stop(self):
        self._running = False
        self._thread.join()
        logging.info("light sensor stopped")

    def get_light(self):
        return self._light, self._timestamp
