from lldPython.design_patterns.observerDpModified.observers.observer import Observer


class Display(Observer):
    def update(self, temperature, humidity):
        print(f"Display updated with temperature: {temperature}, humidity: {humidity}")
