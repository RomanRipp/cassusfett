import RPi.GPIO as GPIO
import logging


class Tracks:
    def __init__(self, power_right,
                 forward_right,
                 backward_right,
                 power_left,
                 forward_left,
                 backward_left):
        self._power_right = power_right
        self._forward_right = forward_right
        self._backward_right = backward_right
        self._power_left = power_left
        self._forward_left = forward_left
        self._backward_left = backward_left
        self._setup_track(self._power_right, self._forward_right, self._backward_right)
        self._setup_track(self._power_left, self._forward_left, self._backward_left)

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
        GPIO.output(self._backward_right, GPIO.LOW)
        GPIO.output(self._backward_left, GPIO.LOW)
        GPIO.output(self._forward_right, GPIO.HIGH)
        GPIO.output(self._forward_left, GPIO.HIGH)

    def backward(self):
        logging.info("backward")
        GPIO.output(self._forward_right, GPIO.LOW)
        GPIO.output(self._forward_left, GPIO.LOW)
        GPIO.output(self._backward_right, GPIO.HIGH)
        GPIO.output(self._backward_left, GPIO.HIGH)

    def stop(self):
        logging.info("stop")
        GPIO.output(self._forward_right, GPIO.LOW)
        GPIO.output(self._forward_left, GPIO.LOW)
        GPIO.output(self._backward_right, GPIO.LOW)
        GPIO.output(self._backward_left, GPIO.LOW)

    def left(self):
        logging.info("left")
        GPIO.output(self._forward_left, GPIO.LOW)
        GPIO.output(self._backward_left, GPIO.HIGH)
        GPIO.output(self._backward_right, GPIO.LOW)
        GPIO.output(self._forward_right, GPIO.HIGH)

    def right(self):
        logging.info("right")
        GPIO.output(self._forward_right, GPIO.LOW)
        GPIO.output(self._backward_right, GPIO.HIGH)
        GPIO.output(self._backward_left, GPIO.LOW)
        GPIO.output(self._forward_left, GPIO.HIGH)
