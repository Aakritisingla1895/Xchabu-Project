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
# ots
otsl= len*0.1
otsw = wid*0.2
otsx=x + otsw/3
otsy=y + otsl/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x , y , otsw, otsl), 2)
foyer= font.render('OTS', True, Black)
DISPLAY.blit(foyer, (otsx, otsy)) 
# toilet:-
toil = len * 0.1
toiw = wid * 0.3
toix = x + otsw + toiw / 3
toiy =y + toil / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x +otsw, y, toiw, toil), 2)
toilet = font.render('Toilet', True, Black)
DISPLAY.blit(toilet, (toix, toiy))
# inner wall toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x +otsw+pt1, y+pt1, toiw-2*pt1, toil-pt1), 2)
# ots 2
# ots
otsl1= len*0.1
otsw1 = wid*0.5
otsx1=x + toiw+otsw+otsw1/3
otsy1=y + otsl/2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+otsw+toiw-1 , y , otsw1, otsl1), 2)
foyer= font.render('OTS', True, Black)
DISPLAY.blit(foyer, (otsx1, otsy1)) 

# bedroom:-
bedl = len * 0.25
bedw = wid * 0.6
bedx = x + bedw / 3
bedy = y + otsl+ bedl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+otsl -1, bedw, bedl), 2)
bed = font.render('Bedroom', True, Black)
DISPLAY.blit(bed, (bedx, y+bedy))
# inner wall
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+otsl -1+pt1, bedw-pt1+1, bedl-pt1), 2)
# kitchen:-
kitl = len * 0.25
kitw = wid * 0.4
kitx = x + bedw+ kitw / 3
kity = y + otsl + kitl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw, y+otsl, kitw, kitl), 2)
Kitcehn = font.render('Kitchen', True, Black)
DISPLAY.blit(Kitcehn, (kitx, kity))
# inner wall
pygame.draw.rect(DISPLAY, (0, 0,0), (x+bedw+pt2, y+otsl+pt1, kitw-pt2-pt1, kitl-pt1), 2)

# stairs:-
stal = len * 0.28
staw = wid * 0.2
stax = x + staw / 3
stay = y  + otsl+bedl+stal / 3
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y+otsl+bedl-1, staw, stal), 2)
stair = font.render('Stair', True, Black)
DISPLAY.blit(stair, (stax, stay))
# stairs wall
pygame.draw.rect(DISPLAY, (0, 0,0), (x+pt1, y+otsl+bedl-1+pt2, staw-pt1, stal-pt2-pt2), 2)
# dining
dinl = len * 0.28
dinw = wid * 0.55
dinx = x +staw+ dinw / 3
diny = y + otsl+bedl + dinl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw-1, y+otsl+bedl -1, dinw, dinl), 2)
din = font.render('Dining', True, Black)
DISPLAY.blit(din, (dinx, diny))
# inner dining
pygame.draw.rect(DISPLAY, (0, 0,0), (x+staw-1, y+otsl+bedl -1+pt2, dinw, dinl-pt2), 2)

#store:-
stol = len * 0.14
stow = wid * 0.25
stox = x + staw + dinw + stow / 3-10
stoy = y + toil + bedl + stol / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x + staw + dinw-1, y + toil + bedl, stow, stol), 2)
wash = font.render('store', True, Black)
DISPLAY.blit(wash, (stox, stoy))
# inner store
pygame.draw.rect(DISPLAY, (0, 0,0), (x + staw + dinw+pt2, y + toil + bedl+pt2, stow-pt2-pt1, stol-pt2), 2)

#c.toilet:-
col = len * 0.14
cow = wid * 0.25
cox = x + staw + dinw + stow / 3-10
coy = y + toil + bedl + stol + stow / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x + staw + dinw-1, y + toil + bedl + stol, stow, stol), 2)
ctoilet = font.render('toilet', True, Black)
DISPLAY.blit(ctoilet, (cox, coy))
# inner toilet
pygame.draw.rect(DISPLAY, (0, 0,0), (x + staw + dinw+pt2, y + toil + bedl + stol+pt2, stow-pt2-pt1, stol-pt2), 2)

# entry
entl = len * 0.275
entw = wid * 0.5
entx = x + entw / 3
enty = y + toil + bedl + stal + entl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x, y + toil + bedl + stal-1, entw, entl), 2)
ent= font.render('Entry', True, Black)
DISPLAY.blit(ent, (entx, enty))

# drawing room
drawl = len * 0.275
draww = wid * 0.5
drawx = x + entw + draww / 3
drawy = y + toil + bedl + stal + drawl / 2
pygame.draw.rect(DISPLAY, (0, 0,0), (x + entw, y + toil + bedl + stal-1, draww, drawl), 2)
draw= font.render('Drawing', True, Black)
DISPLAY.blit(draw, (drawx, drawy))  
# inner
pygame.draw.rect(DISPLAY, (0, 0,0), (x + entw+pt2, y + toil + bedl + stal-1+pt2, draww-pt2-pt1, drawl-pt2-pt1), 2)

# door ways
pygame.draw.rect(DISPLAY, WHITE, (x +otsw+pt1+2, y+toil-2, toidoor, pt1+pt2))
pygame.draw.rect(DISPLAY, Black, (x +otsw+pt1+2, y+toil-2, 2, pt1+2))
pygame.draw.rect(DISPLAY, Black, (x +otsw+pt1+2+toidoor, y+toil-2, 2, pt1+2))
# bedroom way
pygame.draw.rect(DISPLAY, WHITE, (x+bedw-roomdoor, y+otsl -3+bedl, roomdoor, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-roomdoor, y+otsl -3+bedl, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw-2, y+otsl -3+bedl, 2, pt1))
# kitchen door
pygame.draw.rect(DISPLAY, WHITE, (x+bedw+pt2, y+otsl-1, roomdoor, pt1+4))
pygame.draw.rect(DISPLAY, Black, (x+bedw+pt2, y+otsl, 2, pt1+4))
pygame.draw.rect(DISPLAY, Black, (x+bedw+pt2+roomdoor, y+otsl, 2, pt2+4))
# kitchen
pygame.draw.rect(DISPLAY, WHITE, (x+bedw+pt2, y+otsl+kitl-2, 37,pt1))
pygame.draw.rect(DISPLAY, Black, (x+bedw+pt2, y+otsl+kitl-1, 2,pt1-1))
# store
pygame.draw.rect(DISPLAY, WHITE, (x + staw + dinw-1+pt2+1, y + toil + bedl-2,roomdoor,pt1 ))
pygame.draw.rect(DISPLAY, Black, (x + staw + dinw-1+pt2+1, y + toil + bedl-2, 2,pt1 ))
pygame.draw.rect(DISPLAY, Black, (x + staw + dinw-1+pt2+roomdoor, y + toil + bedl-2, 2,pt1 ))
# store
pygame.draw.rect(DISPLAY, WHITE, (x + staw + dinw-2, y + toil + bedl + stol+pt1, pt1, toidoor))
pygame.draw.rect(DISPLAY, Black, (x + staw + dinw-2, y + toil + bedl + stol+pt1, pt1, 2))
pygame.draw.rect(DISPLAY, Black, (x + staw + dinw-2, y + toil + bedl + stol+pt1+toidoor, pt1, 2))
# ddrawing
pygame.draw.rect(DISPLAY, WHITE, (x + entw+pt2, y + toil + bedl + stal-2, draww-toiw, pt1))
pygame.draw.rect(DISPLAY, Black, (x + entw+pt2, y + toil + bedl + stal-2, 2, pt1))
pygame.draw.rect(DISPLAY, Black, (x + entw+pt2+draww-toiw, y + toil + bedl + stal-2, 2, pt1-1))
# entry
pygame.draw.rect(DISPLAY, WHITE, (x+entw-entdoor-2, y + toil + bedl + stal-3, entdoor, pt1))
print("length of  bedroom",bedl/15)
print("Width of bedroom ", bedw/15)
print("length of toilet ",toil/15)
print("Width of toilet ",toiw/15)
print("length of kitchen", kitl/15)
print("Width of kitchen ",kitw/15)
print("length of stairs",stal/15)
print("Width of stairs",staw/15)
print("length of drawing",drawl/15)
print("Width of drawing",draww/15)
print("length of Dining ",dinl/15)
print("Width of Dining",dinw/15)
print("length of entry ",entl/15)
print("Width of entry",entw/15)
print("length of store ",stol/15)
print("Width of store",stow/15)
print("length of ots ",otsl/15)
print("Width of ots",otsw/15)
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()