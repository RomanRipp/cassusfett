import RPi.GPIO as GPIO
from tracks import Tracks
from sonar import Sonar
from light import Light
import logging

logging.basicConfig(level=logging.DEBUG)

GPIO.setmode(GPIO.BCM)

tracks = Tracks(power_left=18,
                forward_left=2,
                backward_left=3,
                power_right=19,
                forward_right=4,
                backward_right=5)

sonar = Sonar(trigger=14, echo=15)
sonar.start()

light = Light(pin=17)
light.start()

while True:

    logging.debug("D: {0}".format(sonar.get_distance()[0]))

    key = input()
    logging.debug("C: {0}".format(key))

    if key == "w":
        tracks.forward()
    elif key == "s":
        tracks.backward()
    elif key == "d":
        tracks.right()
    elif key == "a":
        tracks.left()
    elif key == "q":
        tracks.stop()
    elif key == "e":
        break

tracks.stop()
sonar.stop()
light.stop()
