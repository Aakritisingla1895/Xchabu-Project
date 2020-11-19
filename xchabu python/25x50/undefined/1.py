import pygame, sys
from pygame.locals import *



pygame.init()
DISPLAY=pygame.display.set_mode((1200,800),0,32)
WHITE=(255,255,255)
Black=(0,0,0)
blue =(0,0,255)
DISPLAY.fill(WHITE)
x =10
y=10
scale = 15
pt1 = 0.7 * 15
pt2 = 0.4 * 15
entdoor = 4 * 15
roomdoor= 3 * 15
toidoor = 2.6 * 15
len = 40*15
wid = 20*15
font = pygame.font.SysFont(None, 24)
#bedroom:-
bedl = scale * 10
bedw = scale * 13
bedx = x + bedw / 3
bedy = y  + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y , bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# INNER BEDROOM
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+pt1 , bedw-pt1+1, bedl-pt1-pt2+1), 2)
#wash area:-
washl =  scale * 5
washw =scale * 12
washx = x +bedw+ washw / 3
washy = y + washl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x-1+bedw, y , washw, washl), 2)
wash = font.render('Wash', True, Black)
DISPLAY.blit(wash, (washx, washy))
# inner wash
pygame.draw.rect(DISPLAY, (0, 0,0), (x-1+pt2+bedw, y+pt1 , washw-pt1-pt2, washl-pt1+1), 2)
#kitchen:-
kitl =  scale * 10
kitw =  scale * 12
kitx = x +bedw+ kitw / 3
kity = y +washl+ kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1, y+washl-1 , kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1+pt2, y+washl-1+pt2 , kitw-pt2-pt1, kitl-pt2), 2)
#toilet:-
toil =  scale * 5
toiw =  scale * 7
toix = x  + toiw / 2
toiy =y+bedl-1 + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+bedl-1, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+bedl-1, toiw-pt1+1-pt2, toil), 2)
#stairs:-
stal =  scale * 7
staw =  scale * 10
stax = x + staw / 2
stay = y +bedl+toil-1 + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+bedl+toil-2, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# inner stair
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+bedl+toil-2+pt2, staw-pt1+1, stal-pt2), 2)
#dining
dinl = scale * 13
dinw = scale * 15
dinx = x+staw-1 + dinw / 3
diny = y+toil + bedl + dinl / 2-20
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw-1, y+toil+bedl-2 , dinw, dinl), 2)
din = font.render('Dining', True, Black)
DISPLAY.blit(din, (dinx, diny))
# inner dining
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw-1, y+toil+bedl-2+pt2 , dinw-pt1, dinl-pt2), 2)
# drawing room
drawl = scale * 13
draww = scale * 17
drawx = x+ draww / 3
drawy = y+bedl+toil+stal-2 + drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+bedl+toil+stal-3 , draww, drawl), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))
# foyer
foyl= scale * 7
foyw = scale * 8
foyx=x+draww +toiw/3
foyy=y+toil+bedl+dinl-3 +toil/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-1 , y +toil+bedl+dinl-3, foyw, foyl), 2)
foyer= font.render('Foyer', True, Black)
DISPLAY.blit(foyer, (foyx, foyy))  
# inner foyer
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-1+pt2 , y +toil+bedl+dinl-3, foyw-pt2-pt1, foyl-pt1), 2)
# drawing correction
pygame.draw.rect(DISPLAY, WHITE, (x , y+bedl+toil+stal-3 , draww, drawl))
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+bedl+toil+stal-3 , draww, drawl), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))
# inner drawing
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+bedl+toil+stal-3+pt2, draww-pt1+1, drawl-pt1-pt2), 2)
# garden
garl = scale * 13
garw = scale * 25
garx = x + garw / 3
gary = y+bedl+toil+dinl-3+foyl  + garl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+bedl+toil+dinl-4+foyl , garw, garl), 2)
gal = font.render('Garden', True, Black)
DISPLAY.blit(gal, (garx, gary))
# doors
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-roomdoor-1, y+bedl-pt2-1 , roomdoor,pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-roomdoor-1, y+bedl-pt2-1 ,2 ,pt1-2))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1, y+bedl-pt2-1 ,2 ,pt1-2))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+toiw-pt2- 1, y+bedl+1, pt1, toidoor))
pygame.draw.rect(DISPLAY, Black, (x+toiw-pt2- 1, y+bedl+1+toidoor, pt2, 2))
# wash area
pygame.draw.rect(DISPLAY, WHITE, (x-1+bedw+pt2, y+washl-1, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x-1+bedw+pt2, y+washl-1, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x-1+bedw+pt2+roomdoor, y+washl-1, 2, pt2))
# kitchen back
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-1-roomdoor+2, y+washl-1+kitl-1 , roomdoor-2, pt1))
# kitchen main
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-1, y+washl-1+kitl-1 , kitw-pt1-1, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1, y+washl-1+kitl-1 ,pt2+2, 2))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1+kitw-pt1-1, y+washl-1+kitl-1 , 2, pt1))
# drawing
pygame.draw.rect(DISPLAY, WHITE, (x+draww-pt2 , y+bedl+toil+stal-1+pt2 , pt1, 82))
# foyer
pygame.draw.rect(DISPLAY, WHITE, (x+draww-2+pt1 , y +toil+bedl+dinl-3, foyw-pt1-pt1, pt1))
# main enterance
pygame.draw.rect(DISPLAY, WHITE, (x+draww-1+pt2, y +toil+bedl+dinl-4+foyl-pt1, entdoor, pt1+pt2))
pygame.draw.rect(DISPLAY, Black, (x+draww-1+pt2, y +toil+bedl+dinl-4+foyl-pt1, 2, pt1+pt2-3))
pygame.draw.rect(DISPLAY, Black, (x+draww-1+pt2+entdoor, y +toil+bedl+dinl-4+foyl-pt1, 2, pt1+pt2-3))

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()