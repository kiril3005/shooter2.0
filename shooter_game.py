#Создай собственный Шутер!
from pygame import *
from random import *
font.init()
win = display.set_mode((700, 500))
display.set_caption('Шутер')
lost1 = 0
shet1 = 0
font1 = font.Font(None, 36)
font2 = font.Font(None, 72)
lost = font1.render('Пропущено ' + str(lost1), 1, (255, 255, 255))
shet = font1.render('Счёт ' + str(shet1), 1, (255, 255, 255))
winn = font2.render('''Вы выиграли! 2 уровень''', 1, (255, 255, 255))
winn1 = font2.render('''Вы выиграли!''', 1, (255, 255, 255))
lose = font2.render('''Вы проиграли''', 1, (255, 255, 255))
bg = transform.scale(image.load('galaxy.jpg'), (700, 500))
start = time.get_ticks()

class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, wid, hei, pl_x, pl_y, pl_speed):
        super().__init__()
        self.wid = wid
        self.hei = hei
        self.image = transform.scale(image.load(pl_image), (self.wid, self.hei))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
    def dvizh(self):
        keys_pressed = key.get_pressed()
        if self.rect.y > -50:
            self.rect.y -= self.speed
        if keys_pressed[K_SPACE]:
            bul = GameSprite
            self.rect.x = rock.rect.x + 20
            self.rect.y = rock.rect.y
    
    def update(self):
        global lost1
        self.rect.y += self.speed
        if self.rect.y > 550:
            self.rect.y = -40
            self.rect.x = randint(1, 650)
            self.speed = randint(1, 3)
            
            lost1 += 1

    def upr(self):
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
    def fire(self):
        
        bul = Bullet()
        buls.add(bul)

buls = sprite.Group()
class Bullet(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = transform.scale(image.load('bullet.png'), (30, 30))
        self.speed = 4
        self.rect = self.image.get_rect()
        self.rect.x = rock.rect.x + 20
        self.rect.y = 415
    def update(self):
        if self.rect.y < -5:
            self.kill()
        win.blit(self.image, (self.rect.x, self.rect.y))
        self.rect.y -= self.speed
        keys = key.get_pressed()
        


rock = GameSprite('maz.png', 70, 90, 315, 415, 7)

monsters = sprite.Group()
for i in range(5):
    monster = GameSprite('he.png', 70, 50, randint(1, 650), -40 , randint(1 ,3))
    monsters.add(monster)
a = False
l = False
o = False 
game = True
clock = time.Clock()
fps = 60
while game:
    win.blit(bg, (0, 0))
    rock.reset()
    keys_pressed = key.get_pressed()
    if o:
        game = False
    if l:
        game = False
    else:
        win.blit(lost,(0,0))
    buls.draw(win)
    buls.update()
    rock.upr()
    lost = font1.render('Пропущено ' + str(lost1), 1, (255, 255, 255))
    
    shet = font1.render('Счёт ' + str(shet1), 1, (255, 255, 255))
    win.blit(shet, (0,40))
    monsters.draw(win)
    monsters.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if keys_pressed[K_SPACE]:
            end = time.get_ticks()
            if end - start >= 300:
                rock.fire()
                start = time.get_ticks()
    if sprite.groupcollide(monsters, buls, True, True):
        shet1 += 1
        monster = GameSprite('he.png', 70, 50, randint(1, 650), -50 , randint(1 ,3))
        monsters.add(monster)
    if shet1 == 10:
        win.blit(winn, (50,200))
        if o:
            time.delay(3000)
        bg = transform.scale(image.load('ogo.png'), (700, 500))
        a = True
        
        o = True
    if lost1 == 10:
        lost = font1.render('Пропущено ' + str(lost1), 1, (255, 255, 255))
        win.blit(lost,(0,0))
        win.blit(lose, (150,200))
        if l:
            time.delay(3000)
        
        
        l = True

    clock.tick(fps)
    display.update()

lost1 = 0
shet1 = 0 
game1 = True
for monster in monsters:
    monster.rect.x = randint(1, 650)
    monster.rect.y = -50
for i in buls:
    i.kill()
rock.rect.x = 315
monster = GameSprite('he.png', 70, 50, randint(1, 650), -50 , randint(1 ,3))
monsters.add(monster)
b = False
if a:
    while game1:
        win.blit(bg, (0, 0))
        rock.reset()
        keys_pressed = key.get_pressed()
        if b:
            game1 = False
            
        buls.draw(win)
        buls.update()
        rock.upr()
        lost = font1.render('Пропущено ' + str(lost1), 1, (255, 255, 255))
        win.blit(lost,(0,0))
        shet = font1.render('Счёт ' + str(shet1), 1, (255, 255, 255))
        win.blit(shet, (0,40))
        monsters.draw(win)
        monsters.update()
        for e in event.get():
            if e.type == QUIT:
                game1 = False
            if keys_pressed[K_SPACE]:
                end = time.get_ticks()
                if end - start >= 300:
                    rock.fire()
                    start = time.get_ticks()
        if sprite.groupcollide(monsters, buls, True, True):
            shet1 += 1
            monster = GameSprite('he.png', 70, 50, randint(1, 650), -50 , randint(1 ,3))
            monsters.add(monster)
        if shet1 == 20:
            win.blit(winn1, (200,200))
            if b:
                time.delay(3000)
            bg = transform.scale(image.load('ogo.png'), (700, 500))
            b = True
        clock.tick(fps)
        display.update()