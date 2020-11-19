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

#store:-
stol = len * 0.125
stow = wid * 0.65
stox = x  + stow / 3
stoy = y  + stol / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y, stow, stol), 2)
wash = font.render('Wash', True, Black)
DISPLAY.blit(wash, (stox, stoy))
# inner store
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+pt1, stow-pt1+1, stol-pt1+1), 2)
# wash area
#wash area:-
washl = len * 0.125
washw = wid * 0.35
washx = x+stow + washw / 3
washy = y + washl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+stow-1, y , washw, washl), 2)
wash = font.render('Store', True, Black)
DISPLAY.blit(wash, (washx, washy))
# inner wash
pygame.draw.rect(DISPLAY, (0, 0,0), (x+stow-1+pt2, y+pt1 , washw-pt2-pt1, washl-pt1+1), 2)
#bedroom:-
bedl = len * 0.25
bedw = wid * 0.45
bedx = x + bedw / 3
bedy = y + stol + bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+stol-1 , bedw, bedl), 2)
bed = font.render('Kitchen', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# bedroom inner
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+stol-1+pt2, bedw-pt1+1, bedl-pt2), 2)
#kitchen:-
kitl = len * 0.25
kitw = wid * 0.55
kitx = x+bedw + kitw / 3
kity = y+stol + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1, y+stol -1, kitw, kitl), 2)
Kitcehn = font.render('Bedroom', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# innner kitchen
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw-1+pt2, y+stol -1+pt2, kitw-pt2-pt1, kitl-pt2), 2)
#toilet:-
toil = len * 0.2
toiw = wid * 0.25
toix = x+ toiw / 2-15
toiy =y+stol+bedl-2 + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y+stol+bedl-2, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y+stol+bedl-2+pt2, toiw-pt2-pt1, toil-pt2-pt2), 2)
# drawing room
drawl = len * 0.325
draww = wid * 0.7
drawx = x+ draww / 3
drawy = y+stol+bedl + drawl / 2+40
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y +stol+bedl-2, draww, drawl), 2)
draw= font.render('Hall', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# inner drawing
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1 , y +stol+bedl-2+pt2, draww-pt1+1, drawl-pt2), 2)
#stairs:-
stal = len * 0.325
staw = wid * 0.3
stax = x+draww + staw / 2
stay = y +bedl+stol + stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-1, y+bedl+stol-2, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# inner stairs
pygame.draw.rect(DISPLAY, (0, 0,0), (x+draww-1, y+bedl+stol-2+pt2, staw-pt1, stal-pt2), 2)
# # entry
entl = len * 0.3
entw = wid * 0.4
entx = x + entw / 2
enty = y +stol + bedl + stal + entl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y +bedl + stal+stol-3, entw, entl), 2)
ent= font.render('Entry', True, Black)
DISPLAY.blit(ent, (entx, enty))
# inner entry
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y +bedl + stal+stol-3+pt1, entw, entl-pt1), 2)

#dining
dinl = len * 0.3
dinw = wid * 0.6
dinx = x +entw+ dinw / 3
diny = y +bedl + stal+stol-3 + dinl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+entw-1, y +bedl + stal+stol-3 , dinw, dinl), 2)
din = font.render('Drawing', True, Black)
DISPLAY.blit(din, (dinx, diny))
# inner drawing
pygame.draw.rect(DISPLAY, (0, 0,0), (x+entw-1+pt1, y +bedl + stal+stol-3+pt2 , dinw-pt1-pt1, dinl-pt1-pt2), 2)
# doors
# store
pygame.draw.rect(DISPLAY, WHITE, (x+stow-1 , y+pt1, pt1, roomdoor))
pygame.draw.rect(DISPLAY, Black, (x+stow-1 , y+pt1, pt1, 2))
pygame.draw.rect(DISPLAY, Black, (x+stow-1 , y+pt1+roomdoor, pt2, 2))
# wash
pygame.draw.rect(DISPLAY, WHITE, (x+pt1, y+washl-1 , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1, y+washl-1 , 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+pt1+roomdoor, y+washl-1 , 2, pt1-2))
# bedroom
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-roomdoor, y+stol-2+bedl , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-roomdoor, y+stol-2+bedl , 2, pt1-2))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1, y+stol-2+bedl , 2, pt1-2))
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-1+pt2, y+stol +kitl-2, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1+pt2, y+stol +kitl-2,2, pt1-2))
pygame.draw.rect(DISPLAY, Black, (x+bedw-1+pt2+roomdoor, y+stol +kitl-2,2, pt1-2))
# toilet
pygame.draw.rect(DISPLAY, WHITE, (x+toiw-pt1 , y+stol+bedl+pt2-2, pt1+2, toidoor))
pygame.draw.rect(DISPLAY, Black, (x+toiw-pt1 , y+stol+bedl+pt2-2, pt1+2, 2))
pygame.draw.rect(DISPLAY, Black, (x+toiw-pt2 , y+stol+bedl+pt2-2+toidoor, pt1-3, 2))
# enterance
pygame.draw.rect(DISPLAY, WHITE, (x+entw-entdoor-1 , y +bedl + stal+stol-3, entdoor, pt1+2))
pygame.draw.rect(DISPLAY, Black, (x+entw-entdoor-1 , y +bedl + stal+stol-3, 2, pt1+2))
# drawing
pygame.draw.rect(DISPLAY, WHITE, (x+entw+pt1, y +bedl + stal+stol-4 , roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+entw+pt1-1, y +bedl + stal+stol-3 , 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+entw+pt1+roomdoor, y +bedl + stal+stol-3 , 2, pt1-2))







while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()