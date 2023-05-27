#Click Rangers Code rework for better menu, still V 0.01, which is now v 0.02 as of 2/11/23.
#Making an edit for Click Ranger on 04/23/2023 called "The Wilds" I am adding in another button and game state that will simply allow the player the move around and jump.
#This is to prepare for an idea I have had in the back of my mind since my last good run with coding
#changed the start button to Card Duel in main menu 05/18/2023
#as of 05/22/23 The Card Duel feature will be removed as set aside. Click Ranger will now Turn Into an updated version of my first game release
#Slime Ranger. Slime Ranger will be a 2d platformer to my designs, whereas Click Ranger will be a Click-Based Card game. 



import pygame, sys
import random
import time
import math
import textwrap
#import pygame_textinput   
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
menuintro = font.render("Slime Ranger V 0.05 'ENTER THE VILLAGE!'", False, (180, 180, 165))

#menu buttons
new_game_button = pygame.image.load('graphics/newgamebutton.png')
options_button = pygame.image.load('graphics/optionsbutton.png')
exit_button = pygame.image.load('graphics/exitbutton.png')
spell_library_button = pygame.image.load('graphics/librarybutton.png')
menulogo = pygame.image.load('graphics/menulogo.png')
load_game_button = pygame.image.load('graphics/loadgamebutton.png')
menubutton = pygame.image.load('graphics/menubutton.png')


#menubuttonrects, I want my buttons listed in order as they also appear on my menu in-game.
ingamemenu = pygame.image.load('graphics/ingamegraphics/ingamemenu.png')
ingamemenu_rect = ingamemenu.get_rect(midleft = (600,450))

ingamemenu_exit_button = pygame.image.load('graphics/ingamegraphics/inventory_exit_button.png')
ingamemenu_exit_button_rect = pygame.Rect(ingamemenu_rect.right - 32, ingamemenu_rect.top, 30,30)

ingamemenu_returnmain_button = pygame.image.load('graphics/ingamegraphics/mainmenureturnbutton.png')
ingamemenu_returnmain_button_rect = ingamemenu_returnmain_button.get_rect()
ingamemenu_returnmain_button_rect.center = ingamemenu_rect.center

ingamemenu_savegamebutton = pygame.image.load('graphics/savegamebutton.png')
ingamemenu_savegamebutton_rect = ingamemenu_savegamebutton.get_rect()
ingamemenu_savegamebutton_rect.centery = ingamemenu_rect.centery + 50
ingamemenu_savegamebutton_rect.centerx = ingamemenu_rect.centerx 





#05/16/2023 I want to play with my menu button locations,perhaps try setting the x value as half of the width of the screen so it's centered. 

#05/22/23 working on updates my new menu buttons. 
new_game_button_rect = new_game_button.get_rect(center = (screen_width/2,200)) #starts a card combat game. idea to rename as I go.
load_game_button_rect = load_game_button.get_rect(center = (screen_width/2,275))
options_rect = options_button.get_rect(center = (screen_width/2,350))
spelllib_rect = spell_library_button.get_rect(center = (screen_width/2,425))
exit_rect = exit_button.get_rect(center = (screen_width/2,500))
menulogo_rect = menulogo.get_rect(topleft = (325, 600))
menubutton_rect = menubutton.get_rect(topleft = (50,600))

#Spells Menu images
bookofspells = pygame.image.load('graphics/bookospells.png')

#Spells Menu Rects (undecided if needed)
bookofspells_rect = bookofspells.get_rect(topleft = (1,1))


click = False
#player_score = 0
player = 'player_name'


def main_menu(): 
    while True:
        
        mainmenusplash = pygame.image.load('graphics/mainscreensplash.png')

        screen.blit(mainmenusplash, (0,0))
        

        #screen.fill('grey')
        screen.blit(load_game_button, load_game_button_rect)
        screen.blit(new_game_button, new_game_button_rect)
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
            #if event.type == KEYDOWN:
                #if event.key == K_ESCAPE:
                    #pygame.quit()
                    #sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            #if event.type == VIDEORESIZE:
                #screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

            if new_game_button_rect.collidepoint((mx, my)):
                
                if click:
                    character_creation_screen()

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


            if load_game_button_rect.collidepoint((mx,my)):
                if click:
                    loaded_data = load_saved_player_data()
                    if loaded_data is not None:
                        if 'player' in loaded_data:
                            selected_player = loaded_data['name']
                            enter_village(selected_player)
                    else:
                        main_menu()
            
                    
         
        pygame.display.update()
        clock.tick(60)


def save_player_data(name, player, score):
    with open('save_file.txt', 'w') as file:
        file.write(f'Player Name: {name}\n')
        file.write(f'Selected Player: {player}\n')
        file.write(f'Player Score: {score}\n')


def load_saved_player_data():
    try:
        with open('save_file.txt', 'r') as file:
            loaded_data = {}
            for line in file:
                line = line.strip()
                if line.startswith('Player Name:'):
                    loaded_data['name'] = line.split(':')[1].strip()
                elif line.startswith('Selected Player:'):
                    loaded_data['player'] = line.split(':')[1].strip()
                elif line.startswith('Player Score:'):
                    loaded_data['score'] = int(line.split(':')[1].strip())
            return loaded_data

    except FileNotFoundError:
        print('save file not found.')
    except Exception as e:
        print(f'Error loading saved player data: {str(e)}')






def character_creation_screen():

    mx,my = pygame.mouse.get_pos()
    character = {}  # Dictionary to store character attributes
    click = False
    button_pressed = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0 ,0)

    newplayerscreen = pygame.image.load('graphics/createplayerwindow.png')
    newplayerscreen_rect = newplayerscreen.get_rect(midleft = (400,400))
    menubutton = pygame.image.load('graphics/menubutton.png')
    startgamebutton = pygame.image.load('graphics/startbutton.png')
    #chooseplayerbutton = pygame.image.load('graphics/chooseplayer.png')

    menubutton_rect = menubutton.get_rect(bottomleft=(newplayerscreen_rect.left + 56, newplayerscreen_rect.bottom - 64))
    #chooseplayerbutton_rect = chooseplayerbutton.get_rect(bottom=(newplayerscreen_rect.bottom - 64), centerx=newplayerscreen_rect.centerx)
    startgamebutton_rect = startgamebutton.get_rect(bottomright=(newplayerscreen_rect.right - 56, newplayerscreen_rect.bottom - 64))

    hero_treddo = pygame.image.load('graphics/ingamegraphics/players/treddo.png')
    hero_treddo_rect = hero_treddo.get_rect(topright=(newplayerscreen_rect.right - 96, newplayerscreen_rect.centery - 16))

    hero_rose = pygame.image.load('graphics/ingamegraphics/players/rose.png')
    hero_rose_rect = hero_rose.get_rect(topright=(newplayerscreen_rect.right - 216, newplayerscreen_rect.centery - 16))

    #player_options = ['graphics/ingamegraphics/players/playeroption01.png', 'graphics/ingamegraphics/players/playeroption02.png', 'graphics/ingamegraphics/players/playeroption03.png']

    player_score = 0
    user_input = ''
    selected_player = None


    clock.tick()
    
    while True:
        # ... character creation screen logic ...
        screen.fill('darkgray')

        mx,my = pygame.mouse.get_pos()

        text_surface = font.render('Enter Hero Name: ', True, (255,255,255))
        text_surface_rect = text_surface.get_rect(topleft = (newplayerscreen_rect.left + 64, newplayerscreen_rect.top + 64))
        #save_data = ''
    
        
        
        #player_image = pygame.image.load(random.choice(player_options))
        #player_rect = player_image.get_rect(topright=(newplayerscreen_rect.right, newplayerscreen_rect.top))
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    # Remove the last character from the user input
                    user_input = user_input[:-1]
                else:
                # Append the pressed character to the user input
                    user_input += event.unicode



                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        break

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and not button_pressed:
                    click = True
                    button_pressed = True



                    if hero_treddo_rect.collidepoint(mx, my):
                        selected_player = 'Treddo'
                    elif hero_rose_rect.collidepoint(mx, my):
                        selected_player = 'Rose'

                    #if chooseplayerbutton_rect.collidepoint(mx, my):
                        #player_image = pygame.image.load(random.choice(player_options))
                        #player_rect = player_image.get_rect(topright=(newplayerscreen_rect.right, newplayerscreen_rect.top))
            # ... handle user input and interactions ...
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    button_pressed = False
                
        if click and startgamebutton_rect.collidepoint((mx, my)):
            if user_input and selected_player:
                save_player_data(selected_player, user_input, player_score)  # Call a function to save the data
                enter_village(selected_player)





        if click and menubutton_rect.collidepoint((mx, my)):
            main_menu()

        
        # ... update UI and render the character creation screen ...
        input_x = newplayerscreen_rect.left + 96
        input_y = newplayerscreen_rect.top + 132
        input_surface = font.render(user_input, True, (0, 0, 0))
        input_surface_rect = pygame.Rect(input_x, input_y, 200, 30)
        screen.blit(newplayerscreen, newplayerscreen_rect)
        screen.blit(text_surface, text_surface_rect)
        pygame.draw.rect(screen, (255, 255, 255), input_surface_rect, 2)
        screen.blit(input_surface, input_surface_rect)
        screen.blit(menubutton, menubutton_rect)
        #screen.blit(chooseplayerbutton, chooseplayerbutton_rect)
        screen.blit(startgamebutton, startgamebutton_rect)
        screen.blit(hero_treddo, hero_treddo_rect)
        screen.blit(hero_rose, hero_rose_rect)

        #if button_pressed and chooseplayerbutton_rect.collidepoint(mx, my):
            #player_image = pygame.image.load(random.choice(player_options))
            #player_rect = player_image.get_rect(topright=(newplayerscreen_rect.right, newplayerscreen_rect.top))

        if selected_player == 'Treddo':
            pygame.draw.rect(screen, (255,0,0), hero_treddo_rect, 2)
        elif selected_player == 'Rose':
            pygame.draw.rect(screen, (255,0,0), hero_rose_rect, 2)


        pygame.display.update()
        clock.tick()
        

        click = False

    return character


#This serves to create an in-game menu function outside of the wild and village loops so the main menu can be pressed whenever.
def show_ingame_menu(selected_player):
    #I set the value to false so it only appears when the player pressed the right key, in this case being escape.
    show_ingamemenu = False
    user_input =''

    while True:
        #here I am going to add the code that allows the player to open the in game menu
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    show_ingamemenu = True

            if event.button == 1 and show_ingamemenu:
                if ingamemenu_exit_button_rect.collidepoint(event.pos):
                    show_ingamemenu = False

                if show_ingame_menu and ingamemenu_returnmain_button_rect.collidepoint(event.pos):
                    main_menu()

                if show_ingame_menu and ingamemenu_savegamebutton_rect.collidepoint(event.pos):
                    save_player_data((selected_player, user_input, player_score)) #would I also put in player score 


        
        if show_ingamemenu:
            screen.blit(ingamemenu,ingamemenu_rect)
            screen.blit(ingamemenu_exit_button, ingamemenu_exit_button_rect)
            screen.blit(ingamemenu_returnmain_button, ingamemenu_returnmain_button_rect)
            screen.blit(ingamemenu_savegamebutton, ingamemenu_savegamebutton_rect)


        pygame.display.update()
        clock.tick(60)
    
def enter_village(selected_player):


    screen.fill("lightgray")


    #Environment Variables
    gravity = 0.2
    ground_tile_height = 32
    ground_depth = 3
    groundtile = pygame.image.load('graphics/ingamegraphics/grassblock.png')
    groundtile_rect = pygame.Rect(0, screen_height - 96, screen_width, 32)
    undergroundtile = pygame.image.load('graphics/ingamegraphics/dirtblock.png')
    elapsed_time = 0

    #Player Variables
    vel = 6
    player_gravity = 0
    players_image = pygame.image.load(f'graphics/ingamegraphics/players/{selected_player.lower()}.png')  # Load the image based on the selected player
    players_rect = players_image.get_rect(center=(250, 650))
    show_inventory = False
    show_ingamemenu = False
    interact = False



    #the nps rects will eventually be made into a list and will have about 5 or 6 npc's displayed every time
    villagechief_image = pygame.image.load('graphics/village/chiefbrune.png')
    villagechief_image_rect = villagechief_image.get_rect(center=(350, 750))

    #Non-Playable Character Variables also known as NPC's
    max_width = 50
    npcdialogbox = pygame.image.load('graphics/npcdialogbox.png')
    npcdialogbox_rect = npcdialogbox.get_rect(topleft = (600,650))


    text = """I am Chief Brune of this village \n
    Rosenhall, Nice to meet you traveller"""

    wrapped_lines = textwrap.wrap(text, width=max_width)
    wrapped_text = '\n'.join(wrapped_lines)

    # Render the wrapped text
    npc_dialog_text = font.render(wrapped_text, True, (50, 50, 75))
    npc_dialog_text_rect = npc_dialog_text.get_rect(topleft=(npcdialogbox_rect.left + 10, npcdialogbox_rect.top + 10))

    npc_gravity = 0
    npc_vel = 3
    #npc_direction = random.choice([-1,1])
    #npc_move_timer = random.randint(3000,15000)
    #npc_wait_time = 0
    #npc_min_x = 0
    #npc_max_x = screen_width - villagechief_image_rect.width



    #objects loaded in the village such as signs, spawn, and houses
    thewilds_sign = pygame.image.load('graphics/ingamegraphics/thewildsign.png')
    thewildsign_rect = thewilds_sign.get_rect(left = 0, bottom = groundtile_rect.top)
    village_spawn = pygame.image.load('graphics/village/spawncrystal.png')
    village_spawn_rect = village_spawn.get_rect(left = 600, bottom = groundtile_rect.top)
    village_hall = pygame.image.load('graphics/village/villagehall.png')
    village_hall_rect = village_hall.get_rect(left = 200, bottom = groundtile_rect.top)


    #User Interface Variables
    player_inventory_image = pygame.image.load('graphics/ingamegraphics/playerinventory.png')
    player_inventory_rect = pygame.Rect(200,200, player_inventory_image.get_width(), player_inventory_image.get_height())
    inventoryexit_button = pygame.image.load('graphics/ingamegraphics/inventory_exit_button.png')
    inventoryexit_button_rect = pygame.Rect(player_inventory_rect.right - 32, player_inventory_rect.top, 30,30)



    saved_data = load_saved_player_data()

    if saved_data is not None:
        user_input = saved_data.get('player', '')  # Assign the saved name to user_input
        player_score = saved_data.get('score', '')



    running = True
    click = False




    while running:
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

                if event.button == 1 and show_ingamemenu:
                    if ingamemenu_exit_button_rect.collidepoint(event.pos):
                        show_ingamemenu = False
                    if ingamemenu_returnmain_button_rect.collidepoint(event.pos):
                        running = False
                        main_menu()

                    if ingamemenu_savegamebutton_rect.collidepoint(event.pos):
                        save_player_data(selected_player, user_input, player_score)

            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    show_ingamemenu = True


        #my logic handling player gravity, and what actually makes my character fall
        player_gravity += gravity
        players_rect.y += player_gravity

        #here I am handling NPC logic and gravity and I might have to add gravity per npc unless I discover a better way
        npc_gravity += gravity
        villagechief_image_rect.y += npc_gravity

        #environment logic
        #elapsed_time += clock.tick(60)
        #npc_wait_time += elapsed_time



        if players_rect.bottom >= groundtile_rect.top:
            players_rect.bottom = groundtile_rect.top
            player_gravity = 0
        
        if villagechief_image_rect.bottom >= groundtile_rect.top:
            villagechief_image_rect.bottom = groundtile_rect.top
            npc_gravity = 0



        screen.fill("lightgray")
        screen.blit(thewilds_sign, thewildsign_rect)
        screen.blit(village_spawn, village_spawn_rect)
        screen.blit(village_hall, village_hall_rect)

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
        
        if keys[pygame.K_i]:
            show_inventory = True

        if keys[pygame.K_e]:
            interact = True

        if players_rect.colliderect(thewildsign_rect):
            player_gravity = 0
            enter_wilds(selected_player)

        if interact and players_rect.colliderect(villagechief_image_rect):
            screen.blit(npcdialogbox, npcdialogbox_rect)
            screen.blit(npc_dialog_text, npc_dialog_text_rect)
        else:
            interact = False
        
    
            
            
                

        if show_ingamemenu:
            screen.blit(ingamemenu, ingamemenu_rect)
            screen.blit(ingamemenu_exit_button, ingamemenu_exit_button_rect)
            screen.blit(ingamemenu_returnmain_button, ingamemenu_returnmain_button_rect)
            screen.blit(ingamemenu_savegamebutton, ingamemenu_savegamebutton_rect)
        
        if show_inventory:
            screen.blit(player_inventory_image, player_inventory_rect)
            screen.blit(inventoryexit_button, inventoryexit_button_rect)

        screen.blit(players_image, players_rect)
        screen.blit(villagechief_image, villagechief_image_rect)

        pygame.display.update()
        clock.tick(60)



    pygame.quit()


def enter_wilds(selected_player):

    global player_score

    #Here I want all my player variables
    player_health = 150 #either treddo or rose's health, or whatever the player has named their character
     #also could be referred to as the number of enemies killed. I'm to implement a real inventory and items soon.
    vel = 6 #vel, short for velocity, could be called 'movement' but represents the rate at which it will move.
    gravity = 0.2
    player_gravity = 0.0
    jumping = False
    jump_count = 12
    can_jump = True
    jump_speed = 0.15
    spell_cast_timer = 0
    spell_speed = 10
    magic_attacks = []
    #player_score = 0
    #Here I want my Environment vairables
    ground_depth = 3
    ground_tile_height = 32

    #Here I want logic variables like inventories, items, interactables, and options.
    show_inventory = False
    show_ingamemenu = False

    #here I want all of my enemy variables
    enemy_list = []
    max_slimes = 10
    current_slimes = 0
    enemy_gravity = 4
    spawn_timer = 0
    spawn_interval = 500

    
    #Here I want to load new images for my Environment, Player, enemies, and other entities, and then User Interface.
    #Environment
    groundtile = pygame.image.load('graphics/ingamegraphics/grassblock.png')
    undergroundtile = pygame.image.load('graphics/ingamegraphics/dirtblock.png')

    #Player, enemies, and others.
    #players_image = pygame.image.load('graphics/player.png')
    players_image = pygame.image.load(f'graphics/ingamegraphics/players/{selected_player.lower()}.png')  # Load the image based on the selected player

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

    saved_data = load_saved_player_data()
    if saved_data is not None:
        user_input = saved_data.get('player', '')  # Assign the saved name to user_input
        player_score = saved_data.get('score', '')


    running = True
    




    while running:
        
        
        elapsed_time = clock.tick(60)

        player_gravity += gravity
        players_rect.y += player_gravity

        spell_cast_timer -= elapsed_time
        spawn_timer += elapsed_time
    
        screen.fill('darkgrey')
        screen.blit(sign_village, sign_rect)

        
    

        for y in range(screen_height - ground_tile_height * ground_depth, screen_height, ground_tile_height):
            for x in range(0, screen_width, ground_tile_height):
                if y == screen_height - ground_tile_height * ground_depth:
                    screen.blit(groundtile, (x,y))
                else:  
                    screen.blit(undergroundtile, (x, y))



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


            if enemy_rect.colliderect(players_rect):
                player_health -= 1

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

                if event.button == 1 and show_ingamemenu:
                    if ingamemenu_exit_button_rect.collidepoint(event.pos):
                        show_ingamemenu = False
                    if ingamemenu_returnmain_button_rect.collidepoint(event.pos):
                        running = False
                        main_menu()
                    if ingamemenu_savegamebutton_rect.collidepoint(event.pos):
                        save_player_data(selected_player, user_input, player_score)



            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    show_ingamemenu = True
    
              
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]: #yay movement, this was more challening than initially though
            #print('left was pressed')
            players_rect.x -= vel + 1

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            players_rect.x += vel
        
        
        if keys[pygame.K_i]:
            show_inventory = True

    
        if show_ingamemenu:
            screen.blit(ingamemenu, ingamemenu_rect)
            screen.blit(ingamemenu_exit_button, ingamemenu_exit_button_rect)
            screen.blit(ingamemenu_returnmain_button, ingamemenu_returnmain_button_rect)
            screen.blit(ingamemenu_savegamebutton, ingamemenu_savegamebutton_rect)
        

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
                    enemy_rect.y = - enemy_rect.height

                    #adds one to the player_score or enemies killed, I really need to pick one and stick with it.
                    player_score += 1
                    player_health += 10

                    # Remove the magic attack
                    if (magic_attack_rect,direction) in magic_attacks:
                        magic_attacks.remove((magic_attack_rect, direction))
                    #break

            screen.blit(magic_attack, magic_attack_rect)
        
        #here I want to clearly define my player's score and it's rect.
        player_score_text = font.render("Enemies Killed: " + str(player_score), False, (50, 50, 75))
        player_score_text_rect = player_score_text.get_rect(midleft = (50, 125)) #this is not a button it's the 'background' to the text
        screen.blit(player_score_text,player_score_text_rect)

        player_health_base = pygame.Rect(100, 175, 150, 27)
        player_health_active = pygame.Rect(100, 175, player_health, 27)
        
            
         # Here I want to load text to add to my health bars
        health_text = font.render("Hp: " + str(player_health), False, (65,67,69))
        health_text_rect = health_text.get_rect(topleft = (100,173))

            
            
        # Here I am drawing instead of blitting my health bars
        pygame.draw.rect(screen, (200, 15, 15), player_health_base)
        pygame.draw.rect(screen, (15, 200, 15), player_health_active)



        #here I am going to draw/render/blit my health text to the rects.
        screen.blit(health_text, health_text_rect)
        #screen.blit(playerlevel_text, playerlevel_text_rect)



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
            save_player_data(selected_player, user_input, player_score)
            enter_village(selected_player)

        if player_health >= 150:
            player_health = 150

        if player_health <= 0:
            player_score -= 10
            save_player_data(selected_player, user_input, player_score)
            enter_village(selected_player)

        screen.blit(players_image,players_rect)
        screen.blit(player_score_text, player_score_text_rect)


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
        
    screen.blit(menubutton, menubutton_rect)
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
            if menubutton_rect.collidepoint((mx, my)):
                #print("Hey there is collision")
                if click:
                    return  # Goes back to main menu, as it is the one that calls game
                

        pygame.display.update()




def options():
    screen.fill("lightgray")
        
    screen.blit(menubutton, menubutton_rect)
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
            if menubutton_rect.collidepoint((mx, my)):
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
