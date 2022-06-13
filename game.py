import sys, pygame, pygame.locals
from engine.actor import Actor
from engine.scene import Scene
from engine.staticspritecomponent import StaticSpriteComponent

#Initialize the display module
pygame.init()

#init window surface object
window = pygame.display.set_mode((800, 600), 1)
pygame.display.set_caption("Smiley game");

#Init Scene
scene = Scene()
actor = Actor()

smiley = StaticSpriteComponent("smile.png")
actor.components.append(smiley)
scene.actors.append(actor)
scene.load(window)


quit = False
def process_events():
    global quit
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT :
           quit = True
    return

def update_logic():
    scene.update()

def render():
    scene.render(window)


#game loop
while not quit:
   #process game events
   process_events()

   #update logic
   update_logic()

   #renders new updates
   render()

pygame.quit()
sys.exit()