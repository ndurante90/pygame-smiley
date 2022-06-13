from fileinput import filename
from ctypes.wintypes import RGB

from engine.movementcomponent import MovementComponent
from .component import Component
import pygame

class StaticSpriteComponent(Component):
    def __init__(self, window, filename):
        self.image = pygame.image.load(filename)
        self.movement = None
        self.boundingRect = window.get_rect()

    def load(self):
        self.xCoordinate = self.boundingRect.centerx - (self.image.get_rect().width / 2)
        self.yCoordinate = self.boundingRect.centery - (self.image.get_rect().height/2)
    
    def update(self):
        if(self.movement is not None):
           self.movement.update()
           self.xCoordinate = self.movement.xCoordinate
           self.yCoordinate = self.movement.yCoordinate
    
    def render(self, window):
        BLACK = RGB(0,0,0)
        window.fill(BLACK)
        window.blit(self.image, (self.xCoordinate, self.yCoordinate))
        pygame.display.update()

    #method that adds movement to image
    def addMovement(self, speed):
        self.movement = MovementComponent(speed, self.boundingRect, self.image.get_rect())
