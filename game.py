from pygame import *
font.init()
window = display.set_mode((700, 500))
display.set_caption('ping')
background=transform.scale(image.load('background.png'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, image_1, speed, x, y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(image_1), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys_pressed=key.get_pressed()
        
        if keys_pressed[K_DOWN] and self.rect.y<400:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y> 1:
            self.rect.y -= self.speed

    def update2(self):
        keys_pressed=key.get_pressed()
        
        if keys_pressed[K_s] and self.rect.y<400:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y> 1:
            self.rect.y -= self.speed

finish = False
run = True
clock = time.Clock()
FPS = 60
r_l = Player('r1.png', 3, 50, 50, 42, 118)
r_r = Player('r1.png', 3, 600, 50, 42, 118)
ball = GameSprite('ball.png', 3, 350, 60, 50, 49)
speed_x = 3
speed_y = 3
score_l = 0
score_r = 0
font2 = font.Font(None, 60)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if  finish==False:
        window.blit(background, (0, 0))
        r_l.update2()
        r_l.reset()
        r_r.update1()
        r_r.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(r_l, ball) or sprite.collide_rect(r_r, ball):
        speed_x *= -1

    if ball.rect.x > 700: 
        score_l += 1
        
        ball.rect.x = 100
        ball.rect.y = 10

    if ball.rect.x < 0:
        score_r += 1
        
        ball.rect.x = 100
        ball.rect.y = 10
    text1 = font2.render('left-' + str(score_l), 1, (255, 255, 255))
    window.blit(text1, (175, 450))
    text2 = font2.render('right-' + str(score_r), 1, (255, 255, 255))
    window.blit(text2, (525, 450))

    display.update()
    clock.tick(FPS)
