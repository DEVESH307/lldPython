class Subject:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer {observer.__class__.__name__} registered.")
        else:
            print(f"Observer {observer.__class__.__name__} is already registered.")

    def unregister(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer {observer.__class__.__name__} unregistered.")
        else:
            print(f"Observer {observer.__class__.__name__} is not registered.")

    def notify(self, temperature, humidity):
        print(f"Notifying observers with temperature: {temperature}, humidity: {humidity}")
        for observer in self._observers:
            observer.update(temperature, humidity)
            print(f"Observer {observer.__class__.__name__} notified.")
