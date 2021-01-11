class Settings:
    """setting"""

    def __init__(self):
        """init"""
        # 屏幕设置
        self.screen_width = 1200
        self.scree_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船的设置
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3

