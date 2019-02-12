import pygame
from setup import *
from random import randint

pygame.init()
pygame.display.set_caption("Rane")

DROPLET_AMOUNT = 500
DROPLET_COLORS = (GREEN, RED, BLUE, AQUA, PINK, ORANGE, YELLOW)


class Droplet:
    def __init__(self, x, y, size, speed, color):
        self.defaultPos = (x, y)
        self.position = [x, y]
        self.size = size
        self.speed = speed
        self.color = color

    def fall(self):
        if self.position[1] > WINDOW_HEIGHT:
            self.position[1] = self.defaultPos[1]
        else:
            self.position[1] += self.speed

    def draw(self):
        x = self.position[0]
        y = self.position[1]
        pygame.draw.line(screen, self.color, (x, y), (x, y + self.size), 1)


def getDroplets():
    droplets = []

    for i in range(1, DROPLET_AMOUNT):
        dropX = randint(10, WINDOW_WIDTH)
        dropY = randint(-500, -50)
        dropSize = randint(5, 15)
        dropSpeed = randint(5, 10)
        dropColor = DROPLET_COLORS[randint(0, len(DROPLET_COLORS)-1)]

        newDrop = Droplet(dropX, dropY, dropSize, dropSpeed, dropColor)
        droplets.append(newDrop)

    return droplets


class Button:
    def __init__(self, x, y, sizeX, sizeY):
        self.position = (x, y)
        self.sizeX = sizeX
        self.sizeY = sizeY
        # self.visible = False

    #def drawText(self, text):
        #myfont = pygame.font.SysFont('Century Gothic')

    def drawButton(self):
        pygame.draw.rect(screen, DEEP_PURPLE, (self.position[0], self.position[1],
                                               self.sizeX, self.sizeY))


class AmountButt(Button):
    def __init__(self, x, y, sizeX, sizeY):
        super().__init__(x, y, sizeX, sizeY)

    def action(self):
        global DROPLET_AMOUNT
        DROPLET_AMOUNT += 500


class PlusButt(AmountButt):
    def __init__(self):
        super().__init__(50, 50, 50, 50)

    def draw(self):
        sizeX = self.sizeX
        sizeY = self.sizeY

        stripeWid = sizeX/5
        pygame.draw.rect(screen, BLACK, (self.position[0] + sizeX/2 - stripeWid/2, self.position[1], stripeWid, sizeY))
        pygame.draw.rect(screen, BLACK, (self.position[0], self.position[1] + sizeY/2 - stripeWid/2, sizeX, sizeY/5))


class MinusButt(AmountButt):
    def __init__(self):
        super().__init__(120, 50, 50, 50)

    def action(self):
        global DROPLET_AMOUNT
        DROPLET_AMOUNT -= 500

    def draw(self):
        sizeX = self.sizeX
        sizeY = self.sizeY
        stripeWid = sizeX/5
        pygame.draw.rect(screen, BLACK, (self.position[0], self.position[1] + sizeY/2 - stripeWid/2, sizeX, sizeY/5))


droplets = getDroplets()

plusButton = PlusButt()
minusButton = MinusButt()



while not done:
    change = False
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mouse[0] in range(plusButton.position[0], plusButton.position[0] + plusButton.sizeX) \
                    and mouse[1] in range(plusButton.position[1], plusButton.position[1] + plusButton.sizeY):
                plusButton.action()
                # TODO funkce na tohle
                change = True
            elif mouse[0] in range(minusButton.position[0], minusButton.position[0] + minusButton.sizeX) \
                    and mouse[1] in range(minusButton.position[1], minusButton.position[1] + minusButton.sizeY):
                minusButton.action()
                change = True


    screen.fill(BLACK)

    plusButton.drawButton()
    plusButton.draw()
    minusButton.drawButton()
    minusButton.draw()

    for drop in droplets:
        drop.fall()
        drop.draw()

    pygame.display.flip()

    if change:
        droplets = getDroplets()

    clock.tick(60)
