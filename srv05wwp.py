####

'''this is a current somewhat working version of slime ranger 0.5'''

#Click Rangers Code rework for better menu, still V 0.01, which is now v 0.02 as of 2/11/23.
#Making an edit for Click Ranger on 04/23/2023 called "The Wilds" I am adding in another button and game state that will simply allow the player the move around and jump.
#This is to prepare for an idea I have had in the back of my mind since my last good run with coding
#changed the start button to Card Duel in main menu 05/18/2023
#as of 05/22/23 The Card Duel feature will be removed as set aside. Click Ranger will now Turn Into an updated version of my first game release
#Slime Ranger. Slime Ranger will be a 2d platformer to my designs, whereas Click Ranger will be a Click-Based Card game. 



import pygame, sys
import random
import math
from items import potions, crafting_materials, weapons, trinkets, spell_pages


from pygame.locals import *

pygame.init()

#Window and global variables.
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height), 0, 32)
font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()


#sounds I am bad at making music
#menuloop = pygame.mixer.music.load('gameloop.wav')
#pygame.mixer.music.play(-1)

#Client Version
pygame.display.set_caption('Slime Ranger V 0.05 "ENTER VILLAGE"') #yay we are now 0.01 away from the creation, 1 week in
versiontag = font.render("Slime Ranger V 0.05 'ENTER THE VILLAGE!'", False, (20, 5, 5))
versiontag_rect = versiontag.get_rect(topleft = (780, 850))


#menu buttons
new_game_button = pygame.image.load('graphics/newgamebutton.png')
options_button = pygame.image.load('graphics/optionsbutton.png')
exit_button = pygame.image.load('graphics/exitbutton.png')
spell_library_button = pygame.image.load('graphics/librarybutton.png')
load_game_button = pygame.image.load('graphics/loadgamebutton.png')
menubutton = pygame.image.load('graphics/menubutton.png')


#menubuttonrects, I want my buttons listed in order as they also appear on my menu in-game.
ingamemenu = pygame.image.load('graphics/ingamegraphics/ingamemenu.png')
ingamemenu_rect = ingamemenu.get_rect(midleft = (600,450))

ingamemenu_exit_button = pygame.image.load('graphics/ingamegraphics/inventory_exit_button.png')
ingamemenu_exit_button_rect = pygame.Rect(ingamemenu_rect.right - 32, ingamemenu_rect.top, 30,30) #refer here to exit button locations.

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
        screen.blit(load_game_button, load_game_button_rect)
        screen.blit(new_game_button, new_game_button_rect)
        screen.blit(options_button, options_rect)
        screen.blit(exit_button, exit_rect)
        screen.blit(spell_library_button, spelllib_rect)
        screen.blit(versiontag, versiontag_rect)

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
                            hotbar_items = loaded_data.get('hotbar_items', [])
                            for i in range(min(len(hotbar_items), 5)):
                                hotbar_slots[i].set_item(hotbar_items[i])

                        enter_village(selected_player)
                    else:
                        main_menu()
                                
         
        pygame.display.update()
        clock.tick(60)


def save_player_data(name, player, score, health, mana, level, hotbar_items):

    hotbar_items = [slot.item for slot in hotbar_slots[:5]]
    
    with open('save_file.txt', 'w') as file:
        file.write(f'Player Name: {name}\n')
        file.write(f'Selected Player: {player}\n')
        file.write(f'Player Score: {score}\n')
        file.write(f'Player Health: {health}\n')
        file.write(f'Player Mana: {mana}\n')
        file.write(f'Player Level: {level}\n')
        file.write('Hotbar Items:\n')
        for item in hotbar_items:
            file.write(f'{item}\n')


def load_saved_player_data():

    hotbar_items = []

    try:
        with open('save_file.txt', 'r') as file:
            loaded_data = {}
            hotbar_items = []
            for line in file:
                line = line.strip()
                if line.startswith('Player Name:'):
                    loaded_data['name'] = line.split(':')[1].strip()
                elif line.startswith('Selected Player:'):
                    loaded_data['player'] = line.split(':')[1].strip()
                elif line.startswith('Player Score:'):
                    loaded_data['score'] = int(line.split(':')[1].strip())
                elif line.startswith('Player Health:'):
                    loaded_data['health'] = int(line.split(':')[1].strip())
                elif line.startswith('Player Mana:'):
                    loaded_data['mana'] = int(line.split(':')[1].strip())
                elif line.startswith('Player Level:'):
                    loaded_data['level'] = int(line.split(':')[1].strip())
                elif line == 'Hotbar Items:':
                    # Start reading hotbar items
                    for item_line in file:
                        item_line = item_line.strip()
                        if item_line:
                            hotbar_items.append(item_line)
                        else:
                            # Reached the end of hotbar items
                            loaded_data['hotbar_items'] = hotbar_items
                
                elif line.startswith('Spell Page:'):
                    loaded_data['spell_page'] = line.split(':')[1].strip()

            return loaded_data

    except FileNotFoundError:
        print('save file not found.')
    except Exception as e:
        print(f'Error loading saved player data: {str(e)}')



class Player:
    def __init__(self, selected_player):
        self.player_image = pygame.image.load(f'graphics/ingamegraphics/players/{selected_player.lower()}.png')
        self.player_health = 150
        self.player_mana = 100
        self.player_level = 0
        self.player_score = 0
        self.character_name = ''
        self.selected_player = selected_player
        self.vel = 6
        self.player_gravity = 0
        self.players_rect = self.player_image.get_rect(center=(250, 650))
        self.rect = self.players_rect
        


def character_creation_screen():
    global selected_player

    mx,my = pygame.mouse.get_pos()
    
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


    selected_player = None
    character_name = ''



    clock.tick()
    
    while True:
        # ... character creation screen logic ...
        screen.fill('darkgray')

        mx,my = pygame.mouse.get_pos()
        hotbar_items = [slot.item for slot in hotbar_slots]

        text_surface = font.render('Enter Hero Name: ', True, (255,255,255))
        text_surface_rect = text_surface.get_rect(topleft = (newplayerscreen_rect.left + 64, newplayerscreen_rect.top + 64))
        #save_data = ''
        
    
              

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    # Remove the last character from the user input
                    character_name = character_name[:-1]
                elif event.key == K_RETURN:
                    break
                else:
                    # Append the pressed character to the user input
                    character_name += event.unicode
                    

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
                if character_name and selected_player:
                    
                    start_items = random.sample(potions + crafting_materials + weapons + trinkets + spell_pages, 3)

                    player = Player(selected_player)  # Create an instance of the Player class
                    player.player_score = 0  # Set the player score
                    player.user_input = character_name  # Set the user input
                    player.player_health = 150
                    player.player_mana = 20
                    player.player_level = 0
                    player.selected_player = selected_player  # Set the selected player

                    
                    for i in range(3):
                        hotbar_slots[i].set_item(start_items[i])
                    hotbar_items = [slot.item for slot in hotbar_slots[:5]]
                    save_player_data(player.selected_player, player.user_input, player.player_score, player.player_health, player.player_mana, player.player_level, hotbar_items)
                    enter_village(player)


        if click and menubutton_rect.collidepoint((mx, my)):
            main_menu()

        
        # ... update UI and render the character creation screen ...
        input_x = newplayerscreen_rect.left + 96
        input_y = newplayerscreen_rect.top + 132
        input_surface = font.render(character_name, True, (0, 0, 0))
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

        #return character


#This serves to create an in-game menu function outside of the wild and village loops so the main menu can be pressed whenever.
def show_ingame_menu(selected_player):
    #I set the value to false so it only appears when the player pressed the right key, in this case being escape.
    show_ingamemenu = False
    saved_data = load_saved_player_data()

    if saved_data is not None:
        player = Player(selected_player)
        player.user_input = saved_data.get('player', '')  # Assign the saved name to user_input
        player.score = saved_data.get('score', '')
        player.health = saved_data.get('health', 150)
        player.mana = saved_data.get('mana', 10)
        player.level = saved_data.get('level', 0)
        player.hotbar_items = saved_data.get('hotbar_items', [])

    while True:

        hotbar_items = [slot.item for slot in hotbar_slots]
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
                   save_player_data(player.selected_player, player.user_input, player.player_score, player.player_health, player.player_mana, player.player_level, hotbar_items)

        
        if show_ingamemenu:
            screen.blit(ingamemenu,ingamemenu_rect)
            screen.blit(ingamemenu_exit_button, ingamemenu_exit_button_rect)
            screen.blit(ingamemenu_returnmain_button, ingamemenu_returnmain_button_rect)
            screen.blit(ingamemenu_savegamebutton, ingamemenu_savegamebutton_rect)


        pygame.display.update()
        clock.tick(60)



hotbar = pygame.image.load('graphics/ingamegraphics/playerhotbar.png')
hotbar_rect = hotbar.get_rect(topleft=(500, 100))

class HotbarSlot:
    def __init__(self, item, rect):
        self.item = item
        self.rect = rect
        self.image = pygame.Surface((rect.width, rect.height))

    def set_item(self, item):
        self.item = item

# Create 5 empty hotbar slots with associated rectangles
hotbar_x = hotbar_rect.x  # X position of the hotbar
hotbar_y = hotbar_rect.y  # Y position of the hotbar
slot_width = 50  # Width of each hotbar slot
image_scale_factor = 8

hotbar_slots = []
for i in range(5):
    slot_rect = pygame.Rect(hotbar_x + i * slot_width, hotbar_y, slot_width, slot_width)
    hotbar_slots.append(HotbarSlot(None, slot_rect))

# Display the hotbar
screen.blit(hotbar, hotbar_rect)

# Blit the spell page image onto the corresponding slot's rectangle
for slot in hotbar_slots:
    print("Loop executed")
    if slot.item:
        print(f"Image dimensions: {slot.item.image.get_width()} x {slot.item.image.get_height()}")
        scaled_item_image = pygame.transform.scale(slot.item.image, (slot_width * image_scale_factor, slot_width * image_scale_factor))
        screen.blit(scaled_item_image, slot.rect)
        print('Item exists')
    else:
        print('No item seen')



hotbar_slot_selected = None  # Initially select the first hotbar slot

def update_hotbar_selection(keys):
    global hotbar_slot_selected

    if keys[pygame.K_1]:
        hotbar_slot_selected = hotbar_slots[0]  # Select hotbar slot 1
        print("Selected Slot: 1")
        print("Item in the Slot:", hotbar_slot_selected.item)  # Print the item in the selected slot

    elif keys[pygame.K_2]:
        hotbar_slot_selected = hotbar_slots[1]  # Select hotbar slot 2
        print("Selected Slot: 2")
        print("Item in the Slot:", hotbar_slot_selected.item)


    elif keys[pygame.K_3]:
        hotbar_slot_selected = hotbar_slots[2]  # Select hotbar slot 3
        print("Selected Slot: 3")
        print("Item in the Slot:", hotbar_slot_selected.item)
    elif keys[pygame.K_4]:
        hotbar_slot_selected = hotbar_slots[3]  # Select hotbar slot 3
        print("Selected Slot: 4")
        print("Item in the Slot:", hotbar_slot_selected.item)

    elif keys[pygame.K_5]:
        hotbar_slot_selected = hotbar_slots[4]  # Select hotbar slot 3
        print("Selected Slot: 5")
        print("Item in the Slot:", hotbar_slot_selected.item)
    # Add more key bindings for other hotbar slots

    return hotbar_slot_selected

def draw_hotbar_selection():
    for slot in hotbar_slots:
        if slot is hotbar_slot_selected:
            pygame.draw.rect(screen, (255, 0, 0), slot.rect, 2)
        else:
            pygame.draw.rect(screen, (0, 0, 0), slot.rect, 2)



# Function for using an item inside of the selected slot. 1-5
def use_item(slot, player):
  
    mx, my = pygame.mouse.get_pos()
    
    if slot:
        # Get the item from the selected hotbar slot
        item = slot.item
        
        # Check the type of item and perform the corresponding actions
        if isinstance(item, dict):
            # Check the type of item based on its dictionary structure
            if item['type'] == 'spell':

                print("Spell page item is being used!")
                
                if item['name'] == 'Arcane Ball':
                    print('Arcane Ball was cast')
                    
                    if player.player_mana >= item['mana_cost']:
                        player.player_mana -= item['mana_cost']
                   
                        
                        print('Arcane Ball has consumed:', item['mana_cost'])
                        

                    else:
                        print('Not enough mana')
                
                elif item['name'] == 'Ball of Flame':
                    print('Ball of Flame was cast')
                    
                    if player.player_mana >= item['mana_cost']:
                        player.player_mana -= item['mana_cost']

                        
                        print('Ball of Flame has consumed:', item['mana_cost'])
                        
            
                        
                    else:
                        print('Not enough mana')
                
                # ...
                return player
            
                
            

            elif item['type'] == 'potion':
                # Check the effect of the potion and restore health or mana accordingly
                if item['name'] == 'Sip of Health':
                    player.player_health += item['restore_amount']
                    print('sip of health was used')
                    print(player.player_health)

                elif item['name'] == 'Sip of Mana':
                    player.player_mana += item['restore_amount']  
                    print('sip of mana was used')
                    print(player.player_mana)
                    
                slot.item = None
                    
                return  # No need to return player attributes here
                # ...
            elif item['type'] == 'trinket':
                
                if item['name'] == 'Ring of Restore Mana':
                    
                    player.player_health -= item['restore_amount']
                    player.player_mana += item['restore_amount']
                    print('ring was used')
                    print(player.player_health)
                    print(player.player_mana)
                    # Perform the actions for activating the trinket
                    # ...
            elif item['type'] == 'weapon':
                if item['name'] == 'Twig Wand':
                    print('twig wand is equipped')
                    # Use the weapon based on the mouse position and weapon attributes
                    # ...
                elif item['name'] == 'Crystal Staff':
                    print('crystal staff is equipped')
                    # Use the weapon based on the mouse position and weapon attributes
                    # ...
                # ...
            elif item['type'] == 'crafting_material':
                if item['name'] == 'Slime Eyes':
                    print('slimey')
                
                if item['name'] == 'Stone Fragment':
                    print('oh shiney')

    return player



        # ...
def enter_village(player):
    global player_health
    global player_mana
   

    screen.fill("lightgray")

    # Render the hotbar
    screen.blit(hotbar, hotbar_rect)
    hotbar_items = [slot.item for slot in hotbar_slots]
    hotbar_slots[0]
    

    # Update the display
    pygame.display.flip()

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
    projectiles = []


    players_image = pygame.image.load(f'graphics/ingamegraphics/players/{selected_player.lower()}.png')  # Load the image based on the selected player
    players_rect = players_image.get_rect(center=(250, 650))
    show_inventory = False
    show_ingamemenu = False
    interact = False
    can_interact = False
    beingused = False
    
    #health = player.player_health


    #the nps rects will eventually be made into a list and will have about 5 or 6 npc's displayed every time
    villagechief_image = pygame.image.load('graphics/village/chiefbrune.png')
    villagechief_image_rect = villagechief_image.get_rect(center=(350, 750))

    #Non-Playable Character Variables also known as NPC's
    show_npcdialogbox = False
    npcdialogbox = pygame.image.load('graphics/npcdialogbox.png')
    npcdialogbox_rect = npcdialogbox.get_rect(topleft = (600,650))
    npcexitbutton = pygame.image.load('graphics/village/exit_button.png')
    npcexitbutton_rect = pygame.Rect(npcdialogbox_rect.right - 32, npcdialogbox_rect.top, 30,30)
    npc_dialog_text = None
  

    quotes = [
        "Greetings Traveller!",
        "A fine day for hunting slimes!",
        "This is the village Rosenhall.",
        "Welcome to our village.",
        "May the wisps guide your path.",
        "I am Chief Brune, Chief of\nRosenhall!",
        "Have you been by the Ancient\nRuins?",
        "Stone Golems are formidable\nfoes",
        "have you visited the\nCloud District?",
        "I heard more people are\narriving soon"


    ]

    #this code will attempt to handle or begin the structure to my npc dialog and interaction's with the player.
   
    npc_gravity = 0
    npc_vel = 3

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
        #player_health = saved_data.get('health', 150)
        player_mana = saved_data.get('mana', 10)
        player_level = saved_data.get('level', 0)
        hotbar_items = saved_data.get('hotbar_items', [])





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
                        hotbar_items = [slot.item for slot in hotbar_slots[:5]]
                        save_player_data(player.selected_player, player.user_input, player.player_score, player.player_health, player.player_mana, player.player_level, hotbar_items)


                if event.button == 1 and npcexitbutton_rect.collidepoint(event.pos):
                    show_npcdialogbox = False
                    npc_dialog_text = None
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    show_ingamemenu = True



        #my logic handling player gravity, and what actually makes my character fall
        player_gravity += gravity
        players_rect.y += player_gravity

        #here I am handling NPC logic and gravity and I might have to add gravity per npc unless I discover a better way
        npc_gravity += gravity
        villagechief_image_rect.y += npc_gravity
        health_potion_chance = 0.25
        

        #environment logic
        #elapsed_time += clock.tick(60)

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
        screen.blit(hotbar, hotbar_rect)

        keys = pygame.key.get_pressed()
        update_hotbar_selection(keys)
        draw_hotbar_selection()
  

        for i, slot in enumerate(hotbar_slots):
            screen.blit(slot.image, slot.rect)

            if slot.item:
                # Calculate the position to blit the item image inside the slot
                item_x = slot.rect.x + (slot.rect.width - slot.item['image'].get_width()) // 2
                item_y = slot.rect.y + (slot.rect.height - slot.item['image'].get_height()) // 2

                # Blit the item image onto the hotbar slot
                screen.blit(slot.item['image'], (item_x, item_y))
             

        for y in range(screen_height - ground_tile_height * ground_depth, screen_height, ground_tile_height):
            for x in range(0, screen_width, ground_tile_height):
                if y == screen_height - ground_tile_height * ground_depth:
                    screen.blit(groundtile, (x, y))
                else:
                    screen.blit(undergroundtile, (x, y))

        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: #yay movement, this was more challening than initially though
            #print('left was pressed')
            players_rect.x -= vel + 1

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            players_rect.x += vel
        
        if keys[pygame.K_i]:
            show_inventory = True

 
        if keys[pygame.K_SPACE]:
            print('space was pressed')
                    
            # Check if a hotbar slot is selected
            if hotbar_slot_selected:
                use_item(hotbar_slot_selected, player)
                print('item is supposedly used')
                #hotbar_slot_selected = None



        update_hotbar_selection(keys)
        draw_hotbar_selection()
        
    
        if keys[pygame.K_e]:
            interact = True
            #interact = False
      
        if interact:
            if players_rect.colliderect(villagechief_image_rect):
                show_npcdialogbox = True
                # Check if the player gets a mana/health potion
            if random.random() <= health_potion_chance:
                # Check if there is an empty slot among the first 3 hotbar slots
                empty_slot = next((slot for slot in hotbar_slots[:5] if slot.item is None), None)
                if empty_slot:
                    # Give the player a mana/health potion and set it in the empty slot
                    potion_name = random.choice(['Sip of Health', 'Sip of Mana'])
                    potion = next((potion for potion in potions if potion['name'] == potion_name), None)
                    if potion:
                        empty_slot.set_item(potion)
            else:
                # Calculate the distance between player and NPC
                distance = abs(players_rect.centerx - villagechief_image_rect.centerx)
                if distance >= 32:  # Adjust the threshold as needed
                    interact = False
                    show_npcdialogbox = False
                    npc_dialog_text = None

  
        if players_rect.colliderect(thewildsign_rect):
            player_gravity = 0
            save_player_data(player.selected_player, player.user_input, player.player_score, player.player_health, player.player_mana, player.player_level, hotbar_items)

            enter_wilds(player)
  

        if show_npcdialogbox:
            if npc_dialog_text is None:  # Check if a quote has not been assigned yet
                random_quote = random.choice(quotes)
                lines = random_quote.split('\n')  # Split the quote into lines based on line breaks
                npc_dialog_text = []
                for line in lines:
                    npc_dialog_text.append(font.render(line, True, (0, 0, 0)))

                line_height = npc_dialog_text[0].get_height()
                total_height = line_height * len(npc_dialog_text)
                npc_dialog_text_rect = npcdialogbox_rect.inflate(-20, -(total_height + 20))

            screen.blit(npcdialogbox, npcdialogbox_rect)

            for i, text_surface in enumerate(npc_dialog_text):
                text_rect = text_surface.get_rect(topleft=(npc_dialog_text_rect.left + 10, npc_dialog_text_rect.top + 10 + (i * line_height)))
                screen.blit(text_surface, text_rect)
        
            
            screen.blit(npcexitbutton, npcexitbutton_rect)
            #screen.blit(npc_dialog_text, npc_dialog_text_rect)

            
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

        # Update projectile positions
   

        #active displays of health and mana

        #health
        player_health_base = pygame.Rect(100, 175, 150, 27)
        player_health_active = pygame.Rect(100, 175, player.player_health, 27)
        
        # Here I want to load text to add to my health bars
        health_text = font.render("Hp: " + str(player.player_health), False, (65,67,69))
        health_text_rect = health_text.get_rect(topleft = (100,173))

        # Here I am drawing instead of blitting my health bars
        pygame.draw.rect(screen, (200, 15, 15), player_health_base)
        pygame.draw.rect(screen, (15, 200, 15), player_health_active)

        #here I am going to draw/render/blit my health text to the rects.
        screen.blit(health_text, health_text_rect)

        #mana
        player_mana_base = pygame.Rect(100, 250, 150, 27)
        player_mana_active = pygame.Rect(100, 250, player.player_mana, 27)
        
        # Here I want to load text to add to my mana bars
        mana_text = font.render("Mp: " + str(player.player_mana), False, (100,100,100))
        mana_text_rect = mana_text.get_rect(topleft = (100, 250))

        # Here I am drawing instead of blitting my mana bars
        pygame.draw.rect(screen, (15, 15, 100), player_mana_base)
        pygame.draw.rect(screen, (50, 50, 200), player_mana_active)

        #here I am going to draw/render/blit my mana text to the rects.
        screen.blit(mana_text, mana_text_rect)

        pygame.display.update()
        clock.tick(60)


    pygame.quit()


#the above is the village loop where the player can interact with npc's buy and sell items, and have a safe place from enemies, and respawn if fallen in combat

#the below code will pertain to my other active states where the player can explore environments, defeat enemies and gather resources and items.


#I am going to attempt to make my first enemy class that can then contain multiple enemies instead of just my one earthslime enemy so far.
class Enemy:
    def __init__(self, image, spawn_position, health, exp_value, damage, speed, drop_item):
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = spawn_position
        self.health = health
        self.max_health = health
        self.exp_value = exp_value
        self.damage = damage
        self.speed = speed
        self.drop_item = drop_item
        self.gravity = 4

    def update(self, gravity):
        self.gravity += gravity
        self.rect.y += self.gravity

    def handle_collision(self, groundtile_rect, players_rect, player_health):
        if self.rect.colliderect(groundtile_rect):
            self.gravity = 0



        if self.rect.colliderect(players_rect):
            #print('collision but no damage dealt')
            player_health -= self.damage#this is where I need to ask chatgpt about how to handle damage from different types of enemies.
        return player_health

    def move(self, players_rect):
        
        #this code allows the blitted enemies to follow after the player.
        dx = players_rect.x - self.rect.x
        distance = math.sqrt(dx ** 2)
        if dx >= 50 or dx <= -50:
            self.rect.x += self.speed * (dx / distance)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        

#The wilds is the first area that the player will be able to explore other than the village.
def enter_wilds(player):


    #Here I want all my player variables
    vel = 6 #vel, short for velocity, could be called 'movement' but represents the rate at which it will move.
    gravity = 0.2
    player_gravity = 0.0
    jumping = False
    jump_count = 12
    can_jump = True
    jump_speed = 0.15
    spell_cast_timer = 0


    #Here I want my Environment vairables
    ground_depth = 3
    ground_tile_height = 32
  


    #Here I want logic variables like inventories, items, interactables, and options.
    show_inventory = False
    show_ingamemenu = False
    hotbarslot01_selected = False

    #for now I am placing my spell variables here even though I wish to turn it into a different .py file and import them to reduce overall code.
    #spell variables

    #here I want all of my enemy variables
    earthslime_image = pygame.image.load('graphics/ingamegraphics/earthslime.png')
    stonegolem_image = pygame.image.load('graphics/ingamegraphics/stonegolem.png')

    enemy_options = [
        {
            'image': earthslime_image,
            'spawn_position': (random.randint(0, screen_width - earthslime_image.get_width()), - earthslime_image.get_height()),
            'health': 10,
            'exp_value': 5,
            'damage': 1,
            'speed' : 5,
            'drop_item': 'slime_eyes'
        },
        
        {
            'image': stonegolem_image,
            'spawn_position': (
                random.choice([0, screen_width - stonegolem_image.get_width()]),
                random.randint(0, screen_height - stonegolem_image.get_height())
                ),
            'health': 20,
            'exp_value': 5,
            'damage': 10,
            'speed': 2,
            'drop_item': 'stone_fragment'
        }
        #when the time comes I will start to add more enemies, this is just changing from one enemy, to now

        ]
    
    #enemy variables the reflect the above class enemy and enemy options, starts with an empty list , a max count with the initial start being zero. then the timer and interval.
    enemies = []
    max_enemies = 10
    current_enemies = 0
    enemy_gravity = 4
    spawn_timer = 0
    spawn_interval = 1000

    
    #Here I want to load new images for my Environment, Player, enemies, and other entities, and then User Interface.
    #Environment
    groundtile = pygame.image.load('graphics/ingamegraphics/grassblock.png')
    undergroundtile = pygame.image.load('graphics/ingamegraphics/dirtblock.png')

    #Player, enemies, and other variables.
    #players_image = pygame.image.load('graphics/player.png')
    players_image = pygame.image.load(f'graphics/ingamegraphics/players/{selected_player.lower()}.png')  # Load the image based on the selected player
    player_inventory_image = pygame.image.load('graphics/ingamegraphics/playerinventory.png')
    inventoryexit_button = pygame.image.load('graphics/ingamegraphics/inventory_exit_button.png')
    hotbar = pygame.image.load('graphics/ingamegraphics/playerhotbar.png')

    #magic_attack = pygame.image.load('graphics/ingamegraphics/manablast.png')
    sign_village = pygame.image.load('graphics/ingamegraphics/townsign.png')


    #Here is where I handle the wilds in-game rects for player, enemies, and environment.
    #Environment rects, Player Rect.
    groundtile_rect = pygame.Rect(0, screen_height - 96, screen_width, 32)
    players_rect = players_image.get_rect(center = (250, 350))
    sign_rect = sign_village.get_rect(left =0, bottom = groundtile_rect.top)


    #Player inventory Rects
    player_inventory_rect = pygame.Rect(200,200, player_inventory_image.get_width(), player_inventory_image.get_height())
    inventoryexit_button_rect = pygame.Rect(player_inventory_rect.right - 32, player_inventory_rect.top, 30,30)
    hotbar_rect = hotbar.get_rect(topleft= (800, 500))


    saved_data = load_saved_player_data()

    if saved_data is not None:
        user_input = saved_data.get('player', '')  # Assign the saved name to user_input
        player_score = saved_data.get('score', '')
        player.player_health = saved_data.get('health', 150)
        player_mana = saved_data.get('mana', 10)
        player_level = saved_data.get('level', 0)
        hotbar_items = saved_data.get('hotbar_items', [])

    running = True
    

    while running:
        
        elapsed_time = clock.tick(60)

        player_gravity += gravity
        players_rect.y += player_gravity

        spell_cast_timer -= elapsed_time
        spawn_timer += elapsed_time
    
        screen.fill('darkgrey')
        screen.blit(sign_village, sign_rect)
        #handle_enemy_collision(player_health)



        for i, slot in enumerate(hotbar_slots):
            screen.blit(slot.image, slot.rect)

            if slot.item:
                # Calculate the position to blit the item image inside the slot
                item_x = slot.rect.x + (slot.rect.width - slot.item['image'].get_width()) // 2
                item_y = slot.rect.y + (slot.rect.height - slot.item['image'].get_height()) // 2

                # Blit the item image onto the hotbar slot
                

                screen.blit(slot.item['image'], (item_x, item_y))
                #print(f"Item {i+1}: {slot.item}")
                #print(f"Item position: ({item_x}, {item_y})")


        for y in range(screen_height - ground_tile_height * ground_depth, screen_height, ground_tile_height):
            for x in range(0, screen_width, ground_tile_height):
                if y == screen_height - ground_tile_height * ground_depth:
                    screen.blit(groundtile, (x,y))
                else:  
                    screen.blit(undergroundtile, (x, y))


        #print('before enemy loop')
        for enemy_data in enemy_options:
            #print(type(enemy_data))
            enemy_image = enemy_data['image']
            spawn_position = enemy_data['spawn_position']
            health = enemy_data['health']
            exp_value = enemy_data['exp_value']
            damage = enemy_data['damage']
            enemy_speed = enemy_data['speed']
            drop_item = enemy_data['drop_item']

            if spawn_timer >= spawn_interval and current_enemies <= max_enemies: #I am doing a small change right here because I want to slighlty amp up the slimes and get rid of a cap for now.
                enemy_option = random.choice(enemy_options)
                enemy_image = enemy_option['image']
                spawn_position = enemy_option['spawn_position']
                health = enemy_option['health']
                exp_value = enemy_option['exp_value']
                damage = enemy_option['damage']
                enemy_speed = enemy_option['speed']
                drop_item = enemy_option['drop_item']

                enemy = Enemy(enemy_image, spawn_position, health, exp_value, damage, enemy_speed, drop_item)
                enemies.append(enemy)
                current_enemies += 1
                spawn_timer = 0

                if random.random() < 0.15:
                    spawn_position = (screen_width - spawn_position[0] - enemy_image.get_width(), spawn_position[1])

                    # Spawn the golem from the right side
                    enemy = Enemy(enemy_image, spawn_position, health, exp_value, damage, enemy_speed, drop_item)
                    enemies.append(enemy)
                    current_enemies += 1

                spawn_timer = 0

            
        #print('after enemy loopdd')


        for enemy in enemies:
            enemy.update(gravity)
            enemy.handle_collision(groundtile_rect, players_rect, player.player_health)
            enemy.move(players_rect)
            player.player_health = enemy.handle_collision(groundtile_rect, players_rect, player.player_health)
            enemy.draw(screen)

        #spell_pages = []
        #for option in spell_page:
            #image = option['image']
            #attack_image = option['attack_image']
            #name = option['name']
            #mana_cost = option['mana_cost']
            #damage = option['damage']
            #speed = option['speed']
            #value = option['value']
            #spell_page = SpellPage(image, attack_image, name, mana_cost, damage, speed, value)
            #spell_page.rect = image.get_rect()  # Update the rect attribute
            #attack_image_rect = attack_image.get_rect()
            #spell_pages.append(spell_page)    
            #screen.blit(spell_page.image, spell_page.rect) #these will be blitted in the hotbar.
            #screen.blit(attack_image, attack_image_rect)
                    



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
                        save_player_data(player.selected_player, player.user_input, player.player_score, player.player_health, player.player_mana, player.player_level, hotbar_items)



            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    show_ingamemenu = True
    
              
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]: #yay movement, this was more challening than initially though
            #print('left was pressed')
            players_rect.x -= vel + 1

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            players_rect.x += vel
        
        hotbar_slot = hotbar_slots[0]

        if keys[pygame.K_1]:
            hotbar_slot_selected = hotbar_slot
            pygame.draw.rect(screen, (255,0,0), slot_rect, 2)
            hotbar_slot = hotbar_slots[0]  # Selected hotbar slot 1
            if hotbar_slot.item:
                # Perform the action for using the item (casting the spell)
                spell_page = hotbar_slot.item
                #cast_spell()
            else:
                pass
                # No item in the selected hotbar slot
                # Handle accordingly

                #I need to tell chatgpt that I only want the event or key press '1' to select the 1st slot. the spell does not get cast unless
                #the player presses space and the 1st slot in the hotbar is selected it will fire the selected spell's attack image.
                #I will eventually have items in the hotbar that do other things.

        
        
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

        if keys[pygame.K_SPACE]:
            #cast_spell(keys, players_rect, spell_page)
            player.player_health += 1 #this is just so something happens right now
            print('space was pressed')
            
         #cast_spell()
        #def cast_spell():
            #hotbar_slot = hotbar_slots[0]

           # if hotbar_slot.item and hotbar_slot_selected and keys[pygame.K_SPACE]:

                #spell_page = hotbar_slot.item  # Replace with the appropriate index for the desired spell page
                # Perform the actions for casting the spell using spell_page attributes
                # For example, create a magic attack instance using spell_page.attack_image
               #magic_attack_rect = spell_page.attack_image.get_rect()
                #magic_attack_rect.center = players_rect.center
                            # Rest of the logic for casting the spell
                                


                #THE BELOW CODE IS MY OLD CODE FOR ALLOWING THE PLAYER TO ATTACK, BUT I AM ADDING IN ITEMS AND SPELL PAGES SO I NEED A NEW SYSTEM
                # Fire magic attack
               # dy = mouse_y - magic_attack_rect.centery
                # Normalize the direction vector #thanks to chat gpt honestly, I dont know the logic behind this
               # magnitude = math.sqrt(dx ** 2 + dy ** 2)
                #direction = (dx / magnitude, dy / magnitude)
                # Set the speed of the magic attack
                #spell_speed = 10
                # Adjust the position and speed based on the direction
                #magic_attack_rect.x += direction[0] * spell_speed
                #magic_attack_rect.y += direction[1] * spell_speed
                #magic_attacks.append((magic_attack_rect, direction))
                #spell_cast_timer = 300

        #for magic_attack_rect, direction in magic_attacks:
            #magic_attack_rect.x += direction[0] * spell_speed
            #magic_attack_rect.y += direction[1] * spell_speed

           #   enemies.remove(enemy)
                     #   current_enemies -= 1
                        # Reset the enemy's position to the top of the screen
                        #enemy.rect.x = random.randint(0, screen_width - enemy.rect.width)
                        #enemy.rect.y = -enemy.rect.height

                    #adds one to the player_score or enemies killed, I really need to pick one and stick with it.
                   # player_health += 10

                #Remove the magic attack
                    #if (magic_attack_rect,direction) in magic_attacks:
                        #magic_attacks.remove((magic_attack_rect, direction))
                    #break

            #screen.blit(magic_attack, magic_attack_rect)
        
        #here I want to clearly define my player's score and it's rect.
        player_score_text = font.render("Player Score: " + str(player.player_score), False, (50, 50, 75))
        player_score_text_rect = player_score_text.get_rect(midleft = (50, 125)) #this is not a button it's the 'background' to the text
        screen.blit(player_score_text,player_score_text_rect)

        player_health_base = pygame.Rect(100, 175, 150, 27)
        player_health_active = pygame.Rect(100, 175, player.player_health, 27)
        
            
         # Here I want to load text to add to my health bars
        health_text = font.render("Hp: " + str(player.player_health), False, (65,67,69))
        health_text_rect = health_text.get_rect(topleft = (100,173))

            
            
        # Here I am drawing instead of blitting my health bars
        pygame.draw.rect(screen, (200, 15, 15), player_health_base)
        pygame.draw.rect(screen, (15, 200, 15), player_health_active)



        #here I am going to draw/render/blit my health text to the rects.
        screen.blit(health_text, health_text_rect)
        #screen.blit(playerlevel_text, playerlevel_text_rect)



        if players_rect.colliderect(sign_rect):
            player_gravity = 0
            save_player_data(player.selected_player, player.user_input, player.player_score, player.player_health, player.player_mana, player.player_level, hotbar_items)
            enter_village(player)

        if player.player_health >= 160:
            player.player_health = 150

        if player.player_health <= 0:
            player.player_score -= 10
            player.player_health = 25
            save_player_data(player.selected_player, player.user_input, player.player_score, player.player_health, player.player_mana, player.player_level, hotbar_items)
            enter_village(player)

        #if player_score % 10:
            #player_level += 1

        screen.blit(players_image,players_rect)
        screen.blit(player_score_text, player_score_text_rect)
        screen.blit(hotbar, hotbar_rect)


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

    fullscreenbutton = pygame.image.load('graphics/optionsbuttons/fullscreenop.png')
    fullscreenbutton_rect = fullscreenbutton.get_rect(topleft = (50,500))


        
    screen.blit(menubutton, menubutton_rect)
    screen.blit(fullscreenbutton, fullscreenbutton_rect)
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
            
            if fullscreenbutton_rect.collidepoint((mx, my)):
                if click:
                    if pygame.display.get_surface().get_flags() & pygame.FULLSCREEN:
                        pygame.display.set_mode((screen_width, screen_height))
                    else:
                        pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
                    pygame.display.flip()
                    options()  # Refresh the screen

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
