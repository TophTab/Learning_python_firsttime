import sys
import pygame

from settings import settings
from ship import Ship
import game_functions as  gf
def run_game():
    #初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings=settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color=(230,230,230)
    ship=Ship(ai_settings,screen)
    
    #开始游戏主循环
    while True:
        gf.check_events(ship)
        ship.update()
        #监视键盘和鼠标事件
        gf.update_screen(ai_settings,screen,ship)
run_game()

        
    
