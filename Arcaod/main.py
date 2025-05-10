import pygame as pg
from pygame.locals import  *

BALLSPEED = 10

class  Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((15, 15))
        self.image.fill((255, 255, 255))

        self.rect = self.image.get_rect()

        self.score = 0

        self.isMoving = True

        self.speedX = BALLSPEED
        self.speedY = BALLSPEED * -1

    def update(self, keys, platform, *args):
        if not self.isMoving:
            return

        self.rect.y += self.speedY

        hitGroup = pg.sprite.Group(platform)

        spriteHitList = pg.sprite.spritecollide(self,hitGroup, False)

        if len(spriteHitList) > 0:
            self.speedY *= -1
            self.rect.y += self.speedX

        self.rect.x += self.speedX

        if self.rect.right > 800:
                self.speedX *= -1
                self.rect.right = 800

        if self.rect.left < 0:
                self.speedX *= -1
                self.rect.left = 0

        if self.rect.top < 0:
                self.speedY *= -1
                self.rect.top = 0


class Plaform(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((60, 10))
        self.rect = self.image.get_rect(center=(400, 590))
        self.image.fill( (255, 0, 0) )

    def update(self, keys, *args):
        if keys[pg.K_a] and self.rect.x > 0:
            self.rect.x -= 15
        if keys[pg.K_d] and self.rect.x < 740:
            self.rect.x += 15

class Game:
    def __init__(self):
        self.score = 0
        self.game_over = 0

        self.sprites = pg.sprite.Group()
        self.platform = Plaform()
        ball = Ball()
        self.sprites.add(self.platform)
        self.sprites.add(ball)

    def process_event(self):
        for event in pg.event.get():
            if event.type == QUIT:
                return True
            if event.type == MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()

    def run_logic(self):
        pass

    def display_frame(self, screen, keys):
        screen.fill((0, 0, 0))
        self.sprites.update(keys, self.platform)
        self.sprites.draw(screen)
def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Arcanoid")

    end_game = False
    clock = pg.time.Clock()

    game = Game()

    while not end_game:
        end_game = game.process_event()
        game.run_logic()
        keys = pg.key.get_pressed()
        game.display_frame(screen, keys)

        pg.display.flip()

        clock.tick(60)


main()