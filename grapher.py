import pygame
import numpy as np
from coord_converter import CoordConverter
from vector_helpers import *

class Graph:
    def __init__(self, screen, xlim, ylim, grapher):
        self.screen = screen
        self.grapher = grapher
        self.local_coord_converter = CoordConverter((0.0, 1.0), (1.0, 0.0), xlim, ylim)
    
    def draw_grid(self):
        color = (0, 0, 0)
        color2 = (255, 255, 0)
        pygame.draw.line(self.screen, color, self.local_coord_converter.map(0.0, 0.0), self.local_coord_converter.map(1.0, 0.0), 3)
        for i in range(20):
            pygame.draw.line(self.screen, color, self.local_coord_converter.map(i/20, 0.0), self.local_coord_converter.map(i/20, 0.05), 3)
        pygame.draw.line(self.screen, color, self.local_coord_converter.map(0.5, 0.0), self.local_coord_converter.map(0.5, 1.0), 3)
        for i in range(20):
            pygame.draw.line(self.screen, color, self.local_coord_converter.map(0.45, i/20), self.local_coord_converter.map(0.55, i/20), 3)
        pygame.draw.line(self.screen, color2, self.local_coord_converter.map(0.5, 0.0), self.local_coord_converter.map(0.0, 0.5), 3)
        pygame.draw.line(self.screen, color2, self.local_coord_converter.map(0.5, 0.0), self.local_coord_converter.map(1.0, 0.5), 3)


    def draw(self, start, end, color, pos):
        start = self.local_coord_converter.map(start, 0.0)
        end = self.local_coord_converter.map(end, 1.0)
        pygame.draw.line(self.screen, color, start, end, 3)
        pygame.draw.circle(self.screen, color, self.local_coord_converter.map(*pos), 25)

class Grapher:
    def __init__(self, screen, coord_converter):
        self.screen = screen
        self.coord_converter = coord_converter
        self.local_coord_converter = CoordConverter((0.0, 1.0), (0.0, 1.0), (0, screen.get_size()[0]), (0, screen.get_size()[1]))
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.graphs = [Graph(screen, (0, screen.get_size()[0]/2), (0, screen.get_size()[1] - 100), self),
            Graph(screen, (screen.get_size()[0]/2, screen.get_size()[0]), (0, screen.get_size()[1] - 100), self)]


    def draw_engine(self, engine):
        self.screen.fill((255, 255, 255))
        coord_normalizer = CoordConverter(self.coord_converter.xlim, self.coord_converter.ylim, (0.0, 1.0), (0.0, 1.0))
        for g in self.graphs:
            g.draw_grid()
        for body in engine.bodies:
            radius_x = body.radius_x
            radius_y = body.radius_y
            max_time = 20
            body_tpos = (body.pos[0] - engine.cur_body.pos[0], body.pos[1] - engine.cur_body.pos[1])
            start_x, start_y = coord_normalizer.map(
                body_tpos[0] - body.time * body.vel[0],
                body_tpos[1] - body.time * body.vel[1])
            #start_x, start_y = coord_normalizer.map(bstart_x, bstart_y)
            cur_x, cur_y = coord_normalizer.map(
                body_tpos[0],
                body_tpos[1])
            #cur_x, cur_y = coord_normalizer.map(bcur_x, bcur_y)
            end_x, end_y = coord_normalizer.map(
                body_tpos[0] + (max_time - body.time) * body.vel[0],
                body_tpos[1] + (max_time - body.time) * body.vel[1])
            #end_x, end_y = coord_normalizer.map(bend_x, bend_y)
            self.graphs[0].draw(start_x, end_x, body.color, (cur_x, body.time/max_time))
            self.graphs[1].draw(start_y, end_y, body.color, (cur_y, body.time/max_time))
        rect = pygame.Rect(0, self.screen.get_size()[1] - 100, self.screen.get_size()[0], 100)
        pygame.draw.rect(self.screen, (255, 255, 255), rect, width = 0)
        for i, body in enumerate(engine.bodies):
            vel_text = self.font.render(f'{norm(body.vel):.3f}', False, body.color)
            self.screen.blit(vel_text, [0, self.screen.get_size()[1] - 100 + i*33])
            

    def draw_info(self, time_mul, time):
        time_mul_text = self.font.render(f'Time multiplier: {time_mul:.1f}', False, (0, 0, 0))
        time_text = self.font.render(f'Time: {time:.2f}', False, (0, 0, 0))
        self.screen.blit(time_mul_text, [self.screen.get_size()[0] - 500, self.screen.get_size()[1] - 100])
        self.screen.blit(time_text, [self.screen.get_size()[0] - 500, self.screen.get_size()[1] - 50])