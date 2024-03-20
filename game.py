import pygame # pylint: disable=C0114



pygame.init() # pylint: disable=E1101

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
RUNNING = True
if __name__ == '__main__':
    while RUNNING:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False


        screen.fill(pygame.Color(179,166,196))
        pygame.display.flip()

        clock.tick(60)
    pygame.quit()