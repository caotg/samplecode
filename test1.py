import sys
import pygame as pg


pg.init()

screen = pg.display.set_mode((640, 480))
BLACK = pg.Color('black')
FONT = pg.font.Font(None, 32)


def game():
    clock = pg.time.Clock()
    lefttimer = 0
    righttimer=0
    dt = 0
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if lefttimer == 0:  # First mouse click.
                        lefttimer = 0.001  # Start the timer.
                    # Click again before 0.5 seconds to double click.
                    if righttimer < 0.5 and righttimer>0 :
                        print('both click')
                        lefttimer = 0
                        righttimer = 0
                if event.button == 3:
                    if righttimer == 0:  # First mouse click.
                        righttimer = 0.001  # Start the timer.
                    # Click again before 0.5 seconds to double click.
                    if lefttimer < 0.5 and lefttimer>0:
                        print('both click')
                        lefttimer = 0
                        righttimer = 0
        # Increase timer after mouse was pressed the first time.
        if lefttimer != 0:
            lefttimer += dt
            # Reset after 0.5 seconds.
            if lefttimer >= 0.5:
                print('too late')
                lefttimer = 0
        if righttimer != 0:
            righttimer += dt
            # Reset after 0.5 seconds.
            if righttimer >= 0.5:
                print('too late')
                righttimer = 0

        screen.fill(BLACK)
        txt = FONT.render(str(round(lefttimer, 2)), True, (180, 190, 40))
        screen.blit(txt, (40, 40))
        pg.display.flip()
        # dt == time in seconds since last tick.
        # / 1000 to convert milliseconds to seconds.
        dt = clock.tick(30) / 1000


if __name__ == '__main__':
    game()
    pg.quit()
    sys.exit()