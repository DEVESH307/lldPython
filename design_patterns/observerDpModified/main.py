import time
from lldPython.design_patterns.observerDp.observers.Zomato import Zomato
from lldPython.design_patterns.observerDpModified.observers.display import Display
from lldPython.design_patterns.observerDpModified.subject.weatherStation import WeatherStation


if __name__ == "__main__":
    ws = WeatherStation()

    d1 = Display()
    z = Zomato()

    d1.register_subject(ws)
    z.register_subject(ws)

    ws.update_weather(30.0, 65.0)
    time.sleep(2)

    ws.update_weather(32.0, 70.0)
    time.sleep(2)

    z.unregister_subject(ws)

    ws.update_weather(28.0, 60.0)
    time.sleep(2)

    d1.unregister_subject(ws)

    ws.update_weather(30.0, 70.0)
    time.sleep(2)


