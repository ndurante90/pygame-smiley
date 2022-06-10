from ctypes.wintypes import RGB
import sys, pygame, pygame.locals

#Initialize the display module
pygame.init()

#init window surface object
window = pygame.display.set_mode((800, 600), 1)
pygame.display.set_caption("Smiley");

#load image
image = pygame.image.load("smile.png")

#global variables
xCoordinate = window.get_rect().centerx - (image.get_rect().width / 2)
yCoordinate = window.get_rect().centery - (image.get_rect().height/2)
vx = 0.05
vy = 0.05


quit = False
def process_events():
    global quit
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT :
           quit = True
    return

def update_logic():
    global xCoordinate, yCoordinate, vx, vy

    xCoordinate += vx
    yCoordinate += vy

    # bounce on the x axis
    if xCoordinate < 0 or (xCoordinate+image.get_width()) > window.get_rect().width:
        vx = -vx
    
    # bounce on the y axis
    if yCoordinate < 0 or (yCoordinate + image.get_height()) > window.get_rect().height:
        vy = -vy
    return

def render():

    black = RGB(0,0,0);

    window.fill(black);
    
    window.blit(image, (xCoordinate, yCoordinate))

    pygame.display.update();
    
    if quit == True:
       print("Exit from the program")
    return 


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