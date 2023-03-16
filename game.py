from pygame import *
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

    
    display.update()
    clock.tick(FPS)