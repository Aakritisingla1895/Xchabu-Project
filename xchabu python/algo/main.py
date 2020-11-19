import pygame, sys
from pygame.locals import *
import random



pygame.init()
DISPLAY = pygame.display.set_mode((1200,650),0,32)
WHITE = (255,255,255)
Black = (0,0,0)
blue = (0,0,255)
DISPLAY.fill(WHITE)
x = 10
scale = 15
y1 = 10
pt1 = 0.7 * 15
pt2 = 0.4 * 15
len = 40 * 15
wid = 20 * 15
entdoor = 4 * 15
roomdoor= 3 * 15
toidoor = 2.6 * 15
font = pygame.font.SysFont(None, 24)

List  = [60,75,90]
y = random.choice(List)
#bedroom:-

bedd = 12
if y == 60 :
    bedd = 12
if y == 75 :
    bedd = 11
if y == 90 :
    bedd = 10
bedw = scale * 12
bedl = scale * bedd
bedx = x + bedw / 3
bedy = y  + bedl / 3 -50
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y, bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
#kitchen:-
kitt = 10
kitw =  scale *8
if y == 60 :
    kitt = 12
if y == 75 :
    kitt = 11
if y == 90 :
    kitt = 10
kitl =  scale * kitt
kitx = x+bedw + kitw / 3
kity = y + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1, y , kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
#toilet:-
toill = 5
if y == 60 :
    toill = 6.5
if y == 75 :
    toill = 6
if y == 90 :
    toill = 5
toil =  scale * toill
toiw =  scale * 5
toix = x  + toiw / 2 -15
toiy =y+ bedl + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+bedl-1, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
#dining
dinn = 10
if y == 60 :
    dinn = 12
if y == 75 :
    dinn = 11 
if y == 90 :
    dinn = 10
dinl = scale *dinn
dinw = scale *12
dinx = x + dinw / 3
diny = y + bedl + dinl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+bedl -1 , dinw, dinl), 2)
din = font.render('Dining', True, Black)
DISPLAY.blit(din, (dinx, diny))
#stairs:-
staa = 10
if y == 60 :
    staa = 12
if y == 75 :
    staa = 11 
if y == 90 :
    staa = 10
stal =  scale *staa
staw =  scale * 8
stax = x +dinw-1+ staw / 2
stay = y +bedl-1 + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x+dinw-1, y+bedl-1, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# entry
entt = 15
if y == 60 :
    entt = 15 
if y == 75 :
    entt = 14
if y == 90 :
    entt = 13
entl = scale * entt
entw = scale * 7
entx = x  + entw / 2
enty = y  + bedl + stal + entl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+bedl+stal-2 , entw, entl), 2)
ent= font.render('Entry', True, Black)
DISPLAY.blit(ent, (entx, enty))
# drawing room\
drawi = 15
if y == 60 :
    drawi = 15 
if y == 75 :
    drawi = 14
if y == 90 :
    drawi = 13
drawl = scale *drawi
draww = scale * 13
drawx = x+entw + draww / 3
drawy = y+bedl+stal + drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+entw-1 , y+bedl+stal-2 , draww, drawl), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()