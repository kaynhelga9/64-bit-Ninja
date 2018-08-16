import pygame
import random
import time

#color wheel
colors = {'black': (0,0,0), 'white': (255,255,255), 'blue': (0,102,255), 'green': (0,204,0), 'red': (204,0,0), 'hotpink': (255,96,96), 'lightgreen': (96,255,96)}

paused = False
  
class Settings():
    def __init__(self):
        self.dispW = 800
        self.dispH = 500
        self.bgc = colors['white']

class Ninja():
    def __init__(self):
        self.Width = 26
        self.Height = 26
        self.idle = pygame.image.load('./idle1.png')

class Rain():
    def __init__(self):
        self.X = random.randrange(30, sts.dispW)
        self.Y = -(random.randint(200,600))
        self.Width = 3
        self.Height = 5
        self.Speed = random.randint(2,7)
        self.color = colors['blue']

def intro(d,w):
    font = pygame.font.SysFont('candara.ttf', 50)
    text = font.render('Welcome to 64-bit Ninja',True, colors['black'])
    textRect = text.get_rect(center=(sts.dispW/2, sts.dispH/2-100))
    exitIntro = False
    while exitIntro is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop(d, w)  
                #elif event.key == pygame.k_
                #    gameLoop(d)
        fillscr(disp)
        dead(d)
        won(w)
        disp.blit(text, textRect)
        instruction()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 200 < mouse[0] < 300 and 250 < mouse[1] < 300:
            pygame.draw.rect(disp, colors['lightgreen'], (sts.dispW/2-200, sts.dispH/2, 100, 50))
            if click[0] == 1:
                gameLoop(d,w)
        else: 
            pygame.draw.rect(disp, colors['green'], (sts.dispW/2-200, sts.dispH/2, 100, 50))
        if 500 < mouse[0] < 600 and 250 < mouse[1] < 300:
            pygame.draw.rect(disp, colors['hotpink'], (sts.dispW/2+100, sts.dispH/2, 100, 50))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(disp, colors['red'], (sts.dispW/2+100, sts.dispH/2, 100, 50))
        buttonText('Play', 'Quit')
        pygame.display.update()

def pause(d,w):
    fillscr(disp)
    global paused
    font = pygame.font.SysFont('candara.ttf', 50)
    text = font.render('Paused',True, colors['black'])
    textRect = text.get_rect(center=(sts.dispW/2, sts.dispH/2-100))
    while paused is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
        disp.blit(text, textRect)
        dead(d)
        won(w)
        instruction()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 200 < mouse[0] < 300 and 250 < mouse[1] < 300:
            pygame.draw.rect(disp, colors['lightgreen'], (sts.dispW/2-200, sts.dispH/2, 100, 50))
            if click[0] == 1:
                paused = False
        else: 
            pygame.draw.rect(disp, colors['green'], (sts.dispW/2-200, sts.dispH/2, 100, 50))
        if 500 < mouse[0] < 600 and 250 < mouse[1] < 300:
            pygame.draw.rect(disp, colors['hotpink'], (sts.dispW/2+100, sts.dispH/2, 100, 50))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(disp, colors['red'], (sts.dispW/2+100, sts.dispH/2, 100, 50))
        buttonText('Continue', 'Quit')
        pygame.display.update()
    
def buttonText(text1, text2):
    font = pygame.font.SysFont('candara.ttf', 25)
    text1 = font.render(text1, True, colors['white'])
    text2 = font.render(text2, True, colors['white'])
    textRect1 = text1.get_rect(center=(sts.dispW/2-150, sts.dispH/2+25))
    textRect2 = text2.get_rect(center=(sts.dispW/2+150, sts.dispH/2+25))
    disp.blit(text1, textRect1)
    disp.blit(text2, textRect2)

def instruction():
    font = pygame.font.SysFont('candara.ttf', 25)
    text1 = font.render('Move: Arrow Keys', True, colors['black'])
    text2 = font.render('Pause: Space Bar', True, colors['black'])
    text3 = font.render('Goal: Reach Right Side Of Screen', True, colors['black'])
    textRect1 = text1.get_rect(center=(sts.dispW/2-150, sts.dispH/2+100))
    textRect2 = text2.get_rect(center=(sts.dispW/2+150, sts.dispH/2+100))
    textRect3 = text3.get_rect(center=(sts.dispW/2, sts.dispH/2+150))
    disp.blit(text1, textRect1)
    disp.blit(text2, textRect2)
    disp.blit(text3, textRect3)

def njdisplay(tp):
    disp.blit(ninja1.idle, (tp))

def fillscr(disp):
    disp.fill(sts.bgc)
    pygame.draw.rect(disp, colors['green'], (0,475,sts.dispW,200))

def dispMessage(text):
    font = pygame.font.SysFont('candara.ttf', 50)
    text = font.render(text, True, colors['black'])
    textRect = text.get_rect(center=(sts.dispW/2, sts.dispH/2-100))
    disp.blit(text, textRect)
    pygame.display.update()
    time.sleep(2)

def dead(num):
    font = pygame.font.SysFont('candara.ttf', 25)
    text = font.render('Deaths:' + str(num), True, colors['black'])
    disp.blit(text, (sts.dispW-100,0))

def won(num):
    font = pygame.font.SysFont('candara.ttf', 25)
    text = font.render('Wins:' + str(num), True, colors['black'])
    disp.blit(text, (sts.dispW-180,0))

def startRain(rainX, rainY, rainW, rainH, color):
    pygame.draw.rect(disp, color, [rainX, rainY, rainW, rainH])

def dodged(count):
    font = pygame.font.SysFont('candara.ttf', 25)
    text = font.render('Dodged: ' + str(count), True, colors['black'])
    disp.blit(text, (0,0))

def collision(ax, ay, aw, ah, bx, by, bw, bh):
    return (ax < bx+bw and ay < by+bh and bx < ax+aw and by < ay+ah)

def crash(theRain, died, w):
    dispMessage('You Lost')
    for rain in theRain:
        rain.Y = -(random.randint(300,600))
    intro(died, w)

#game loop
def gameLoop(d,w):
    global paused
    exitLoop = False
    ninjaX = (sts.dispW * 0.01)
    ninjaY = (sts.dispH * 0.9)
    move = 0
    rainDodged = 0
    while exitLoop is False:
        fillscr(disp)
        #keys logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move = 4
                elif event.key == pygame.K_LEFT:
                    move = -4
                elif event.key == pygame.K_SPACE:
                    paused = True
                    pause(d, w)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    move = 0
            
        #move / if sprite hits right edge of screen -> win & exit / update rain pos
        ninjaX += move
        for rain in rains:
            rain.Y += rain.Speed    
        #display
        for rain in rains:
            startRain(rain.X, rain.Y, rain.Width, rain.Height, rain.color)
        njdisplay((ninjaX, ninjaY))
        dodged(rainDodged)
        dead(d)
        won(w)

        #logic
        if ninjaX > (sts.dispW):
            dispMessage('You Win')
            won(w+1)
            for rain in rains:
                rain.Y = -(random.randint(300,600)) 
            intro(d, w+1)
        for rain in rains:
            if rain.Y >= (sts.dispH-25):
                rain.Y = -(random.randint(200,600))
                rain.X = random.randrange(30, sts.dispW)
                rainDodged += 1
                if len(rains)<100 and rainDodged>=100:
                    rains.append(Rain())
        for rain in rains:
            if collision(ninjaX, ninjaY, ninja1.Width, ninja1.Height, rain.X, rain.Y, rain.Width, rain.Height):
                dead(d+1)
                crash(rains, (d+1), w)

        #update screen
        pygame.display.update()
        clock.tick(60)

#init
pygame.init()
sts = Settings()
ninja1 = Ninja()
rains = [Rain() for i in range(80)]
pygame.display.set_caption('64-bit Ninja')
gameIcon = pygame.image.load('./icon.png')
pygame.display.set_icon(gameIcon)
disp = pygame.display.set_mode((sts.dispW, sts.dispH))
clock = pygame.time.Clock()

#run / quit 
intro(0,0)
pygame.quit()
quit()
