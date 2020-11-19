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
len = 37 * scale
wid = 30 * scale
entdoor = 4 * scale
roomdoor= 3 * scale
toidoor = 2.6 * scale
font = pygame.font.SysFont(None, 24)

#wash area:-
washl = len * 0.135
washw = wid * 0.63
washx = x + washw / 3
washy = y + washl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y , washw, washl), 2)
wash = font.render('Wash', True, Black)
DISPLAY.blit(wash, (washx, washy))
# inner wash area
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+pt1 , washw-pt1-pt2, washl-pt1), 2)
#kitchen:-
kitl = len * 0.225
kitw = wid * 0.37
kitx = x +washw+ kitw / 3
kity = y + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+washw-1, y , kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
pygame.draw.rect(DISPLAY, (0, 0,0), (x+washw-1, y+pt1 , kitw-pt1, kitl-pt1), 2)
#toilet:-
toil = len * 0.16
toiw = wid * 0.26
toix = x +washw-toiw + toiw / 2
toiy =y +washl+ toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x +washw-toiw, y+washl-1, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x +washw-toiw+pt2, y+washl-1+pt2, toiw-pt2, toil-pt2-pt2), 2)
#bedroom:-
bedl = len * 0.38
bedw = wid * 0.43
bedx = x + bedw / 3
bedy = y +washl+ bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y +washl, bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y +washl+pt2, bedw-pt1, bedl-pt2), 2)
# drawing room
drawl = len * 0.35
draww = wid * 0.57
drawx = x +bedw+ draww / 3
drawy = y +washl+ drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1 , y+kitl -1, draww, drawl), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# inner drawing
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1+pt2 , y+kitl -1+pt2, draww-pt2-pt1, drawl-pt2), 2)
# toilet correction
pygame.draw.rect(DISPLAY, WHITE, (x +washw-toiw+2, y+washl-1+2, toiw-2, toil-2))
pygame.draw.rect(DISPLAY, (0, 0,0), (x +washw-toiw, y+washl-1, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
pygame.draw.rect(DISPLAY, (0, 0,0), (x +washw-toiw+pt2, y+washl-1+pt2, toiw-pt2-pt2, toil-pt2-pt2), 2)
#stairs:-
stal = len * 0.33
staw = wid * 0.28
stax = x + staw / 2
stay = y+washl+bedl  + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+washl+bedl-1, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# inner stairs
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+washl+bedl-1, staw-pt1-pt1, stal-pt1), 2)
#parking:-
parl = len * 0.33
parw = wid * 0.36
parx = x+staw  + parw / 2-10
pary =y+washl+bedl+ parl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw-1, y+washl+bedl-1, parw, parl), 2)
toilet = font.render('Parking', True, Black)
DISPLAY.blit(toilet, (parx, pary))
#bedroom:-
bedl2 = len * 0.27
bedw2 = wid * 0.36
bedx2 = x+staw+parw + bedw2 / 3
bedy2 = y+kitl+drawl  + bedl2 / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw+parw-1, y+kitl+drawl-2 , bedw2, bedl2), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx2,bedy2))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw+parw-1+pt1, y+kitl+drawl-2+pt2 , bedw2-pt1-pt1, bedl2-pt2-pt1), 2)
# correction parking
pygame.draw.rect(DISPLAY, WHITE, (x+staw-1+2, y+washl+bedl-1+2, parw-3, parl-2))
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw-1, y+washl+bedl-1, parw, parl), 2)
toilet = font.render('Parking', True, Black)
DISPLAY.blit(toilet, (parx, pary))
# doors
# wash 
pygame.draw.rect(DISPLAY, WHITE, (x+washw-1-pt2, y+washl-roomdoor , pt1-2, roomdoor))
pygame.draw.rect(DISPLAY, Black, (x+washw-1-pt2, y+washl-roomdoor , pt1-2, 2))
pygame.draw.rect(DISPLAY, Black, (x+washw-1-pt2, y+washl-1 , pt1-2, 2))
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+washw-1+pt1, y+kitl -2 ,roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+washw-1+pt1, y+kitl -1 ,2, pt1-2))
pygame.draw.rect(DISPLAY, Black, (x+washw-1+pt1+roomdoor, y+kitl -1 ,2, pt1-2))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-2, y +washl+toil-3, pt1, roomdoor))
pygame.draw.rect(DISPLAY, Black, (x+bedw-2, y +washl+toil-3, pt1, 2))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1, y +washl+toil+roomdoor-3, pt1-2, 2))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x +washw-10-toidoor, y+washl+toil-pt1, toidoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x +washw-10-toidoor, y+washl+toil-pt1+1, 2, pt1-2))
pygame.draw.rect(DISPLAY, Black, (x +washw-10, y+washl+toil-pt1+1, 2, pt1-2))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+staw+parw+pt1, y+kitl+drawl- 3, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+staw+parw+pt1-1, y+kitl+drawl-2 , 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+staw+parw+pt1+roomdoor-1, y+kitl+drawl-2 , 2,pt1-2))

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()