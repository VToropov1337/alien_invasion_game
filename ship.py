import pygame


class Ship:

    def __init__(self,ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.ai_settings = ai_settings
        # Сохранение вещественной координаты центра корабля.
        self.center = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # if self.moving_right:
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        # if self.moving_left:
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Обновление атрибута rect на основании self.center.
        self.rect.centerx = self.center