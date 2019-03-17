import pygame,sys
from pygame.locals import *
FPS = 30
WINDOWHEIGHT = 700
WINDOWWIDTH = 700
BLACK=(0,0,0,128)
GRAY = (100, 100, 100)
NAVYBLUE = ( 60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0,128)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255,0,255,128)
CYAN = (0, 255, 255)
TAN=(210,180,140)
def NextWin():
    VsCompImg=pygame.image.load('1 Player.png')
    VsCompRect=VsCompImg.get_rect()
    VsPlayerImg=pygame.image.load('2 Player.png')
    VsPlayerRect=VsPlayerImg.get_rect()
    VsCompRect.center=(WINDOWWIDTH/2,WINDOWHEIGHT/2-80)
    VsPlayerRect.center=(WINDOWWIDTH/2,WINDOWHEIGHT/2+180)
    FirstWin.blit(VsCompImg,VsCompRect)
    FirstWin.blit(VsPlayerImg,VsPlayerRect)
    while(True):
        for event in pygame.event.get():
            if(event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE)):
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mox, moy = event.pos
                if(VsPlayerRect.collidepoint(mox,moy)):
                    import Gameplay
        pygame.display.update()
        FPSClock.tick(FPS)
def First():
    global FPSClock,FirstWin
    pygame.font.init()
    FPSClock=pygame.time.Clock()
    FirstWin=pygame.display.set_mode((WINDOWHEIGHT,WINDOWWIDTH))
    OthelloImg=pygame.image.load('Othello.jpg')
    OthelloImg = pygame.transform.scale(OthelloImg, (700, 700))
    NewGameImg=pygame.image.load('Button.png')
    NewGameRect=NewGameImg.get_rect()
    NewGameObj = pygame.font.Font('calibri.ttf', 32)
    NewGameSurfaceObj = NewGameObj.render('New Game', True,BLACK,TAN)
    NewGameRectObj = NewGameSurfaceObj.get_rect()
    NewGameRectObj.center = (WINDOWWIDTH/2,300)
    ExitImg=pygame.image.load('Button.png')
    ExitRect=ExitImg.get_rect()
    ExitObj = pygame.font.Font('calibri.ttf', 32)
    ExitSurfaceObj = ExitObj.render('Exit', True,BLACK,TAN)
    ExitRectObj = ExitSurfaceObj.get_rect()
    ExitRectObj.center = (WINDOWWIDTH/2,400)
    pygame.init()
    pygame.display.set_caption('OTHELLO')
    FirstWin.fill(WHITE)
    NewGameRect.center=(WINDOWWIDTH/2,300)
    ExitRect.center=(WINDOWWIDTH/2,400)
    FirstWin.blit(OthelloImg,(0,0))
    FirstWin.blit(NewGameImg,NewGameRect)
    FirstWin.blit(ExitImg,ExitRect)
    FirstWin.blit(NewGameSurfaceObj,NewGameRectObj)
    FirstWin.blit(ExitSurfaceObj,ExitRectObj)
    while(True):
        for event in pygame.event.get():
            if(event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE)):
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mx, my = event.pos
                if(NewGameRect.collidepoint(mx,my)):
                    FirstWin.blit(OthelloImg,(0,0))
                    NextWin()
                elif(ExitRect.collidepoint(mx,my)):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        FPSClock.tick(FPS)
First()
