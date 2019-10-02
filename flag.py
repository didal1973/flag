# Флаг
import pygame

# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = 800, 600
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('gray'))
# формирование кадра:
# команды рисования на холсте
# Рисуем древко
screen.fill(pygame.Color('brown'), pygame.Rect(10, 10, 15, 580))
# Белый
screen.fill(pygame.Color('white'), pygame.Rect(25, 10, 675, 150))
# Синий
screen.fill(pygame.Color('blue'), pygame.Rect(25, 160, 675, 150))
# Красный
screen.fill(pygame.Color('red'), pygame.Rect(25, 310, 675, 150))
# смена (отрисовка) кадра:
pygame.display.flip()
# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()
