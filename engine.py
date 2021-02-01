from body import Body
import numpy as np
from vector_helpers import *

class Engine:
    def __init__(self, pos1, vel1, pos2, vel2):
        self.bodies = [
            Body(color = (255, 0, 0)),
            Body(color = (0, 255, 0), pos = np.array([*pos1]), vel = np.array([*vel1])),
            Body(color = (0, 0, 255), pos = np.array([*pos2]), vel = np.array([*vel2]))]
        self.cur_body = self.bodies[0]
        self.v3 = np.array([0.0, 0.0, 0.0])
    
    def update(self, t):
        for body in self.bodies:
            body.update(t)       
    
    def choose_body(self, number):
        body = self.bodies[number]
        if body is self.cur_body:
            return
        v = body.vel
        for b in self.bodies:
            b.transform(v)
        self.cur_body = body

    def adjust_bodies(self):
        for b in self.bodies:
            b.adjust(self.cur_body.time)