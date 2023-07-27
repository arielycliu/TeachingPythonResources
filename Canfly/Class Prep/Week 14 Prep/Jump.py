import pygame
import random
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Game")

x = 50
y = 50
w = 40
h = 60
speed = 5
color = (255, 255, 255)

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - w - speed:
        x += speed
    if keys[pygame.K_UP] and y > speed:
        y -= speed
    if keys[pygame.K_DOWN] and y < 500 - h - speed:
        y += speed
    if keys[pygame.K_SPACE]:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    win.fill((0,0,0))
    pygame.draw.rect(win, color, (x, y, w, h))
    pygame.draw.circle(win, color, (250, 250), 75)

    pygame.display.update()

pygame.quit()