import os
import sys

import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 600, 95
FPS = 30


class Car(pygame.sprite.Sprite):
    def __init__(self, size, group):
        super().__init__()
        self.image = load_image("car2.png")
        self.size = size
        group.add(self)
        self.rect = self.image.get_rect()
        self.mirror_image = pygame.transform.flip(self.image, True, False)
        self.speed = 6
        self.direction = 1

    def update(self, *args):
        if self.rect.right >= self.size[0]:
            self.direction = -1
        elif self.rect.left <= 0:
            self.direction = 1
        self.rect.x += self.speed * self.direction
        if self.direction == -1:
            self.image = self.mirror_image
        elif self.direction == 1:
            self.image = load_image("car2.png")


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
    pygame.display.set_caption('Машинка')

    all_sprites = pygame.sprite.Group()
    car = Car(WINDOW_SIZE, all_sprites)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        screen.fill('white')
        all_sprites.draw(screen)
        pygame.mouse.set_visible(True)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
