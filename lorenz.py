import numpy as np
import sys
import matplotlib.pyplot as plt 

start_pos = np.array([0.1, 0.5, 0.1])
#                     x  , y  , z
sigma = 10
beta = 8/3
rho = 28
numiter = 10000
dt = 0.01

class Lorenz:

    def __init__(self, pos, sigma, beta, rho, numiter, dt):
        self.pos = pos
        self.sigma = sigma
        self.beta = beta
        self.rho = rho
        self.numiter = numiter
        self.x = np.array([])
        self.y = np.array([])
        self.z = np.array([]) 
        self.dt = dt 

    def update(self):
        self.pos[0] += (self.sigma * (self.pos[1] - self.pos[0])) * self.dt
        self.pos[1] += (self.pos[0] * ( self.rho - self.pos[2]) - self.pos[1]) * self.dt
        self.pos[2] += (self.pos[0] * self.pos[1] - self.beta * self.pos[2]) * self.dt

    def gen(self):
        for i in range(self.numiter):
            self.x = np.append(self.x, self.pos[0])
            self.y = np.append(self.y, self.pos[1])
            self.z = np.append(self.z, self.pos[2])
            self.update()
            
    def plot(self):
        self.gen()
        print(self.x)
        ax = plt.figure().add_subplot(projection='3d')
        ax.plot(self.x, self.y, self.z)
        plt.show()
lor = Lorenz(start_pos, sigma, beta, rho, numiter, dt)
lor.plot()