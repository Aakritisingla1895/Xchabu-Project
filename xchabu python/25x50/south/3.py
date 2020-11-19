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
wid = 25 * scale
entdoor = 4 * scale
roomdoor= 3 * scale
toidoor = 2.6 * scale
font = pygame.font.SysFont(None, 24)
#toilet:-
toil = len *  0.08
toiw = wid * 0.24
toix = x  + toiw / 2-10
toiy =y + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+pt1, toiw-2*pt1, toil-pt1), 2)
# ots
otsl= len*0.08
otsw = wid*0.38
otsx=x +toiw+ otsw/3
otsy=y  +otsl/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw , y , otsw, otsl), 2)
foyer= font.render('OTS', True, Black)
DISPLAY.blit(foyer, (otsx, otsy)) 
#c.toilet:-
col = len * 0.08
cow = wid * 0.34
cox = x +toiw+otsw + cow / 3
coy = y + col / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw+otsw , y , cow, col), 2)
ctoilet = font.render('toilet', True, Black)
DISPLAY.blit(ctoilet, (cox, coy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+toiw+otsw+pt1 , y+pt1 , cow-pt1-pt1, col-pt1+1), 2)
#bedroom:-
bedl = len * 0.28
bedw = wid * 0.48
bedx = x + bedw / 3
bedy = y +otsl + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+otsl-1 , bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+otsl+pt2 , bedw-pt1+1, bedl-pt2), 2)
#bedroom2:-
bedl = len * 0.28
bedw = wid * 0.48
bedx = x+bedw + bedw / 3
bedy = y +otsl + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1, y+otsl-1 , bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw+pt1, y+otsl+pt2 , bedw-2*pt1, bedl-pt2), 2)

#stairs:-
stal = len * 0.24
staw = wid * 0.16
stax = x + staw / 2-10
stay = y +bedl+otsl + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x,y+bedl+otsl-1, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# inner stairs
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+bedl+otsl+pt2, staw-pt1, stal-pt2), 2)
# dining
col = len * 0.08
cow = wid * 0.2
dinl = len * 0.24
dinw = wid * 0.60+cow
dinx = x+staw + dinw / 3
diny = y + bedl+otsl + dinl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw-1, y+bedl+otsl-1 , dinw, dinl), 2)
din = font.render('Dining', True, Black)
DISPLAY.blit(din, (dinx, diny))
# inner dining
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw,y+bedl+otsl-1+pt2 , dinw-pt1, dinl-pt2), 2)
#c.toilet:-
col = len * 0.08
cow = wid * 0.2
cox = x +staw+dinw + cow / 3-10
coy = y +toil+bedl + col / 2

##wash area:-
washl = len * 0.08
washw = wid * 0.2
washx = x+staw+dinw + washw / 3-10
washy = y +otsl+bedl+ col + washl / 2

# drawing room
drawl = len * 0.2
draww = wid * 0.48
drawx = x  + draww / 3
drawy = y + otsl+stal+ bedl + drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+ otsl+stal+ bedl-1, draww, drawl), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# drawing inner
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+ otsl+stal+ bedl-1+pt2, draww-pt1-pt1, drawl-pt2-pt1), 2)
#kitchen:-
kitl = len * 0.2
kitw = wid * 0.48
kitx = x +draww+ kitw / 3
kity = y+otsl+bedl+toil+washl + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-1, y+otsl+bedl+toil+washl-1 , kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-1+pt2, y+otsl+bedl+toil+washl-1+pt2 , kitw-pt2-pt1, kitl-pt2-pt1), 2)

# garden
garl = len * 0.20
garw = wid * 0.48
garx = x + garw / 3
gary = y +otsl+bedl+stal+drawl + garl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+otsl+bedl+stal+drawl-1 , garw, garl), 2)
gal = font.render('Garden', True, Black)
DISPLAY.blit(gal, (garx, gary))
#parking:-
parl = len * 0.28
parw = wid * 0.48
parx = x +draww + parw / 2-10
pary =y+otsl+bedl+toil+washl +kitl+parl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-1, y+otsl+bedl+toil+washl+kitl-1, parw, parl), 2)
toilet = font.render('Parking', True, Black)
DISPLAY.blit(toilet, (parx, pary))
# door
# kitchen correction
pygame.draw.rect(DISPLAY, WHITE, (x+draww+2, y+otsl+bedl+toil+washl , kitw-2, kitl-2))
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-1, y+otsl+bedl+toil+washl-1 , kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)

DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-1, y+otsl+bedl+toil+washl-1+pt2 , kitw-pt1, kitl-pt2-pt1), 2)
pygame.draw.rect(DISPLAY, WHITE, (x+draww-1, y+otsl+bedl+toil+washl-1 , kitw-1-pt1, pt1))
pygame.draw.rect(DISPLAY, Black, (x+draww+kitw-2-pt1, y+otsl+bedl+toil+washl-1 , 2, pt1))
# drawing
pygame.draw.rect(DISPLAY, WHITE, (x +draww-entdoor-20, y+ otsl+stal+ bedl+drawl-pt1-2,entdoor , pt1+pt1))
pygame.draw.rect(DISPLAY, Black, (x +draww-entdoor-20, y+ otsl+stal+ bedl+drawl-pt1-2, 2, pt1+2))
pygame.draw.rect(DISPLAY, Black, (x +draww-20, y+ otsl+stal+ bedl+drawl-pt1-2, 2, pt1+2))
# drawing to dining
pygame.draw.rect(DISPLAY, WHITE, (x +draww-roomdoor-20, y+ otsl+stal+ bedl-pt1-2, roomdoor, pt1+pt1))
pygame.draw.rect(DISPLAY, Black, (x +draww-roomdoor-20, y+ otsl+stal+ bedl-2, 2, pt2+3))
pygame.draw.rect(DISPLAY, Black, (x +draww-20, y+ otsl+stal+ bedl-2, 2, pt2+2))
# kitchen upper correct
pygame.draw.rect(DISPLAY, WHITE, (x+draww-1, y+otsl+bedl+toil+washl-1 , kitw/1.7, kitl/2.5))

# bedroom 2
pygame.draw.rect(DISPLAY, WHITE, (x+bedw+pt1, y+otsl-1+bedl-2 , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw+pt1, y+otsl-1+bedl-2 , 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw+pt1+roomdoor, y+otsl-1+bedl-1 , 2, pt1-2))
# bedroom 1
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-roomdoor, y+otsl-2+bedl ,roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-roomdoor, y+otsl-2+bedl , 2, pt1-1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-2, y+otsl-2+bedl , 2, pt1-1))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+toiw-toidoor-10 , y+toil-2, toidoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+toiw-toidoor-10 , y+toil-2, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+toiw-13 , y+toil-2, 3, pt1))
# toilet 2
pygame.draw.rect(DISPLAY, WHITE, (x+toiw+otsw+pt1 , y+col-1 , toidoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+toiw+otsw+pt1 , y+col-1 , 2, pt1-1))
pygame.draw.rect(DISPLAY, Black, (x+toiw+otsw+pt1+toidoor , y+col-1 , 2, pt1-1))
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()