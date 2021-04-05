import RPi.GPIO as GPIO
from tracks import Tracks
from sonar import Sonar
import time
import logging

logging.basicConfig(level=logging.DEBUG)

GPIO.setmode(GPIO.BCM)

tracks = Tracks(power_right=18,
                forward_right=2,
                backward_right=3,
                power_left=19,
                forward_left=4,
                backward_left=5)

sonar = Sonar(trigger=14, echo=15)
sonar.start()

while True:

    logging.debug("distance: {0}".format(sonar.get_distance()[0]))

    time.sleep(1)
    # key = input()
    # if key == 'w':
    #     tracks.forward()
    # elif key == 's':
    #     tracks.backward()
    # elif key == 'd':
    #     tracks.right()
    # elif key == 'a':
    #     tracks.left()
    # else:
    #     tracks.stop()
