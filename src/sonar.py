import RPi.GPIO as GPIO
from sensor import Sensor
from threading import Thread
import time
import logging


class Sonar(Sensor):
    def __init__(self, trigger, echo):
        Sensor.__init__(self)
        self._distance = 0
        self._trigger_pin = trigger
        self._echo_pin = echo
        GPIO.setup(self._trigger_pin, GPIO.OUT)
        GPIO.setup(self._echo_pin, GPIO.IN)
        self._thread = Thread(target=self._run)

    def _read_sensor(self):
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
        self._distance = round(pulse_duration * 171500, 2)
        self._timestamp = time.time()
        logging.debug("distance: {0}".format(self._distance))

    def _run(self):
        while self._running:
            self._read_sensor()
            for s in self._subscribers:
                s.on_distance_change(self._distance)

    def get_distance(self):
        return self._distance, self._timestamp
