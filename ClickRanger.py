#Click Rangers Code rework for better menu, still V 0.01, which is now v 0.02 as of 2/11/23.
#Making an edit for Click Ranger on 04/23/2023 called "The Wilds" I am adding in another button and game state that will simply allow the player the move around and jump.
#This is to prepare for an idea I have had in the back of my mind since my last good run with coding

import pygame, sys
import random
import time
#import time to actually work on this

from pygame.locals import *

pygame.init()

pygame.display.set_caption('Click Ranger V 0.04') #yay we are now 0.01 away from the creation, 1 week in
screen = pygame.display.set_mode((800,600), 0, 32)
font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()


#sounds I am bad at making music
#menuloop = pygame.mixer.music.load('gameloop.wav')
#pygame.mixer.music.play(-1)


# menuimages
menuintro = font.render("Click Ranger V 0.04 'The Wilds'", False, (65, 67, 69))
start_button = pygame.image.load('graphics/startbutton.png')
options_button = pygame.image.load('graphics/optionsbutton.png')
exit_button = pygame.image.load('graphics/exitbutton.png')
spell_library_button = pygame.image.load('graphics/librarybutton.png')
menulogo = pygame.image.load('graphics/menulogo.png')
the_wilds_button = pygame.image.load('graphics/thewildsbutton.png')


menuintro_rect = menuintro.get_rect(midleft = (50, 125)) #this is not a button it's the 'background' to the text

#menubuttonrects, I want my buttons listed in order as they also appear on my menu in-game.

start_button_rect = start_button.get_rect(midleft = (50,200)) #starts a card combat game. idea to rename as I go.
the_wilds_rect = the_wilds_button.get_rect(midleft=(50, 275))
options_rect = options_button.get_rect(midleft = (50, 365))
exit_rect = exit_button.get_rect(midleft = (50, 550))
spelllib_rect = spell_library_button.get_rect(midleft = (50, 450))
menulogo_rect = menulogo.get_rect(topleft = (325, 200))

#Spells Menu images
bookofspells = pygame.image.load('graphics/bookospells.png')

#Spells Menu Rects (undecided if needed)
bookofspells_rect = bookofspells.get_rect(topleft = (1,1))

#in-game images (player, slime, ground, future background, ect.)
player_image = pygame.image.load('graphics/player.png')
earthslime = pygame.image.load('graphics/earthslime.png')
ground = pygame.image.load('graphics/grass.png')
player_level_icon = pygame.image.load('graphics/playerlevelicon.png')
enemy_level_icon = pygame.image.load('graphics/enemylevelicon.png')



#my in-game player and slime rect locations, eventually want to set equal to distance of screen for resizing properly
ground_rect = ground.get_rect(midleft = (100, 265))
player_rect = player_image.get_rect(midbottom = (110, 250))
playerlevelicon_rect = player_level_icon.get_rect(topleft = (110, 270))
earthslime_rect = earthslime.get_rect(midbottom = (450, 250))
enemylevelicon_rect = enemy_level_icon.get_rect(topleft = (435, 270))

#in-game buttons
menubutton = pygame.image.load('graphics/menubutton.png')
drawspellbutton = pygame.image.load('graphics/drawspellbutton.png')

#attack_icon = pygame.image.load('graphics/attack_button.png')
castaspell_button = pygame.image.load('graphics/castspellbutton.png')
strike_button = pygame.image.load('graphics/strikebutton.png')
end_turn_button = pygame.image.load('graphics/endturnbutton.png')
igattack_icon = pygame.image.load('graphics/ingamegraphics/igattack.png')

#in-game button rects
endturnbutt_rect = end_turn_button.get_rect(midleft = (250, 150))
spellbutt_rect = drawspellbutton.get_rect(midleft = (250, 392))
castaspell_rect = castaspell_button.get_rect(midleft = (250, 445))
strike_button_rect = strike_button.get_rect(midleft = (250, 497))
menubutt_rect = menubutton.get_rect(midleft = (250, 550))
#attack_icon_rect = attack_icon.get_rect(midleft = (750, 432))



#in-game cards that I could also set as a library.
manashot = pygame.image.load('graphics/cards/manashot.png')
topcard = pygame.image.load('graphics/cards/cardback.png')
cardpanimg = pygame.image.load('graphics/cards/cardpanel.png')
healthdrop = pygame.image.load('graphics/cards/healthdrop.png')
sipomana = pygame.image.load('graphics/cards/sipomana.png')
fireball_shot = pygame.image.load('graphics/cards/fireball.png')

#in-game card rects
#keep location same for all cards .get_rect(topleft = (505, 370))
manashot_rect = manashot.get_rect(topleft = (485, 370))
healthdrop_rect = healthdrop.get_rect(topleft = (485, 370))
sipomana_rect = sipomana.get_rect(topleft = (485, 370))
topcard_rect = topcard.get_rect(topleft = (50, 375))
casted_spell_rect = topcard.get_rect(topleft = (485, 370))
fireball_shot_rect = fireball_shot.get_rect(topleft = (485, 370))
cardpanimg_rect = cardpanimg.get_rect(midleft = (0, 445))

#going to try to create a list here and use the random code. will do two to start.

spell_library = [(manashot, manashot_rect), (healthdrop, healthdrop_rect),(fireball_shot,fireball_shot_rect)]
#random_spell = random.choice(spell_library)

click = False


def main_menu(): 
    while True:
        
        screen.fill('grey')
        screen.blit(menuintro, menuintro_rect)
        screen.blit(the_wilds_button, the_wilds_rect)
        screen.blit(start_button, start_button_rect)
        screen.blit(menulogo, menulogo_rect)
        screen.blit(options_button, options_rect)
        screen.blit(exit_button, exit_rect)
        screen.blit(spell_library_button, spelllib_rect)

        mx,my = pygame.mouse.get_pos()


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

            if start_button_rect.collidepoint((mx, my)):
                #print('Hey james there is collision')
                if click:
                    game()

            if options_rect.collidepoint((mx, my)):
                if click:
                    options()
            

            if spelllib_rect.collidepoint((mx, my)):
                if click:
                    spells_library()

            if exit_rect.collidepoint((mx,my)):
                if click:
                    pygame.quit()
                    sys.exit()


            if the_wilds_rect.collidepoint((mx,my)):
                if click:
                    enter_wilds()

                    
         
        pygame.display.update()
        clock.tick(0)


#

def game(): #reworked enough to be called my own again. 
    current_state = "Existing"
    
    

 
        

    if current_state == "Existing": #anything I set before existing will become updated in existing.

        #I need to reorganize some of my variables but will do later

        player_health = 150
        enemy_health = 100 
        spell_active = 'None'
        card_active = False
        casts = 0
        game_round = 0 #ignoring might remove
        cards_drawn = 0
        running = True       
        player_level = 0
        earthslime_level = 0

        #this is where I will make my enemy attack variable
        enemy_attacking = True
        enemy_attack_timer = 3
        enemy_charge_attack = 0

        # Always draw the following
        screen.fill("lightgray")
        screen.blit(cardpanimg, cardpanimg_rect)
        
        screen.blit(player_image, player_rect)
        #screen.blit(player_level_icon, playerlevelicon_rect)
        
        screen.blit(earthslime, earthslime_rect)
        #screen.blit(enemy_level_icon, enemylevelicon_rect)

        
        screen.blit(ground, ground_rect)

        # want to add my 'draw' button 'menu' button and card(s).
        screen.blit(menubutton, menubutt_rect)
        screen.blit(drawspellbutton, spellbutt_rect)
        screen.blit(topcard, topcard_rect)
            
        #screen.blit(attack_icon, attack_icon_rect)
        screen.blit(strike_button, strike_button_rect)
        screen.blit(castaspell_button, castaspell_rect)
        #screen.blit(end_turn_button, endturnbutt_rect)

        
        
        while running:
            #earthslime_health = 100 + int(earthslime_level * 2)
            mx, my = pygame.mouse.get_pos()
            click = False
            enemy_attacking = True
            

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
                #print("Hey there is collision")
                if click:
                    return  # Goes back to main menu, as it is the one that calls game
                
            # Only occurs in blank state
            
                
            if spellbutt_rect.collidepoint((mx, my)):
                if click:
                    if card_active != True:
                        random_spell = random.choice(spell_library)
                        print('there is a card on display')                    
                        print('you have drawn', cards_drawn)
                        screen.blit(random_spell[0],random_spell[1])
                        
                        #screen.blit(manashot,manashot_rect)#change from spell button to end turn button stat
                        cards_drawn += 1
                        card_active = False

                        if cards_drawn % 3 == 0:
                            player_health -= 10


                        if random_spell == (manashot, manashot_rect):
                            print('manashot was drawn')
                            spell_active = 'manashot'
                    
                        if random_spell == (healthdrop, healthdrop_rect):
                            print('healthdrop was drawn')
                            spell_active = 'healthdrop'

                        if random_spell == (fireball_shot, fireball_shot_rect):
                            print('fireball shot was drawn')
                            spell_active = 'fireball_shot'
            
                        
            if strike_button_rect.collidepoint((mx, my)) and click:
                enemy_health -= 10
                player_health += 1
                
            if castaspell_rect.collidepoint((mx, my)):
                if click:
                    if card_active != True:
                        if spell_active == 'manashot':
                            enemy_health -= 10
                            player_health += 2
                            screen.blit(topcard, casted_spell_rect)
                            casts += 1                   
                            print('your casts are',  casts)
                            spell_active = 'None'
                            
                        if spell_active == 'healthdrop':
                            player_health += 10
                            screen.blit(topcard, casted_spell_rect)
                            casts += 1                   
                            print('your casts are',  casts)
                            spell_active = 'None'
                            
                        if spell_active == 'fireball_shot':
                            enemy_health -= 15
                            player_health += 2
                            screen.blit(topcard, casted_spell_rect)
                            casts += 1                   
                            print('your casts are',  casts)
                            spell_active = 'None'
                        
                        card_active = False
                        #player_health -= 10
                        #enemy_turn()
                        #I want to do something here to signify turn
                        #current_state = "player_turn"            
          

            if player_health <= 0:
                return
               
                
            if enemy_health <= 0:
                earthslime_level += 1
                enemy_health = 100 
                player_level += 1
                print("the earthslime is Level", earthslime_level)
                print("the player is Level", player_level)
                print(enemy_health)
                player_health -= 25

            if player_health >= 150:
                player_health = 150
            
           
            #if current_state == "Enemy Attacking":


                #current_state = "passive"

            #I am going to define player health and enemy slime health here to use pygame rects as hp bars


            #Here is where I am going to test/put my if statement for enemy attacks
            
            #if enemy_attacking:
            #    enemy_charge_attack += 1
            #    pygame.time.delay(200)

            #    if enemy_charge_attack == enemy_attack_timer:
            #        player_health -= 2
            #       enemy_charge_attack = 0

                 
                
                    
            
        


            
            # Here I want to load in my health bars
            player_health_base = pygame.Rect(100, 175, 150, 27)
            player_health_active = pygame.Rect(100, 175, player_health, 27)
            earthslime_health_base = pygame.Rect(435, 175, 100, 27)
            earthslime_health_active = pygame.Rect(435, 175, enemy_health, 27)
            
            # Here I want to load text to add to my health bars
            health_text = font.render("Hp: " + str(player_health), False, (65,67,69))
            health_text_rect = health_text.get_rect(topleft = (100,173))

            
            # Here I am drawing instead of blitting my health bars
            pygame.draw.rect(screen, (200, 15, 15), player_health_base)
            pygame.draw.rect(screen, (15, 200, 15), player_health_active)

            pygame.draw.rect(screen, (200, 15, 15), earthslime_health_base)
            pygame.draw.rect(screen, (15, 200, 15), earthslime_health_active)

            #here I am going to draw/render/blit my health text to the rects.
            screen.blit(health_text, health_text_rect)


            #down here is where I can handle all my active/in game events like levels and displaying player/enemy damage
               
            #currentplayerlevel = font.render(str(player_level), False, (65, 67, 69))
            #currentpl_rect = currentplayerlevel.get_rect(midleft = (140, 248))
            #screen.blit(player_level_icon, playerlevelicon_rect)
            #screen.blit(currentplayerlevel, currentpl_rect)        
           
        
            
            pygame.display.update()
            clock.tick(30)


def enter_wilds():
    screen.fill("darkgray")
    wildsbackground = pygame.image.load('graphics/wildsbg.png')
    
        
    screen.blit(menubutton, menubutt_rect)
    screen.blit(wildsbackground, (0,0))
    screen.blit(menubutton,menubutt_rect)
    screen.blit(player_image, (50,450))
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

                #movement will have to come when my mind has refreshed or whenver I get the time again. Honestly I am surprised I did this much this evening.
                        
            if event.type == MOUSEBUTTONDOWN:
                    
                if event.button == 1:
                    click = True
                

            # No check for current_state, so occurs regardless of state
            if menubutt_rect.collidepoint((mx, my)):
                #print("Hey there is collision")
                if click:
                    return  # Goes back to main menu, as it is the one that calls game
                

        pygame.display.update()






def spells_library():
    
    screen.fill("lightgray")
        
    screen.blit(menubutton, menubutt_rect)
    screen.blit(bookofspells, bookofspells_rect)
    running = True
    
    while running:
        
            
        mx, my = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                
                    
            if event.type == KEYDOWN:
                    
                if event.key == K_ESCAPE:
                        running = False
                        
            if event.type == MOUSEBUTTONDOWN:
                    
                if event.button == 1:
                    click = True
                

            # No check for current_state, so occurs regardless of state
            if menubutt_rect.collidepoint((mx, my)):
                #print("Hey there is collision")
                if click:
                    return  # Goes back to main menu, as it is the one that calls game
                

        pygame.display.update()

def options():
    screen.fill("lightgray")
        
    screen.blit(menubutton, menubutt_rect)
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
                #print("Hey there is collision")
                if click:
                    return  # Goes back to main menu, as it is the one that calls game
                

        pygame.display.update()

            
main_menu()


#CHANGES AND BUGS AND TODO LIST
#make a card timer 2/15/23 NULL 02/21/23
#make an options menu and a spells menu 02/21/23
#
