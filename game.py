import pygame  # pylint: disable=C0114
from pytmx import load_pygame

from tiles import Tile

pygame.init()  # pylint: disable=E1101

screen = pygame.display.set_mode((960, 640))
clock = pygame.time.Clock()
RUNNING = True
tmx_data = load_pygame("./assets/test_map.tmx")
sprite_group = pygame.sprite.Group()

for layer in tmx_data.visible_layers:
    # if layer.name in ('Floor', 'Plants and rocks', 'Pipes')
    if hasattr(layer, "data"):
        for x, y, surf in layer.tiles():
            pos = (x * 16, y * 16)
            Tile(pos=pos, surf=surf, groups=sprite_group)
if __name__ == "__main__":
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        screen.fill(pygame.Color(179, 166, 196))
        sprite_group.draw(screen)
        pygame.display.flip()  # flip updates the entire display, update method only updates part of the display

        clock.tick(60)
    pygame.quit()
