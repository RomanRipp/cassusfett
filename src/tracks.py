import RPi.GPIO as GPIO
import logging


class Tracks:
    def __init__(self, power_right,
                 forward_right,
                 backward_right,
                 power_left,
                 forward_left,
                 backward_left):
        self._prp = power_right
        self._frp = forward_right
        self._brp = backward_right
        self._plp = power_left
        self._flp = forward_left
        self._blp = backward_left
        self._setup_track(self._prp, self._frp, self._brp)
        self._setup_track(self._plp, self._flp, self._blp)

    @classmethod
    def _setup_track(cls, power_pin, forward_pin, backward_pin):
        GPIO.setup(forward_pin, GPIO.OUT)
        GPIO.setup(backward_pin, GPIO.OUT)
        GPIO.setup(power_pin, GPIO.OUT)
        GPIO.output(forward_pin, GPIO.LOW)
        GPIO.output(backward_pin, GPIO.LOW)
        GPIO.PWM(power_pin, 1000).start(25)

    def forward(self):
        logging.info("forward")
        GPIO.output(self._brp, GPIO.LOW)
        GPIO.output(self._blp, GPIO.LOW)
        GPIO.output(self._frp, GPIO.HIGH)
        GPIO.output(self._flp, GPIO.HIGH)

    def backward(self):
        logging.info("backward")
        GPIO.output(self._frp, GPIO.LOW)
        GPIO.output(self._flp, GPIO.LOW)
        GPIO.output(self._brp, GPIO.HIGH)
        GPIO.output(self._blp, GPIO.HIGH)

    def stop(self):
        logging.info("stop")
        GPIO.output(self._frp, GPIO.LOW)
        GPIO.output(self._flp, GPIO.LOW)
        GPIO.output(self._brp, GPIO.LOW)
        GPIO.output(self._blp, GPIO.LOW)

    def left(self):
        logging.info("left")
        GPIO.output(self._flp, GPIO.LOW)
        GPIO.output(self._brp, GPIO.LOW)
        GPIO.output(self._blp, GPIO.LOW)
        GPIO.output(self._frp, GPIO.HIGH)

    def right(self):
        logging.info("right")
        GPIO.output(self._frp, GPIO.LOW)
        GPIO.output(self._brp, GPIO.LOW)
        GPIO.output(self._blp, GPIO.LOW)
        GPIO.output(self._flp, GPIO.HIGH)
