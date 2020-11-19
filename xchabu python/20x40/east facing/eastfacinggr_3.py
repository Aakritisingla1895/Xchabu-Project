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

# utlity
util = len * 0.1
utiw = wid * 0.6
utix = x + utiw / 2
utiy = y + util / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x,y, utiw+20,util), 2)
img = font.render('Utility', True, Black)
DISPLAY.blit(img, (utix, utiy))
# inner utility
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1,y+pt1, utiw-pt1+21-pt2,util-pt1), 2)
# toilet
toil = len * 0.175
toiw = wid * 0.4
toix = x + utiw + toiw / 2
toiy =y + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x + utiw+20, y, toiw-20, toil), 2)
toilet = font.render('Store', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x + utiw+20, y+pt1, toiw-pt1-20, toil-pt1+1), 2)
# bedroom outer
bedl = len * 0.275
bedw = wid * 0.6
bedx = x + bedw / 3
bedy = y + util + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y + util, bedw+20, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# bedroom inner
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y + util+pt2, bedw-pt1-pt2+20,bedl-pt2), 2)
# .toilet
col = len * 0.2
cow = wid * 0.4
cox = x + bedw + cow / 3
coy = y + toil + col / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x + bedw+20, y + toil, cow-20, col), 2)
ctoilet = font.render('toilet', True, Black)
DISPLAY.blit(ctoilet, (cox, coy))
# innerc.toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x + bedw+20, y + toil+pt2, cow-pt1-20, col-pt2-pt2), 2)
# stairs
stal = len * 0.4
staw = wid * 0.5
stax = x + staw / 2
stay = y + util + bedl + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y + util + bedl, staw, stal-50), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# innner wall
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y + util + bedl+pt2, staw-pt1+1, stal-pt2-50), 2)
# wash area
washl = len * 0.125
washw = wid * 0.5
washx = x + washw / 3
washy = y + util + bedl + stal - washl + washl / 2-50
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y + util + bedl + stal - washl-50, washw, washl), 2)
wash = font.render('Toilet', True, Black)
DISPLAY.blit(wash, (washx, washy))
# wash inner
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y + util + bedl + stal - washl+pt2-50, washw-pt1+1, washl-pt2-pt2), 2)

# drawing room
dral = len * 0.4
draw = wid * 0.5
drawx = x + staw + draw / 3
drawy = y + util + bedl + dral / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x + staw, y + util + bedl, draw, dral), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# drawing
dral1 = len * 0.4-pt2
draw1 = wid * 0.5-pt1-pt2
pygame.draw.rect(DISPLAY, (0, 0,0), (x + staw+pt2, y + util + bedl, draw1, dral1), 2)
# empty block
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y + util + bedl + stal-50, staw, 50),2)
# inner empty
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y + util + bedl + stal-50, staw-pt1, 50),2)
# drawing room
dral = len * 0.4
draw = wid * 0.5
drawx = x + staw + draw / 3
drawy = y + util + bedl + dral / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x + staw, y + util + bedl, draw, dral), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# drawing
dral1 = len * 0.4-pt2
draw1 = wid * 0.5-pt1-pt2
pygame.draw.rect(DISPLAY, (0, 0,0), (x + staw+pt2, y + util + bedl, draw1, dral1), 2)
# kitchen
kitl = len * 0.225
kitw = wid * 0.4
kitx = x + kitw / 3
kity = y + util + bedl + stal + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y + util + bedl + stal, kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y + util + bedl + stal+pt2, kitw-pt1-pt1, kitl-pt2-pt1), 2)
# entry
entl = len * 0.225
entw = wid * 0.6
entx = x + kitw + entw / 2
enty = y + util + bedl + stal + entl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x + kitw, y + util + bedl + stal, entw, entl), 2)
ent= font.render('Entry', True, Black)
DISPLAY.blit(ent, (entx, enty))
# door way
# utility
pygame.draw.rect(DISPLAY, WHITE, (x+utiw-roomdoor,y+util-2, roomdoor ,pt1))
pygame.draw.rect(DISPLAY, Black, (x+utiw-roomdoor,y+util-2,2 ,pt1))
pygame.draw.rect(DISPLAY, Black, (x+utiw,y+util-2, 2 ,pt1))
# wash
pygame.draw.rect(DISPLAY, WHITE, (x+pt1+2, y + util + bedl + stal - washl-50+washl-pt2-2, 40, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1+2+40, y + util + bedl + stal - washl-50+washl-pt2-2, 2, pt1))
# store
pygame.draw.rect(DISPLAY, WHITE, (x + washw+pt1-2, y + util + bedl + stal - washl-50+washl-2, 40, pt1))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-22, y + util+bedl-2, 34, pt2))
# drawing
pygame.draw.rect(DISPLAY, WHITE, (x + staw+8, y + util + bedl+dral-pt1+3, 50, pt1))
pygame.draw.rect(DISPLAY, Black, (x + staw+8, y + util + bedl+dral-pt1+3, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x + staw+8+50, y + util + bedl+dral-pt1+3, 2, pt1))
# empty block
pygame.draw.rect(DISPLAY, WHITE, (x+staw-2, y + util + bedl + stal-48, pt1+2, 47))
pygame.draw.rect(DISPLAY, WHITE, (x+staw-2, y + util + bedl + stal-48, pt1+2, 47))
pygame.draw.rect(DISPLAY, Black, (x+staw-2, y + util + bedl + stal-50, pt1+1, 2))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x + utiw-pt1+23, y+toil-30, pt1, 28))
pygame.draw.rect(DISPLAY, Black, (x + utiw-pt1+23, y+toil-30, pt1, 3))
pygame.draw.rect(DISPLAY, Black, (x + utiw-pt1+23, y+toil-2, pt1, 3))
# c.toilet
pygame.draw.rect(DISPLAY, WHITE, (x + bedw+2+pt1+pt2+4, y + toil+col-pt1+3, toidoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x + bedw+2+pt1+pt2+4+toidoor, y + toil+col-pt1+3, 2, pt1))
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+pt1, y + util + bedl + stal-2, kitw-pt1+50, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1, y + util + bedl + stal-2,2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1+kitw-pt1-pt1, y + util + bedl + stal-2+pt1,pt1, 2))
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()