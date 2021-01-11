import sys
import pygame
from game.settings import Settings
from game.ship import Ship
import game.game_functions

from pygame.sprite import Group


"""游戏入口"""


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.scree_height))
    pygame.display.set_caption("alien invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 开始游戏的主循环
    while True:
        game.game_functions.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        game.game_functions.update_bullets(bullets)
        game.game_functions.update_screen(ai_settings, screen, ship,bullets)


run_game()
