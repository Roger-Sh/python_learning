import pygame


# class Button
class Button:
    def __init__(self, x=50, y=25, width=100, height=50, text='button', font='Arial',font_size=16):
        # pos
        self.x = x
        self.y = y

        # size
        self.width = width
        self.height = height

        # text and font
        self.text = text
        self.font = font
        self.font_size = font_size

        # color
        self.color = (255, 255, 255)
        self.color_light = (170, 170, 170)
        self.color_dark = (0, 0, 0)

    def draw(self, screen):
        # mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # if mouse is hovered on a button it changes to lighter shade
        if self.x <= mouse_pos[0] <= (self.x + self.width) and self.y <= mouse_pos[1] <= (self.y + self.height):
            # mouse on button
            pygame.draw.rect(screen, self.color_light, [self.x, self.y, self.width, self.height])
            # print('on button')

            # check if mouse click
            mouse_click = pygame.mouse.get_pressed()
            # event: exit game
            if mouse_click[0] and self.text == 'Exit':
                print('Game quit!')
                ev = pygame.event.Event(pygame.QUIT)
                pygame.event.post(ev)
            # event: game restart
            elif mouse_click[0] and self.text == 'Restart':
                print('Game restart!')
                restart_event = pygame.USEREVENT + 0    # restart event
                ev = pygame.event.Event(restart_event)
                pygame.event.post(ev)

        else:
            pygame.draw.rect(screen, self.color_dark, [self.x, self.y, self.width, self.height])
            # print('not on button')

        # text
        text_font = pygame.font.SysFont(self.font, self.font_size)      # font
        text = text_font.render(self.text, True, self.color)            # render text
        screen.blit(text, (int(self.x + self.font_size/2), int(self.y)))

    def __str__(self):
        return 'button_Size: %d x %d, button_text: %s, button_color: %s' % (
                self.width, self.height, self.text, self.color)


if __name__ == '__main__':
    button = Button()
    print(button)
