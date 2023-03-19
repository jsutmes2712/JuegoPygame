import pygame
import math
import Ball

def createBumper(x, y):

    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load("Images/bumper.png")
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = x
    sprite.rect.y = y

    return sprite

def createBumperList(gameSprites):
    listaBumpers = pygame.sprite.Group()

    bumper = createBumper(135,85)
    listaBumpers.add(bumper)
    gameSprites.add(bumper)

    bumper = createBumper(485,85)
    listaBumpers.add(bumper)
    gameSprites.add(bumper)

    bumper = createBumper(310,335)
    listaBumpers.add(bumper)
    gameSprites.add(bumper)

    return listaBumpers


def collisionBumper(gameSprites, ballList,bumperList, points,gravity, lives, timer):
    nt = timer
    for ball in ballList:
        impacts = pygame.sprite.spritecollide(ball, bumperList, False)
        for bumper in impacts:

            n = pygame.math.Vector2(ball.rect.centerx - bumper.rect.centerx , ball.rect.centery - bumper.rect.centery)
            z= bumper.rect.width/2 +ball.rect.width/2

            if n.length() < z:
                n = n.normalize()
                ball.v.x -= n.x
                ball.v.y -= n.y
                ball.v = ball.v.reflect(n)

                points += 25
                
                if points % 750 == 0:
                    Ball.modifyGravity(ball)
                    gravity +=0.1
                if points % 500 ==0:
                    Ball.addBall(gameSprites, ballList,gravity)
                if points % 1000 ==0:
                    nt = pygame.time.get_ticks() +5000
                    lives = True

    return points, gravity, lives , nt

def collisionBumperVida(gameSprites, ballList,bumper, points,gravity, lives):

    for ball in ballList:
        
        if pygame.sprite.collide_rect(ball, bumper):

            n = pygame.math.Vector2(ball.rect.centerx - bumper.rect.centerx , ball.rect.centery - bumper.rect.centery)
            z= bumper.rect.width/2 +ball.rect.width/2

            if n.length() < z:
                n = n.normalize()
                ball.v.x -= n.x
                ball.v.y -= n.y
                ball.v = ball.v.reflect(n)
                lives += 1
                points += 25

                if points % 750 == 0:
                    Ball.modifyGravity(ball)
                    gravity +=0.1
                if points % 500 ==0:
                    Ball.addBall(gameSprites, ballList,gravity)
            
    
    return points, gravity, lives