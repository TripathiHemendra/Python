class Calculatar:
    def __init__(self, num):
        self.number = num

    def squre(self):
        print(f"The value of {self.number} squre is {self.number**2}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number**3}")       

    def squreroot(self):
        print(f"The value of {self.number} squreroot is {self.number**0.5}")

a = Calculatar(3)
a.squre
a.cube
a.squreroot
     