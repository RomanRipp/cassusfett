from prometheus_client import start_http_server, Gauge


class Monitoring:
    def __init__(self, port: int, light, sonar, ths):
        self._light = light
        self._light.subscribe(self)
        self._sonar = sonar
        self._sonar.subscribe(self)
        self._ths = ths
        self._ths.subscribe(self)

        self._lightGauge = Gauge("light", "Light sensor readings", namespace="cassusfett")
        self._sonarGauge = Gauge("distance", "Distance measurement", namespace="cassusfett")
        self._temperatureGauge = Gauge("temperature", "Temperature sensor readings", namespace="cassusfett")
        self._humidityGauge = Gauge("humidity", "Humidity sensor readings", namespace="cassusfett")

        start_http_server(port)

    def on_light_change(self, light):
        self._lightGauge.set(light)

    def on_distance_change(self, dist):
        self._sonarGauge.set(dist)

    def on_temperature_humidity_change(self, temperature, humidity):
        self._temperatureGauge.set(temperature)
        self._humidityGauge.set(humidity)

    def close(self):
        self._light.unsubscribe(self)
        self._sonar.unsubscribe(self)
        self._ths.unsubscribe(self)
