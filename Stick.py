import pygame
import Ball
AZUL = (0, 0, 255)

def createStickR(x, y):

    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load("Images/flipperR.png")
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y

    return sprite

def createStickL(x, y):

    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load("Images/flipperL.png")
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y

    return sprite

def createStickDownR(x, y, ang):

    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load("Images/flipperR.png")
    
    sprite.image = pygame.transform.rotate(sprite.image,ang)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y

    return sprite

def createStickDownL(x, y, ang):

    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load("Images/flipperL.png")
    
    sprite.image = pygame.transform.rotate(sprite.image,ang)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y

    return sprite

def createSticks():
    stickList = pygame.sprite.Group()

    stick = createStickL(185,916)
    stickList.add(stick)

    stick = createStickR(375,916)
    stickList.add(stick)

    return stickList

def createSticksDown():
    stickList = pygame.sprite.Group()

    stick = createStickDownL(183,910,-25)
    stickList.add(stick)
    

    stick = createStickDownR(377,910,25)
    stickList.add(stick)
    

    return stickList

def collisionStick(ballList,sticksList, sticksUp):

    for ball in ballList:
        impacts = pygame.sprite.spritecollide(ball, sticksList, False)
        for stick in impacts:
            if not sticksUp:
                Ball.modifyVelocity(ball, ball.v.x, -20)
            else:
                if ball.rect.centerx < 350:
                    m = 128/285
                    n1 = 46699/57
                    n2 = 48409/57
                    if ball.rect.x*m +n1 < ball.rect.centery+ball.rect.width and ball.rect.x*m +n2 > ball.rect.centery-ball.rect.width:
                        n = pygame.math.Vector2(320-35,963-835)
                        n = n.normalize()
                        n.update(-n.y,n.x)
                        ball.v = ball.v.reflect(n)
                else:
                    m = -128/277
                    n1 = 315007/277
                    n2 = 323317/277
                    if ball.rect.x*m +n1 < ball.rect.centery+ball.rect.width and ball.rect.x*m +n2 > ball.rect.centery-ball.rect.width:
                        n = pygame.math.Vector2(654- 377, 835-963)
                        n = n.normalize()
                        n.update(-n.y,n.x)
                        ball.v = ball.v.reflect(n)
