# Разработай свою игру в этом файле!
from pygame import *
# Блок основной части программы
#Персонаж
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed) :
        super().__init__()
        self.image = transform.scale(image.load (player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#наследник. Управление стрелками
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 400:
            self.direction = 'right'

        if self.rect.x >= win_width -85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

#Класс для спрайтов-препятствий
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        #картинка стены - прямоугольник нужных размеров
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))

        #каждый спрайт должен хранить свойство rect- прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image,( self.rect.x, self.rect.y))
        
# Сцена
win_width = 700
win_height = 500
background = transform.scale(image.load('background1.jpg'), (win_width, win_height))
display.set_caption('Моя вторая игра')
window = display.set_mode((700,500))
run = True

#Игровая сцена
player = Player('pig.png',325 ,  win_height - 300, 4)
monster = Enemy('gamer.png', win_width - 80, 280, 2)
final = GameSprite('game_over.png', win_width - 120, win_height - 80, 0)

w1 = Wall(150, 0, 0, 150, 110, 350, 10)
w2 = Wall(150, 0, 0, 250, 300, 150, 10)
w6 = Wall(150, 0, 0, 400, 420, 100, 10)
w7 = Wall(150, 0, 0, 10, 150, 150, 10)
w3 = Wall(150, 0, 0, 490, 110, 10, 200)
w4 = Wall(150, 0, 0, 150, 110, 10, 200)
w5 = Wall(150, 0, 0, 400, 300, 10, 130)

#Таймер
game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0,))

#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('win.ogg')
kick = mixer.Sound('lose.ogg')

#Игровой цикл
while run:
    for e in event.get():
        if e .type == QUIT:
            run = False
    if finish != True:
        window.blit(background, (0,0))
        player.update()
        monster.update()


        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()

        #Ситуация - Проигрыш
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
            

        #Ситуация - выинрыш
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()
            

        display.update()
        clock.tick(FPS)
    else:
        finish = False
        time.delay(1000)
        player = Player('pig.png',325 ,  win_height - 300, 4)
        player.reset()
    
    

