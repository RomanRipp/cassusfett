import RPi.GPIO as GPIO
from tracks import Tracks
from sonar import Sonar
from light import Light
from brain import Brain, ZombieBrain
import logging
import sys


def main():
    logging.basicConfig(level=logging.INFO)

    GPIO.setmode(GPIO.BCM)

    tracks = Tracks(power_left=18,
                    forward_left=2,
                    backward_left=3,
                    power_right=19,
                    forward_right=4,
                    backward_right=5)
    sonar = Sonar(trigger=14, echo=15)
    light = Light(pin=17)

    zombie_mode = False
    args = sys.argv[1:]
    if len(args) > 0:
        args[0] == "--zombie"
        zombie_mode = True
        logging.info("Zombie mode enabled: w - forward, s - backward, a - left, b - right")
    else:
        logging.info("Autonomous mode enabled: e - exit")

    brain = ZombieBrain(tracks, sonar, light) if zombie_mode else Brain(tracks, sonar, light)

    brain.run()
    while True:
        key = input()
        if zombie_mode:
            brain.on_command(key)
        if key == "e":
            break
    brain.die()
    GPIO.cleanup()


if __name__ == "__main__":
    main()
