import pygame
from random import randint

import ball as ba
import color as co
import button as bu


def ball_check(balls, screen):
    # print or remove balls
    for ball in balls:
        if ball.alive:
            ball.draw(screen)
        else:
            balls.remove(ball)

    return balls


def ball_move(balls, screen):
    # change ball position per 10ms
    pygame.time.delay(10)
    for ball in balls:
        ball.move(screen)
        # check this ball can eat other ball or not
        for other in balls:
            ball.eat(other)

    return balls

def main():
    # container for all balls
    balls = []

    # win_flag
    win_flag = False

    # init pygame
    pygame.init()

    # init screen
    screen = pygame.display.set_mode((800, 600))
    screen_width, screen_height = screen.get_size()

    # title
    pygame.display.set_caption('big ball eats small ball')

    # init button
    # button base para
    button_width = screen_width/20
    button_height = button_width/2
    button_pos_x = button_width/2
    button_pos_y = button_height/2

    # button_exit para
    button_exit_x = button_pos_x
    button_exit_y = button_pos_y
    button_exit_height = button_height
    button_exit_width = button_width
    button_exit = bu.Button(x=button_exit_x, y=button_exit_y,
                            height=button_exit_height, width=button_exit_width, text='Exit', )

    # button_restart para
    button_restart_x = button_pos_x + button_width + button_width/2
    button_restart_y = button_pos_y
    button_restart_height = button_height
    button_restart_width = button_width*1.5
    button_restart = bu.Button(x=button_restart_x, y=button_restart_y,
                               height=button_restart_height, width=button_restart_width, text='Restart')

    # button_counter para
    button_counter_x = button_restart_x + button_restart_width + button_width/2
    button_counter_y = button_pos_y
    button_counter_height = button_height
    button_counter_width = button_width*3.5
    button_counter = bu.Button(x=button_counter_x, y=button_counter_y,
                               height=button_counter_height, width=button_counter_width, text='ball counter: ')

    # running loop
    running = True
    while running:
        # loop event queue
        for event in pygame.event.get():
            # exit event
            if event.type == pygame.QUIT:
                running = False

            # restart event
            if event.type == (pygame.USEREVENT + 0):
                # check balls, draw or remove
                balls = []
                win_flag = False

            # mouse event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and win_flag == False:

                # get mouse click position
                x, y = event.pos

                # get radius, sx, sy, color randomly
                radius = randint(10, 30)
                sx, sy = randint(-3, 3), randint(-3, 3)
                color = co.Color.random_color()

                # generate a random ball in mouse click position
                ball = ba.Ball(x, y, radius, sx, sy, color)

                # put ball in ball container
                balls.append(ball)

        # screen background
        screen.fill((255, 255, 255))

        # check balls, draw or remove
        balls = ball_check(balls, screen)

        # check if win
        if len(balls) >= 5:
            button_counter.text = 'ball counter: ' + str(len(balls)) + ' win!'
            button_counter.draw(screen)

            win_flag = True

        else:
            # move balls
            balls = ball_move(balls, screen)
            balls = ball_check(balls, screen)

            button_counter.text = 'ball counter: ' + str(len(balls))
            button_counter.draw(screen)

        # draw button
        button_exit.draw(screen)
        button_restart.draw(screen)

        # screen update
        pygame.display.update()


if __name__ == '__main__':
    main()
