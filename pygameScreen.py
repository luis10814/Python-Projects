import sys

import pygame

from settings import Settings

def run_game():
	
	pygame.init()
	ai_settings = Settings()
	
	# set screen size
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alian Invasion")
	# set screen color
	bg_color = (230, 230, 230)
	
	# start main loop of game
	while True:
		#watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		#redraw the screen during each pass through of the loop
		screen.fill(bg_color)
		# make each screen visible		
		pygame.display.flip()
		
run_game()
