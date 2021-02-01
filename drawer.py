import pygame
import numpy as np
from vector_helpers import *

class Drawer:
    def __init__(self, screen, coord_converter):
        self.screen = screen
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.coord_converter = coord_converter

    def _draw_arrow(self, x, y, dir):
        color = (255, 255, 0)
        n = norm(dir)
        rot_matrix = np.array([
            np.array([dir[0]/n, -dir[1]/n]),
            np.array([dir[1]/n, dir[0]/n])
        ])
        base_arrow = [(0, 0.3), (0, 0.6), (0.6, 0.6), (0.6, 0.9), (0.9, 0.45), (0.6, 0), (0.6, 0.3)]
        rotated_arrow = [rot_matrix @ np.array([i,j]) for i,j in base_arrow]
        arrow = [self.coord_converter.map(x + i*n, y + j*n) for i,j in rotated_arrow]
        pygame.draw.polygon(self.screen, color, arrow)

    def draw_grid(self):
        color = (255, 255, 255)
        for i in range(19):
            pygame.draw.line(self.screen, color, self.coord_converter.map(i - 9, -10), self.coord_converter.map(i - 9, 10), 1)
            pygame.draw.line(self.screen, color, self.coord_converter.map(-10, i - 9), self.coord_converter.map(10, i - 9), 1)

    def draw_engine(self, engine):
        self.screen.fill((0, 0, 0))
        self.draw_grid()
        for body in engine.bodies:
            radius_x = body.radius_x
            radius_y = body.radius_y
            body_tpos = (body.pos[0] - engine.cur_body.pos[0], body.pos[1] - engine.cur_body.pos[1])
            rect = pygame.Rect(*self.coord_converter.map(body_tpos[0] - radius_x, body_tpos[1] - radius_y),
                *self.coord_converter.map_values(2*radius_x, 2*radius_y))
            pygame.draw.ellipse(self.screen, body.color, rect, 0)
            # time_text = self.font.render(f'{body.time:.2f}', False, (255, 255, 255))
            # self.screen.blit(time_text, (rect.left, rect.top))
        for body in engine.bodies:
            body_tpos = (body.pos[0] - engine.cur_body.pos[0], body.pos[1] - engine.cur_body.pos[1])
            self._draw_arrow(*body_tpos, body.vel)
        for i, body in enumerate(engine.bodies):
            vel_text = self.font.render(f'{norm(body.vel):.3f}', False, body.color)
            self.screen.blit(vel_text, [0, i*50])
            

    def draw_info(self, time_mul, time):
        time_mul_text = self.font.render(f'Time multiplier: {time_mul:.1f}', False, (255, 255, 255))
        time_text = self.font.render(f'Time: {time:.2f}', False, (255, 255, 255))
        self.screen.blit(time_mul_text, [self.screen.get_size()[0] - 500, self.screen.get_size()[1] - 100])
        self.screen.blit(time_text, [self.screen.get_size()[0] - 500, self.screen.get_size()[1] - 50])