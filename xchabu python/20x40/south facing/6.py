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

#store:-
stol = len * 0.15
stow = wid * 0.4
stox = x-1 + stow / 3
stoy = y  + stol / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y, stow, stol), 2)
wash = font.render('Toilet', True, Black)
DISPLAY.blit(wash, (stox, stoy))
# inner store
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+pt1, stow-pt1-pt1+1, stol-pt1+1), 2)
#utility:-
util = len * 0.15
utiw = wid * 0.2
utix = x +stow+ utiw / 2-20
utiy = y + util / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+stow-1,y, utiw,util), 2)
img = font.render('OTS', True, Black)
DISPLAY.blit(img, (utix, utiy))

#toilet:-
toil = len * 0.15
toiw = wid * 0.4
toix = x +stow+utiw+ toiw / 2
toiy =y + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+stow+utiw-1.5, y, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+stow+utiw+pt1-1.5 , y+pt1, toiw-pt1-pt1+1.5, toil-pt1+1), 2)
#kitchen:-
kitl = len * 0.275
kitw = wid * 0.5
kitx = x + kitw / 3
kity = y+toil + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+toil-1 , kitw, kitl), 2)
Kitcehn = font.render('Bedroom', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+toil+pt2 , kitw-pt1+1, kitl-pt2-1), 2)
#dining
dinl = len * 0.275
dinw = wid * 0.5
dinx = x+kitw-1 + dinw / 3
diny = y +toiw + dinl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+kitw-1, y +toil-1, dinw-1, dinl), 2)
din = font.render('Bedroom', True, Black)
DISPLAY.blit(din, (dinx, diny))
# inner dining
pygame.draw.rect(DISPLAY, (0, 0,0), (x+kitw+pt2, y +toil+pt2, dinw-pt2-pt1, dinl-pt2-1), 2)
# drawing room
drawl = len * 0.3
draww = wid * 0.65
drawx = x+ draww / 3
drawy = y +toil+kitl+ drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+toil+kitl-1.5 , draww, drawl), 2)
draw= font.render('Living Room', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# inner hall
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+toil+kitl+pt2 , draww-pt1+1, drawl-pt2-1.5), 2)
#stairs:-
stal = len * 0.3
staw = wid * 0.35
stax = x+draww + staw / 2
stay = y+util+kitl+ stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-0.5, y+util+kitl-1.5, staw-0.5, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# inner stairs
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-0.5, y+util+kitl+pt2, staw-pt1, stal-pt2-1.5), 2)

# etnry
entl = len * 0.275
entw = wid * 0.46
entx = x + entw / 2
enty = y+toil+kitl+drawl + entl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+stol+kitl+stal-3, entw, entl), 2)
ent= font.render('Entry', True, Black)
DISPLAY.blit(ent, (entx, enty))
# inner entry
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+stol+kitl+stal-3+pt1, entw, entl-pt1), 2)
#bedroom:-
bedl = len * 0.275
bedw = wid * 0.54
bedx = x+entw+ bedw / 3
bedy = y + util+kitl+stal + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+entw-1, y+util+kitl+stal-3 , bedw-0.5, bedl), 2)
bed = font.render('Kitchen', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+entw-1+pt1, y+util+kitl+stal-3+pt2 , bedw-0.5-pt1-pt1, bedl-pt2-pt1), 2)
# doors
# store
pygame.draw.rect(DISPLAY, WHITE, (x+pt1, y+stol-1, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1, y+stol-1, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1+roomdoor, y+stol-1, 2, pt1-1))

# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+stow+utiw-1.5+pt1, y+toil-1, toidoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+stow+utiw-1.5+pt1, y+toil-1, 2, pt1-1))
pygame.draw.rect(DISPLAY, Black, (x+stow+utiw-1.5+pt1+toidoor, y+toil-1, 2, pt1-1))
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+pt1, y+toil-2+kitl , roomdoor,pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1, y+toil-2+kitl , 2,pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1+roomdoor, y+toil-2+kitl , 2,pt1))
# dining
pygame.draw.rect(DISPLAY, WHITE, (x+kitw-4+pt1, y +toil-2+dinl, roomdoor-7, pt1))
pygame.draw.rect(DISPLAY, Black, (x+kitw-4+pt1, y +toil-2+dinl, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+kitw-2+pt1+roomdoor-9, y +toil-2+dinl, 2, pt1))
# entry
pygame.draw.rect(DISPLAY, WHITE, (x+entw-entdoor , y+stol+kitl+stal-3, entdoor, pt1+3))
pygame.draw.rect(DISPLAY, Black, (x+entw-entdoor, y+stol+kitl+stal-3, 2, pt1+2))
pygame.draw.rect(DISPLAY, Black, (x+entw-1 , y+stol+kitl+stal-3, 2, pt1+3))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+entw+pt1, y+util+kitl+stal-3 , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+entw+pt1-1, y+util+kitl+stal-3 , 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+entw+pt1+roomdoor, y+util+kitl+stal-3 , 2, pt1-2))

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()