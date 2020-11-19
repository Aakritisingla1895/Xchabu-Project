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
len = 40 * 15
wid = 20 * 15
entdoor = 4 * 15
roomdoor= 3 * 15
toidoor = 2.6 * 15
font = pygame.font.SysFont(None, 24)
#toilet:-
toil = len * 0.125
toiw = wid * 0.35
toix = x + toiw / 2-20
toiy =y + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+pt1, toiw-pt1-pt1, toil-pt1), 2)
#ots
otsl= len * 0.125
otsw = wid * 0.4
otsx=x+toiw +otsw/3
otsy=y +otsl/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw-1 , y, otsw, otsl), 2)
foyer= font.render('OTS', True, Black)
DISPLAY.blit(foyer, (otsx, otsy)) 
#store:-
stol = len * 0.125
stow = wid * 0.25
stox = x+toiw+otsw + stow / 3-10
stoy = y  + stol / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw+otsw-1 , y, stow, stol), 2)
wash = font.render('store', True, Black)
DISPLAY.blit(wash, (stox, stoy))
# inner store
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw+otsw-1+pt1 , y+pt1, stow-2*pt1, stol-pt1), 2)
#bedroom:-
bedl = len * 0.25
bedw = wid * 0.55
bedx = x + bedw / 3
bedy = y +toil + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y +toil-1, bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y +toil-1+pt2, bedw-pt1, bedl-pt2), 2)
#kitchen:-
kitl = len * 0.25
kitw = wid * 0.45
kitx = x+bedw + kitw / 3
kity = y+toil + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1, y+toil-1 , kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1+pt2, y+toil-1+pt2 , kitw-pt2-pt1, kitl-pt2), 2)
#stairs:-
stal = len * 0.30
staw = wid * 0.35
stax = x + staw / 2
stay = y+toil+bedl  + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+toil+bedl, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# inner stairs
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+toil+bedl+pt2, staw-pt1+1, stal-pt2), 2)
# dining
dinl = len * 0.30
dinw = wid * 0.65
dinx = x+staw + dinw / 3
diny = y + bedl+otsl + dinl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw, y+bedl+otsl, dinw, dinl), 2)
din = font.render('Dining', True, Black)
DISPLAY.blit(din, (dinx, diny))
# inner dining
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw, y+bedl+otsl+pt2, dinw-pt1, dinl-pt2), 2)
# drawing room
drawl = len * 0.325
draww = wid * 0.55
drawx = x  + draww / 3
drawy = y +toil+bedl+dinl + drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+toil+bedl+dinl-1 , draww, drawl), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy)) 
# inner drawing
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+toil+bedl+dinl+pt2 , draww-pt1-pt1, drawl-pt2-pt1), 2)
# entry
entl = len * 0.325
entw = wid * 0.45
entx = x ++draww+ entw / 2
enty = y +toil+bedl+dinl + entl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x +draww-1, y + toil + bedl + dinl-1 , entw, entl), 2)
ent= font.render('Entry', True, Black)
DISPLAY.blit(ent, (entx, enty))
pygame.draw.rect(DISPLAY, (0, 0,0), (x +draww-1, y + toil + bedl + dinl-1+pt1 , entw, entl-pt1), 2)
# doors
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+pt1, y+toil-2,toidoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1 , y+toil-2,2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1 +toidoor, y+toil-2,2, pt1))
# store
pygame.draw.rect(DISPLAY, WHITE, (x+toiw+otsw+pt1 , y+stol-2, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+toiw+otsw+pt1 , y+stol-2, 2, pt1-1))
pygame.draw.rect(DISPLAY, Black, (x+toiw+otsw+pt1+roomdoor , y+stol-1, 2, pt1-1))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-roomdoor-13, y +toil-2+bedl,roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-13, y +toil-2+bedl, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw, y +toil-2+bedl, 2, pt1))
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+bedw+pt1, y+toil-2+kitl , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw+pt1, y+toil-2+kitl , 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw+pt1+roomdoor, y+toil-2+kitl , 2, pt1))
# drawing
pygame.draw.rect(DISPLAY, WHITE, (x+draww-60 , y+toil+bedl+dinl-2 , roomdoor , pt1))
pygame.draw.rect(DISPLAY, Black, (x+draww-60 , y+toil+bedl+dinl-2 , 2 , pt1))
pygame.draw.rect(DISPLAY, Black, (x+draww-pt1-pt2 , y+toil+bedl+dinl-1 , 2 , pt1-1))
# entry
pygame.draw.rect(DISPLAY, WHITE, (x +draww+1, y + toil + bedl + dinl-2 , entdoor, pt1+5))
pygame.draw.rect(DISPLAY, Black, (x +draww+1+entdoor, y + toil + bedl + dinl-1 , 2, pt1+2))
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()