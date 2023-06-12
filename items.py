import pygame
import math


#this is my items.py file
#from items import  Potion, Weapon, Trinket, SpellPage, this is the line I am using in my main file SlimeRanger.py


screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height), 0, 32)

spell_page_01 = pygame.image.load('graphics/spells/arcane_ball.png')
spell_page_02 = pygame.image.load('graphics/spells/ball_of_fire.png')

spell_pages = [
    {   
        'image': spell_page_01,
        'name': 'Arcane Ball',
        'type': 'spell',
        'magic_attack_image': pygame.image.load('graphics/spells/arcane_ball_cast.png'),
        'mana_cost': 5,
        'damage': 10,
        'spell_speed': 1,
        'value': 10
    },
    {   
        'image': spell_page_02,
        'name': 'Ball of Flame',
        'type': 'spell',
        'magic_attack_image': pygame.image.load('graphics/spells/ball_of_fire_cast.png'),
        'mana_cost': 8,
        'damage': 15,
        'spell_speed': 2,
        'value': 15
    }
]


potions = [
    {
        'image': pygame.image.load('graphics/potions/sipofhealth.png'),
        'name': 'Sip of Health',
        'type': 'potion',
        'effects': 'restore_health',
        'restore_amount': 25,
        'value': 20
    },
    {
        'image': pygame.image.load('graphics/potions/sipofmana.png'),
        'name': 'Sip of Mana',
        'type': 'potion',
        'effects': 'restore_mana',
        'restore_amount': 15,
        'value': 20
    }
]

crafting_materials = [
    {
        'image': pygame.image.load('graphics/craftingmats/slimeeyes.png'),
        'name': 'Slime Eyes',
        'type': 'crafting_material',
        'value': 10,
        'cancraft': False
    },
    {
        'image': pygame.image.load('graphics/craftingmats/stonefragment.png'),
        'name': 'Stone Fragment',
        'type': 'crafting_material',
        'value': 10,
        'cancraft': False
    }
]

weapons = [
    {
        'image': pygame.image.load('graphics/items/weapons/twig_wand.png'),
        'name': ' Twig Wand',
        'type': 'weapon',
        'damage': 5,
        'speed': 2,
        'value' : 20
    },

    {
        'image': pygame.image.load('graphics/items/weapons/crystal_staff.png'),
        'name': 'Crystal Staff',
        'type': 'weapon',
        'damage': 15,
        'speed': 3,
        'value' : 25
    }
]
trinkets = [
    {
        'image': pygame.image.load('graphics/items/trinkets/ringofmanarestore.png'),
        'name' : "Ring of Restore Mana",
        'type' : 'trinket',
        'effects': 'restore_mana',
        'restore_amount': 20, #I want this trinket to take away twenty health and add twenty mana
        'value' : 25
    }
]




class Item:
    def __init__(self, image, name, item_type, value):
        self.image = image
        self.name = name
        self.item_type = item_type
        self.value = value

class CraftingMaterial(Item):
    def __init__(self, image, name, value, can_craft):
        super().__init__(image, name, 'CraftingMaterial', value)
        self.can_craft = can_craft

class Potion(Item):
    def __init__(self, image, name, value, effects, restore_amount):
        super().__init__(image, name, 'Potion', value)
        self.effects = effects
        self.restore_amount = restore_amount

    def activate(self, player):
        if self.effects == 'restore_mana':
            player.player_mana += self.restore_amount #increases mana 
            print("restored mana: ", self.restore_amount)
            return player.player_mana

        elif self.effects == 'restore_health':
            player.player_health += self.restore_amount#increase health
            print('restored_health:', self.restore_amount)
            return player.player_health

class Weapon(Item):
    def __init__(self, image, name, damage, speed, value):
        super().__init__(image, name, 'Weapon', value)

class Trinket(Item):
    def __init__(self, image, name, value, effects, restore_amount):
        super().__init__(image, name, 'Trinket', value)
        self.effects = effects
        self.restore_amount = restore_amount

    def activate(self, player):
        if self.name == 'Ring of Restore Mana':
            player.player_mana += self.restore_amount #increases mana by taking away from player health
            player.player_health -= self.restore_amount
            print("Ring of Restore was activated")
            return player.player_health, player.player_mana
            



class SpellPage(Item):
    def __init__(self, image, magic_attack_image, name, mana_cost, damage, spell_speed, value):
        super().__init__(image, name, 'Spell', value)
        self.attack_image = magic_attack_image
        self.mana_cost = mana_cost
        self.damage = damage
        self.spell_speed = spell_speed

    

      


      
          


