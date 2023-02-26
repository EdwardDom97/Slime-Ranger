#Click Rangers Code rework for better menu, still V 0.01

import pygame, sys

from pygame.locals import *

pygame.init()

pygame.display.set_caption('Click Ranger V 0.01')
screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)
font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()


#sounds
#menuloop = pygame.mixer.music.load('gameloop.wav')
#pygame.mixer.music.play(-1)


# menuimages
menulogo = font.render("Click Ranger V 0.01", False, (65, 67, 69))
start_button = pygame.image.load('graphics/startbutton.png')
options_button = pygame.image.load('graphics/optionsbutton.png')
exit_button = pygame.image.load('graphics/exitbutton.png')
spell_library_button = pygame.image.load('graphics/librarybutton.png')



#in-game images
player_image = pygame.image.load('graphics/player.png')
earthslime = pygame.image.load('graphics/earthslime.png')
menubutton = pygame.image.load('graphics/menubutton.png')
drawspellbutton = pygame.image.load('graphics/drawspellbutton.png')
ground = pygame.image.load('graphics/grass.png')



#in-game cards
manashot = pygame.image.load('graphics/cards/manashot.png')
topcard = pygame.image.load('graphics/cards/cardback.png')
cardpanimg = pygame.image.load('graphics/cards/cardpanel.png')



#menubuttonrects
start_button_rect = start_button.get_rect(midleft = (50,250))
menulogo_rect = menulogo.get_rect(midleft = (50, 150))
options_rect = options_button.get_rect(midleft = (50, 350))
exit_rect = exit_button.get_rect(midleft = (50, 550))
spelllib_rect = spell_library_button.get_rect(midleft = (50, 450))

#my in-game player and slime rect locations, eventually want to set equal to distance of screen for resizing properly
player_rect = player_image.get_rect(midbottom = (350, 300))
earthslime_rect = earthslime.get_rect(midbottom = (750, 300))
menubutt_rect = menubutton.get_rect(midleft = (50, 150))
spellbutt_rect = drawspellbutton.get_rect(midleft = (50, 300))
ground_rect = ground.get_rect(midleft = ( 332, 316))

#in-game card rects
manashot_rect = manashot.get_rect(topleft = (550, 395))
topcard_rect = topcard.get_rect(topleft = (50, 375))
cardpanimg_rect = cardpanimg.get_rect(midleft = (0, 480))


click = False

spell_library = ['']

def main_menu():
    while True:
        screen.fill('grey')
        screen.blit(start_button, start_button_rect)
        screen.blit(menulogo, menulogo_rect)
        screen.blit(options_button, options_rect)
        screen.blit(exit_button, exit_rect)
        screen.blit(spell_library_button, spelllib_rect)

        mx,my = pygame.mouse.get_pos()

        if start_button_rect.collidepoint((mx, my)):
            #print('Hey james there is collision')
            if click:
                game()
        


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            #if event.type == VIDEORESIZE:
                #screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
 
        pygame.display.update()
        clock.tick(0)


#

def game():
    running = True
    while running:
        mx,my = pygame.mouse.get_pos()
        click = False

        
        screen.fill('lightgray')
        screen.blit(cardpanimg, cardpanimg_rect)
        screen.blit(player_image, player_rect)
        screen.blit(earthslime, earthslime_rect)
        screen.blit(ground, ground_rect)
        #want to add my 'draw' button 'menu' button and card(s).
        screen.blit(menubutton, menubutt_rect)
        screen.blit(drawspellbutton, spellbutt_rect)
        #screen.blit(manashot, manashot_rect)
        screen.blit(topcard, topcard_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if menubutt_rect.collidepoint((mx, my)):
                print('Hey there is collision')
                if click:
                    main_menu()
        
            if spellbutt_rect.collidepoint((mx, my)):
                if click:
                    screen.blit(manashot, manashot_rect)
                    draw_card()
                   
            pygame.display.update()
            clock.tick(0)


def draw_card():
    running = True
    while running:
        mx,my = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        
        cards_drawn = 0
        if cards_drawn <= 1 and spellbutt_rect.collidepoint((mx,my)):
            if click:
                screen.blit(manashot, manashot_rect)
                cards_drawn += 1
                print('it is stuck in this loop')
                pygame.display.update()
                
                return
    
        
 
main_menu()


