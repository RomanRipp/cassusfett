from unittest import TestCase
from sonar import Sonar
import time


class TestSonar(TestCase):
    def test_start(self):
        sonar = Sonar(1, 2)
        sonar.start()
        for i in range(0, 5):
            d, t = sonar.get_distance()
            print(d)
            print(t)
            time.sleep(5)
        sonar.stop()


