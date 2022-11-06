import RPi.GPIO as GPIO
from sensor import Sensor
from threading import Thread
import time
import logging


class Light(Sensor):
    def __init__(self, pin, sleep=1):
        Sensor.__init__(self)
        self._sleep = sleep
        self._pin = pin
        self._light = False
        GPIO.setup(self._pin, GPIO.IN)
        self._thread = Thread(target=self._run)

    def _run(self):
        while self._running:
            self._light = (GPIO.input(self._pin) == 0)
            self._timestamp = time.time()
            logging.debug("light: {}".format(self._light))
            for s in self._subscribers:
                s.on_light_change(self._light)
            time.sleep(self._sleep)

    def get_light(self):
        return self._light, self._timestamp
