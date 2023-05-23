#I want to store my Card_Duel code from my initial project Click Ranger and store it here for a later date in time
#ultimately I will have two seperate games, Slime Ranger which is a 2d platformer, and Click Ranger which is a click-based
#dungeon game with cards. Both games will have similar elements and will draw inspiration from each other.


#THIS IS A NOTE FOR MYSELF THAT I COPIED THE ENTIRE VERSION OF CLICK RANGER 0.0.5 AND PASTED IT HERE, I WILL DELETE THIS CODE FROM THE OTHER ONE SO MY
#CARD GAME WILL ONLY EXIST HERE PAST THIS POINT.



import pygame, sys
import random
import time
import math
#import time to actually work on this

from pygame.locals import *

pygame.init()
screen_width = 1600
screen_height = 900
pygame.display.set_caption('Slime Ranger V 0.05 "ENTER VILLAGE"') #yay we are now 0.01 away from the creation, 1 week in
screen = pygame.display.set_mode((screen_width,screen_height), 0, 32)
font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()


#sounds I am bad at making music
#menuloop = pygame.mixer.music.load('gameloop.wav')
#pygame.mixer.music.play(-1)


# menuimages
menuintro = font.render("Click Ranger V 0.05 'ENTER THE VILLAGE!'", False, (180, 180, 165))
start_button = pygame.image.load('graphics/startbutton.png')
options_button = pygame.image.load('graphics/optionsbutton.png')
exit_button = pygame.image.load('graphics/exitbutton.png')
spell_library_button = pygame.image.load('graphics/librarybutton.png')
menulogo = pygame.image.load('graphics/menulogo.png')
the_wilds_button = pygame.image.load('graphics/thewildsbutton.png')


menuintro_rect = menuintro.get_rect(midleft = (50, 125)) #this is not a button it's the 'background' to the text

#menubuttonrects, I want my buttons listed in order as they also appear on my menu in-game.

#05/16/2023 I want to play with my menu button locations,perhaps try setting the x value as half of the width of the screen so it's centered. 

start_button_rect = start_button.get_rect(center = (screen_width/2,200)) #starts a card combat game. idea to rename as I go.
the_wilds_rect = the_wilds_button.get_rect(center = (screen_width/2,275))
options_rect = options_button.get_rect(center = (screen_width/2,350))
spelllib_rect = spell_library_button.get_rect(center = (screen_width/2,425))
exit_rect = exit_button.get_rect(center = (screen_width/2,500))
menulogo_rect = menulogo.get_rect(topleft = (325, 600))

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
help_button_icon = pygame.image.load('graphics/helpbutton.png')
#adding in the player level background to experiment with
playerlevelbackg = pygame.image.load('graphics/playerlevelbg.png')



#my in-game player and slime rect locations, eventually want to set equal to distance of screen for resizing properly
ground_rect = ground.get_rect(midleft = (100, 265))
player_rect = player_image.get_rect(midbottom = (110, 250))
playerlevelicon_rect = player_level_icon.get_rect(topleft = (110, 270))
earthslime_rect = earthslime.get_rect(midbottom = (450, 250))
enemylevelicon_rect = enemy_level_icon.get_rect(topleft = (435, 270))
help_button_rect = help_button_icon.get_rect(topleft = (325,150))
playerlevelbackg_rect = playerlevelbackg.get_rect(topleft = (100,50))


#in-game buttons
menubutton = pygame.image.load('graphics/menubutton.png')
drawspellbutton = pygame.image.load('graphics/drawspellbutton.png')
#attack_icon = pygame.image.load('graphics/attack_button.png')
castaspell_button = pygame.image.load('graphics/castspellbutton.png')
strike_button = pygame.image.load('graphics/strikebutton.png')
end_turn_button = pygame.image.load('graphics/endturnbutton.png')
igattack_icon = pygame.image.load('graphics/ingamegraphics/igattack.png')
player_info = pygame.image.load('graphics/ingamegraphics/ranger_card.png')


#in-game button rects
endturnbutt_rect = end_turn_button.get_rect(midleft = (250, 150))
spellbutt_rect = drawspellbutton.get_rect(midleft = (250, 392))
castaspell_rect = castaspell_button.get_rect(midleft = (250, 445))
strike_button_rect = strike_button.get_rect(midleft = (250, 497))
menubutt_rect = menubutton.get_rect(midleft = (250, 550))
#attack_icon_rect = attack_icon.get_rect(midleft = (750, 432))
player_info_rect = player_info.get_rect(center=(1000,425))



#in-game cards that I could also set as a library.
manashot = pygame.image.load('graphics/cards/manashot.png')
topcard = pygame.image.load('graphics/cards/cardback.png')
cardpanimg = pygame.image.load('graphics/cards/cardpanel.png')
healthdrop = pygame.image.load('graphics/cards/healthdrop.png')
sipomana = pygame.image.load('graphics/cards/sipomana.png')
fireball_shot = pygame.image.load('graphics/cards/fireball.png')
newcardpanel = pygame.image.load('graphics/cards/newercardpanel.png')

#in-game card rects
#keep location same for all cards .get_rect(topleft = (505, 370))
manashot_rect = manashot.get_rect(topleft = (485, 370))  
healthdrop_rect = healthdrop.get_rect(topleft = (485, 370))
sipomana_rect = sipomana.get_rect(topleft = (485, 370))
topcard_rect = topcard.get_rect(topleft = (50, 375))
casted_spell_rect = topcard.get_rect(topleft = (485, 370))
fireball_shot_rect = fireball_shot.get_rect(topleft = (485, 370))
cardpanimg_rect = cardpanimg.get_rect(midleft = (0, 445))
newcardpanel_rect = newcardpanel.get_rect(midleft=(0,screen_height/2))

#going to try to create a list here and use the random code. will do two to start.

spell_library = [(manashot, manashot_rect), (healthdrop, healthdrop_rect),(fireball_shot,fireball_shot_rect)]
#random_spell = random.choice(spell_library)

click = False


def main_menu(): 
    while True:
        
        mainmenusplash = pygame.image.load('graphics/mainscreensplash.png')

        screen.blit(mainmenusplash, (0,0))
        

        #screen.fill('grey')
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

        #seeing if I can load the player's level background here, update: it works now I need to get both text and image together.
        screen.blit(newcardpanel,newcardpanel_rect)

        screen.blit(playerlevelbackg,playerlevelbackg_rect)
        #screen.blit(cardpanimg, cardpanimg_rect)
        
        screen.blit(player_image, player_rect)
        #screen.blit(player_level_icon, playerlevelicon_rect)
        
        screen.blit(earthslime, earthslime_rect)
        #screen.blit(enemy_level_icon, enemylevelicon_rect)
        screen.blit(help_button_icon,help_button_rect)

        
        #screen.blit(ground, ground_rect)

        # want to add my 'draw' button 'menu' button and card(s).
        screen.blit(menubutton, menubutt_rect)
        screen.blit(drawspellbutton, spellbutt_rect)
        screen.blit(topcard, topcard_rect)
            
        #screen.blit(attack_icon, attack_icon_rect)
        screen.blit(strike_button, strike_button_rect)
        screen.blit(castaspell_button, castaspell_rect)
        #screen.blit(end_turn_button, endturnbutt_rect)

        #add in a keyevent for I, representing inventory, that when pressed shows the rangers card.
        
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

                    if event.key == pygame.K_i:
                        screen.blit(player_info,player_info_rect)
                        
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

                        if cards_drawn % 3 == 0:  #this exists to deal some kind of damage to the player, note that I need to implement a real combat system or turn it into a feature via monster cards.
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
            
                        
            if strike_button_rect.collidepoint((mx, my)) and click: #gives the players the opportunity to physically attack and restore health. helps balance mana.
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
                screen.blit(playerlevel_text, playerlevel_text_rect)
                current_state = "Existing"
                earthslime_level += 1
                enemy_health = 100 
                player_level += 1
                print("the earthslime is Level", earthslime_level)
                print("the player is Level", player_level)
                print(enemy_health)
                player_health -= 15

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

            #I can make player level appear in the same way
            playerlevel_text = font.render("Level: " +str(player_level), False, (10,10,10))
            playerlevel_text_rect = playerlevel_text.get_rect(center = (100,50))

            
            # Here I am drawing instead of blitting my health bars
            pygame.draw.rect(screen, (200, 15, 15), player_health_base)
            pygame.draw.rect(screen, (15, 200, 15), player_health_active)

            pygame.draw.rect(screen, (200, 15, 15), earthslime_health_base)
            pygame.draw.rect(screen, (15, 200, 15), earthslime_health_active)

            #here I am going to draw/render/blit my health text to the rects.
            screen.blit(health_text, health_text_rect)
            #screen.blit(playerlevel_text, playerlevel_text_rect)


            #down here is where I can handle all my active/in game events like levels and displaying player/enemy damage
               
            #currentplayerlevel = font.render(str(player_level), False, (65, 67, 69))
            #currentpl_rect = currentplayerlevel.get_rect(midleft = (140, 248))
            #screen.blit(player_level_icon, playerlevelicon_rect)
            #screen.blit(currentplayerlevel, currentpl_rect)        
           
        
            
            pygame.display.update()
            clock.tick(30)


def enter_wilds():

    player_score = 0 #also could be referred to as the number of enemies killed. I'm to implement a real inventory and items soon.
    vel = 6 #vel, short for velocity, could be called 'movement' but represents the rate at which it will move.
    gravity = 0.2
    player_gravity = 0.0
    jumping = False
    jump_count = 12
    can_jump = True
    jump_speed = 0.15
    enemy_gravity = 4
    ground_depth = 3
    ground_tile_height = 32
    magic_attacks = []
    enemy_list = []
    player_direction = 'right'
    spell_cast_timer = 0
    spell_speed = 10
    show_inventory = False
    #here I want all of my enemy variables
    max_slimes = 10
    current_slimes = 0
    spawn_timer = 0
    spawn_interval = 500
    
    
    
    #Here I want to load new images for my Environment, Player, enemies, and other entities, and then User Interface.
    #Environment
    groundtile = pygame.image.load('graphics/ingamegraphics/grassblock.png')
    undergroundtile = pygame.image.load('graphics/ingamegraphics/dirtblock.png')

    #Player, enemies, and others.
    players_image = pygame.image.load('graphics/player.png')
    earthslime_enemy = pygame.image.load('graphics/ingamegraphics/earthslime.png')
    magic_attack = pygame.image.load('graphics/ingamegraphics/manablast.png')
    sign_village = pygame.image.load('graphics/ingamegraphics/townsign.png')

    #the Inventory the player can see when they press 'i'
    player_inventory_image = pygame.image.load('graphics/ingamegraphics/playerinventory.png')
    inventoryexit_button = pygame.image.load('graphics/ingamegraphics/inventory_exit_button.png')


    #Here is where I handle the wilds in-game rects for player, enemies, and environment.
    #Environment rects, Player Rect.
    groundtile_rect = pygame.Rect(0, screen_height - 96, screen_width, 32)
    players_rect = players_image.get_rect(center = (250, 350))
    sign_rect = sign_village.get_rect(left =0, bottom = groundtile_rect.top)

    #Player inventory Rects
    player_inventory_rect = pygame.Rect(200,200, player_inventory_image.get_width(), player_inventory_image.get_height())
    inventoryexit_button_rect = pygame.Rect(player_inventory_rect.right - 32, player_inventory_rect.top, 30,30)

    #enemy rect for slime but can and will be updated later.
    enemy_rect = earthslime_enemy.get_rect()
    enemy_rect.x = random.randint(0, screen_width - enemy_rect.width)
    enemy_list.append(enemy_rect)


    running = True
    
    while running:

        elapsed_time = clock.tick(60)
        spell_cast_timer -= elapsed_time
        
        spawn_timer += elapsed_time
    
        screen.fill('darkgrey')
        screen.blit(menubutton,menubutt_rect)
        screen.blit(sign_village, sign_rect)
    

        for y in range(screen_height - ground_tile_height * ground_depth, screen_height, ground_tile_height):
            for x in range(0, screen_width, ground_tile_height):
                if y == screen_height - ground_tile_height * ground_depth:
                    screen.blit(groundtile, (x,y))
                else:  
                    screen.blit(undergroundtile, (x, y))

        player_gravity += gravity

        players_rect.y += player_gravity

        for enemy_rect in enemy_list:
            enemy_gravity = 4
            enemy_gravity += gravity
            enemy_rect.y += enemy_gravity
            screen.blit(earthslime_enemy, enemy_rect)
            #if enemy_rect.y > screen_height:
                #if the slime somehow goes off screen it will be removed
                #enemy_list.remove(enemy_rect)
                #current_slimes -= 1
                #continue
          
            if enemy_rect.colliderect(groundtile_rect):
                enemy_rect.y = groundtile_rect.y - enemy_rect.height  
                enemy_gravity = 0
                dx = players_rect.x - enemy_rect.x
                dy = players_rect.y - enemy_rect.y
                distance = math.sqrt(dx ** 2 + dy ** 2)
                

            # Adjust slime's x-coordinate towards the player (a mighty thanks to the chatgpt no shame in the game)
                if dx >= 50 or dx <= -50:
                    enemy_rect.x += vel * (dx / distance)


        #adding in a collision dectection to stop when the player touches the ground
        if players_rect.colliderect(groundtile_rect):
            players_rect.y = groundtile_rect.y - players_rect.height
            player_gravity = 0
            can_jump = True

        
        if jumping: #this is for the player might try to do something similar for my slime enemies.
            if jump_count >= -12:
                players_rect.y -= (jump_count * abs(jump_count)) * jump_speed
                jump_count -= .8
            else:
                jumping = False
                jump_count = 12
            
        mx, my = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                        
            if event.type == MOUSEBUTTONDOWN:
                    
                if event.button == 1:
                    click = True

                if event.button == 1 and show_inventory:
                    if inventoryexit_button_rect.collidepoint(event.pos):
                        show_inventory = False

    
            # No check for current_state, so occurs regardless of state, happens at anytime inside the for event in pygame.event.get():
            if menubutt_rect.collidepoint((mx, my)):
                #print("Hey there is collision")
                if click:
                    return  # Goes back to main menu, as it is the one that calls game

              
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]: #yay movement, this was more challening than initially though
            #print('left was pressed')
            players_rect.x -= vel + 1

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            players_rect.x += vel
        
        if keys[pygame.K_ESCAPE]:
            running = False
            main_menu()

        
        if keys[pygame.K_i]:
            show_inventory = True
    
        
        if show_inventory:
            screen.blit(player_inventory_image, player_inventory_rect)
            screen.blit(inventoryexit_button, inventoryexit_button_rect)

        if keys[pygame.K_UP] or keys[pygame.K_w] and can_jump: #jump is not that bad right now but there is a slight bug. Player can repeatedly jump until they are floating.
            jumping = True
            player_gravity = 0
            can_jump = False
            
        if spell_cast_timer <= 0:
            if keys[pygame.K_SPACE]: #I had a hard time figuring out how to shoot a projectile. 
                # Fire magic attack
                magic_attack_rect = magic_attack.get_rect()
                magic_attack_rect.center = players_rect.center
                # Get the direction from the player to the mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - magic_attack_rect.centerx
                dy = mouse_y - magic_attack_rect.centery

                # Normalize the direction vector #thanks to chat gpt honestly, I dont know the logic behind this
                magnitude = math.sqrt(dx ** 2 + dy ** 2)
                direction = (dx / magnitude, dy / magnitude)

                # Set the speed of the magic attack
                spell_speed = 10

                # Adjust the position and speed based on the direction
                magic_attack_rect.x += direction[0] * spell_speed
                magic_attack_rect.y += direction[1] * spell_speed

                magic_attacks.append((magic_attack_rect, direction))

                spell_cast_timer = 500

        for magic_attack_rect, direction in magic_attacks:
            magic_attack_rect.x += direction[0] * spell_speed
            magic_attack_rect.y += direction[1] * spell_speed

            for enemy_rect in enemy_list:
                if magic_attack_rect.colliderect(enemy_rect):
                    #if slime collides with manablast it will be 'killed' or removed.
                    enemy_list.remove(enemy_rect)
                    current_slimes -= 1
                    # Reset the enemy's position to the top of the screen
                    enemy_rect.x = random.randint(0, screen_width - enemy_rect.width)
                    enemy_rect.y = -enemy_rect.height

                    #adds one to the player_score or enemies killed, I really need to pick one and stick with it.
                    player_score += 1

                    # Remove the magic attack
                    if (magic_attack_rect,direction) in magic_attacks:
                        magic_attacks.remove((magic_attack_rect, direction))
                    #break

            screen.blit(magic_attack, magic_attack_rect)
        
        #here I want to clearly define my player's score and it's rect.
        player_score_text = font.render("Enemies Killed: " + str(player_score), False, (50, 50, 75))
        player_score_text_rect = player_score_text.get_rect(midleft = (50, 125)) #this is not a button it's the 'background' to the text
        screen.blit(player_score_text,player_score_text_rect)



        if spawn_timer >= spawn_interval and current_slimes <= max_slimes: #I am doing a small change right here because I want to slighlty amp up the slimes and get rid of a cap for now.
            # Spawn a slime enemy
            enemy_rect = earthslime_enemy.get_rect()
            enemy_rect.x = random.randint(0, screen_width - enemy_rect.width)
            enemy_rect.y = -enemy_rect.height
            enemy_list.append(enemy_rect)

            #add a slime per loop up to the max slime which was defined as 10
            current_slimes += 1
            # Reset the spawn timer
            spawn_timer = 0

        if players_rect.colliderect(sign_rect):
            player_gravity = 0
            enter_village()

        screen.blit(players_image,players_rect)
        screen.blit(player_score_text, player_score_text_rect)


        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def enter_village():
    vel = 6
    player_gravity = 0
    gravity = 0.2
    ground_tile_height = 32
    ground_depth = 3

    screen.fill("lightgray")

    groundtile = pygame.image.load('graphics/ingamegraphics/grassblock.png')
    undergroundtile = pygame.image.load('graphics/ingamegraphics/dirtblock.png')
    players_image = pygame.image.load('graphics/player.png')
    thewilds_sign = pygame.image.load('graphics/ingamegraphics/thewildsign.png')
    village_spawn = pygame.image.load('graphics/village/spawncrystal.png')

    #groundtile_rect = groundtile.get_rect()
    groundtile_rect = pygame.Rect(0, screen_height - 96, screen_width, 32)
    thewildsign_rect = thewilds_sign.get_rect(left = 0, bottom = groundtile_rect.top)
    village_spawn_rect = village_spawn.get_rect(left = 600, bottom = groundtile_rect.top)
    

    players_rect = players_image.get_rect(center=(250, 650))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player_gravity += gravity
        players_rect.y += player_gravity

        if players_rect.bottom >= groundtile_rect.top:
            players_rect.bottom = groundtile_rect.top
            player_gravity = 0

        screen.fill("lightgray")
        screen.blit(thewilds_sign, thewildsign_rect)
        screen.blit(village_spawn, village_spawn_rect)

        for y in range(screen_height - ground_tile_height * ground_depth, screen_height, ground_tile_height):
            for x in range(0, screen_width, ground_tile_height):
                if y == screen_height - ground_tile_height * ground_depth:
                    screen.blit(groundtile, (x, y))
                else:
                    screen.blit(undergroundtile, (x, y))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]: #yay movement, this was more challening than initially though
            #print('left was pressed')
            players_rect.x -= vel + 1

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            players_rect.x += vel
        
        if keys[pygame.K_ESCAPE]:
            running = False
            main_menu()


        if players_rect.colliderect(thewildsign_rect):
            player_gravity = 0
            enter_wilds()

        screen.blit(players_image, players_rect)

        pygame.display.update()
        clock.tick(60)



    pygame.quit()



    #INSERT THE MUTHAFRICKIN CODE FOR THE NEWEST ALMOST UPDATE ENTER VILLAGE!

"""05/20/23 12:56 AM I did it!, I can now move my character around and off the screen,
 from here I need to spend moretime adding im more controls, preferably towards WASD and 
 arrow keys. once I add in gravity and the world's most basic enemy (our slime), 
 I might spice it up with gamepad controls too.
"""
#2:24am after messing around some there is so much to do.






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
#-make a card timer 2/15/23 NULL 02/21/23
#-make an options menu and a spells menu 02/21/23
#-04/23/2023 began a new update 'the wilds' and began to tweak some things.
#-05/22/23 I want to make a building in the village, I want NPC's to roam about in the village. Certain NPC's will follow the player like the
#slime dx = player_rect so on. I am slowly building up to my 2d style dungeon siege-ish game. I also
#might get rid of the card battling for now and make Click Ranger and updated better version of Slime Ranger.
#-instead of a score, slimes drop coins/slime eyes and there is a visual ui for it.
#-redo menu screen with new buttons: start game, options, Lore (for eye candy but basically spells/monsters/items and info, just a bunch of cards in a book.), credits, exit.
#-the start game button places the player in the village.
#I need to add some sort of tutorial button or a help button that shows a picture of the basics.
