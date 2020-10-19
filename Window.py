import pygame
import os
from Utility.Board import button
from man.main import human
from AI.main import computer
from AivsAi.main import comp
from Utility.path import path1

wid,hei=500,500
rows,cols=8,8
block_size=wid//hei
#Orange=(255, 128, 0)
WHITE=(255,255,255)
Orange=(0,255,255)
FPS=60
pygame.init()
win = pygame.display.set_mode((wid, hei))

pygame.display.set_caption('Checkers-IIT2018202')
pic = pygame.image.load(path1)
#pic = pygame.image.load("/home/nkit/Desktop/Submit/checker_master/man/kingimage/B.png")

#def redrawwindow():

def main():
    run =True
    clock = pygame.time.Clock()
    B=button(WHITE,50,250,150,50,'Human vs Human')
    B2=button(WHITE,300,250,150,50,'Ai vs Human')
    B3=button(WHITE,175,350,150,50,'Ai vs Ai')
    while run:
        #win.fill((255,255,255))
        #win.fill((75, 139, 190))
        win.blit(pygame.transform.scale(pic, (500,500)), (0,0))
        #pygame.display.flip()
        B.draw(win,(0,0,0))
        B2.draw(win,(0,0,0))
        B3.draw(win,(0,0,0))
        pygame.display.update()
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                quit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if B.isOver(pos):
                    B.color=(255,0,0)
                    obj=human()
                    obj.start()
                elif B2.isOver(pos):
                    B2.color=(255,0,0)
                    obj2=computer()
                    obj2.start()
                elif B3.isOver(pos):
                    B3.color=(255,0,0)
                    obj3=comp()
                    obj3.start()
                else:
                    B3.color=(0,255,0)
                   
    pygame.quit()

main()