import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((600,600))
font = pygame.font.SysFont('arial', 30)
clock = pygame.time.Clock()

frames = 0
inputs = {"x": 0, "drop": False, "rotate": False}

particles = []

running = True
while running:
    inputs["x"] = 0
    inputs["drop"] = False
    inputs["rotate"] = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: inputs["x"] = 1
            elif event.key == pygame.K_RIGHT: inputs["x"] = -1
            if event.key == pygame.K_DOWN: inputs["drop"] = True
            if event.key == pygame.K_UP: inputs["rotate"] = True

    screen.fill((0,0,0))

    
