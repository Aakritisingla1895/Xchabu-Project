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
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1,y+pt1, utiw-pt1+21-pt2-1,util-pt1), 2)
# toilet
toil = len * 0.175
toiw = wid * 0.4


# bedroom outer
bedl = len * 0.275
bedw = wid * 0.6
bedx = x + bedw / 3
bedy = y + util + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y + util, bedw+20, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# bedroom inner
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y + util+pt2, bedw-pt1-pt2+20,bedl-pt2-pt2), 2)
# .toilet
col = len * 0.2 + toil
cow = wid * 0.4
cox = x + bedw + cow / 3
coy = y  + col / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x + bedw+20, y , cow-20, col), 2)
ctoilet = font.render('toilet', True, Black)
DISPLAY.blit(ctoilet, (cox, coy))
# innerc.toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x + bedw+20, y +pt1, cow-pt1-20, col-pt1-pt2), 2)
# stairs
stal = len * 0.4
staw = wid * 0.4
stax = x + staw / 2
stay = y + util + bedl + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y + util + bedl, staw, stal-50), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# innner wall
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y + util + bedl, staw-pt1+1, stal-50), 2)
# wash area
washl = len * 0.125
washw = wid * 0.2
washx = x + washw / 3-5
washy = y + util + bedl + stal - washl + washl / 2-50
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y + util + bedl + stal - washl-50, washw, washl), 2)
wash = font.render('Wash', True, Black)
DISPLAY.blit(wash, (washx, washy))
# wash inner
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y + util + bedl + stal - washl+pt2-50, washw-pt1+1, washl-pt2-pt2), 2)
# store
stol = len * 0.125
stow = wid * 0.2
stox = x + washw + stow / 3-10
stoy = y + util + bedl + stal - washl + stol / 2-50
pygame.draw.rect(DISPLAY, (0, 0,0), (x + washw, y + util + bedl + stal - washl-50, stow, stol), 2)
wash = font.render('store', True, Black)
DISPLAY.blit(wash, (stox, stoy))
# inner store
pygame.draw.rect(DISPLAY, (0, 0,0), (x + washw+pt2, y + util + bedl + stal - washl+pt2-50, stow-pt2-pt2, stol-pt2), 2)

# drawing room
dral = len * 0.4
draw = wid * 0.6
drawx = x + staw + draw / 3
drawy = y + util + bedl + dral / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x + staw, y + util + bedl, draw, dral), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))
# inner drawing
drawl =len * 0.4-pt2
draww =wid * 0.6-pt1
pygame.draw.rect(DISPLAY, (0, 0,0), (x + staw, y + util + bedl, draww, drawl), 2)
# empty block
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y + util + bedl + stal-50, staw, 50),2)
# inner empty
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y + util + bedl + stal-50, staw-pt1, 50),2)

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
pygame.draw.rect(DISPLAY, WHITE, (x+utiw-10-roomdoor,y+util-2, roomdoor ,pt1))
pygame.draw.rect(DISPLAY, Black, (x+utiw-10-roomdoor,y+util-1, 2 ,pt1-1))
pygame.draw.rect(DISPLAY, Black, (x+utiw-10,y+util-1, 2 ,pt1-1))
# wash
pygame.draw.rect(DISPLAY, WHITE, (x+pt1+2, y + util + bedl + stal - washl-50+washl-pt2-2, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1+2+roomdoor, y + util + bedl + stal - washl-50+washl-pt2-2, 2, pt1))

# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-58, y + util+bedl-pt1+4,roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-58, y + util+bedl-pt1+4,2, pt1-1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-58+roomdoor, y + util+bedl-pt1+4,2, pt1-1))
# drawing
pygame.draw.rect(DISPLAY, WHITE, (x + staw+2, y + util + bedl+dral-pt1+3, entdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x + staw+2+entdoor, y + util + bedl+dral-pt1+3, 2, pt1))
# empty block
pygame.draw.rect(DISPLAY, WHITE, (x+staw-13, y + util + bedl + stal-49.5, pt1+5, 50))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x + bedw+22, y +col-pt1, toidoor, pt1+pt1))
pygame.draw.rect(DISPLAY, Black, (x + bedw+22+toidoor, y +col-pt1+3, 2, pt1-2))
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+pt1, y + util + bedl + stal-2, kitw-pt1-pt1-1, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1, y + util + bedl + stal-2,2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1+ kitw-pt1-pt1-1, y + util + bedl + stal,2, pt1))
# store
pygame.draw.rect(DISPLAY, WHITE, (x + washw+pt1-2, y + util + bedl + stal - washl-50+washl-2, toidoor, pt1))

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()