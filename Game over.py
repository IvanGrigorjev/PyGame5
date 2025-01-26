import os
import sys

import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 600, 300
FPS = 30
SPEED = 200


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
    pygame.display.set_caption('Game over')

    gameover = load_image('gameover.png')
    current_position = -WINDOW_WIDTH
    speed = 8

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('blue')
        screen.blit(gameover, (current_position, 0))
        if current_position < 0:
            current_position += SPEED//FPS
        # pygame.mouse.set_visible(True)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
