import pygame
from pygame.locals import *
pygame.init()

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
black = (0, 0, 0) 
red = (255, 0, 0) 
  
# assigning values to X and Y variable 
X = 400
Y = 400

# create the display surface object 
# of specific dimension..e(X,Y). 
display_surface = pygame.display.set_mode((X, Y )) 
  
# set the pygame window name 
pygame.display.set_caption('Drawing') 
  
# completely fill the surface object  
# with white colour  
display_surface.fill(white) 
rects=[]
img0 = pygame.image.load(".\minesweeper.jpg")
img0.convert()
img0=pygame.transform.rotozoom(img0, 0, 0.1)
rect0 = img0.get_rect()

display_surface.blit(img0, rect0)
#pygame.draw.rect(display_surface, green, rect0, 1)

# for i in range(1,9):
#     for j in range (1,9):
#         rect=Rect((i-1)*50+1, (j-1)*50+1, 48, 48)
#         rects.append(rect)
#         pygame.draw.rect(display_surface, white, 
#                     ((i-1)*50, (j-1)*50, 50, 50),1) 
#         pygame.draw.rect(display_surface, (181, 187, 196), 
#                     rect,0) 

def get_rect(event)->pygame.rect.Rect:
    for rect in rects:
        if rect.collidepoint(event.pos):
            return rect
    return None  
# infinite loop 
while True : 
      
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
  
            # deactivates the pygame library 
            pygame.quit() 
  
            # quit the program. 
            quit() 
        elif event.type == pygame.MOUSEBUTTONUP:  # Mouse released 
            rect=get_rect(event)
            if rect !=None:
                pygame.draw.rect(display_surface, (237, 239, 242), 
                    rect,0) 
            print("Mouse button has been released") 
  
        # Draws the surface object to the screen.  
        pygame.display.update()  

