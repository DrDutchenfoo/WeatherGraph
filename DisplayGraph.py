import WeatherGraph
def displaythingy():
    import pygame
    import time
    from pygame.locals import (
        K_ESCAPE,
        KEYDOWN,
        QUIT,
        MOUSEBUTTONDOWN,
    )
    screenwidth = 800
    screenheight = 500

    pygame.init()
    screen = pygame.display.set_mode((screenwidth, screenheight))
    screen.fill((255, 255, 255))

    open('graph.png')
    plot_img = pygame.image.load('graph.png')
    screen.blit(plot_img, (0, 0))

    buttonX = 630
    buttonY = 200
    open('ReloadButton1.png')
    plot_button = pygame.image.load('ReloadButton1.png')
    screen.blit(plot_button, (buttonX, buttonY))

    open('ReloadButton2.png')
    plot_button = pygame.image.load('ReloadButton2.png')
    screen.blit(plot_button, (buttonX, buttonY))

    pygame.display.flip()

    running = True
    while running:
        mousex, mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            if buttonX <= mousex <= buttonX + 128 and buttonY <= mousey <= buttonY + 128 and event.type == pygame.MOUSEBUTTONDOWN:
                print('success')
                WeatherGraph.makegraph()
                running = False
                pygame.quit()
    pygame.display.update()
