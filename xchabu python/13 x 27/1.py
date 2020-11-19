import pygame, sys
from pygame.locals import *
from pygame import *

pygame.init()
DISPLAY = pygame.display.set_mode((1200,650),0,32)
WHITE = (255,255,255)
Black = (0,0,0)
blue = (0,0,255)
DISPLAY.fill(WHITE)
x = 10
y = 10
pt1 = 0.7 * 15
pt2 = 0.4 * 15
len = 27 * 15
wid = 13 * 15
entdoor = 4 * 15
roomdoor= 3 * 15
toidoor = 2.6 * 15
font = pygame.font.SysFont(None, 24)
#toilet:-
toil = len * 0.26
toiw = wid * 0.39
toix = x + toiw / 2-15
toiy =y + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+pt1, toiw-pt1+1, toil-pt1+1), 2)
#bedroom:-
bedl = len * 0.41
bedw = wid * 0.61
bedx = x+toiw + bedw / 3-20
bedy = y  + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw, y , bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw+pt2, y+pt2 , bedw-pt2-pt1, bedl-pt2-pt2), 2)
#kitchen:-
kitl = len * 0.30
kitw = wid * 1
kitx = x + kitw / 3-50
kity = y+toil + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y +toil, kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y +toil+pt2, kitw-pt1-pt1, kitl-pt2), 2)
# bedroom correction
pygame.draw.rect(DISPLAY, WHITE, (x+toiw+2, y+2 , bedw-2, bedl-2))
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw, y , bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw+pt2, y+pt1 , bedw-pt2-pt1, bedl-pt1-pt2), 2)
# drawing room
drawl = len * 0.37
draww = wid * 0.69
drawx = x  + draww / 3
drawy = y +toil+kitl+ drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+toil+kitl-1, draww, drawl), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# inner drawing
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+toil+kitl+pt2, draww-pt1, drawl-pt2-pt1), 2)
#stairs:-
stal = len * 0.37
staw = wid * 0.32
stax = x+ draww+ staw / 2-20
stay = y+ toil+kitl + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-1, y+toil+kitl-1, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# stairs
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-1, y+toil+kitl-1+pt2, staw-pt1, stal-pt2-pt1), 2)
# door
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+toiw-1 , y+toil-toidoor, pt1-1, toidoor))
pygame.draw.rect(DISPLAY, Black, (x+toiw-1 , y+toil-toidoor, pt1-1, 2-1))
pygame.draw.rect(DISPLAY, Black, (x+toiw-1 , y+toil-2, pt1-1, 2))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+toiw+bedw-roomdoor-pt1, y+bedl-pt1+2 , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+toiw+bedw-roomdoor-pt1, y+bedl-pt1+2 , 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+toiw+bedw-pt1-1, y+bedl-pt1+2 , 2, pt1))
#main entry
pygame.draw.rect(DISPLAY, WHITE, (x+draww/2-20 , y+toil+kitl-1+drawl-pt1-1, entdoor, pt1+1))
pygame.draw.rect(DISPLAY, Black, (x+draww/2-20 , y+toil+kitl-1+drawl-pt1-1, 2, pt1+1))
pygame.draw.rect(DISPLAY, Black, (x+draww/2+entdoor-20 , y+toil+kitl-1+drawl-pt1-1, 2, pt1+1))
# kitcehn to drawing
pygame.draw.rect(DISPLAY, WHITE, (x+draww/2 , y+toil+kitl-1-1, roomdoor, pt1+1))
pygame.draw.rect(DISPLAY, Black, (x+draww/2 , y+toil+kitl-1, 2, pt1-1))
pygame.draw.rect(DISPLAY, Black, (x+draww/2+roomdoor , y+toil+kitl-1,2 , pt1-1))




while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()