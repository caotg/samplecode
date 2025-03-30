import pygame
from pygame.locals import *
pygame.init()

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
black = (0, 0, 0) 
red = (255, 0, 0) 
  
# assigning values to X and Y variable 
X = 450
Y = 550

# create the display surface object 
# of specific dimension..e(X,Y). 
display_surface = pygame.display.set_mode((X, Y )) 
  
# set the pygame window name 
pygame.display.set_caption('mine sweeper') 
  
# completely fill the surface object  
# with white colour  
display_surface.fill((173, 168, 160))
pygame.draw.rect(display_surface, black, 
                    (0, 10, 150, 80)) 
pygame.draw.rect(display_surface, black, 
                    (300, 10, 150, 80)) 
#### happy face#####
img0 = pygame.image.load(".\smiley.webp")
img0.convert()
img0=pygame.transform.rotozoom(img0, 0, 0.1)
rect0 = img0.get_rect(center=(225,50))
display_surface.blit(img0, rect0)

#### counter #####
spacing=25
counter_start_x=50
img1 = pygame.image.load("zero.png")
img1.convert()
img1=pygame.transform.rotozoom(img1, 0, 0.5)
rect1 = img1.get_rect(center=(counter_start_x,50))
display_surface.blit(img1, rect1)

img2 = pygame.image.load("zero.png")
img2.convert()
img2=pygame.transform.rotozoom(img2, 0, 0.5)
rect2 = img2.get_rect(center=(counter_start_x+spacing,50))
display_surface.blit(img2, rect2)

img3 = pygame.image.load("zero.png")
img3.convert()
img3=pygame.transform.rotozoom(img3, 0, 0.5)
rect3 = img3.get_rect(center=(counter_start_x+spacing*2,50))
display_surface.blit(img3, rect3)


######timer #####
timer_start_x=350
img4 = pygame.image.load("zero.png")
img4.convert()
img4=pygame.transform.rotozoom(img4, 0, 0.5)
rect4 = img1.get_rect(center=(timer_start_x,50))
display_surface.blit(img4, rect4)

img5 = pygame.image.load("zero.png")
img5.convert()
img5=pygame.transform.rotozoom(img5, 0, 0.5)
rect5 = img5.get_rect(center=(timer_start_x+spacing,50))
display_surface.blit(img5, rect5)

img6 = pygame.image.load("zero.png")
img6.convert()
img6=pygame.transform.rotozoom(img6, 0, 0.5)
rect6 = img6.get_rect(center=(timer_start_x+spacing*2,50))
display_surface.blit(img6, rect6)


# def get_rect(event)->pygame.rect.Rect:
#     for rect in rects:
#         if rect.collidepoint(event.pos):
#             return rect
#     return None  
# infinite loop 
while True : 

    for i in range(1,10):
        for j in range (1,10):
            
            pygame.draw.rect(display_surface, white, 
                        ((i-1)*50, (j-1)*50+100, 50, 50),1) 
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
  
            # deactivates the pygame library 
            pygame.quit() 
  
       
                # pygame.draw.rect(display_surface, (181, 187, 196), 
            #             rect,0) 

       
       
  
        # Draws the surface object to the screen.  
        pygame.display.update()  

