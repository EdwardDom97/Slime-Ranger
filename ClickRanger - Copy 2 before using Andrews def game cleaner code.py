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
attack_icon = pygame.image.load('graphics/attack_button.png')



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
ground_rect = ground.get_rect(midleft = ( 332, 316))


#in-game button rects
menubutt_rect = menubutton.get_rect(midleft = (50, 150))
spellbutt_rect = drawspellbutton.get_rect(midleft = (50, 300))
attack_icon_rect = attack_icon.get_rect(midleft = (250, 432))

#in-game card rects
manashot_rect = manashot.get_rect(topleft = (360, 375))
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
    current_state = ""

    cards_drawn = 0

    #I am going to define player health and enemy slime health here to use pygame rects as hp bars
    player_health = 150
    earthslime_health = 100

    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
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
                

        # No check for current_state, so occurs regardless of state
        if menubutt_rect.collidepoint((mx, my)):
            print("Hey there is collision")
            if click:
                return  # Goes back to main menu, as it is the one that calls game

        #I assume this is where I put my attack button code
        if attack_icon_rect.collidepoint((mx,my)):
            print('collision is working boss')
            if click:
                print('click but no boom')
                earthslime_health -= 10
        

            
        # Only occurs in blank state
        if current_state == "":
            if spellbutt_rect.collidepoint((mx, my)):
                if click:
                    current_state = "drawing_card"
            if attack_icon_rect.collidepoint((mx, my)):
                if click:
                    earthslime_health -= 10
                    if earthslime_health <= 80:
                        print('health is going down with no visual')
        

        # Only occurs when drawing card
        elif current_state == "drawing_card":
            if cards_drawn <= 1 and spellbutt_rect.collidepoint((mx, my)):
                if click:
                    cards_drawn += 1

      
    

        # Always draw the following
        screen.fill("lightgray")
        screen.blit(cardpanimg, cardpanimg_rect)
        screen.blit(player_image, player_rect)
        screen.blit(earthslime, earthslime_rect)
        screen.blit(ground, ground_rect)
        screen.blit(attack_icon, attack_icon_rect)

        
        #Here I want to load in my health bars
        player_health_base = pygame.Rect(332, 200, 150, 25)
        player_health_active = pygame.Rect(332, 200, player_health, 25)

        earthslime_health_base = pygame.Rect(675, 200, 100, 25)
        earthslime_health_active = pygame.Rect(675, 200, earthslime_health, 25)
        
        
        # want to add my 'draw' button 'menu' button and card(s).
        screen.blit(menubutton, menubutt_rect)
        screen.blit(drawspellbutton, spellbutt_rect)
        screen.blit(topcard, topcard_rect)

        
        # Here I am drawing instead of blitting my health bars
        pygame.draw.rect(screen, (200, 15, 15), player_health_base)
        pygame.draw.rect(screen, (15, 200, 15), player_health_active)

        pygame.draw.rect(screen, (200, 15, 15), earthslime_health_base)
        pygame.draw.rect(screen, (15, 200, 15), earthslime_health_active)

        #if attack_icon_rect.collidepoint((mx,my)):
            #earthslime_health -= 10
        

        # Only blits when "drawing_card"
        if current_state == "drawing_card":
            screen.blit(manashot, manashot_rect)

        pygame.display.update()
                
        #return
    
        
 
main_menu()


