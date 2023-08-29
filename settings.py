# 将新的一些设置存储在该模块中，用来统一管理
class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        # 设置飞船的移动速度
        self.ship_speed = 1.5
        # 添加子弹的设置
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)


