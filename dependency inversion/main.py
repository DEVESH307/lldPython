# # 0. Define an interface for switchable devices(original code)

# from abc import ABC, abstractmethod


# class SwitchAble(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass

#     @abstractmethod
#     def turn_off(self):
#         pass



# class Light(SwitchAble):
#     def turn_on(self):
#         print("light Turning on")

#     def turn_off(self):
#         print("light Turning off")


# class fan(SwitchAble):
#     def turn_on(self):
#         print("fan Turning on")

#     def turn_off(self):
#         print("fan Turning off")


# class microwave(SwitchAble):
#     def turn_on(self):
#         print("microwave Turning on")

#     def turn_off(self):
#         print("microwave Turning off")


# class Switch:
#     def __init__(self, appliance):
#         self.appliance = appliance

#     def toggle(self, state):
#         if state == "on":
#             self.appliance.turn_on()

#         else:
#             self.appliance.turn_off()


# light = Light()
# s = Switch(light)

# s.toggle("on")
# s.toggle("off")

# f = fan()
# s2 = Switch(f)
# s2.toggle("on")
# s2.toggle("off")

# m = microwave()
# s3 = Switch(m)
# s3.toggle("on")
# s3.toggle("off")

# # class SwitchFan:
# #     def __init__(self, light):
# #         self.light = light
# #
# #     def toggle(self, state):
# #         if state == "on":
# #             self.light.turn_on_fan()
# #
# #         else:
# #             self.light.turn_off_fan()



# # class fan():
# #     def turn_on_fan(self):
# #         print("fan Turning on")
# #
# #     def turn_off_fan(self):
# #         print("fan Turning off")



# 1. switchable devices without interface (tight coupling)
# class Light:
#     def turn_on(self):
#         print("Light is turning on")

#     def turn_off(self):
#         print("Light is turning off")


# class Switch:
#     def __init__(self, light):
#         self.light = light
        
#     def toggle(self, state):
#         if state == "on":
#             self.light.turn_on()
#         else:
#             self.light.turn_off()

# light = Light()
# switch = Switch(light)
# switch.toggle("on") # output: Light is turning on
# switch.toggle("off") # output: Light is turning off

# class Fan:
#     def turn_on_fan(self):
#         print("Fan is turning on")

#     def turn_off_fan(self):
#         print("Fan is turning off")
        
# # switch2 = Switch(Fan())
# # switch2.toggle("on") # output: AttributeError: 'Fan' object has no attribute 'turn_on'
# # switch2.toggle("off") # output: AttributeError: 'Fan' object has no attribute 'turn_off'


# class SwitchFan:
#     def __init__(self, fan):
#         self.fan = fan
        
#     def toggle(self, state):
#         if state == "on":
#             self.fan.turn_on_fan()
#         else:
#             self.fan.turn_off_fan()
# fan = Fan()
# switch2 = SwitchFan(fan)
# switch2.toggle("on") # output: Fan is turning on
# switch2.toggle("off") # output: Fan is turning off


# 2. Switchable devices with interface (loose coupling)
from abc import ABC, abstractmethod
class Switchable (ABC):
    @abstractmethod
    def turn_on(self):
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def turn_off(self):
        raise NotImplementedError("Subclasses should implement this!")
    
class Light(Switchable):
    def turn_on(self):
        print("Light is turning on")

    def turn_off(self):
        print("Light is turning off")

class Fan(Switchable):
    def turn_on(self):
        print("Fan is turning on")

    def turn_off(self):
        print("Fan is turning off")

class Microwave(Switchable):
    def turn_on(self):
        print("Microwave is turning on")

    def turn_off(self):
        print("Microwave is turning off")
        
class switchable5Amp(Switchable):
    def turn_on(self):
        print("5 Amp appliance is turning on")

    def turn_off(self):
        print("5 Amp appliance is turning off")

class switchable50Amp(Switchable):
    def turn_on(self):
        print("50 Amp appliance is turning on")

    def turn_off(self):
        print("50 Amp appliance is turning off")

class Switch:
    def __init__(self, appliance: Switchable):
        self.appliance = appliance

    def toggle(self, state):
        if state == "on":
            self.appliance.turn_on()
        else:
            self.appliance.turn_off()
            
light = Light()
switch_light = Switch(light)
switch_light.toggle("on")  # output: Light is turning on
switch_light.toggle("off")  # output: Light is turning off

fan = Fan()
switch_fan = Switch(fan)
switch_fan.toggle("on")  # output: Fan is turning on
switch_fan.toggle("off")  # output: Fan is turning off

microwave = Microwave()
switch_microwave = Switch(microwave)
switch_microwave.toggle("on")  # output: Microwave is turning on
switch_microwave.toggle("off")  # output: Microwave is turning off

switchable_5_amp = switchable5Amp()
switch_5_amp = Switch(switchable_5_amp)
switch_5_amp.toggle("on")  # output: 5 Amp appliance is turning on
switch_5_amp.toggle("off")  # output: 5 Amp appliance is turning off

switchable_50_amp = switchable50Amp()
switch_50_amp = Switch(switchable_50_amp)
switch_50_amp.toggle("on")  # output: 50 Amp appliance is turning on
switch_50_amp.toggle("off")  # output: 50 Amp appliance is turning off
