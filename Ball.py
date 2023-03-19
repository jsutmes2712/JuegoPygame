import pygame
import random

def createBall(gameSprites, x, y, gravity):

    ball = pygame.sprite.Sprite()
    ball.image = pygame.image.load("Images/ball.png")

    ball.rect = ball.image.get_rect()
    ball.rect.x = x
    ball.rect.y = y

    ball.v = pygame.math.Vector2()
    ball.v.x = -3
    ball.v.y = 0

    ball.gravedad = pygame.math.Vector2()

    ball.gravedad.x = 0
    ball.gravedad.y = gravity
    gameSprites.add(ball)
    
    return ball

def createBallList(gameSprites, gravity):

    ballList = pygame.sprite.Group()
    sprite =createBall(gameSprites, 325, 500,gravity)
    ballList.add(sprite)
    gameSprites.add(sprite)
    return ballList

def addBall(gameSprites, ballList, gravity):
    sprite =createBall(gameSprites, random.randint(1,100),random.randint(1,100),gravity)
    ballList.add(sprite)
    gameSprites.add(sprite)
    sprite =createBall(gameSprites, random.randint(450,600),random.randint(1,100),gravity)
    ballList.add(sprite)
    gameSprites.add(sprite)

def newBall(gameSprites, ballList, gravity):
    sprite =createBall(gameSprites, 325, 500,gravity)
    ballList.add(sprite)
    gameSprites.add(sprite)


def updateBall(ball):
    ball.rect.x += ball.v.x
    ball.rect.y += ball.v.y

def modifyVelocity(ball, x,y):

    aux_x = ball.v.x
    aux_y = ball.v.y
    ball.v.x = x
    ball.v.y = y

    if ball.v.length() > 20:
        ball.v.x = aux_x
        ball.v.y = aux_y 

def gravityBall(ball):
    modifyVelocity(ball, ball.v.x + ball.gravedad.x, ball.v.y + ball.gravedad.y)

def modifyGravity(ball):
    ball.gravedad.y += 0.1