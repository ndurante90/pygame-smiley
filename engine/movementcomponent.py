from .component import Component


class MovementComponent(Component):
    def __init__(self, speed, windowBoundingRect, imageBoundingRect):
        self.vx = speed
        self.vy = speed
        self.windowBoundingRect = windowBoundingRect
        self.imageBoundingRect = imageBoundingRect
        self.xCoordinate = windowBoundingRect.centerx - (imageBoundingRect.width / 2)
        self.yCoordinate = windowBoundingRect.centery - (imageBoundingRect.height/2)
    
    def load(self):
       return

    def update(self):
        self.xCoordinate += self.vx
        self.yCoordinate += self.vy

        # bounce on the x axis
        if self.xCoordinate < 0 or (self.xCoordinate+self.imageBoundingRect.width) > self.windowBoundingRect.width:
           self.vx = -self.vx
        
        # bounce on the y axis
        if self.yCoordinate < 0 or (self.yCoordinate + self.imageBoundingRect.height) > self.windowBoundingRect.height:
           self.vy = -self.vy
    
    def render(self, window):
        return
