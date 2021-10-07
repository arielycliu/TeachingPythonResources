
import pygame
import random

pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Game")

x, y, w, h = 250, 250, 75, 90
speed = 5

color = (255, 255, 255)

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Top left corner is 0,0
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - speed - w:
        x += speed
    if keys[pygame.K_DOWN] and y < 500 - speed - h:
        y += speed
    if keys[pygame.K_UP] and y > speed:
        y -= speed
    if keys[pygame.K_SPACE]:
        # change the color of the rectangle to a random value
        r, b, g = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        color = (r, b, g)

    window.fill((0,0,0))
    pygame.draw.rect(window, color, (x, y, w, h))
    # restrict the movement, add boundaries

    pygame.display.update()

pygame.quit()






