# Создайте программу для игры в "Крестики-нолики".

import pygame
import sys

def winner_check(mass, sign):
    zeroes = 0
    for row in mass:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return f'Победитель "{sign}"!'
    for column in range(3):
        if mass[0][column] == sign and mass[1][column] == sign and mass[2][column]:
            return f'Победитель "{sign}"!'
    if mass[0][0] == sign and mass[1][1] == sign and mass[2][2]:
            return f'Победитель "{sign}"!'
    if mass[0][2] == sign and mass[1][1] == sign and mass[2][0]:
        return f'Победитель "{sign}"!'
    if zeroes == 0:
        return 'А у вас НИЧЬЯ! Победила ДРУЖБА!'
    return False

pygame.init()
block_size = 100
indent = 10
width = height = block_size * 3 + indent * 4

window_size = (width, height)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('КРЕСТИКИ-НОЛИКИ')

black = (0, 0, 0)
white = (255, 255, 255)
light_blue = (175, 238, 238)
peach = (255, 229, 180)
mass = [[0] * 3 for i in range(3)]
game_queue = 0
game_over = False
game_restart = 'Введите "Пробел" для начала новой игры! :-)'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse =pygame.mouse.get_pos()
            column = x_mouse // (block_size + indent)
            row = y_mouse // (block_size + indent)
            if mass[row][column] == 0:
                if game_queue % 2 == 0:
                    mass[row][column] = 'x'
                else:
                    mass[row][column] = 'o'
                game_queue += 1

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mass = [[0] * 3 for i in range(3)]
            game_queue = 0
            screen.fill(black)

        if not game_over:
            for row in range(3):
                for column in range(3):
                    if mass[row][column] == 'x':
                        color = light_blue
                    elif mass[row][column] == 'o':
                        color = peach
                    else:
                        color = white

                    x = column * block_size + (column + 1) * indent
                    y = row * block_size + (row + 1) * indent
                    pygame.draw.rect(screen, color, (x, y, block_size, block_size))
                    if color == light_blue:
                        pygame.draw.line(screen, black, (x + 25, y + 25), (x + block_size - 25, y + block_size - 25), 15)
                        pygame.draw.line(screen, black, (x + block_size - 25, y + 25), (x + 25, y + block_size - 25), 15)
                    elif color == peach:
                        pygame.draw.circle(screen, black, (x + block_size // 2, y + block_size // 2), block_size // 2 - 15, 10)
        
        if (game_queue % 2 == 0):
            game_over = winner_check(mass, 'x')
        else:
            game_over = winner_check(mass, 'o')

        if game_over:
            screen.fill(black)
            font = pygame.font.SysFont('Times New Roman', 30)
            text_1 = font.render(game_over, True, white)
            text_rect = text_1.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            font2 = pygame.font.SysFont('Times New Roman', 15)
            text2 = font2.render(game_restart, True, white)
            text2_x = screen.get_width() / 2 - text_rect.width / 2 - 30
            text2_y = screen.get_height() / 2 - text_rect.height / 2 + 40
            screen.blit(text_1, [text_x, text_y])
            screen.blit(text2, [text2_x, text2_y])

        pygame.display.update()
