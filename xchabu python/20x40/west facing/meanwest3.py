
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
#ots
otsl= len*0.1
otsw = wid*0.35
otsx=x +otsw/3
otsy=y +otsl/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y , otsw, otsl), 2)
foyer= font.render('OTS', True, Black)
DISPLAY.blit(foyer, (otsx, otsy)) 
#toilet:-
toil = len * 0.1
toiw = wid * 0.4
toix = x + otsw + toiw / 2
toiy =y + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+otsw-1 , y, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+otsw+pt1 , y+pt1, toiw-pt1, toil-pt1), 2)
#wash area:-
washl = len * 0.1
washw = wid * 0.25
washx = x +otsw+toiw+ washw / 3-10
washy = y + washl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+otsw+toiw-1, y , washw, washl), 2)
wash = font.render('Wash', True, Black)
DISPLAY.blit(wash, (washx, washy))
# inner wash area
pygame.draw.rect(DISPLAY, (0, 0,0), (x+otsw+toiw+pt2, y+pt1 , washw-pt2-pt1, washl-pt1), 2)
#bedroom:-
bedl = len * 0.275
bedw = wid * 0.57
bedx = x + bedw / 3
bedy = y +otsl + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y +otsl-1, bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y +otsl+pt2, bedw-pt1, bedl-pt2), 2)
#kitchen:-
kitl = len * 0.275
kitw = wid * 0.43
kitx = x+bedw + kitw / 3
kity = y+otsl + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1, y+otsl -1, kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw+pt2, y+otsl+pt2, kitw-pt2-pt1, kitl-pt2), 2)
# dining
dinl = len * 0.25
dinw = wid * 0.75
dinx = x + dinw / 2
diny = y+otsl+bedl  + dinl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+otsl+bedl-1 , dinw, dinl), 2)
din = font.render('Dining', True, Black)
DISPLAY.blit(din, (dinx, diny))
# inner dining
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+otsl+bedl+pt2 , dinw-pt1, dinl-pt2), 2)
#c.toilet:-
col = len * 0.15
cow = wid * 0.2
cox = x  + cow / 3-5
coy = y + otsl+bedl + col / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+otsl+bedl , cow, col), 2)
ctoilet = font.render('toilet', True, Black)
DISPLAY.blit(ctoilet, (cox, coy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+otsl+bedl , cow-pt2, col-pt2), 2)
#stairs:-
stal = len * 0.25
staw = wid * 0.25
stax = x+dinw + staw / 2-10
stay = y+otsl+bedl   + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x+dinw-1, y+otsl+bedl-1 , staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# inner stairs
pygame.draw.rect(DISPLAY, (0, 0,0), (x+dinw, y+otsl+bedl+pt2 , staw-pt1, stal-pt2), 2)
# parking
parl = len * 0.375
parw = wid * 0.5
parx = x  + parw / 2
pary = y + otsl + bedl + stal + parl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y + otsl + bedl + stal-1  , parw, parl), 2)
ent= font.render('Parking', True, Black)
DISPLAY.blit(ent, (parx, pary))
# inner entry
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y + otsl + bedl + stal-1 +pt1 , parw, parl-pt1), 2)
# foyer
foyl= len*0.125
foyw = wid*0.25
foyx=x +foyw/2+50
foyy=y + otsl + bedl + stal-1 +foyl/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+parw-foyw ,  y + otsl + bedl + stal-1, foyw, foyl), 2)
foyer= font.render('Foyer', True, Black)
DISPLAY.blit(foyer, (foyx, foyy))

# drawing room
drawl = len * 0.25
draww = wid * 0.5
drawx = x+parw  + draww / 3
drawy = y + otsl + bedl + stal +drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+parw -1, y+ otsl + bedl + stal-1 , draww, drawl), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# inner drawing
pygame.draw.rect(DISPLAY, (0, 0,0), (x+parw+pt1, y+ otsl + bedl + stal+pt2 , draww-pt1-pt1, drawl-pt2-pt1), 2)
# garden
garl = len * 0.125
garw = wid * 0.5
garx = x +parw+ garw / 3
gary = y+ otsl + bedl + stal+drawl + garl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+parw-1, y+ otsl + bedl + stal+drawl-1 , garw, garl), 2)
gal = font.render('garden', True, Black)
DISPLAY.blit(gal, (garx, gary))
# door
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+otsw-1+pt1+3 , y+toil-2, toidoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+otsw-1+pt1+3 , y+toil-2, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+otsw-1+pt1+3+toidoor , y+toil-2, 2, pt1))
# wash area
pygame.draw.rect(DISPLAY, WHITE, (x+otsw+toiw+pt1-2, y +washl-2, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+otsw+toiw+pt1-2, y +washl-2, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+otsw+toiw+pt1-2+roomdoor, y +washl-2, 2, pt1))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-roomdoor-1, y +otsl+bedl-2, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-roomdoor-1, y +otsl+bedl-2, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1, y +otsl+bedl-2, 2, pt1))
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+bedw+pt2+2, y+otsl -2+kitl, roomdoor-1, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw+pt2+2, y+otsl -2+kitl, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw+pt2+2+roomdoor-1, y+otsl -2+kitl, 2, pt1))
# toilet2
pygame.draw.rect(DISPLAY, WHITE, (x+cow -pt2-1, y+otsl+bedl+pt1-2 , pt1, toidoor))
pygame.draw.rect(DISPLAY, Black, (x+cow -pt2-1, y+otsl+bedl+pt1-2+toidoor , pt2, 2))
#  main entrance
pygame.draw.rect(DISPLAY, WHITE, (x+parw-entdoor-1 , y + otsl + bedl + stal-2  , entdoor, pt1+pt2))
pygame.draw.rect(DISPLAY, Black, (x+parw-entdoor-1 , y + otsl + bedl + stal-2  , 2, pt1+pt2-3))
# dining to drawing
pygame.draw.rect(DISPLAY, WHITE, (x+parw -1+pt1+10, y+ otsl + bedl + stal-2 , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+parw -1+pt1+10, y+ otsl + bedl + stal-2 , 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+parw -1+pt1+10+roomdoor, y+ otsl + bedl + stal-2 , 2, pt1))
# garden
pygame.draw.rect(DISPLAY, WHITE, (x+parw+pt1, y+ otsl + bedl + stal+dinl-pt1-2 , entdoor, pt1+pt2))
pygame.draw.rect(DISPLAY, Black, (x+parw+pt1, y+ otsl + bedl + stal+dinl-pt1-2 , 2, pt1+pt2-2))
pygame.draw.rect(DISPLAY, Black, (x+parw+pt1+entdoor, y+ otsl + bedl + stal+dinl-pt1-2 , 2, pt1+pt2-2))
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()