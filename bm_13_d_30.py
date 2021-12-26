import math
from matplotlib import pyplot as plt

MODEL_G = 9.81
MODEL_DT = 0.001

class Body:

    def __init__(self, x, y, vx, vy):

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.trajectory_x = []
        self.trajectory_y = []

    def advance(self):
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT


class Rocket(Body):

    def __init__(self, x, y, fuel, rocket, vf, angle, m):

        self.rocket = rocket
        self.fuel = fuel
        self.vf = vf
        self.ang = angle
        self.weight = fuel + rocket
        self.time = 0
        self.m = m

        super().__init__(x, y, 0, 0)

    def advance(self):

        fuel = self.fuel
        if self.time * self.m <= fuel:
            self.trajectory_x.append(self.x)
            self.trajectory_y.append(self.y)

            self.vx = math.log(self.weight/(self.weight - self.m*self.time)) * self.vf * math.cos(self.ang)
            self.vy = math.log(self.weight/(self.weight - self.m*self.time)) * self.vf * math.sin(self.ang)

            self.weight = (self.fuel + self.rocket) / 2.71**(self.vx/(self.vf*math.sin(self.ang)))
            self.time += MODEL_DT
        else:
            self.trajectory_x.append(self.x)
            self.trajectory_y.append(self.y)
            self.x += self.vx * MODEL_DT
            self.y += self.vy * MODEL_DT
            self.vy -= MODEL_G * MODEL_DT


d30 = Body(0, 0, 50, 50)
while d30.y >= 0:
    d30.advance()

katusha = Rocket(0, 0, 5, 50, 2000, 0.79, 0.5)
while katusha.y >= 0:
    katusha.advance()

plt.figure(figsize=(10, 6))
plt.plot(katusha.trajectory_x, katusha.trajectory_y, 'b', label = 'Траектория "Катюши"')
plt.plot(d30.trajectory_x, d30.trajectory_y, 'g', label = 'Траектория Д-30')
plt.title('Полет снарядов под углом в 45 градусов')
plt.xlabel('X, м')
plt.ylabel('Y, м')
plt.grid()
plt.legend()
plt.show()
