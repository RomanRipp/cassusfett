import RPi.GPIO as GPIO
from tracks import Tracks
from sonar import Sonar
from light import Light
from temperature import TemperatureHumidity
from brain import Brain, ZombieBrain
from metrics import Monitoring
import logging
import sys


def parse_flags():
    args = sys.argv[1:]
    zombie_mode = "--zombie" in args
    debug_mode = "--debug" in args
    return zombie_mode, debug_mode


def main():
    GPIO.setmode(GPIO.BCM)

    tracks = Tracks(power_left=18,
                    forward_left=2,
                    backward_left=3,
                    power_right=19,
                    forward_right=4,
                    backward_right=5)
    sonar = Sonar(trigger=14, echo=15)
    light = Light(pin=17)
    ths = TemperatureHumidity(pin=27, sleep=5)

    zombie_mode, debug_mode = parse_flags()
    if debug_mode:
        logging.basicConfig(level=logging.DEBUG)
        logging.info("Debug mode enabled")
    else:
        logging.basicConfig(level=logging.INFO)

    if zombie_mode:
        logging.info("Zombie mode enabled: w - forward, s - backward, a - left, b - right")
        brain = ZombieBrain(tracks, sonar, light, ths)
    else:
        logging.info("Autonomous mode enabled: e - exit")
        brain = Brain(tracks, sonar, light, ths)

    brain.run()
    monitoring = Monitoring(9100, light, sonar, ths)
    while True:
        key = input()
        if zombie_mode:
            brain.on_command(key)
        if key == "e":
            break
    monitoring.close()
    brain.die()
    GPIO.cleanup()


if __name__ == "__main__":
    main()
