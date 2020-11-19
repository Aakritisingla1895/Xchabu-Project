import pygame, sys
from pygame.locals import *
from pygame import *

pygame.init()
DISPLAY = pygame.display.set_mode((1200,800),0,32)
WHITE = (255,255,255)
Black = (0,0,0)
blue = (0,0,255)
DISPLAY.fill(WHITE)
x = 10
y = 10
scale = 15
pt1 = 0.7 * scale
pt2 = 0.4 * scale
len = 50 * scale
wid = 20 * scale
entdoor = 4 * scale
roomdoor= 3 * scale
toidoor = 2.6 * scale
font = pygame.font.SysFont(None, 24)
# gallery
gall = len * 0.08
galw = wid * 1
galx = x + galw / 3
galy = y  + gall / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y , galw, gall), 2)
gal = font.render('Gallery', True, Black)
DISPLAY.blit(gal, (galx, galy))
#bedroom:-
bedl = len * 0.24
bedw = wid * 0.6
bedx = x + bedw / 3
bedy = y + gall + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+gall-1 , bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+gall-1 +pt1, bedw-pt1+1, bedl-pt1), 2)
#toilet:-
toil = len * 0.1
toiw = wid * 0.4
toix = x + bedw + toiw / 2
toiy =y +gall+ toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1 , y+gall-1, toiw, toil), 2)
toilet = font.render('Dress', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1+pt2 , y+gall-1+pt1, toiw-pt2-pt1, toil-pt1), 2)
#c.toilet:-
drel = len * 0.14
drew = wid * 0.4
drex = x + bedw + drew / 3
drey = y + toil+gall + drel / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1 , y+gall+toil-1 , drew, drel), 2)
ctoilet = font.render('Toilet', True, Black)
DISPLAY.blit(ctoilet, (drex, drey))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1+pt2 , y+gall+toil-1+pt2 , drew-pt2-pt1, drel-pt2), 2)

# stairs:-
stal = len * 0.24
staw = wid * 0.12
stax = x + staw / 2
stay = y  +gall+bedl+ stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+gall+bedl-1, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# wall stairs
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+gall+bedl+pt2, staw-pt1, stal-pt2-1), 2)
# dining
dinl = len * 0.24
dinw = wid * 0.88
dinx = x+staw + dinw / 3
diny = y + bedl+gall + dinl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw-1, y+bedl+gall-1 , dinw, dinl), 2)
din = font.render('Dining', True, Black)
DISPLAY.blit(din, (dinx, diny))
# dinning walls
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw-1, y+bedl+gall-1+pt2 , dinw-pt1, dinl-pt2), 2)
#kitchen:-
kitl = len * 0.2
kitw = wid * 0.48
kitx = x + kitw / 3
kity = y+gall+bedl+stal + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+gall+bedl+stal , kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+gall+bedl+stal+pt2 , kitw-2*pt1, kitl-pt2-pt1), 2)
#Garden:-
garl = len * 0.14
garw = wid * 0.48
garx = x + garw / 3
gary = y+gall+bedl+stal+kitl + garl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+gall+bedl+stal+kitl-1 , garw, garl), 2)
Kitcehn = font.render('Garden', True, Black)
DISPLAY.blit(Kitcehn, (garx, gary))
#Entry:dre
entl = len * 0.34
entw = wid * 0.52
entx = x+kitw  + entw / 2-10
enty =y+gall+kitl +dinl+ entl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+kitw-1, y+gall+bedl+dinl-1, entw, entl), 2)
toilet = font.render('Entry', True, Black)
DISPLAY.blit(toilet, (entx, enty))
# inner
pygame.draw.rect(DISPLAY, (0, 0,0), (x+kitw-1, y+gall+bedl+dinl-1+pt1, entw, entl-pt1), 2)
# door 
# gallery
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-roomdoor-1, y+gall-1 , roomdoor, pt1+pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-roomdoor-1, y+gall-1 , 2, pt1+2))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-roomdoor-1, y+gall-1+bedl-2, roomdoor, pt1+pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-roomdoor-1, y+gall-1+bedl-2, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1, y+gall-1+bedl-2, 2, pt1))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-2 , y+gall-1+pt1, pt1, toidoor))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1 , y+gall-1+pt1,pt1 -1, 2))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1 , y+gall-1+pt1+toidoor, pt1-2, 2))
# c.toilet
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-5+pt1 , y+gall+toil-3 , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-5+pt1 , y+gall+toil-2 , 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-5+pt1+roomdoor , y+gall+toil-2 , 2, pt1-1))
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+kitw-roomdoor-pt1-1, y+gall+bedl+stal-2 ,roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+kitw-roomdoor-pt1-1, y+gall+bedl+stal-2 , 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+kitw-pt1-1, y+gall+bedl+stal-2 , 2, pt1))
# parking
pygame.draw.rect(DISPLAY, WHITE, (x+kitw+1, y+gall+bedl+dinl-2, entdoor, pt1+pt1))
pygame.draw.rect(DISPLAY,Black , (x+kitw+entdoor, y+gall+bedl+dinl-2, 2, pt1+2))

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()