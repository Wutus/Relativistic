import pygame
from interface import Interface
from engine import Engine
from drawer import Drawer
from vector_helpers import *
from grapher import Grapher
from coord_converter import CoordConverter

class App:
    def __init__(self):
        pygame.init()
        self.running = False
        self.interface = Interface(self)
        self.time_increment = 0.1
        self.body_misplace = 0.3
        self.size = [1000, 1000]

    def run(self, pos1, vel1, pos2, vel2):
        self.screen = pygame.display.set_mode(self.size)
        self.coord_converter = CoordConverter((-10, 10), (-10, 10), (0, self.screen.get_size()[0]), (0, self.screen.get_size()[1]))
        pygame.display.set_caption('Relativistic')
        self.engine = Engine(pos1, vel1, pos2, vel2)
        self.time_multiplier = 1.0
        self._drawer = Drawer(self.screen, self.coord_converter)
        self._grapher = Grapher(self.screen, self.coord_converter)
        #self.drawer = Drawer(self.screen, self.coord_converter)
        self.drawer = self._drawer
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.interface.handle_event(event)
            self.clock.tick(60)
            if self.drawer is self._drawer:
                self.engine.adjust_bodies()
            self.engine.update(self.clock.get_time()/1000 * self.time_multiplier)
            self.draw()

    def draw(self):
        self.drawer.draw_engine(self.engine)
        self.drawer.draw_info(self.time_multiplier, self.engine.cur_body.time)
        pygame.display.flip()

    def change_system(self, body_no):
        #eng_pos = np.array(self.coord_converter.reverse_map(*pos))
        #self.engine.choose_body(eng_pos, self.body_misplace)
        self.engine.choose_body(body_no)

    def slowdown(self, val):
        self.time_multiplier -= val

    def set_drawer_view(self):
        self.drawer = self._drawer
        self.engine.adjust_bodies()

    def set_graph_view(self):
        self.drawer = self._grapher

    def force_adjust(self):
        self.engine.adjust_bodies()

    def __del__(self):
        pygame.quit()