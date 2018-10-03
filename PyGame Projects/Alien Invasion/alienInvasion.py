import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	
	pygame.init()
	ai_settings = Settings()
	
	# set screen size
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	
	#draw ship
	ship = Ship(ai_settings, screen)
	
	# start main loop of game
	while True:
		#watch for keyboard and mouse events
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)
		
		
run_game()
