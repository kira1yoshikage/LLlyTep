from pygame import *
from GameSprite import GameSprite
from Bullet import *
from time import *

class Player(GameSprite):
    def movement(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < self.width - 90:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.top,15,20,-15,self.width,self.height,self.window)
        return bullet