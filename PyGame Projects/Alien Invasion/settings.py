import pygame

class Settings():
	
	def __init__(self):
		
		self.screen_width = 1200
		self.screen_height = 600
		
		self.bg_color = (230, 230, 230)
		
		#For setting image as background
		#self.bg_color = pygame.image.load('Images/tiles-map.png')
		self.ship_speed_factor = 1.5
