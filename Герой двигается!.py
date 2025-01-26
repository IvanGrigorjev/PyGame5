import os
import sys

import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 300, 300
FPS = 30


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
    pygame.display.set_caption('Герой двигается!')

    clock = pygame.time.Clock()
    running = True
    image = load_image("creature.png", 1)
    x, y = 0, 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                y -= 10
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                y += 10
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                x -= 10
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                x += 10

        screen.fill('white')

        screen.blit(image, (x, y))

        pygame.mouse.set_visible(True)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
