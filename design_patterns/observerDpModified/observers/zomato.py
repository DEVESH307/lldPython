from lldPython.design_patterns.observerDpModified.observers.observer import Observer


class ZOmato(Observer):
    def update(self, temperature, humidity):
        print(f"Zomato updated with temperature: {temperature}, humidity: {humidity}")
        if humidity > 20:
            print("Zomato updated price of delivery..")
        if humidity <= 20:
            print("Zomato updated price increased already increase of delivery..")