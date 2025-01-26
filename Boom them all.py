import os
import random
import sys
from random import randint

import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
FPS = 30
N = 20


class Bomb(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__()
        self.image = load_image("bomb.png")
        self.size = WINDOW_SIZE
        group.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, WINDOW_WIDTH - self.rect[2])
        self.rect.y = randint(0, WINDOW_HEIGHT - self.rect[3])
        self.status = 1

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = load_image("boom.png")


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Boom them all')

    all_sprites = pygame.sprite.Group()

    for _ in range(N):
        Bomb(all_sprites)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('white')
        all_sprites.update(event)
        all_sprites.draw(screen)
        pygame.mouse.set_visible(True)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
