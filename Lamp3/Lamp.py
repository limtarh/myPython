class Lamp:
    
    __isOn = None

    def __init__(self, *args):
        if len(args) == 0:
            self.__isON = False
        elif len(args) == 1:
            self.__isOn = args[0]
        else:
            raise Exception("Invalid Construction")

    def __str__(self):
        if self.__isOn:
            out = "{:3s} ".format("On")
        else:
            out = "{:3s} ".format("Off")
        return out

    def turnOn(self):
        self.__isON = True

    def turnOff(self):
        self.__isON = False

    def flip(self):
        self.__isOn = not self.__isOn

    def setLamp(self, isOn):
        self.__isOn  = isOn

    def __eq__(self, other):
        return 
