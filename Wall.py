import pygame
import Ball

AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

def createWall(x, y, ang):

    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load("Images/wall.png")
    sprite.image = pygame.transform.rotate(sprite.image,ang)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y

    

    return sprite

def createBorder(x, y, width, height):

    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.Surface([width, height])
    sprite.image.fill(AZUL)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y

    return sprite

def createPortal(x, y, width, height):

    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.Surface([width, height])
    sprite.image.fill(ROJO)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y

    return sprite

def createWallLists(gameSprites):
    wallList = pygame.sprite.Group()
    
    diagonalList = pygame.sprite.Group()

    portalList = pygame.sprite.Group()

    pared = createWall(462,840,25)
    diagonalList.add(pared)
    gameSprites.add(pared)
    
    pared = createWall(625,662,90)
    wallList.add(pared)
    gameSprites.add(pared)
    
    pared = createWall(35,840,-25)
    diagonalList.add(pared)
    gameSprites.add(pared)

    pared = createWall(35,662,90)
    wallList.add(pared)
    gameSprites.add(pared)
 
    
    
    pared = createBorder(0,-30,700,30)
    wallList.add(pared)
    gameSprites.add(pared) 

    pared = createBorder(-30,0,30,1000)
    wallList.add(pared)
    gameSprites.add(pared)

    pared = createBorder(700,0,30,1000)
    wallList.add(pared)
    gameSprites.add(pared)



    portal = createPortal(0, 662, 50, 10)
    portalList.add(portal)
    gameSprites.add(portal)

    portal = createPortal(650, 662, 50, 10)
    portalList.add(portal)
    gameSprites.add(portal)

    return wallList, diagonalList, portalList



def collisionWall(listaBall,listaWall):

    for ball in listaBall:
        impacts = pygame.sprite.spritecollide(ball, listaWall, False)
        for stick in impacts:

            if ball.rect.bottom > stick.rect.top and ball.rect.top < stick.rect.top:
                
                ball.v = ball.v.reflect(pygame.math.Vector2(0,-1))

            if ball.rect.top < stick.rect.bottom and ball.rect.bottom > stick.rect.bottom:
            
                ball.v = ball.v.reflect(pygame.math.Vector2(0,1))

            if ball.rect.left < stick.rect.right and ball.rect.right > stick.rect.right:
                
                ball.v = ball.v.reflect(pygame.math.Vector2(-1,0))

            if ball.rect.right > stick.rect.left and ball.rect.left < stick.rect.left:
                
                ball.v = ball.v.reflect(pygame.math.Vector2(1,0))


def colisionWallOb(ballList,wallList):

    for ball in ballList:
        impacts = pygame.sprite.spritecollide(ball, wallList, False)
        for stick in impacts:

            if ball.rect.x < 350:
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


def potalCollide (ballList, portalList):

    for ball in ballList:
        impactos = pygame.sprite.spritecollide(ball, portalList, False)

        for portal in impactos:

            arrayPortal = portalList.sprites()

            if ball.rect.x < 350:
                ball.rect.x =  650
                ball.v.reflect(pygame.math.Vector2(0,-1))
            else:
                ball.rect.x =  10
                ball.v.reflect(pygame.math.Vector2(0,-1))


    