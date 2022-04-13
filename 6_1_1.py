from time import sleep

class TrafficLight:
    __color = "Black"

    def running(self):
        while True:
            print("Trafficlight is red now")
            sleep(7)
            print("Trafficlight in yellow now")
            sleep(2)
            print("Trafficlight is green now")
            sleep(10)
            print("Trafficlight is yellow now")
            sleep(2)

trafficlight = TrafficLight()
trafficlight.running()
