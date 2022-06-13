from fileinput import filename
from ctypes.wintypes import RGB
from .component import Component
import pygame

class StaticSpriteComponent(Component):
    def __init__(self, filename):
        self.image = pygame.image.load(filename)

    def load(self, window):
        self.xCoordinate = window.get_rect().centerx - (self.image.get_rect().width / 2)
        self.yCoordinate = window.get_rect().centery - (self.image.get_rect().height/2)
        self.vx = 0.05
        self.vy = 0.05
        self.windowWidth = window.get_rect().width
        self.windowHeight = window.get_rect().height
    
    def update(self):
        self.xCoordinate += self.vx
        self.yCoordinate += self.vy

        # bounce on the x axis
        if self.xCoordinate < 0 or (self.xCoordinate+self.image.get_width()) > self.windowWidth:
           self.vx = -self.vx
        
        # bounce on the y axis
        if self.yCoordinate < 0 or (self.yCoordinate + self.image.get_height()) > self.windowHeight:
           self.vy = -self.vy
    
    def render(self, window):
        BLACK = RGB(0,0,0)
        window.fill(BLACK)
        window.blit(self.image, (self.xCoordinate, self.yCoordinate))
        pygame.display.update()
