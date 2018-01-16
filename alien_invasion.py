import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
	#initialize game and create screen object.

	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	play_button = Button(ai_settings, screen, "Play")
	stats = GameStats(ai_settings)
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#Start main loop for the game.
	while True:

		gf.check_events(ai_settings, screen, ship, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, 
			play_button)

def check_events(ship, screen, ai_settings, bullets):
	#Watch for keyboard and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship, screen, ai_settings, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship, screen, ai_settings, bullets)
	

run_game()