import pygame
import pymunk

def convert_pos(pm_pos: tuple, screen_size_y: int):
    return (int(pm_pos[0]), int(screen_size_y - pm_pos[1]))

class Block:
    def __init__(self):
        pass

class SandParticle:
    def __init__(self, screen: pygame.display, color, position: tuple, radius: int, density: float):
        self.screen = screen
        self.color = color
        self.rad = radius

        self.body = pymunk.Body()
        self.body.position = position

        self.shape = pymunk.Circle(self.body, self.rad)
        self.shape.density = density

    def draw(self):
        pos = convert_pos(self.body.position, self.screen.get_size()[1])

        pygame.draw.circle(self.screen, self.color, pos, self.rad)

class Segment:
    def __init__(self, screen: pygame.display, color, start_pos: tuple, end_pos: tuple, thickness: int):
        self.screen = screen
        self.color = color
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.thickness = thickness

        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, self.start_pos, self.end_pos, thickness)

    def draw(self):
        start = convert_pos(self.start_pos, self.screen.get_size()[1])
        end = convert_pos(self.end_pos, self.screen.get_size()[1])

        pygame.draw.line(self.screen, self.color, start, end, self.thickness)