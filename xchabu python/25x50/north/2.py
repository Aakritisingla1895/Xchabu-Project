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
wid = 25 * scale
entdoor = 4 * scale
roomdoor= 3 * scale
toidoor = 2.6 * scale
font = pygame.font.SysFont(None, 24)

#ots:-
otsl = len *  0.06
otsw = wid * 1
otsx = x + otsw / 2
otsy = y + otsl / 2-5
pygame.draw.rect(DISPLAY, (0, 0,0), (x,y, otsw,otsl), 2)
img = font.render('ots', True, Black)
DISPLAY.blit(img, (otsx, otsy))
# inner ots
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1,y+pt1, otsw-2*pt1,otsl-pt1), 2)

#kitchen:-
kitl = len * 0.22
kitw = wid * 0.4
kitx = x + kitw / 3
kity = y  +otsl+ kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+otsl -1, kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# innner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+otsl -1+pt2, kitw-pt1-pt2, kitl-pt2), 2)
#bedroom:-
bedl = len * 0.22
bedw = wid * 0.6
bedx = x +kitw+ bedw / 3
bedy = y + otsl + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+kitw, y +otsl-1, bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+kitw, y +otsl+pt2, bedw-pt1, bedl-pt2), 2)
# stairs:-
stal = len * 0.24   
staw = wid * 0.24
stax = x + staw / 2-10
stay = y +otsl+kitl + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+otsl+kitl-1, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# stair wall
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+otsl+kitl+pt2, staw-pt1+1, stal-pt2), 2)
# dining
dinl = len * 0.24
dinw = wid *0.44
dinx = x +staw+ dinw / 3
diny = y  +kitl+otsl + dinl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw, y +kitl+otsl-1, dinw, dinl), 2)
din = font.render('Dining', True, Black)
DISPLAY.blit(din, (dinx, diny))
# inner dining 
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw, y +kitl+otsl-1+pt2, dinw, dinl-pt2), 2)
#toilet:-
toil = len * 0.12
toiw = wid * 0.32
toix = x +staw+dinw + toiw / 2-10
toiy =y+otsl+kitl + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw+dinw , y+otsl+kitl-1, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw+dinw+pt2 , y+otsl+kitl+pt2, toiw-pt2-pt1, toil-pt2), 2)
#Dress2:-
drel = len * 0.12
drew = wid * 0.32
drex = x+dinw+staw + toiw / 2-10
drey =y+otsl+kitl +toil+ drel / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw+dinw , y+otsl+kitl+drel-1, toiw, drel), 2)
toilet = font.render('Dress', True, Black)
DISPLAY.blit(toilet, (drex, drey))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw+dinw+pt2 , y+otsl+kitl+toil-1+pt2, drew-pt2-pt1, drel-pt2), 2)
#parking:-
parl = len * 0.24
parw = wid * 0.48
parx = x  + parw / 2-10
pary =y+otsl+kitl +dinl+ parl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+otsl+kitl+dinl-1, parw, parl), 2)
toilet = font.render('Parking', True, Black)
DISPLAY.blit(toilet, (parx, pary))

# drawing room
drawl = len * 0.24
draww = wid * 0.52
drawx = x +parw + draww / 3
drawy = y + otsl + bedl+stal + drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+parw , y+otsl+bedl+stal-1, draww, drawl), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy)) 
# inner drawing
pygame.draw.rect(DISPLAY, (0, 0,0), (x+parw+pt1 , y+otsl+bedl+stal-1+pt2, draww-2*pt1, drawl-pt2-pt1), 2)
# doors
#utility
pygame.draw.rect(DISPLAY,WHITE, (x+kitw-roomdoor-8, y+otsl -2,roomdoor, pt1))
pygame.draw.rect(DISPLAY,Black, (x+kitw-roomdoor-8, y+otsl -2, 2, pt1-1))
pygame.draw.rect(DISPLAY,Black, (x+kitw-8, y+otsl -1, 2, pt1))
# kitchen
pygame.draw.rect(DISPLAY,WHITE, (x+kitw-roomdoor-13, y+otsl+kitl -2,roomdoor, pt1))
pygame.draw.rect(DISPLAY,Black, (x+kitw-13, y+otsl+kitl -1, 2, pt1-2))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+kitw, y +otsl+bedl-2, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+kitw, y +otsl+bedl-2, 2, pt1-1))
pygame.draw.rect(DISPLAY, Black, (x+kitw+roomdoor, y +otsl+bedl-1, 2, pt1-2))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+staw+dinw+pt1 , y+otsl+kitl-2, toidoor ,pt1))
pygame.draw.rect(DISPLAY, Black, (x+staw+dinw+pt1 , y+otsl+kitl-2, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+staw+dinw+pt1+toidoor , y+otsl+kitl-2, 2, pt1))
# toilet 2
pygame.draw.rect(DISPLAY, WHITE, (x+staw+dinw-2 , y+otsl+kitl+toil-1+toil-toidoor-2 ,pt1, toidoor))
pygame.draw.rect(DISPLAY, Black, (x+staw+dinw-1 , y+otsl+kitl+toil-1+toil-toidoor-2, pt1-1, 2))
# drawing
pygame.draw.rect(DISPLAY, WHITE, (x+parw +pt1, y+otsl+bedl+stal-2, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+parw +pt1, y+otsl+bedl+stal-2, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+parw +pt1+roomdoor, y+otsl+bedl+stal-1, 2, pt1-2))
# parking
pygame.draw.rect(DISPLAY, WHITE, (x+parw-entdoor-1, y+otsl+kitl+dinl-2, entdoor, pt1))
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()