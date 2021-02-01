import numpy as np
from vector_helpers import *

class Body:
    def __init__(self, color, pos = np.zeros(2),
                    vel = np.zeros(2),
                    force = np.zeros(2),
                    mass = 1.0):
        self.pos = pos
        self.vel = vel
        self.force = force
        self.mass = mass
        self.radius = 0.2
        self.color = color
        self.time = 0.0
    
    def update(self, t):
        #self.vel += t*self.acc
        gamma = 1/np.sqrt(1 - norm(self.vel)**2)
        self.pos += t*self.vel
        self.time += t

    def transform(self, v):
        gamma = 1/np.sqrt(1 - norm(v)**2)
        #npos =  gamma*(self.pos - v * time)
        v3 = np.array([self.time, *self.pos])
        n = norm(v)
        lorentz_boost = np.array([
            np.array([gamma, -v[0]*gamma, -v[1]*gamma]),
            np.array([-v[0]*gamma, 1 + (gamma - 1)*v[0]**2/n**2, (gamma - 1)*v[0]*v[1]/n**2]),
            np.array([-v[1]*gamma, (gamma - 1)*v[0]*v[1]/n**2, 1 + (gamma - 1)*v[1]**2/n**2])
        ])
        v3_res = lorentz_boost @ v3
        npos = v3_res[1:]
        self.time = v3_res[0]
        nvel = np.divide(
            self.vel + np.multiply((gamma - 1)/np.dot(v,v) * np.dot(self.vel,v) - gamma, v),
            gamma * (1 - np.dot(self.vel,v)))
        self.vel = nvel
        self.pos = npos

    def translate(self, p):
        self.pos += p

    def adjust(self, time):
        diff = time - self.time
        self.pos += self.vel * diff
        self.time += diff

    @property
    def radius_x(self):
        return self.radius * np.sqrt(1 - self.vel[0]**2)
    
    @property
    def radius_y(self):
        return self.radius * np.sqrt(1 - self.vel[1]**2)

    # @property
    # def acc(self):
    #     return self.force/self.rmass

    # @property
    # def gamma(self):
    #     return 1/np.sqrt(1 - norm(self.vel)**2)

    # @property
    # def rmass(self):
    #     return self.mass/self.gamma

    