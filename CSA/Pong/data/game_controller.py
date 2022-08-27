import pygame,sys

from prepare import *

class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(caption)
        self.objects = pygame.sprite.Group()
    def set_objects(self, ball, left_player):
        self.objects.add(ball, left_player)
        
    def draw_screen(self):
        self.screen.fill(bg_color)
        self.objects.draw(self.screen)
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            sys.exit()
        pygame.display.flip()
        self.clock.tick(60)
    def update(self):
        self.objects.update()