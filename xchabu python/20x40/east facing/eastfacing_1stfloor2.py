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
stow = wid * 0.25
washl = len * 0.125
washw = wid * 0.5
washx = x + washw / 3
washy = y + util + bedl + stal - washl + washl / 2-50
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y + util + bedl + stal - washl-50, washw, washl), 2)
wash = font.render('Toilet', True, Black)
DISPLAY.blit(wash, (washx, washy))
# wash inner
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y + util + bedl + stal - washl+pt2-50, washw-pt1+1, washl-pt2-pt2), 2)

stow = wid * 0.25

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
# bedroom
#bedroom:-
bedl1 = len * 0.35
bedw1 = wid * 0.5
bedx1 = x + bedw / 3
bedy1 = y+y + util + bedl+dral -10 + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+y + util + bedl+dral -60, bedw1, bedl1), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx1, bedy1))
# inner bedroom
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+y + util + bedl+dral -60, bedw1-pt1, bedl1-pt1), 2)
# terreace
terrl = len * 0.275
terrw = wid * 0.5
terrx = x +bedw+ terrw / 3
terry = y + util + bedl+dral  + terrl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw1-1, y + util + bedl+dral  , terrw, terrl), 2)
bed = font.render('Terrace', True, Black)
DISPLAY.blit(bed, (terrx, terry))
# terrace inner
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw1-1+pt1, y + util + bedl+dral  , terrw-pt1-pt1, terrl-pt2-pt1), 2)
# door way
# utility
pygame.draw.rect(DISPLAY, WHITE, (x+utiw-60,y+util-2, 50 ,pt1))
pygame.draw.rect(DISPLAY, Black, (x+utiw-60,y+util-2, 3 ,pt1))
pygame.draw.rect(DISPLAY, Black, (x+utiw-10,y+util-2, 3 ,pt1))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x + utiw-pt1+23, y+toil-30, pt1, 28))
pygame.draw.rect(DISPLAY, Black, (x + utiw-pt1+23, y+toil-30, pt1, 3))
pygame.draw.rect(DISPLAY, Black, (x + utiw-pt1+23, y+toil-2, pt1, 3))
# c.toilet
pygame.draw.rect(DISPLAY, WHITE, (x + bedw+2, y + toil+col-pt1+3, 50, pt1))
pygame.draw.rect(DISPLAY, Black, (x + bedw+2+50, y + toil+col-pt1+3, 2.5, pt1))
# wash
pygame.draw.rect(DISPLAY, WHITE, (x+pt1+2, y + util + bedl + stal - washl-50+washl-pt2-2, 40, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1+2+40, y + util + bedl + stal - washl-50+washl-pt2-2, 2, pt1))
# store
pygame.draw.rect(DISPLAY, WHITE, (x + washw+pt1-2, y + util + bedl + stal - washl-50+washl-2, 40, pt1))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-22, y + util+bedl-2, 25, pt2))
# drawing
pygame.draw.rect(DISPLAY, WHITE, (x + staw+8, y + util + bedl+dral-pt1+3, 50, pt1))
pygame.draw.rect(DISPLAY, Black, (x + staw+8, y + util + bedl+dral-pt1+3, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x + staw+8+50, y + util + bedl+dral-pt1+3, 2, pt1))

# toilet
pygame.draw.rect(DISPLAY, WHITE, (x + utiw-pt1+23, y+toil-30, pt1, 28))
pygame.draw.rect(DISPLAY, Black, (x + utiw-pt1+23, y+toil-30, pt1, 3))
pygame.draw.rect(DISPLAY, Black, (x + utiw-pt1+23, y+toil-2, pt1, 3))
# c.toilet
pygame.draw.rect(DISPLAY, WHITE, (x + bedw+2, y + toil+col-pt1+3, 50, pt1))
pygame.draw.rect(DISPLAY, Black, (x + bedw+12, y + toil+col-pt1+3, pt1, 2))
pygame.draw.rect(DISPLAY, Black, (x + bedw+2+50, y + toil+col-pt1+3, 2.5, pt1))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+bedw1-2, y+y + util + bedl+dral -58, pt1, 40))
pygame.draw.rect(DISPLAY, Black, (x+bedw1-2, y+y + util + bedl+dral -58, pt1, 2))
pygame.draw.rect(DISPLAY, Black, (x+bedw1-2, y+y + util + bedl+dral -18, pt1, 2))
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()