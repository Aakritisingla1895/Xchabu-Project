import pygame, sys
from pygame.locals import *



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
#bedroom:-
bedl = len * 0.375
bedw = wid * 0.5
bedx = x + bedw / 3
bedy = y + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y , bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, bedy))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+pt1 , bedw-pt1+1, bedl-pt1+1), 2)

#wash area:-
washl = len * 0.125
washw = wid * 0.5
washx = x +bedw+ washw / 3
washy = y + washl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1, y , washw, washl), 2)
wash = font.render('Wash', True, Black)
DISPLAY.blit(wash, (washx, washy))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1+pt2, y+pt1 , washw-pt2-pt1, washl-pt1+1), 2)

#kitchen:-
kitl = len * 0.25
kitw = wid * 0.5
kitx = x+bedw + kitw / 3
kity = y+washl + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1, y + washl-1, kitw, kitl+1), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1+pt2, y + washl+pt2, kitw-pt2-pt1, kitl-pt2), 2)
#toilet:-
toil = len * 0.15
toiw = wid * 0.3
toix = x + toiw / 2-10
toiy =y +bedl+ toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+bedl-1, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+bedl-1+pt2, toiw-pt1-pt2+1, toil-pt2), 2)
#stairs:-
stal = len * 0.2
staw = wid * 0.3
stax = x + staw / 2
stay = y+bedl+toil  + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+bedl+toil-2, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# inner stairs
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+bedl+toil-1+pt2, staw-pt1+1, stal-pt2-pt1), 2)
# drawing room
drawl = len * 0.35
draww = wid * 0.7
drawx = x+toiw+ draww / 3
drawy = y+bedl + drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw-1 , y+bedl-1, draww, drawl-1), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# inner drawing
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw-1 , y+bedl-1+pt2, draww-pt1, drawl-1-pt2-pt1), 2)
# garden
garl = len * 0.275
garw = wid * 1
garx = x + garw / 3
gary = y+bedl+drawl  + garl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y +bedl+drawl-3, garw-1, garl), 2)
gal = font.render('Garden', True, Black)
DISPLAY.blit(gal, (garx, gary))
# foyer
foyl= len*0.2
foyw = wid*0.4
foyx=x+garw-foyw +foyw/3
foyy=y +bedl+drawl-3 +foyl/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+garw-foyw , y +bedl+drawl-3 , foyw-1, foyl), 2)
foyer= font.render('Foyer', True, Black)
DISPLAY.blit(foyer, (foyx, foyy))  
# door
# bedroom1
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-roomdoor-1, y+bedl-1 , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1-roomdoor, y+bedl-1 , 2, pt1-2))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1, y+bedl-1 , 2, pt1-2))
# wash area
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-1+pt2, y+washl-1 , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1+pt2, y+washl-1 , 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1+pt2+roomdoor, y+washl-1 , 2, pt1-1))
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-1+pt2, y + washl-1+kitl, kitw-pt1-7, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1+pt2, y + washl-1+kitl, 2, pt1-2))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1+pt2+kitw-pt1-7, y + washl-1+kitl, 2, pt1))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+toiw-pt2-1 , y+bedl+pt2-1, pt1, toidoor))
pygame.draw.rect(DISPLAY, Black, (x+toiw-pt2-1 , y+bedl+pt2-1, pt1, 2))
pygame.draw.rect(DISPLAY, Black, (x+toiw-pt2 , y+bedl+pt2+toidoor-1, pt1-3, 2))
# foyer
pygame.draw.rect(DISPLAY, WHITE, (x+garw-entdoor-pt1-2 , y +bedl+drawl-4-pt1 , entdoor, pt1+pt2))
pygame.draw.rect(DISPLAY, 2, (x+garw-entdoor-pt1-2 , y +bedl+drawl-4-pt1 , 2, pt1+pt2-2))
pygame.draw.rect(DISPLAY, 2, (x+garw-pt1-2 , y +bedl+drawl-4-pt1 , 2, pt1+pt2-2))

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()