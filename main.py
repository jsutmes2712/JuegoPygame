import pygame
import Ball
import Wall
import Stick
import Bumper
import asyncio

async def main():

    #Constants
    BLACK = (0, 0, 0) 
    WINDOW_HEIGTH  = 700
    WINDOW_WIDHT = 1000


    def EventManager(isRunning, stickDown):
        #Manage the user inputs
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                isRunning = False      
            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_SPACE:
                    stickDown = False
                    
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_SPACE:
                    stickDown = True
            
        return isRunning , stickDown

    #Game variables
    points = 0
    gravity = 0.1
    lives = 3
    clock = pygame.time.Clock()
    isRunning = True
    stickDown = True
    bumperV = False
    time = 0
    timer = 0

    #Inicialize the game
    pygame.init()
    window = pygame.display.set_mode([WINDOW_HEIGTH, WINDOW_WIDHT])
    gameSprites = pygame.sprite.Group()

    #Create the elements of the game
    ballList = Ball.createBallList(gameSprites, gravity)
    wallList, diagonalList, portalList = Wall.createWallLists(gameSprites)
    bumperList = Bumper.createBumperList(gameSprites)
    lifeBumper = Bumper.createBumper(310,185)
    groupBumperLife = pygame.sprite.Group()
    groupBumperLife.add(lifeBumper)
    stickList = Stick.createSticks()
    stickListDown = Stick.createSticksDown()

    #Game loop
    while isRunning:
        window.fill(BLACK)
        #Save the actual time
        time = pygame.time.get_ticks() 
        #Check the user inputs
        isRunning ,stickDown= EventManager(isRunning, stickDown)
        #Move the sticks
        if stickDown:
            stickListDown.draw(window)
        else:
            stickList.draw(window)

        #check for collisions
        Stick.collisionStick(ballList,stickList,stickDown)
        Wall.potalCollide(ballList, portalList)
        Wall.collisionWall(ballList,wallList)
        Wall.colisionWallOb(ballList,diagonalList)

        points ,gravity, bumperV, timer= Bumper.collisionBumper(gameSprites,ballList, bumperList,points, gravity, bumperV, timer)
        
        if bumperV :
            
            groupBumperLife.draw(window)
            points ,gravity, lives = Bumper.collisionBumperVida(gameSprites, ballList,lifeBumper, points, gravity, lives) 
            if time > timer:
                bumperV = False
        
        #Apply the gravity
        for ball in ballList:
            Ball.gravityBall(ball)
            Ball.updateBall(ball)
            if ball.rect.bottom > 1000:
                lives -=1
                ball.kill()
        #Generate a new ball when all others are lost
        if len(ballList.sprites())<=0:
            Ball.newBall(gameSprites, ballList,gravity)


        #Draw the text
        letra30 = pygame.font.SysFont("Arial", 30)
        imagenTextoPresent = letra30.render("Puntos: " + str(points),True, (200,200,200), (0,0,0) )
        rectanguloTextoPresent = imagenTextoPresent.get_rect()
        rectanguloTextoPresent.centerx = 350
        rectanguloTextoPresent.centery = 520

        window.blit(imagenTextoPresent, rectanguloTextoPresent)
        
        imagenTextoPresent = letra30.render("Vidas: " + str(lives),True, (200,200,200), (0,0,0) )
        rectanguloTextoPresent = imagenTextoPresent.get_rect()
        rectanguloTextoPresent.centerx = 350
        rectanguloTextoPresent.centery = 600

        window.blit(imagenTextoPresent, rectanguloTextoPresent)

        #Draw the elemets
        gameSprites.draw(window)
        #Update the window
        pygame.display.update()
        #Check if the game must stop
        if lives <= 0:
            isRunning = False;
    
        clock.tick(60)
                    


    await asyncio.sleep(0)
asyncio.run(main())