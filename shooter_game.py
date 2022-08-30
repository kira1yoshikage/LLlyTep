#Создай собственный Шутер!

from pygame import *
from GameSprite import GameSprite
from Player import *
from Enemy import *
from Bullet import *

def main():
    clock = time.Clock()
    FPS = 60

    mixer.init()
    mixer.music.load('space.ogg')
    #mixer.music.play()

    font.init()
    font1 = font.SysFont('Arial', 35)
    win = font1.render('YOU WIN!',True,(255,255,255))
    lose = font1.render('YOU LOSE!',True,(180,0,0))

    image_back = 'galaxy.jpg'
    image_player = 'rocket.png'
    image_ufo = 'ufo.png'
    image_asteroid = 'asteroid.png'

    win_width = 1200
    win_height = 700
    window = display.set_mode((win_width,win_height))
    display.set_caption('ВАУ ВАУ ОМГ МДЖА ВЫПАЛ да кста реально выпал всё-таки')

    background = transform.scale(image.load(image_back),(win_width,win_height))

    ship = Player(image_player,5,win_height-100,80,100,10,win_width,win_height,window)

    monsters = sprite.Group()
    for i in range(1,6):
        monster = Enemy(image_ufo,randint(80,win_width-80),-40,80,50,randint(1,3),win_width,win_height,window)
        monsters.add(monster)

    bullets = sprite.Group()
    asteroids = sprite.Group()
    for i in range(1,3):
        asteroid = Enemy(image_asteroid,randint(80,win_width-80),-40,80,50,randint(1,5),win_width,win_height,window)
        asteroids.add(asteroid)
    
    score = 0
    lost = 0
    ammo = 10
    reload_ammo = 0

    game = True
    finale = False
    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    #fire_sound.play()
                    bullets.add(ship.fire())
                    ammo = ammo - 1
                    if ammo <= 0:
                        reload_ammo = reload_ammo + 1

        if not finale:
            window.blit(background,(0,0))

            lose_text = font1.render('Пропущено:' + str(lost),True,(255,255,255))
            window.blit(lose_text,(10,10))
            score_text = font1.render('Счёт:' + str(score),True,(255,255,255))
            window.blit(score_text,(10,35))

            ship.reset() 
            monsters.update()
            bullets.update()
            asteroids.update()

            ship.movement()

            monsters.draw(window)
            if ammo >= 0:
                collides = sprite.groupcollide(monsters,bullets,True,True)
                for c in collides:
                    score = score + 1
                    monster = Enemy(image_ufo,randint(80,win_width - 80), -40,80,50,randint(1,3),win_width,win_height,window)  
                    monsters.add(monster)
                ammo_text = font1.render('Патроны:' + str(ammo),True,(255,255,255))
                window.blit(ammo_text,(10,60))
                bullets.draw(window)  
            elif ammo <= 0:
                ammo_text = font1.render('Перезарядка...(нажмите 5 раз "пробел")',True,(255,255,255))
                window.blit(ammo_text,(10,60))
                if reload_ammo >= 5:
                    reload_ammo = 0
                    ammo = 10

            asteroids.draw(window)
            for a in monsters:
                lost += a.update()

            if sprite.spritecollide(ship,monsters,False) or lost >= 5:
                finale = True
                window.blit(lose,(200,200))

            if sprite.spritecollide(ship,asteroids,False):
                finale = True
                window.blit(lose,(200,200))

            if score >= 15:
                finale = True
                window.blit(win,(200,200))

            display.update()
        
        clock.tick(FPS)

if __name__ == '__main__':
    main()