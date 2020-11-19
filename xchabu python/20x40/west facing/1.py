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
bedl = len * 0.28
bedw = wid * 0.5
bedx = x + bedw / 3
bedy = y  + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y , bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# iner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+pt1 , bedw-pt1, bedl-pt1), 2)
# ots
otsl= len*0.08
otsw = wid*0.5
otsx=x +bedw+otsw/3
otsy=y +otsl/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1 , y , otsw, otsl), 2)
foyer= font.render('OTS', True, Black)
DISPLAY.blit(foyer, (otsx, otsy)) 
#kitchen:-
kitl = len * 0.2
kitw = wid * 0.5
kitx = x +bedw+ kitw / 3
kity = y+otsl + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1, y+otsl-1 , kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1+pt1, y+otsl-1+pt1 , kitw-2*pt1, kitl-pt1-pt2), 2)
#toilet:-
toil = len * 0.125
toiw = wid * 0.35
toix = x  + toiw / 2-15
toiy =y+bedl + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+bedl-1, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+bedl-1+pt2, toiw-pt1, toil-pt2), 2)
# ots
otsl= len*0.125
otsw = wid*0.15
otsx=x+otsw/3
otsy=y+bedl+toil +otsl/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+bedl+toil , otsw, otsl), 2)
foyer= font.render('OTS', True, Black)
DISPLAY.blit(foyer, (otsx, otsy)) 
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+bedl+toil+pt2-1 , otsw-pt1+1, otsl-pt2), 2)
# c.toilet
col = len * 0.125
cow = wid * 0.2
cox = x+otsl + cow / 3-35
coy = y+bedl+toil  + col / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+otsw , y +bedl+toil-1, cow, col), 2)
ctoilet = font.render('toilet', True, Black)
DISPLAY.blit(ctoilet, (cox, coy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+otsw+pt2 , y +bedl+toil+pt2, cow-pt2, col-pt2), 2)
# foyer
foyl= len*0.1
foyw = wid*0.35
foyx=x +toiw/3
foyy=y +bedl+toil+col+toil/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+bedl+toil+col-1 , foyw, foyl), 2)
foyer= font.render('Foyer', True, Black)
DISPLAY.blit(foyer, (foyx, foyy))  
# inner
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+bedl+toil+col-1+pt2 , foyw-pt1, foyl-pt2), 2)
# dining
dinl = len * 0.35
dinw = wid * 0.65
dinx = x +foyw+ dinw / 3
diny = y + bedl + dinl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+foyw-1, y+bedl-1 , dinw, dinl), 2)
din = font.render('Dining', True, Black)
DISPLAY.blit(din, (dinx, diny))
# innner dining
pygame.draw.rect(DISPLAY, (0, 0,0), (x+foyw-1+pt2, y+bedl-1 , dinw-pt1-pt2, dinl), 2)
#stairs:-
stal = len * 0.287
staw = wid * 0.4
stax = x + staw / 2
stay = y +bedl+dinl + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+bedl+dinl-1, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# inner stairs
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+bedl+dinl-1+pt2, staw-pt1, stal-pt2-pt1), 2)
# drawing room
drawl = len * 0.287
draww = wid * 0.6
drawx = x +stal+ draww / 3-30
drawy = y +dinl + bedl + drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw-1 , y +dinl+bedl-1, draww, drawl), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# inner drawing
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw-1, y +dinl+bedl-1+pt2, draww-pt1, drawl-pt2-pt1), 2)
# doors
#bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-37, y +bedl-2, 36, pt1))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+toil-11, y+bedl-2, toidoor+0.5, pt1))
pygame.draw.rect(DISPLAY, Black, (x+toil-11, y+bedl-2,2, pt1))
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-1+pt1+2, y+otsl+kitl-36, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1+pt1+2+roomdoor, y+otsl+kitl-36, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1+pt1+2, y+otsl+kitl-36, 2, pt1))
# co.toilet
pygame.draw.rect(DISPLAY, WHITE, (x+otsw+cow-2 , y +bedl+toil+pt2, pt1, toidoor))
pygame.draw.rect(DISPLAY, Black, (x+otsw+cow-2 , y +bedl+toil+pt2, pt1, 2))
pygame.draw.rect(DISPLAY, Black, (x+otsw+cow-2 , y +bedl+toil+pt2+toidoor, pt1, 2))
# foyer
pygame.draw.rect(DISPLAY, WHITE, (x+foyw -2, y+bedl+toil+col-1+pt2 , pt1, foyl-pt2-1))
pygame.draw.rect(DISPLAY, Black, (x+foyw -2, y+bedl+toil+col-1+pt2 , pt1, 2))
# drawing
pygame.draw.rect(DISPLAY, WHITE, (x+staw-1 , y +dinl+bedl-2, entdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+staw-1, y +dinl+bedl-2, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+staw-1+entdoor , y +dinl+bedl-2, 2, pt1-1))



while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
