import pygame


def main():
    # init pygame
    pygame.init()

    # init window
    screen = pygame.display.set_mode((800, 600))

    # title
    pygame.display.set_caption('big ball eats small ball')

    # # load image
    # ball_image = pygame.image.load('..\\res\\ball.png')
    # # render image on the screen
    # screen.blit(ball_image, (50, 50))
    # # flash the screen
    # pygame.display.flip()

    # ball init position
    x, y = 50, 50

    # running loop
    running = True
    while running:
        # get event from event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # background
        screen.fill((255, 255, 255))

        # draw a circle (screen, color, position, radio, 0 for fill)
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)

        # flip the screen
        pygame.display.flip()

        # change ball position per 50s
        pygame.time.delay(10)
        x, y = x + 2, y + 2


if __name__ == '__main__':
    main()
