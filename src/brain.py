import logging
import time
import random

OBSTACLE = "obstacle"
DROP = "drop"
NORMAL = "normal"


def solve_distance(dist):
    normal = 100
    delta = 10
    err = normal - dist
    if abs(err) > delta:
        if dist < normal:
            return OBSTACLE
        else:
            return DROP
    else:
        return NORMAL


class WalkState:
    def __init__(self, tracks):
        self._tracks = tracks

    def handle_light_change(self, light):
        if light:
            self._tracks.stop()
            logging.debug("found light!")
            return RestState(self._tracks)
        return self

    def _try_avoid_obstacle(self):
        logging.debug("avoiding obstacle")
        self._tracks.backward()
        time.sleep(0.5)
        if bool(random.getrandbits(1)):
            self._tracks.right()
        else:
            self._tracks.left()
        time.sleep(random.uniform(1, 3))
        self._tracks.forward()

    def handle_distance_change(self, dist):
        switch = solve_distance(dist)
        if switch == DROP or switch == OBSTACLE:
            self._try_avoid_obstacle()
            return self
        return self


class RestState:
    def __init__(self, tracks):
        self._tracks = tracks

    def handle_light_change(self, light):
        if not light:
            self._tracks.forward()
            return WalkState(self._tracks)
        return self

    def handle_distance_change(self, dist):
        logging.debug("distance changed while resting: {0}".format(dist))
        return self


class Brain:
    def __init__(self, tracks, sonar, light):
        self._current_state = RestState(tracks)
        self._tracks = tracks
        self._sonar = sonar
        self._light = light

    def run(self):
        self._tracks.stop()
        self._sonar.start()
        self._light.start()
        self._sonar.subscribe(self)
        self._light.subscribe(self)

    def die(self):
        self._tracks.stop()
        self._sonar.unsubscribe(self)
        self._light.unsubscribe(self)
        self._sonar.stop()
        self._light.stop()

    def on_light_change(self, light):
        self._current_state = self._current_state.handle_light_change(light)

    def on_distance_change(self, dist):
        self._current_state = self._current_state.handle_distance_change(dist)


class ZombieBrain:
    def __init__(self, tracks, sonar, light):
        self._tracks = tracks
        self._sonar = sonar
        self._light = light

    def on_command(self, cmd):
        if cmd == "w":
            self._tracks.forward()
        elif cmd == "s":
            self._tracks.backward()
        elif cmd == "d":
            self._tracks.right()
        elif cmd == "a":
            self._tracks.left()
        elif cmd == "q":
            self._tracks.stop()

    def run(self):
        self._tracks.stop()
        self._sonar.start()
        self._light.start()

    def die(self):
        self._tracks.stop()
        self._sonar.stop()
        self._light.stop()
