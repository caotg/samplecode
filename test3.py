import pygame
from pygame.locals import *
pygame.init()

white = (255, 255, 255) 
  
# create the display surface object 
# of specific dimension..e(X,Y). 
display_surface = pygame.display.set_mode((400, 400 )) 
  
# set the pygame window name 
pygame.display.set_caption('Drawing') 
  
# completely fill the surface object  
# with white colour  
display_surface.fill(white) 
pygame.draw.rect(display_surface, (255,23,30), (30,30,60,60)) 
while True : 
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
  
            # deactivates the pygame library 
            pygame.quit() 
    pygame.display.update()  
