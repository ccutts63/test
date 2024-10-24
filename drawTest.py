import pygame as pg
import threading


#main threaded loop
def go():

    #initial location of square
    locationX = 50
    locationY = 50

    #initialize pygame
    pg.fastevent.init()

    #set our surface
    surf = pg.display.set_mode((640,480))

    #check keys and draw rectangle loop
    while True:
        e = pg.fastevent.poll()
        if e.type == pg.KEYDOWN and e.unicode == 'q':
            return
        elif e.type == pg.QUIT:
            return
        elif e.type == pg.KEYDOWN and e.unicode == 'w':
            locationY = locationY - 20
        elif e.type == pg.KEYDOWN and e.unicode == 's':
            locationY = locationY + 20          
        elif e.type == pg.KEYDOWN and e.unicode == 'a':
            locationX = locationX - 20  
        elif e.type == pg.KEYDOWN and e.unicode == 'd':
            locationX = locationX + 20
        
        
        location = (locationX , locationY)
        size = (50,50)

        rect = location + size

        surf.fill("Black")
        pg.draw.rect(surf, "White", rect)
        pg.display.flip()


def main():
    """
    set window name

    initialize threading

    """
    pg.display.set_caption('Draw Test')
    t = threading.Thread(target=go)
    t.start()
    t.join()

if __name__ == "__main__":
   main()