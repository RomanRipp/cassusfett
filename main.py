import RPi.GPIO as GPIO
from tracks import Tracks
from sonar import Sonar


tracks = Tracks(power_right=18,
                forward_right=2,
                backward_right=3,
                power_left=19,
                forward_left=4,
                backward_left=5)

sonar = Sonar(trigger=14, echo=15)
sonar.start()

while True:

    print("distance: " + sonar.get_distance())

    key = input()
    if key == 'w':
        tracks.forward()
    elif key == 's':
        tracks.backward()
    elif key == 'd':
        tracks.right()
    elif key == 'a':
        tracks.left()
    else:
        tracks.stop()
