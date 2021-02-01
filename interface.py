import pygame

class Interface:
    def __init__(self, app):
        self.app = app
        self.keypressed = set()
        self.mouse_pos = (0,0)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            self._handle_key_down(event.key)
        elif event.type == pygame.KEYUP:
            self._handle_key_up(event.key)
        elif event.type == pygame.MOUSEMOTION:
            self._handle_mouse_move(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN :
            self._handle_key_down(event.button)
        elif event.type == pygame.MOUSEBUTTONUP :
            self._handle_key_up(event.button)


    def _handle_key_down(self, key):
        self.keypressed.add(key)
        if key == 1:
            pass
            #self.app.change_system(self.mouse_pos)
        elif key == pygame.K_LEFT:
            self.app.slowdown(0.1)
        elif key == pygame.K_RIGHT:
            self.app.slowdown(-0.1)
        elif key == pygame.K_UP:
            self.app.slowdown(-1.0)
        elif key == pygame.K_DOWN:
            self.app.slowdown(1.0)
        elif key == pygame.K_1:
            self.app.change_system(0)
        elif key == pygame.K_2:
            self.app.change_system(1)
        elif key == pygame.K_3:
            self.app.change_system(2)
        elif key == pygame.K_q:
            self.app.set_drawer_view()
        elif key == pygame.K_w:
            self.app.set_graph_view()
        elif key == pygame.K_e:
            self.app.force_adjust()

    def _handle_key_up(self, key):
        self.keypressed.remove(key)

    def _handle_mouse_move(self, pos):
        self.mouse_pos = pos