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
#bedroom:-
bedl = len * 0.2
bedw = wid * 0.60
bedx = x + bedw / 3
bedy = y + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y , bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+pt1 , bedw-pt1+1, bedl-pt1), 2)
#wash area:-
washl = len * 0.08
washw = wid * 0.40
washx = x +bedw+ washw / 3
washy = y  + washl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1, y , washw, washl), 2)
wash = font.render('Wash', True, Black)
DISPLAY.blit(wash, (washx, washy))
# inner wash
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw+pt2, y+pt1 , washw-pt2-pt1+1, washl-pt1), 2)
# ots
otsl= len*0.08
otsw = wid*0.14
otsx=x +otsw/3
otsy=y + bedl +otsl/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+bedl-1 , otsw, otsl), 2)
foyer= font.render('OTS', True, Black)
DISPLAY.blit(foyer, (otsx, otsy)) 
# inner ots
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+bedl+pt2 , otsw-pt1+1, otsl-pt2), 2)
# toilet:-
toil = len * 0.08
toiw = wid * 0.26
toix = x +otsw + toiw / 2-10
toiy =y + bedl + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+otsw-1 , y+bedl-1, toiw+1, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+otsw+pt2 , y+bedl+pt2, toiw-pt2+1, toil-pt2), 2)
# Empty:-
emtl = len * 0.08
emtw = wid * 0.12
emtx = x +otsw + emtw / 2-10
emty =y + bedl + emtl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+otsw+toiw-1 , y+bedl-1, emtw, emtl), 2)
toilet = font.render('', True, Black)
DISPLAY.blit(toilet, (emtx, emty))
# inner empty
pygame.draw.rect(DISPLAY, (0, 0,0), (x+otsw+toiw-1+pt2, y+bedl-1+pt2, emtw-pt2, emtl-pt2), 2)
#kitchen:-
kitl = len * 0.2
kitw = wid * 0.40
kitx = x+bedw + kitw / 3
kity = y+washl + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1, y+washl-1, kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1+pt2, y+washl -1+pt2, kitw-pt2-pt1, kitl-pt2), 2)
#stairs:-
stal = len * 0.12   
staw = wid * 0.52
stax = x + staw / 2
stay = y+bedl+toil  + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+bedl+toil-1, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# inner stair
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+bedl+toil-1+pt2, staw-pt1, stal-pt2), 2)
# dining
dinl = len * 0.2
dinw = wid * 0.48
dinx = x+staw + dinw / 3
diny = y+bedl+toil+ dinl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw-1, y+bedl+toil-1, dinw, dinl), 2)
din = font.render('Dining', True, Black)
DISPLAY.blit(din, (dinx, diny))
# inner dining
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw-1+pt2, y+bedl+toil-1+pt2, dinw-pt2-pt1, dinl-pt2), 2)
# drawing room
drawl = len * 0.24
draww = wid * 0.68
drawx = x + draww / 3
drawy = y+stal+toil  + bedl + drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+stal+toil+bedl-1, draww, drawl), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# inner drawing
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+stal+toil+bedl+pt2, draww-pt1, drawl-pt2-pt1+2), 2)
# foyer
foyl= len*0.16
foyw = wid*0.32
foyx=x + draww+toiw/3
foyy=y+kitl+dinl+washl +toil/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-1 , y+kitl+dinl+washl-1 , foyw, foyl), 2)
foyer= font.render('Foyer', True, Black)
DISPLAY.blit(foyer, (foyx, foyy))  
# door
# dining coorectiong
pygame.draw.rect(DISPLAY, WHITE, (x+staw+1, y+bedl+toil-1+pt2+stal-pt2-1, staw/3, stal/1.55))
# dining
pygame.draw.rect(DISPLAY, WHITE, (x+staw-1, y+bedl+toil-1+dinl/1.5, dinw/2.5, dinl/2.8-1))
# foyer
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-1 , y+kitl+dinl+washl-2 , foyw, foyl+1), 2)
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-1+pt1, y+washl-1+kitl-1, kitw-2*pt1-1, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1+pt1, y+washl-1+kitl-1, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1+pt1+kitw-2*pt1-1, y+washl-1+kitl-1, 2, pt1))
# wash area
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-1+pt1, y+washl-2 , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1+pt1, y+washl-2 , 2, pt1-2))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1+pt1+roomdoor, y+washl-2 , 2, pt1-2))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+otsw+toiw+pt2 , y+bedl-2, emtw+23, toil))
pygame.draw.rect(DISPLAY, Black, (x+otsw+toiw-2+pt2 , y+bedl-2,2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+otsw+toiw-2+pt2+3 , y+bedl-2+toil, 2, pt1-2))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+otsw+toiw-2 , y+bedl-2+pt1, pt1, toidoor))
pygame.draw.rect(DISPLAY, Black, (x+otsw+toiw-1 , y+bedl-2+pt1, pt1-3, 2))
pygame.draw.rect(DISPLAY, Black, (x+otsw+toiw-1, y+bedl-2+pt1+toidoor, pt1-2, 2))
# entry to bed room
pygame.draw.rect(DISPLAY, WHITE, (x+otsw-1+toiw+pt1 , y+bedl-1+toil-1, toiw+1/4, stal))
# correction
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1, y+washl-2+kitl, pt1-2, 2))
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()