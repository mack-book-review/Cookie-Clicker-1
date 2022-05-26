import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

size = (width,height) = (500,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
cookie = pygame.image.load("Cookie.png")
clicks = 0
font = pygame.font.SysFont("Helvetica",20)


WHITE = (255,255,255)
BLUE = (0,0,255)

def main():
    global cookie,clicks
    cookie = pygame.transform.smoothscale(cookie,(250,180))
    cookie_rect = cookie.get_rect()
    cookie_rect.center = (width/2,height/2)

    text = font.render("Clicks: 0",True,BLUE)
    text_rect = text.get_rect()
    text_rect.center = (width/2,50)

    while True:
        clock.tick(60)

        text = font.render("Clicks: {}".format(clicks), True, BLUE)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, 50)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if cookie_rect.collidepoint(x,y):
                    clicks += 1


        screen.fill(WHITE)
        screen.blit(cookie,cookie_rect)
        screen.blit(text,text_rect)
        pygame.display.flip()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
