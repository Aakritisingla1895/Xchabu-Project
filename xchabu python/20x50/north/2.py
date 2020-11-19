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
scale = 15
pt1 = 0.7 * scale
pt2 = 0.4 * scale
len = 50 * scale
wid = 20 * scale
entdoor = 4 * scale
roomdoor= 3 * scale
toidoor = 2.6 * scale
font = pygame.font.SysFont(None, 24)
#ots
otsl= len*0.1   
otsw = wid*0.52
otsx=x +otsw/3
otsy=y +otsl/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y , otsw, otsl), 2)
foyer= font.render('OTS', True, Black)
DISPLAY.blit(foyer, (otsx, otsy))
#toilet:-
toil = len * 0.1
toiw = wid * 0.48
toix = x +otsw+ toiw / 2
toiy =y + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+otsw-1 , y, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+otsw-1+pt1 , y+pt1, toiw-2*pt1, toil-pt1), 2)
#kitchen:-
kitl = len * 0.2
kitw = wid * 0.40
kitx = x + kitw / 3
kity = y+otsl + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+otsl-1 , kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+otsl+pt1 , kitw-pt1, kitl-pt1), 2)
#bedroom:-
bedl = len * 0.2
bedw = wid * 0.60
bedx = x +kitw+ bedw / 3
bedy = y +otsl + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+kitw-1, y +otsl-1, bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# bedroom inner
pygame.draw.rect(DISPLAY, (0, 0,0), (x+kitw+pt2, y +otsl+pt2, bedw-pt2-pt1, bedl-pt2), 2)
#store:-
stol = len * 0.14
stow = wid * 0.25
stox = x + stow / 3
stoy = y+otsl+kitl + stol / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+otsl+kitl-1, stow, stol), 2)
wash = font.render('store', True, Black)
DISPLAY.blit(wash, (stox, stoy))
# inner store
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+otsl+kitl+pt2, stow-pt1, stol-pt2), 2)
#c.toilet:-
col = len * 0.14
cow = wid * 0.25
cox = x  + cow / 3
coy = y+otsl+kitl+stol  + col / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+otsl+kitl+stol-1, cow, col), 2)
ctoilet = font.render('toilet', True, Black)
DISPLAY.blit(ctoilet, (cox, coy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+otsl+kitl+stol+pt2 , cow-pt1, col-pt2), 2)
## dining
dinl = len * 0.28
dinw = wid * 0.55
dinx = x+cow + dinw / 3
diny = y +otsl+kitl + dinl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+cow-1, y+otsl+kitl-1 , dinw, dinl), 2)
din = font.render('Dining', True, Black)
DISPLAY.blit(din, (dinx, diny))
# inner dining
pygame.draw.rect(DISPLAY, (0, 0,0), (x+cow-1+pt2, y+otsl+kitl-1 +pt2, dinw-pt2, dinl-pt2), 2)
#stairs:-
stal = len * 0.28
staw = wid * 0.2
stax = x +cow+dinw+ staw / 2-20
stay = y +otsl+kitl + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x+cow+dinw-1, y+otsl+kitl-1, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# inner stairs
pygame.draw.rect(DISPLAY, (0, 0,0), (x+cow+dinw, y+otsl+kitl+pt2, staw-pt1, stal-pt2-pt2), 2)
# drawing room
drawl = len * 0.26
draww = wid * 0.5
drawx = x + draww / 3
drawy = y+otsl+bedl+dinl + drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x-1 , y+otsl+bedl+dinl -1, draww, drawl), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# inner drawing
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+otsl+bedl+dinl+pt2 , draww-2*pt1, drawl-pt2-pt1), 2)
# entry
entl = len * 0.26
entw = wid * 0.5
entx = x + draww + entw / 2
enty = y+otsl+bedl+dinl + entl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww -1, y+otsl+bedl+dinl-1 , entw, entl), 2)
ent= font.render('Entry', True, Black)
DISPLAY.blit(ent, (entx, enty))
# door
# entry
pygame.draw.rect(DISPLAY, WHITE, (x+draww -8+pt1, y+otsl+bedl+dinl-3 , entdoor, pt1))
# 2nd toilet
pygame.draw.rect(DISPLAY, WHITE, (x+cow-2 , y+otsl+kitl+stol-1+col-40, pt1,toidoor))
pygame.draw.rect(DISPLAY, Black, (x+cow-2 , y+otsl+kitl+stol-1+col-40, pt1-1,2))
# store
pygame.draw.rect(DISPLAY, WHITE, (x+stow-roomdoor-2 , y+otsl+kitl-2, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+stow-roomdoor-3 , y+otsl+kitl-1, 2, pt1-1))
pygame.draw.rect(DISPLAY, Black, (x+stow-2 , y+otsl+kitl-1, 2, pt1-1))
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+kitw-47, y+otsl- 1, roomdoor, 2*pt1))
pygame.draw.rect(DISPLAY, Black, (x+kitw-47, y+otsl- 1, 2, pt1+2))
pygame.draw.rect(DISPLAY, Black, (x+kitw-47+roomdoor, y+otsl- 1, 2, pt1+2))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+otsw+pt1 , y+toil-2, toidoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+otsw+pt1 , y+toil-2, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+otsw+pt1+toidoor , y+toil-2, 2, pt1))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+kitw-1+pt1, y +otsl-1+bedl-2, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+kitw-1+pt1, y +otsl-1+bedl-1,2 , pt1-1))
pygame.draw.rect(DISPLAY, Black, (x+kitw-1+pt1+roomdoor, y +otsl-1+bedl-1,2 , pt1-1))
# kitchen 2nd
pygame.draw.rect(DISPLAY, WHITE, (x+kitw-roomdoor+pt2, y+otsl-1+kitl-1 , 37, pt1))
pygame.draw.rect(DISPLAY, Black, (x+kitw-roomdoor+pt2-1, y+otsl-1+kitl-1 , 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+kitw-roomdoor+pt2+37, y+otsl-1+kitl-1 , 2, pt1-1))
# drawing
pygame.draw.rect(DISPLAY,WHITE, (x-1+draww-roomdoor-10 , y+otsl+bedl+dinl -2, roomdoor, pt1))
pygame.draw.rect(DISPLAY,Black, (x-1+draww-roomdoor-10 , y+otsl+bedl+dinl -2, 2, pt1))
pygame.draw.rect(DISPLAY,Black, (x-1+draww-11 , y+otsl+bedl+dinl -2, 2, pt1))


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()