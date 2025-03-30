import pygame
from pygame.locals import *
import minelayout
pygame.mixer.init()  # Initialize the mixer module.
sound1 = pygame.mixer.Sound('SpeechOn.wav')  # Load a sound.
square_size=25
row=9  
col=9
mines=10
# level="Beginner"
# level="Intermediate"
level="Expert"
if level=="Beginner":
    row=9  
    col=9
    mines=10
if level=="Intermediate":
    row=16  
    col=16
    mines=40
if level=="Expert":
    row=16  
    col=30
    mines=99
game_board=minelayout.board(square_size,row,col,mines)
first_click=True 
previousblock=None
both_button_pressed=False
left_button_pressed=False
right_button_pressed=False
game_started=False
clock = pygame.time.Clock()
timer=0
dt=0
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)
block=None
reset_btn=None
while True : 
    clock.tick(20)

    for event in pygame.event.get() :  
       
        if event.type == pygame.QUIT : 
            pygame.quit() 
        elif event.type == timer_event:
            game_board.update_timer()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #sound1.play()
            block=game_board.get_rect(event)
            if  event.button==1:
                left_button_pressed=True
            if  event.button==3:
                    right_button_pressed=True
            if left_button_pressed and right_button_pressed:
                both_button_pressed=True
            if block!=None and not block.is_flaged and not game_board.game_end:
                game_board.mouse_down(block,both_button_pressed)
                img = pygame.image.load("scary.png")
                img.convert()
                img=pygame.transform.rotozoom(img, 0, game_board.zoom_factor)
                game_board.display_surface.blit(img, game_board.reset_button)
            else:
                if game_board.reset_button.collidepoint(event.pos):
                       reset_btn=game_board.reset_button
                       game_board.update_pic("happyfaceclicked.png",game_board.zoom_factor,reset_btn)
        elif event.type == pygame.MOUSEMOTION:
             if not game_board.game_end:
                if left_button_pressed or right_button_pressed:
                    if block!=None:
                        game_board.mouse_off(block,both_button_pressed)
                    if reset_btn !=None:
                       game_board.update_pic("happyface.png",game_board.zoom_factor,reset_btn)
                       reset_btn=None
                    block=game_board.get_rect(event)
                    if block!=None:
                        game_board.mouse_down(block,both_button_pressed)
                    if game_board.reset_button.collidepoint(event.pos):
                       reset_btn=game_board.reset_button
                       game_board.update_pic("happyfaceclicked.png",game_board.zoom_factor,reset_btn)
        elif event.type == pygame.MOUSEBUTTONUP:  # Mouse released 
            block=game_board.get_rect(event)
            if block==None:
                if game_board.reset_button.collidepoint(event.pos):
                    game_board=minelayout.board(square_size,row,col,mines)
                    first_click=True
            else:              
                if not game_board.game_end:
                    game_board.update_pic("happyface.png",game_board.zoom_factor,game_board.reset_button)
                    game_board.mouse_off(block,both_button_pressed)
                    if not both_button_pressed:
                        if event.button==1: # Left click
                            if first_click:
                                first_click=False
                                game_board.create_layout(block)
                            game_board.reveal_block(block)
                        if event.button==3: # right click
                            game_board.flag(block)
                    else:                   
                        if block.is_revealed and block.surrounding_mines!=0:
                            game_board.reveal_blocks(block)                      
                    
                
            if event.button==1: # Left click
                left_button_pressed=False
            if event.button==3: # right click
                right_button_pressed=False
            if not left_button_pressed and not right_button_pressed:
                both_button_pressed=False
        pygame.display.update()  
      
  
        
