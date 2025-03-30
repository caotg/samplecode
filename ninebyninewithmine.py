import pygame
from pygame.locals import *
import minelayout
import numpy
pygame.init()

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
black = (0, 0, 0) 
red = (255, 0, 0) 


num_rows=9
num_cols=9
num_mines=10  
square_size=50
header_size=2*square_size
margin=10
# assigning values to X and Y variable 
X = num_rows*square_size
Y = num_cols*square_size+ header_size

# create the display surface object 
# of specific dimension..e(X,Y). 
display_surface = pygame.display.set_mode((X, Y )) 
  
# set the pygame window name 
pygame.display.set_caption('mine sweeper') 
  
# completely fill the surface object  
# with white colour  
display_surface.fill((173, 168, 160))
pygame.draw.rect(display_surface, black, 
                    (0, margin, 3*square_size, header_size-2*margin)) 
pygame.draw.rect(display_surface, black, 
                    (6*square_size, margin, 3*square_size, header_size-2*margin)) 
#### happy face#####
img0 = pygame.image.load(".\smiley.webp")
img0.convert()
img0=pygame.transform.rotozoom(img0, 0, 0.1)
rect0 = img0.get_rect(center=(X/2,header_size/2))
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

mine_layout=minelayout.create_layout(num_mines,num_rows,num_cols)

for i in range(0,num_rows):
    for j in range(0,num_cols):
        center=(i*square_size+square_size/2,j*square_size+header_size+square_size/2)
        rect=Rect(center[0]-square_size/2,center[1]-square_size/2,square_size,square_size)
        mine_layout[i,j].rect=rect
        if mine_layout[i,j].has_mine:
            mine = pygame.image.load("right.png")
            mine.convert()
            mine=pygame.transform.rotozoom(mine, 0, 0.5)
            minerect = mine.get_rect(center=center)
            display_surface.blit(mine, minerect) 
        else:
            num=mine_layout[i,j].surrounding_mines
            pic=minelayout.get_pic(num)
            if pic==None:
                continue
            numpic = pygame.image.load(pic)
            numpic.convert()
            numpic=pygame.transform.rotozoom(numpic, 0, 0.5)
            numpicrect = numpic.get_rect(center=center)
            display_surface.blit(numpic, numpicrect) 


# def get_rect(event)->pygame.rect.Rect:
#     for rect in rects:
#         if rect.collidepoint(event.pos):
#             return rect
#     return None  
# infinite loop 
for i in range(0,num_rows):
        for j in range (0,num_cols):
            
            # pygame.draw.rect(display_surface, white, 
            #             ((i-1)*50, (j-1)*50+100, 50, 50),1) 
            square = pygame.image.load("unopened.png")
            square.convert()
            square=pygame.transform.rotozoom(square, 0, 0.85)
            squarerect = square.get_rect(center=(i*square_size+square_size/2,j*square_size+header_size+square_size/2))
            display_surface.blit(square, squarerect) 
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
  
       
                # pygame.draw.rect(display_surface, (181, 187, 196), 
            #             rect,0) 
        #elif event.type == pygame.MOUSEBUTTONDOWN:
            # block=game_board.minelayout.get_rect(event,mine_layout)
            # if block!=None:
            #      pygame.draw.rect(display_surface, (237, 239, 242), 
            #          block.rect,0) 
            # print("Mouse button has been released") 
        elif event.type == pygame.MOUSEBUTTONUP:  # Mouse released 
            block=minelayout.get_rect(event,mine_layout)
            if block!=None:
                pygame.draw.rect(display_surface, (237, 239, 242), 
                    block.rect,0) 
            print("Mouse button has been released") 
       
  
        # Draws the surface object to the screen.  
        pygame.display.update()  

