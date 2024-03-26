class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1366
        self.screen_height = 680
        self.bg_color = (31, 7, 43) # rgb

        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 8
        self.bullet_color = (255, 0, 229)
        self.bullets_allowed = 5

        # Настройки пришельцев
        self.alien_speed = 10
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево
        self.fleet_direction = 1