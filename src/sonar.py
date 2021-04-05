import RPi.GPIO as GPIO
from threading import Thread
import time
import logging


class Sonar: 
    def __init__(self, trigger, echo):
        self.distance = 0
        self.timestamp = time.time()
        self._trigger_pin = trigger
        self._echo_pin = echo
        self._running = False
        GPIO.setup(self._trigger_pin, GPIO.OUT)
        GPIO.setup(self._echo_pin, GPIO.IN)
        self._thread = Thread(target=self._running)

    def _read_sensor(self):
        logging.debug("measuring distance")
        GPIO.output(self._trigger_pin, False)
        time.sleep(1)
        GPIO.output(self._trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self._trigger_pin, False)
        while GPIO.input(self._echo_pin) == 0:
            pulse_start = time.time()
        while GPIO.input(self._echo_pin) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        self.distance = round(pulse_duration * 171500, 2)
        self.timestamp = time.time()
        logging.debug("distance: {0}".format(self.distance))

    def _run(self):
        while self._running:
            self._read_sensor()

    def start(self):
        self._running = True
        self._thread.start()

    def stop(self):
        self._running = False
        self._thread.join()

    def get_distance(self):
        return self.distance, self.timestamp


