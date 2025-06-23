from lldPython.design_patterns.observerDpModified.subject.subject import Subject


class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0.0
        self._humidity = 0.0

    def update_weather(self, temperature: float, humidity: float):
        self._temperature = temperature
        self._humidity = humidity
        print(f"WeatherStation updated with temperature: {temperature}, humidity: {humidity}")
        self.notify(temperature, humidity)