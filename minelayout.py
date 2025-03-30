import numpy
import random
import math
import pygame
from pygame.locals import *
import helper
import time

###################  Board ################################
class block:
    has_mine:bool=False
    surrounding_mines:int=0
    is_flaged:bool=False
    is_revealed:bool=False
    rect:pygame.Rect=None
    row:int=None
    col:int=None
    pic:str=None
    def __init__(self,row,col,has_mine):
        self.row=row
        self.col=col
        self.has_mine=has_mine
        self.pic="unopened.png"
    def explode(self,surface,zoom_factor):
        self.is_revealed=True
        explode_pic= pygame.image.load("explode.png")
        explode_pic.convert()
        explode_pic=pygame.transform.rotozoom(explode_pic, 0, zoom_factor)
        explode_pic_rect = explode_pic.get_rect(center=self.rect.center)
        surface.blit(explode_pic, explode_pic_rect) 
    def reveal(self,surface,zoom_factor):
        self.is_revealed=True
        pic=pygame.image.load(helper.get_pic(self.surrounding_mines))
        pic.convert()
        pic=pygame.transform.rotozoom(pic, 0, zoom_factor)
        pic_rect = pic.get_rect(center=self.rect.center)
        surface.blit(pic, pic_rect) 


###################  Board ################################
class board:
    square_size:int=None
    num_rows:int=None
    num_cols:int=None
    num_mines:int=None
    remaining_mines:int=None
    revealed_blocks:int=0
    flaged_blocks:int=0
    header_size:int
    margin:int 
    mine_layout:numpy.ndarray=None
    timer:list[pygame.Rect]=None
    counter:list[pygame.Rect]=None
    reset_button:pygame.Rect=None
    display_surface:pygame.Surface=None
    game_end:bool=False
    game_start:bool=False
    start_time:int=0
    zoom_factor:float=0.5
    level:int=1
    def __init__(self,square_size,num_rows,num_cols,num_mines):
        self.square_size=square_size
        self.num_cols=num_cols
        self.num_rows=num_rows
        self.num_mines=num_mines
        self.remaining_mines=num_mines
        self.header_size=2*self.square_size
        self.margin=square_size/5
        self.mine_layout=numpy.empty((num_rows, num_cols), dtype=block)
        self.timer=[]
        self.counter=[]
        self.zoom_factor=square_size/50*0.8
        self.create_board()
    def create_board(self)->pygame.Surface:
        # assigning values to X and Y variable 
        X = self.num_cols*self.square_size
        Y = self.num_rows*self.square_size+ self.header_size
        
        # create the display surface object 
        # of specific dimension..e(X,Y). 
        self.display_surface = pygame.display.set_mode((X, Y )) 
        # set the pygame window name 
        pygame.display.set_caption('mine sweeper') 
        self.display_surface.fill((173, 168, 160))
       
        #### happy face#####
        img = pygame.image.load("happyface.png")
        img.convert()
        img=pygame.transform.rotozoom(img, 0, self.zoom_factor)
        self.reset_button = img.get_rect(center=(X/2,self.header_size/2))
        self.display_surface.blit(img, self.reset_button)

        #### counter and timer #####
        spacing=self.square_size*self.zoom_factor*2
        for i in range(0,3):
            counter_start_x=self.square_size+spacing*i
            timer_start_x=X-self.square_size-spacing*(2-i)
            img = pygame.image.load("zero.png")
            img.convert()
            img=pygame.transform.rotozoom(img, 0, self.zoom_factor)
            timer_rect = img.get_rect(center=(counter_start_x,self.square_size))
            count_rect=img.get_rect(center=(timer_start_x,self.square_size))
            self.timer.append(timer_rect)
            self.counter.append(count_rect)
            self.display_surface.blit(img, timer_rect)
            self.display_surface.blit(img, count_rect)
        self.update_counter()
        ######blocks #####
        for i in range(0,self.num_rows):
            for j in range(0,self.num_cols):
                center=(j*self.square_size+self.square_size/2,i*self.square_size+self.header_size+self.square_size/2)
                rect=Rect(center[0]-self.square_size/2,center[1]-self.square_size/2,self.square_size,self.square_size)
                self.mine_layout[i,j]=block(i,j,False)
                self.mine_layout[i,j].rect=rect
                self.update_pic(self.mine_layout[i,j].pic,self.zoom_factor,rect)
                
        return self.display_surface
    #--------------------------------------------------------------#
    def update_counter(self):
        ones=self.remaining_mines%10
        tens=self.remaining_mines%100//10
        hundreds= self.remaining_mines//100
        digits=[hundreds,tens,ones]
        i=0
        for d in self.counter:
            self.clear_pic(d)
            self.update_pic(helper.get_pic(digits[i],False),self.zoom_factor,d)
            i+=1

    def update_timer(self):
        time_eclipse=int(time.time()-self.start_time)
        if time_eclipse>=999:
            time_eclipse=999
        if time_eclipse>0 and self.game_start and not self.game_end:
            ones=time_eclipse%10
            tens=time_eclipse%100//10
            hundreds= time_eclipse//100
            digits=[hundreds,tens,ones]
            i=0
            for d in self.timer:
                self.clear_pic(d)
                self.update_pic(helper.get_pic(digits[i],False),self.zoom_factor,d)
                i+=1

    def flag(self,block):
        if not block.is_revealed:
            block.is_flaged=not block.is_flaged
            if block.is_flaged:
                pic= "flag.png"
                self.remaining_mines-=1
            else:
                pic='unopened.png'
                self.remaining_mines+=1
            self.update_counter()
            self.update_pic(pic,self.zoom_factor,block.rect)

    def reveal_map(self):
        self.game_end=True
        for x in self.mine_layout:
            for y in x:
                if y.is_revealed:
                    continue
                pic=None
                if y.is_flaged:
                    if not y.has_mine:
                        pic="wrong.png"
                elif y.has_mine:
                    pic= "right.png"
                else:
                    pic=helper.get_pic(y.surrounding_mines)
                if pic!=None:
                    self.update_pic(pic,self.zoom_factor,y.rect)

    #############################################################
    def is_resolved(self)->bool:
        if self.revealed_blocks==self.num_cols*self.num_rows-self.num_mines:
            self.game_end=True
            self.update_pic("win.png",self.zoom_factor,self.reset_button)

            for x in self.mine_layout:
                for y in x:
                    if not y.is_revealed and not y.is_flaged:
                        self.flag(y)

            return True
        return False

    def reveal_blocks(self,block:block):
        if block.is_flaged or not block.is_revealed:
            return
        blocks=self.get_surrounding_blocks(block)
        num_mines=len([b for b in blocks if b.is_flaged])
        if num_mines==block.surrounding_mines:
            for b in blocks:
                if not b.is_flaged:
                    self.reveal_block(b)
        
    def reveal_block(self,block:block):
    
        if block.is_flaged:
            return
        if block.has_mine:
            block.explode(self.display_surface,self.zoom_factor)
            self.update_pic("loss.png",self.zoom_factor,self.reset_button)

            self.reveal_map()
            self.game_end=True
            return
        if self.is_resolved():
            self.game_end=True
            return
        if block.is_revealed:
            return
        block.reveal(self.display_surface,self.zoom_factor)
        self.revealed_blocks+=1
        if block.surrounding_mines==0:
            row=block.row
            col=block.col
            indices=self.get_surrounding_indices(row,col)
            for t in indices:
                block=self.mine_layout[t[0],t[1]]
                if not block.is_revealed and not block.is_flaged:
                    self.reveal_block(block)       
        if self.is_resolved():
           self.game_end=True

    def create_layout(self,block:block):
        block_array=self.mine_layout
        mine_layout=numpy.zeros(shape=(self.num_rows,self.num_cols))
        fill_percentage=self.num_mines/(self.num_rows*self.num_cols)
        allocated=0
        indices=self.get_surrounding_indices(block.row,block.col)
        indices.append((block.row,block.col))
        while allocated<self.num_mines:
            a=math.floor(random.random()*self.num_cols*self.num_rows)
            i=math.floor(a/self.num_cols)
            j=a%self.num_cols
            if (i,j) in indices:

                continue
            if mine_layout[i,j]==1:
                continue;
            if self.check_surrounding_blocks(i,j,mine_layout)>fill_percentage*1.2:
                continue 
            mine_layout[i,j]=1
            allocated+=1
        for i in range(0,self.num_rows):
            for j in range(0,self.num_cols):
                mine_count=self.get_mine_count_from_surrounding_blocks(i,j,mine_layout)
                if block_array[i,j] ==None:
                        block_array[i,j]=block(i,j,False)
                if mine_layout[i,j]==1:
                    block_array[i,j].has_mine=True
                block_array[i,j].surrounding_mines=mine_count
        self.start_time=int(time.time())
        self.game_start=True
        return block_array    

    def check_surrounding_blocks(self,i,j,block_array):
        available_blocks=1
        count=0
        indices=self.get_surrounding_indices(i,j)
        for t in indices:
            count+=block_array[t[0],t[1]]
            available_blocks+=1    
        return count/available_blocks
    
    def get_mine_count_from_surrounding_blocks(self,i,j,block_array):
        
        count=0
        indices=self.get_surrounding_indices(i,j)
        for t in indices:
            count+=block_array[t[0],t[1]]
        return count
    
    def get_rect(self,event)->block:
        for x in self.mine_layout:
            for y in x:
                if y.rect.collidepoint(event.pos):
                    return y 
        return None  

    def get_surrounding_blocks(self,block:block)->list[block]:
        blocks=[]
        i=block.row
        j=block.col
        indices=self.get_surrounding_indices(i,j)
        for t in indices:
            blocks.append(self.mine_layout[t[0],t[1]])
        return blocks
    def get_surrounding_indices(self,i,j):
        indices=[]
        if i+1<self.num_rows:
            indices.append((i+1,j))
        if j+1 <self.num_cols:
            indices.append((i,j+1))
        if j-1 >=0:    
            indices.append((i,j-1))
        if i-1>=0:
            indices.append((i-1,j))
        if j+1<self.num_cols and i-1>=0:
            indices.append((i-1,j+1))
        if j-1>=0 and i-1>=0:
            indices.append((i-1,j-1))
        if j-1>=0 and i+1<self.num_rows:
            indices.append((i+1,j-1))
        if j+1<self.num_cols and i+1<self.num_rows:
            indices.append((i+1,j+1))
        return indices
    def mouse_down(self,block:block,both_button_pressed:bool, is_reset_btn=False):
        if not is_reset_btn:
            blocks=[block]
            if both_button_pressed:
                blocks.extend(self.get_surrounding_blocks(block))
            for b in blocks:
                if not b.is_revealed and not b.is_flaged:
                    self.update_pic("opened.png",self.zoom_factor,b.rect)

        else:
            pass
    def mouse_off(self,block,both_button_pressed, is_reset_btn=False):
        if not is_reset_btn:
            blocks=[block]
            if both_button_pressed:
                blocks.extend(self.get_surrounding_blocks(block))
            for b in blocks:
                if not b.is_revealed and not b.is_flaged:
                    self.update_pic("unopened.png",self.zoom_factor,b.rect)

        else:
            pass
    def update_pic(self,pic_file:str,zoom_factor:float,rect:pygame.Rect):
        
        
        pic=pygame.image.load(pic_file)
        pic.convert()
        pic=pygame.transform.rotozoom(pic, 0, zoom_factor)
        self.display_surface.blit(pic, rect)
    def clear_pic(self,rect:pygame.Rect):
        pic=pygame.Surface((rect.width,rect.height))
        pic.fill((0,0,0))
        self.display_surface.blit(pic, rect)