from pygame.locals import *

def get_pic(num, for_mine:bool=True):
    if for_mine:
        if num==1:
            return "1.png"
        elif num==2:
            return "2.png"
        elif num==3:
            return "3.png"
        elif num==4:
            return "4.png"
        elif num==5:
            return "5.png"
        elif num==6:
            return "6.png"
        elif num==7:
            return "7.png"
        elif num==8:
            return "8.png"
        else:
            return "opened.png"
    else:
        if num==0:
            return "zero.png"
        elif num==1:
            return "one.png"
        elif num==2:
            return "two.png"
        elif num==3:
            return "three.png"
        elif num==4:
            return "four.png"
        elif num==5:
            return "five.png"
        elif num==6:
            return "six.png"
        elif num==7:
            return "seven.png"
        elif num==8:
            return "eight.png"
        elif num==9:
            return "nine.png"
        else:
            return "dash.png"

