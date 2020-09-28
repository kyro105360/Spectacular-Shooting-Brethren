#########################################
# File Name: isuGame.py
# Description: Final isu game 
# Author: Kyrollous Nassif
# Date: 6/16/2018
#########################################
import pygame
from random import randint

pygame.init()
WIDTH  = 1024
HEIGHT = 1024
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OUTLINE=0
playerFont = pygame.font.SysFont("Impact", 25)
healthBarFont = pygame.font.SysFont("Impact", 35)
powerUpFont = pygame.font.SysFont("Impact", 25)
powerUp = pygame.image.load("images/powerUp.png")
healthApple = pygame.image.load("images/healthApple.png")
kenPlayer1 = pygame.image.load("images/kenPlayer1.png")
kenPlayer1 = pygame.transform.scale(kenPlayer1, (31, 26))
loukasPlayer2 = pygame.image.load("images/loukasPlayer2.png")
loukasPlayer2 = pygame.transform.scale(loukasPlayer2, (33, 39))
enterScreenPicture = pygame.image.load("Menus/enterScreen.png")
enterScreenPicture = pygame.transform.scale(enterScreenPicture, (WIDTH, HEIGHT))
mainMenuScreenPicture = pygame.image.load("Menus/menuScreen.png")
mainMenuScreenPicture = pygame.transform.scale(mainMenuScreenPicture, (WIDTH, HEIGHT))
controlsScreenPicture = pygame.image.load("Menus/controlsScreen.png")
controlsScreenPicture = pygame.transform.scale(controlsScreenPicture, (WIDTH, HEIGHT))
powerUpsScreenPicture = pygame.image.load("Menus/powerUpsScreen.png")
powerUpsScreenPicture = pygame.transform.scale(powerUpsScreenPicture, (WIDTH, HEIGHT))
platformScreenPicture = pygame.image.load("Menus/platformScreen.png")
platformScreenPicture = pygame.transform.scale(platformScreenPicture, (WIDTH, HEIGHT))
howToWinScreenPicture = pygame.image.load("Menus/howToWinScreen.png")
howToWinScreenPicture = pygame.transform.scale(howToWinScreenPicture, (WIDTH, HEIGHT))
loukasWinnerScreenPicture = pygame.image.load("Menus/loukasWinner.png")
loukasWinnerScreenPicture = pygame.transform.scale(loukasWinnerScreenPicture, (WIDTH, HEIGHT))
kenWinnerScreenPicture = pygame.image.load("Menus/kenWinner.png")
kenWinnerScreenPicture = pygame.transform.scale(kenWinnerScreenPicture, (WIDTH, HEIGHT))

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
def redrawGameWindow():
    gameWindow.fill(BLACK)
    drawBackground()
    drawPlatforms()
    drawPowerups()
    drawApple()
    drawPlayers()
    drawHealthBars()
    drawBullets()
    drawPowerUpText(player1Invincibility, player1RapidFire, player1Frozen, player1X, player1Y)
    drawPowerUpText(player2Invincibility, player2RapidFire, player2Frozen, player2X, player2Y)
    pygame.display.update()        
def drawPlatforms():
    for i in range(len(platformX)):
        gameWindow.blit(mainPlatform[i], (platformX[i],platformY[i]))
def drawPowerups():
    for i in range(len(powerUpX)):
        gameWindow.blit(powerUp,(powerUpX[i],powerUpY[i]))
def drawBullets():
    for i in range(len(player2BulletX)):
        pygame.draw.rect(gameWindow, YELLOW, (player2BulletX[i],player2BulletY[i],player2BulletW,player2BulletH), 0)
    for i in range(len(player1BulletX)):
        pygame.draw.rect(gameWindow, YELLOW, (player1BulletX[i],player1BulletY[i],player1BulletW,player1BulletH), 0)
def drawBackground():
    gameWindow.blit(galaxy1, (galaxy1X,galaxy1Y))
    gameWindow.blit(galaxy2, (galaxy2X,galaxy2Y))
def drawApple():
    for i in range(len(appleX)):
        gameWindow.blit(healthApple, (appleX[i], appleY[i]))
def drawPlayers():
    #player1
    player1Text = playerFont.render("KEN", 1, YELLOW)
    gameWindow.blit(player1Pic[player1PicNum], (player1X, player1Y))
    gameWindow.blit(player1Text, (player1X, player1Y-35))
    #face
    gameWindow.blit(kenPlayer1, (player1X, player1Y))                                            
    player2Text = playerFont.render("LOUKAS", 1, YELLOW)
    gameWindow.blit(player2Pic[player2PicNum], (player2X, player2Y))
    gameWindow.blit(player2Text, (player2X-22, player2Y-35))
    #face
    gameWindow.blit(loukasPlayer2, (player2X, player2Y - 4))
def drawHealthBars():
    # player1
    healthBar1Text = healthBarFont.render("KEN", 1, GREEN)
    gameWindow.blit(healthBar1Text, (healthBarOutline1X, healthBarOutline1Y + 34))
    pygame.draw.rect(gameWindow, YELLOW, (healthBarOutline1X, healthBarOutline1Y, healthBarOutline1W, healthBarOutline1H), 0)
    pygame.draw.rect(gameWindow, RED, (healthBar1X, healthBar1Y, healthBar1W, healthBar1H), 0)
                                       
    # player2
    healthBar2Text = healthBarFont.render("LOUKAS", 1, GREEN)
    gameWindow.blit(healthBar2Text, (healthBarOutline2X + 195, healthBarOutline2Y + 34))
    pygame.draw.rect(gameWindow, YELLOW, (healthBarOutline2X, healthBarOutline2Y, healthBarOutline2W, healthBarOutline2H), 0)
    pygame.draw.rect(gameWindow, RED, (healthBar2X, healthBar2Y, healthBar2W, healthBar2H), 0)

def drawPowerUpText(playerInvincibility, playerRapidFire, playerFrozen, playerX, playerY):
 # powerup text render
    invincibleText = powerUpFont.render("INVINCIBLE!", 1, BLUE)
    rapidFireText = powerUpFont.render("RAPIDFIRE!", 1, BLUE)
    frozenText = powerUpFont.render("Frozen :(", 1, BLUE)
    # player1 drawing text
    if playerInvincibility and playerRapidFire:
        gameWindow.blit(invincibleText, (playerX-22, playerY-60))
        gameWindow.blit(rapidFireText, (playerX-22, playerY-90))

    elif playerInvincibility and playerFrozen:
        gameWindow.blit(frozenText, (playerX-22, playerY-60))
        gameWindow.blit(invincibleText, (playerX-22, playerY-90))

    elif playerRapidFire and playerFrozen:
        gameWindow.blit(rapidFireText, (playerX-22, playerY-90))
        gameWindow.blit(frozenText, (playerX-22, playerY-60))

    elif playerInvincibility:
        gameWindow.blit(invincibleText, (playerX-22, playerY-60))

    elif playerRapidFire:
        gameWindow.blit(rapidFireText, (playerX-22, playerY-60))

    elif playerFrozen:
        gameWindow.blit(frozenText, (playerX-22, playerY-60))
def popOutOfScreen(playerBulletX,playerBulletY,playerBulletW,playerBulletShift):
    for i in reversed(range(len(playerBulletX))):
        if playerBulletX[i] >= WIDTH or playerBulletX[i] + playerBulletW <= 0:
            playerBulletX.pop(i)
            playerBulletY.pop(i)
            playerBulletShift.pop(i)
def movingWithPlatform(playerX,playerY,playerW,playerH):
    for i in range(1,len(platformX)):
        if playerX +player1W > platformX[i] and playerX < platformX[i] + platformW[i] and playerY + playerH == platformY[i] + 15:
            playerX += platformShift[i]
    return playerX
def powerUpCollision(bulletX, bulletY, bulletW, bulletH, bulletShift, playerInvincibility, playerRapidFire, oppositeFrozen):
    for i in reversed(range(len(powerUpX))):
        powerUpRect = pygame.Rect(powerUpX[i], powerUpY[i], powerUpW, powerUpH)
        for index in reversed(range(len(bulletX))):
            bulletRect = pygame.Rect(bulletX[index], bulletY[index], bulletW, bulletH)
            if bulletRect.colliderect(powerUpRect):
                powerUpSound.play()
                bulletX.pop(index)
                bulletY.pop(index)
                bulletShift.pop(index)
                powerUpX.pop(i)
                powerUpY.pop(i)
                powerUpShiftX.pop(i)
                powerUpShiftY.pop(i)
                despawnPowerUpCounter.pop(i)
                powerUpDecider = randint(1,3)
                if powerUpDecider == 1:
                    playerInvincibility = True
                elif powerUpDecider == 2:
                    oppositeFrozen = True
                else:
                    playerRapidFire = True
    powerUps = [playerInvincibility, playerRapidFire, oppositeFrozen]
    return powerUps
def turnOffPowerUp(playerInvincibility, oppositeFrozen, playerRapidFire, powerUpCounter, frozenCounter):
    if playerInvincibility or playerRapidFire:
        powerUpCounter += 1
        if powerUpCounter >= 150:
            playerInvincibility = False
            playerRapidFire = False            
            powerUpCounter = 0
    if oppositeFrozen:
        frozenCounter += 1
        if frozenCounter >= 65:
            oppositeFrozen = False
            frozenCounter = 0
    powerUpOffList = [playerInvincibility,oppositeFrozen,playerRapidFire, powerUpCounter, frozenCounter]
    return powerUpOffList
def shootCounter(shootCounter, playerRapidFire):
    shootCounter += 1
    if playerRapidFire:
        shootCounter += 2
    return shootCounter
def enterScreen():
    gameWindow.blit(enterScreenPicture,(0, 0))
    pygame.display.update()
def mainMenuScreen():
    gameWindow.blit(mainMenuScreenPicture, (0, 0))
    pygame.display.update()
def controlsScreen():
    gameWindow.blit(controlsScreenPicture, (0, 0))
    pygame.display.update()
def powerUpsScreen():
    gameWindow.blit(powerUpsScreenPicture, (0, 0))
    pygame.display.update()
def platformScreen():
    gameWindow.blit(platformScreenPicture, (0, 0))
    pygame.display.update()
def howToWinScreen():
    gameWindow.blit(howToWinScreenPicture, (0, 0))
    pygame.display.update()
def endGameScreen():
    if player1Lives <= 0:
        gameWindow.blit(loukasWinnerScreenPicture,(0, 0))
    else:
        gameWindow.blit(kenWinnerScreenPicture, (0, 0))
    pygame.display.update()
def menuMusic():
    pygame.mixer.music.load('Sounds/menuMusic.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops = -1)
def gameMusic():
    pygame.mixer.music.load('Sounds/gameMusic.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops = -1)
def endScreenMusic():
    pygame.mixer.music.load('Sounds/endGameMusic.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops = -1)


playingGame = True
while playingGame:                
    #---------------------------------------#
    # main program starts here              #
    #---------------------------------------#

    # jumping properties 
    GROUND = HEIGHT
    RUN_SPEED = 10
    GRAVITY = 3
    JUMP_SPEED = -30

    # music and sound effects
    menuMusic()
    click = pygame.mixer.Sound('Sounds/clickSound.wav')
    click.set_volume(50)
    shoot = pygame.mixer.Sound('Sounds/gunShot.wav')
    shoot.set_volume(0.9)
    hit = pygame.mixer.Sound('Sounds/hitSound.wav')
    hit.set_volume(0.9)
    appleEat = pygame.mixer.Sound('Sounds/appleSoundEffect.wav')
    appleEat.set_volume(0.9)
    powerUpSound = pygame.mixer.Sound('Sounds/powerUp.wav')
    powerUpSound.set_volume(0.9)
    
    

    # PLATFORM properties
    platformX = [180,0,465,0,465]
    platformY = [GROUND-90,400,300,200,100]
    platformW = [670,120,160,210,135]
    platformH = [50,50,50,50,50]
    mainPlatform = []
    platformShift = [0]
    for i in range(1,len(platformX)):    
        platformShift.append(6)
    for i in range(len(platformX)):
        mainPlatform.append(pygame.image.load("images/mainPlatform.png"))
    for i in range(len(platformX)):
        mainPlatform[i] = pygame.transform.scale(mainPlatform[i], (platformW[i],platformH[i]))
        

    # player1 properties
    player1 = pygame.image.load("sprites/player1_00.png")
    player1Lives = 10
    player1W = 33
    player1H = 63
    player1X = platformX[0] + platformW[0] - 60
    player1Y = platformY[0] - player1H
    player1Vx = 0
    player1Vy = 0
    player1Invincibility = False
    powerUpCounter1 = 0
    player1RapidFire = False
    player1Frozen = False
    frozenCounter1 = 0
    healthBar1X = 576
    healthBar1Y = 10
    healthBar1W = 30
    healthBar1H = 35
    player1PicNum = 1                         # current picture of player1
    player1Dir = "left"                       # direction in which player1 is facing
    player1Pic =[0]*10                        # 10 pictures represent all animated views of player1
    for i in range(10):                       # these pictures must be in the same folder
        player1Pic[i] = pygame.image.load("sprites/player1_0" + str(i) + ".png")

    # player1 bullet properties
    player1BulletX = []  
    player1BulletY = []
    player1BulletW = 15
    player1BulletH = 5
    player1BulletShift = []
     
    nextRightPic1  = [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    nextLeftPic1 = [4, 4, 4, 4, 5, 6, 7, 5, 4, 4, 4, 4]

    # player2 properties
    player2 = pygame.image.load("sprites/player1_00.png")
    player2Lives = 10
    player2W = 33
    player2H = 63
    player2X = platformX[0] + 60
    player2Y = platformY[0] - player1H
    player2Vx = 0
    player2Vy = 0
    player2Invincibility = False
    powerUpCounter2 = 0
    player2RapidFire = False
    player2Frozen = False
    frozenCounter2 = 0
    healthBar2X = 120
    healthBar2Y = 10
    healthBar2W = 30
    healthBar2H = 35
    player2PicNum = 1                         # current picture of player2
    player2Dir = "right"                       # direction in which player2 is facing
    player2Pic =[0]*10                        # 10 pictures represent all animated views of player1
    for i in range(10):                     # these pictures must be in the same folder
        player2Pic[i] = pygame.image.load("sprites/player1_0" + str(i) + ".png")
     
    nextRightPic2  = [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    nextLeftPic2 = [4, 4, 4, 4, 5, 6, 7, 5, 4, 4, 4, 4]

    # player2 bullet properties
    player2BulletX = []  
    player2BulletY = []
    player2BulletW = 15
    player2BulletH = 5
    player2BulletShift = []

    # background properties   
    galaxy1 = pygame.image.load("images/galaxy.bmp")
    galaxy1W = 800 
    galaxy1X = 0
    galaxy1Y = 0
    galaxy2 = pygame.image.load("images/galaxy_flipped.bmp")
    galaxy2W = 800
    galaxy2X = -800
    galaxy2Y = 0
    galaxySpeed = 5

    # power up properties
    powerUpX = []
    powerUpY = []
    powerUpW = 40
    powerUpH = 40
    powerUpShiftX = []
    powerUpShiftY = []
    powerUpCounter = 0
    despawnPowerUpCounter = []
    powerUp = pygame.transform.scale(powerUp, (powerUpW,powerUpH))
    GRIDSIZE=10

    # health apple Properties
    appleX = []
    appleY = []
    appleW = 50
    appleH = 40
    appleCounter = 0
    healthApple = pygame.transform.scale(healthApple, (appleW,appleH))

    # player1 health bar outline
    healthBarOutline1X = 576
    healthBarOutline1Y = 10
    healthBarOutline1W = 300
    healthBarOutline1H = 35

    # player1 health bar outline
    healthBarOutline2X = 120
    healthBarOutline2Y = 10
    healthBarOutline2W = 300
    healthBarOutline2H = 35

    # delay for bullets
    shootCounter1 = 0
    shootCounter2 = 0



#-----------------------------------------# 
    clock = pygame.time.Clock()
    FPS = 30
# menu screens
    inPlay = True
    inEnterScreen = True
    inGame = False
    inMainMenu = False
    inControls = False
    inPowerUps = False
    inPlatforms = False
    inHowToWin = False   
    inEndScreen = False
    while inPlay:

        if inEnterScreen:
            enterScreen()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    inEnterScreen = False
                    inMainMenu = True

        elif inMainMenu:
            mainMenuScreen()
            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX,mouseY) = pygame.mouse.get_pos()
                    if mouseX >= 280 and mouseX <= 520 and mouseY >=220 and mouseY<= 320:
                        inMainMenu = False
                        inGame = True
                        click.play()
                        gameMusic()
                    if mouseX >= 280 and mouseX <=520 and mouseY >=340 and mouseY<= 430:
                        inMainMenu = False
                        inControls = True
                        click.play()
                    if mouseX >= 315 and mouseX <=490 and mouseY >=460 and mouseY<= 550:
                        inMainMenu = False
                        inPlay = False
                        playingGame = False
                        click.play()

        elif inControls:
            controlsScreen()
            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX,mouseY) = pygame.mouse.get_pos()
                    if mouseX >= 35 and mouseX <=215 and mouseY >=500 and mouseY<= 575:
                        inControls = False
                        inMainMenu = True
                        click.play()
                    if mouseX >= 585 and mouseX <=765 and mouseY >=500 and mouseY<= 575:
                        inControls = False
                        inPowerUps = True
                        click.play()

        elif inPowerUps:
            powerUpsScreen()
            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX,mouseY) = pygame.mouse.get_pos()
                    if mouseX >= 35 and mouseX <=215 and mouseY >=500 and mouseY<= 575:
                        inPowerUps = False
                        inControls = True
                        click.play()
                    if mouseX >= 585 and mouseX <=765 and mouseY >=500 and mouseY<= 575:
                        inPowerUps = False
                        inPlatforms = True
                        click.play()

        elif inPlatforms:
            platformScreen()
            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX,mouseY) = pygame.mouse.get_pos()
                    if mouseX >= 35 and mouseX <=215 and mouseY >=500 and mouseY<= 575:
                        inPlatforms = False
                        inPowerUps = True
                        click.play()
                    if mouseX >= 585 and mouseX <=765 and mouseY >=500 and mouseY<= 575:
                        inPlatforms = False
                        inHowToWin = True
                        click.play()

        elif inHowToWin:
            howToWinScreen()
            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX,mouseY) = pygame.mouse.get_pos()
                    if mouseX >= 35 and mouseX <=215 and mouseY >=500 and mouseY<= 575:
                        inHowToWin = False
                        inPlatforms = True
                        click.play()
                    if mouseX >= 585 and mouseX <=765 and mouseY >=500 and mouseY<= 575:
                        inHowToWin = False
                        inGame = True
                        click.play()
                        gameMusic()

        elif inGame:
            player1Rect = pygame.Rect(player1X+3,player1Y,player1W-7,player1H)
            player2Rect = pygame.Rect(player2X+3,player2Y,player2W-7,player2H)

            redrawGameWindow()
            clock.tick(FPS)
            pygame.event.get() 
            keys = pygame.key.get_pressed() 
            if keys[pygame.K_ESCAPE]:
                inPlay = False

            # player1 key events #
    #-------------------------------------------#
            if keys[pygame.K_ESCAPE]:
                inGame = False
                playingGame = False
            if keys[pygame.K_p] and shootCounter1 >= 35 and not player1Frozen:
                shoot.play()
                player1BulletX.append(player1X+10)
                player1BulletY.append(player1Y+29)
                if player1Dir == "left":
                    player1BulletShift.append(-35)
                elif player1Dir == "right":
                    player1BulletShift.append(35)
                shootCounter1 = 0

        # move playerBullets
            for i in range(len(player1BulletX)):
                player1BulletX[i] += player1BulletShift[i]

        # set horizontal and vertical velocity
            for i in range(len(platformX)):
                platformRect = pygame.Rect(platformX[i], platformY[i], platformW[i], platformH[i])
                if keys[pygame.K_LEFT]:
                    player1Vx = -RUN_SPEED
                    player1Dir = "left"
                    if player1Vy == 0:
                        player1PicNum = nextLeftPic1[player1PicNum]
                    else:
                        player1PicNum = 8
                elif keys[pygame.K_RIGHT]:
                    player1Vx = RUN_SPEED
                    player1Dir = "right"
                    if player1Vy == 0:
                        player1PicNum = nextRightPic1[player1PicNum]
                    else:
                        player1PicNum = 9
                else:                                 # if neither left nor right arrow is pressed
                    player1Vx = 0                     # player1 is standing still (horizontally)
                    if player1Dir == "left":          # when standing,
                        player1PicNum = 4             # the animation view is either 1 or 5,
                    elif player1Dir == "right":       # depending on the direction in which
                        player1PicNum = 0             # player1 is facing
                if keys[pygame.K_UP] and (player1Y+player1H == platformY[i]+15 and player1X +player1W > platformX[i] and player1X < platformX[i] + platformW[i] and player1Vy == 0) and not player1Frozen:
                    player1Vy = JUMP_SPEED
                    if player1Dir == "left":          # when jumping,
                        player1PicNum = 8             # the animation view is either 9 or 10,
                    else:                             # depending on the direction in which
                        player1PicNum = 9             # player1 is facing
                if not player1Rect.colliderect(platformRect):
                    if player1Vy != 0:                  
                        if player1Dir == "left":          # when jumping,
                            player1PicNum = 8             # the animation view is either 9 or 10,
                        else:                             # depending on the direction in which
                            player1PicNum = 9 
        

                # player2 events #
    #----------------------------------------------#
            if keys[pygame.K_r] and shootCounter2 >= 35 and not player2Frozen:
                shoot.play()
                player2BulletX.append(player2X+10)
                player2BulletY.append(player2Y+29)
                if player2Dir == "left":
                    player2BulletShift.append(-35)
                elif player2Dir == "right":
                    player2BulletShift.append(35)
                shootCounter2 = 0
                
        # move player2Bullets
            for i in range(len(player2BulletX)):
                player2BulletX[i] += player2BulletShift[i]

        # set horizontal and vertical velocity 
            for i in range(len(platformX)):
                platformRect = pygame.Rect(platformX[i], platformY[i], platformW[i], platformH[i])
                if keys[pygame.K_a]:
                    player2Vx = -RUN_SPEED
                    player2Dir = "left"
                    if player2Vy == 0:
                        player2PicNum = nextLeftPic2[player2PicNum]
                    else:
                        player2PicNum = 8
                elif keys[pygame.K_d]:
                    player2Vx = RUN_SPEED
                    player2Dir = "right"
                    if player2Vy == 0:
                        player2PicNum = nextRightPic2[player2PicNum]
                    else:
                        player2PicNum = 9
                else:                               # if neither left nor right arrow is pressed
                    player2Vx = 0                     # player2 is standing still (horizontally)
                    if player2Dir == "left":          # when standing,
                        player2PicNum = 4             # the animation view is either 1 or 5,
                    elif player2Dir == "right":       # depending on the direction in which
                        player2PicNum = 0             # player2 is facing
                if keys[pygame.K_w] and (player2Y+player2H == platformY[i]+15 and player2X +player2W > platformX[i] and player2X < platformX[i] + platformW[i] and player2Vy == 0):
                    player2Vy = JUMP_SPEED
                    if player2Dir == "left":          # when jumping,
                        player2PicNum = 8             # the animation view is either 9 or 10,
                    elif player2Dir == "right":       # depending on the direction in which
                        player2PicNum = 9             # player2 is facing

                        
                # scroll background #
    #---------------------------------------------#
            galaxy1X = galaxy1X + galaxySpeed
            if galaxy1X + galaxySpeed > galaxy1W: 
                galaxy1X = -galaxy2W
            galaxy2X = galaxy2X + galaxySpeed
            if galaxy2X + galaxySpeed > galaxy2W:
                galaxy2X = -galaxy1W

                # player 1 movements #
    #---------------------------------------------#        
        # move the players in horizontal direction
            if not player1Frozen:
                player1X = player1X + player1Vx
        # update player1's vertical velocity    
                player1Vy = player1Vy + GRAVITY
        # move the player1 in vertical direction
                player1Y = player1Y + player1Vy
            if player1Y+player1H >= GROUND:
                player1Y = GROUND - player1H
                player1Vy = 0        
                
            for i in range(len(platformX)):
                if player1X+player1W>platformX[i]+30 and player1X<platformX[i]+platformW[i]-30 and player1Y+player1H>platformY[i]+15 and player1Vy>0:
                        # if the player1 is horizontlly within the platform ends, and if it is falling below the platform
                    if player1Y < platformY[i] + 15:
                        player1Vy = 0
                        player1Y = platformY[i] - player1H + 15

                # player 2 movements #
    #----------------------------------------------#                
        # move the players in horizontal direction
            if not player2Frozen:
                player2X = player2X + player2Vx
        # update player2's vertical velocity    
                player2Vy = player2Vy + GRAVITY
        # move the player2 in vertical direction
                player2Y = player2Y + player2Vy
            if player2Y+player2H >= GROUND:
                player2Y = GROUND - player2H
                player2Vy = 0
                
            for i in range(len(platformX)):
                if player2X+player2W>platformX[i]+30 and player2X<platformX[i]+platformW[i]-30 and player2Y+player2H>platformY[i]+15 and player2Vy>0:
                    if player2Y < platformY[i] + 15:
                    # if the player2 is horizontlly within the platform ends, and if it is falling below the platform
                        player2Y = platformY[i] - player2H+15
                        player2Vy = 0            

                # check for collision #
    #---------------------------------------------#
        # if player2 gets hit
            for i in reversed(range(len(player1BulletX))):
                player1BulletRect = pygame.Rect(player1BulletX[i],player1BulletY[i],player1BulletW,player1BulletH)
                if player1BulletRect.colliderect(player2Rect) and not player2Invincibility:
                    hit.play()
                    if player1BulletShift[i] == 35:
                        player2X += 10
                    else:
                        player2X -= 10
                    player1BulletX.pop(i)
                    player1BulletY.pop(i)
                    player1BulletShift.pop(i)
                    player2Lives -= 1
                    healthBar2X += 30


        # if player1 gets hit
            for i in reversed(range(len(player2BulletX))):
                player2BulletRect = pygame.Rect(player2BulletX[i],player2BulletY[i],player2BulletW,player2BulletH)
                if player2BulletRect.colliderect(player1Rect) and not player1Invincibility:
                    hit.play()
                    if player2BulletShift[i] == 35:
                        player1X += 10
                    else:
                        player1X -= 10
                    player2BulletX.pop(i)
                    player2BulletY.pop(i)
                    player2BulletShift.pop(i)
                    player1Lives -= 1

        # if bullet goes out of screen    
            popOutOfScreen(player1BulletX,player1BulletY,player1BulletW,player1BulletShift)
            popOutOfScreen(player2BulletX,player2BulletY,player2BulletW,player2BulletShift)

                # platforms #
    #---------------------------------------------#
        # move platforms
            for i in range(len(platformX)):  
                if platformX[i] + platformW[i] >= WIDTH:
                    platformShift[i] = -6
                if platformX[i]  <= 0:
                    platformShift[i] = 6
            for i in range(1,len(platformX)): # starts from second index so that main platform doesnt move
                platformX[i] += platformShift[i]
                
        # if player is on platform
            player1X = movingWithPlatform(player1X,player1Y,player1W,player1H)
            player2X = movingWithPlatform(player2X,player2Y,player2W,player2H)

            # if player falling off map #
    #----------------------------------------------#
        # player1
            if player1Y + player1H == GROUND:
                player1X = platformX[0] + platformW[0] - (platformW[0] * 0.5)
                player1Y =  platformY[0] - player1H
                player1Lives -= 1
                hit.play()
        # player2
            if player2Y + player2H == GROUND:
                player2X = platformX[0] + platformW[0] - (platformW[0] * 0.5)
                player2Y =  platformY[0] - player1H
                player2Lives -= 1
                healthBar2X += 30
                hit.play()

                # power ups #
    #------------------------------------------------#                
        # power up 
            powerUpCounter += 1
            if powerUpCounter >= 400:
                powerUpX.append(randint(50,750))
                powerUpY.append(randint(50,550))
                powerUpShiftX.append(7)
                powerUpShiftY.append(7)
                despawnPowerUpCounter.append(0)
                powerUpCounter = 0

        # bounce the powerup ball
            for i in range(len(powerUpX)):
                if powerUpX[i] >= WIDTH - 40 or powerUpX[i] <= 0:        # if the ball passes the left or right border of the gameWindow
                    powerUpShiftX[i] = -powerUpShiftX[i]                  # reverse the direction of horizontal movement

                if powerUpY[i] >= HEIGHT - 40 or powerUpY[i]<=0:       # if the ball passes the top or bottom of the gameWindow
                    powerUpShiftY[i] = -powerUpShiftY[i]                  # reverse the direction of vertical movement

        # move power up ball
            for i in range(len(powerUpX)):
                powerUpX[i] = powerUpX[i] + powerUpShiftX[i]
                powerUpY[i] = powerUpY[i] + powerUpShiftY[i]
                despawnPowerUpCounter[i] += 1

        # enable powerups
        # player1
            powerUpList1 = powerUpCollision(player1BulletX, player1BulletY, player1BulletW, player1BulletH, player1BulletShift,  player1Invincibility, player1RapidFire, player2Frozen)
            player1Invincibility = powerUpList1[0]
            player1RapidFire = powerUpList1[1]
            player2Frozen = powerUpList1[2]
        # player2                               
            powerUpList2 = powerUpCollision(player2BulletX, player2BulletY, player2BulletW, player2BulletH, player2BulletShift, player2Invincibility, player2RapidFire, player1Frozen)
            player2Invincibility = powerUpList2[0]
            player2RapidFire = powerUpList2[1]
            player1Frozen = powerUpList2[2]

        # despawn powerUp            
            for i in reversed(range(len(powerUpX))):
                if despawnPowerUpCounter[i] >= 420:
                    powerUpX.pop(i)
                    powerUpY.pop(i)
                    powerUpShiftX.pop(i)
                    powerUpShiftY.pop(i)
                    despawnPowerUpCounter.pop(i)
                    
                # shooting counter #
    #-------------------------------------------------#
            shootCounter1 = shootCounter(shootCounter1, player1RapidFire)
            shootCounter2 = shootCounter(shootCounter2, player2RapidFire)

        # turn off powerups
        # player1
            powerUpOffList1 = turnOffPowerUp(player1Invincibility, player2Frozen, player1RapidFire, powerUpCounter1, frozenCounter2)
            player1Invincibility = powerUpOffList1[0]
            player2Frozen = powerUpOffList1[1]
            player1RapidFire = powerUpOffList1[2]
            powerUpCounter1 = powerUpOffList1[3]
            frozenCounter1 = powerUpOffList1[4]
        # player2
            powerUpOffList2 = turnOffPowerUp(player2Invincibility, player1Frozen, player2RapidFire, powerUpCounter2, frozenCounter1)
            player2Invincibility = powerUpOffList2[0]
            player1Frozen = powerUpOffList2[1]
            player2RapidFire = powerUpOffList2[2]
            powerUpCounter2 = powerUpOffList2[3]
            frozenCounter2 = powerUpOffList2[4]

               # health apples #
    #------------------------------------------------#
        # counter for apppending apples
            appleCounter += 1
            if appleCounter >= 500:
                appleX.append(randint(70,670))
                appleY.append(0)
                appleCounter = 0
        # move the apple
            for i in range(len(appleX)):
                appleY[i] += GRAVITY
        # if apple is on platform
            for i in range(len(platformX)):
                for a in range(len(appleX)):
                        if appleX[a]+appleW>platformX[i] + 20 and appleX[a]<platformX[i]+platformW[i] - 20 and appleY[a]+appleH>platformY[i]+15:
                                # if the player1 is horizontlly within the platform ends, and if it is falling below the platform
                            if appleY[a] < platformY[i] - 15:
                                appleY[a] = platformY[i] - appleH + 15
                                appleX[a] += platformShift[i]
                            if appleX[a] + appleW >= 802:   # push apple back as if it border was a wall
                                appleX[a] -= 4
                            if appleX[a] <= -2:
                                appleX[a] += 4
                
        # if player1 touches apple
            for i in reversed(range(len(appleX))):
                appleRect = pygame.Rect(appleX[i],appleY[i],appleW,appleH)        
                if appleRect.colliderect(player1Rect) and player1Lives != 10:
                    appleEat.play()
                    appleX.pop(i)
                    appleY.pop(i)
                    player1Lives += 1

        # if player2 touches apple
            for i in reversed(range(len(appleX))):
                appleRect = pygame.Rect(appleX[i],appleY[i],appleW,appleH)        
                if appleRect.colliderect(player2Rect) and player2Lives != 10:
                    appleEat.play()
                    appleX.pop(i)
                    appleY.pop(i)
                    healthBar2X -= 30
                    player2Lives += 1

                # update health bars #
    #-------------------------------------------------#
        # reduce health bars upon hit
            healthBar1W = 30 * player1Lives
            healthBar2W = 30 * player2Lives

            # if any player dies #
    #-------------------------------------------------#    
            if player1Lives <= 0 or player2Lives <= 0:
                inGame = False
                inEndScreen = True
                endScreenMusic()

            # end menu screen #
    #-------------------------------------------------#
        elif inEndScreen:
            endGameScreen()
            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX,mouseY) = pygame.mouse.get_pos()
                    if mouseX >= 230 and mouseX <= 685 and mouseY >= 250 and mouseY <= 350:
                        inPlay = False
                        inEndScreen = False
                        click.play()
                    if mouseX >= 230 and mouseX <=685 and mouseY >= 425 and mouseY <= 530:
                        inEndScreen = False
                        inPlay = False
                        playingGame = False
                        click.play()
                                    
    #---------------------------------------# 
pygame.quit()




  
