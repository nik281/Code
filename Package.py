class Car:
    def __init__(s,b,m,y):
        s.b = b 
        s.m = m
        s.y = y
    def disp(s):
        print(s.b,s.m,s.y)
class Ev(Car):
    def __init__(s, b, m, y,battery):
        super().__init__(b, m, y)
        s.battery = battery
    def disp(s):
        super().disp()
        print(s.battery)