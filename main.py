import pygame

class Player():
    def __init__(self, x, y, filename, speed, w, h,):
        super().__init__()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.w = w
        self.h = h
        self.filename = filename
        self.rect = self.player_image.get_rect()



platform = Player(10, 350,"pixil-frame.png" , 5, 30, 10)

pygame.init()
window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()

run = True
while run:
    for e in pygame.event.get():
        if e.type ==pygame.QUIT:
            run = False



    #оновлення

    #рендер


    pygame.display.update()

    fps.tick(60)
