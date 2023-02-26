#This is going to be my work project, I am ideally thinking this will be the clickbase
#or turn base 8bit or 16 bit style

import pygame, sys
from pygame.locals import *


pygame.init()
test_font = pygame.font.Font(None, 50)

pygame.display.set_caption('Click Rangers V 0.01 TRISTAN DOMBROSKI')
#I want to load my basic images here
#player = pygame.image.load('player.png')
screen = pygame.display.set_mode(size = (800, 600))
screen.fill('lightgray')

introbutton = test_font.render("Click Rangers", False, (125,100,100))
introbutton_rect = introbutton.get_rect(midleft = (50,150))
#screen.fill('gray')
screen.blit(introbutton, introbutton_rect)


running = True


def main_menu():


    main_menu()



while True:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if running:
        #screen.fill('grey')
        #screen.blit(introbutton, introbutton_rect)
        

        pygame.display.update()
