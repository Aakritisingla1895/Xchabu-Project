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
toil = len * 0.15
toiw = wid * 0.3
toix = x + toiw / 2-10
toiy =y + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y, toiw, toil), 2)
toilet = font.render('store', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+pt1, toiw-pt1+1-pt1, toil-pt1+1), 2)
#ots
otsl= len*0.15
otsw = wid*0.2
otsx=x+toiw +otsw/3-5
otsy=y +otsl/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw-1 , y , otsw, otsl), 2)
foyer= font.render('OTS', True, Black)
DISPLAY.blit(foyer, (otsx, otsy)) 
#wash area:-
washl = len * 0.15
washw = wid * 0.5
washx = x+toiw+otsw-1 + washw / 3
washy = y + washl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw+otsw-2, y , washw, washl), 2)
wash = font.render('Toilet', True, Black)
DISPLAY.blit(wash, (washx, washy))
# wash area
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw+otsw-1+pt1, y+pt1 , washw-pt1-pt1, washl-pt1+1), 2)
#kitchen:-
kitl = len * 0.275
kitw = wid * 0.45
kitx = x + kitw / 3
kity = y +washl+ kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+washl-1 , kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+washl-1+pt2 , kitw-pt1+1, kitl-pt2), 2)

#dining
dinl = len * 0.275
dinw = wid * 0.55
dinx = x+kitw + dinw / 3
diny = y+washl + dinl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+kitw-1, y+washl-1, dinw, dinl), 2)
din = font.render('Bedroom', True, Black)
DISPLAY.blit(din, (dinx, diny))
# inner dining
pygame.draw.rect(DISPLAY, (0, 0,0), (x+kitw-1+pt2, y+washl+pt2-1, dinw-pt2-pt1, dinl-pt2), 2)
# licing
drawl = len * 0.3
draww = wid * 0.6
drawx = x+ draww / 3
drawy = y+washl+kitl-1 + drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+washl+kitl-1.5 , draww+wid*0.4, drawl), 2)
draw= font.render('Hall', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# inner drawing
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+washl+kitl-1.5 +pt2, draww-pt1+1+wid*0.4, drawl-pt2), 2)

#stairs:-
stal = len * 0.175
staw = wid * 0.4
stax = x+draww + staw / 2
stay = y +kitl+washl+ stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x-1+draww, y+kitl+washl-2.5, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# stairs
pygame.draw.rect(DISPLAY, (0, 0,0), (x-1+draww, y+kitl+washl-1.5+pt2, staw-pt1, stal-pt2-1), 2)
#store:-
stol = len * 0.125
stow = wid * 0.25


#utility:-
util = len * 0.125
utiw = wid * 0.25
utix = x+draww+stow+ utiw / 2-50
utiy =  y+kitl+washl+stal + util / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww+staw-utiw-1.5, y+kitl+washl+stal-3.5, utiw+1.5,util), 2)
img = font.render('Store', True, Black)
DISPLAY.blit(img, (utix, utiy))
# inner utility
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww+staw-utiw-1.5+pt2, y+kitl+washl+stal-3.5+pt2, utiw+1.5-pt1-pt2,util-pt2), 2)
#parking:-
parl = len * 0.275
parw = wid * 0.45
parx = x  + parw / 2-10
pary =y+kitl+washl+drawl+ parl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+kitl+washl+drawl-3, parw, parl), 2)
toilet = font.render('garden', True, Black)
DISPLAY.blit(toilet, (parx, pary))
# inner parking
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+kitl+washl+drawl-3+pt1, parw, parl-pt1), 2)

# foyer
foyl= len*0.125
foyw = wid*0.35
foyx=x+parw-foyw +toiw/3-10
foyy=y+washl+kitl+draww +toil/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x +parw-foyw, y+toil+kitl+drawl-3 , foyw, foyl), 2)
foyer= font.render('Foyer', True, Black)
DISPLAY.blit(foyer, (foyx, foyy))  

#bedroom:-
bedl = len * 0.275
bedw = wid * 0.55
bedx = x+parw + bedw / 3
bedy = y +washl+kitl+drawl + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+parw-1, y+washl+kitl+drawl-3.5, bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx,  y+bedy))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+parw+pt1, y+washl+kitl+drawl-3+pt2 , bedw-pt1-pt1, bedl-pt2-pt1), 2)
# doors
# parking
pygame.draw.rect(DISPLAY, WHITE, (x+parw-entdoor, y+kitl+washl+drawl-3, entdoor, pt1+pt2))
pygame.draw.rect(DISPLAY, Black, (x+parw-entdoor, y+kitl+washl+drawl-3, 2, pt1+pt2-4))
pygame.draw.rect(DISPLAY, Black, (x+parw-1, y+kitl+washl+drawl-3, 2, pt1+pt2))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+parw+pt1, y+washl+kitl+drawl-4 , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+parw+pt1, y+washl+kitl+drawl-3 , 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+parw+pt1+roomdoor-1, y+washl+kitl+drawl-3 , 2, pt1-2))
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+pt1, y+washl-2 +kitl, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1, y+washl-2 +kitl, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1+roomdoor, y+washl-2 +kitl, 2, pt1-2))
# dining
pygame.draw.rect(DISPLAY, WHITE, (x+kitw-1+pt2, y+washl-2+dinl, roomdoor-6, pt1))
pygame.draw.rect(DISPLAY, Black, (x+kitw-1+pt2, y+washl-2+dinl, 2, pt1-2))
pygame.draw.rect(DISPLAY, Black, (x+kitw-1+pt2+roomdoor-6, y+washl-2+dinl, 2, pt1-2))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+toiw-toidoor-pt1 , y+toil-1, toidoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+toiw-toidoor-pt1 , y+toil-1, 2, pt1-2))
pygame.draw.rect(DISPLAY, Black, (x+toiw-1-pt1 , y+toil-1, 2, pt1-2))
# wash
pygame.draw.rect(DISPLAY, WHITE, (x+toiw+otsw+pt1, y+washl-1 , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+toiw+otsw+pt1, y+washl-1 , 2, pt1-2))
pygame.draw.rect(DISPLAY, Black, (x+toiw+otsw+pt1+roomdoor, y+washl-1 , 2, pt1-2))

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()