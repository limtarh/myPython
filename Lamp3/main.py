from Lamp import Lamp
import random
def main():
    lamp1 = Lamp()
    print("lamp1 is "+ str(lamp1))
    lamp = [Lamp() for i in range(30)]
    for i in range(30):
        print(lamp[i], end = "")

main()