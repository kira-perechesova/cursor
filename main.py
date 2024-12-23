import pygame
import sys

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
cursor_img = pygame.image.load('data/arrow.png')
cursor_rect = cursor_img.get_rect()

pygame.mouse.set_visible(False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_focused():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.fill((0, 0, 0))
        screen.blit(cursor_img, (mouse_x - cursor_rect.width // 2, mouse_y - cursor_rect.height // 2))
    else:
        screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()
