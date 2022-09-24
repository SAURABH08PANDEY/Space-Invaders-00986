import pygame,sys,os
#from pygame.locals import*
import random
from math import*
from pygame import mixer
import time


#initialize pygame
pygame.init()
clock= pygame.time.Clock()


#background sound
mixer.music.load('musics/music2.mp3')
mixer.music.play(-1)
musics=os.listdir('./musics')
spot=len(musics)

# create screen 
screen = pygame.display.set_mode((1050,600))

#background image
background=pygame.image.load('req/space.png')



#title and icon
pygame.display.set_caption("SPACE SHOOTER     -by SAURABH PANDEY")
icon=pygame.image.load('req/ufo.png')
pygame.display.set_icon(icon) 


#player
playerimg = pygame.image.load('req/space-invaders.png')
playerx=370
playery=480
xupdate=0
cheats=['*','+','slow','fast','upup','m','reset']
cheat=""
speedx,speedy=1.5,40##############
speedb=3
spot=0

#enemy
enemyimg=[]
enemyx=[]
enemyy=[]
updateenemyx=[]
updateenemyy=[]

numenemy=6
panda=0

for i in range (25):
    enemyimg.append(pygame.image.load('req/alien.png'))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,150))
    updateenemyx.append(speedx)
    updateenemyy.append(speedy)


#bullet
bulletimg = pygame.image.load('req/bullet.png')
bulletx=0
bullety=480
updatebulletx=0
updatebullety=speedb
bulletstate="ready"


highscore=0
score=0
font=pygame.font.Font('req/text.ttf',35)
textx=10
texty=10

overfont=pygame.font.Font('req/text.ttf',70)
overfont1=pygame.font.Font('req/text.ttf',30)
overfont2=pygame.font.Font('req/text.ttf',20)

def gameover():
    global speedb
    global highscore
    speedb=3
    ################
    overtext=overfont.render("GAME OVER",True,(255,255,255))
    screen.blit(overtext,(260,151))
    overtext=overfont.render("PRESS Y TO PLAY AGAIN",True,(255,255,255))
    screen.blit(overtext,(120,230))
    overtext=overfont1.render("MADE BY:SAURABH PANDEY",True,(255,255,255))
    screen.blit(overtext,(520,540))


    if (score >highscore):
        highscore=score
    showscore=font.render("HIGH SCORE : "+str(highscore),True,(255,255,255))
    screen.blit(showscore,(600,20))
def ch():
    overtext=overfont1.render("CHEATS MENU:",True,(255,255,255))
    screen.blit(overtext,(810,0))
    overtext=overfont2.render("SCORE 10+ : x*",True,(255,255,255))
    screen.blit(overtext,(810,40))
    overtext=overfont2.render("SCORE 25+ : x+",True,(255,255,255))
    screen.blit(overtext,(810,80))
    overtext=overfont2.render("BULLET SPEED+ : XUPUP",True,(255,255,255))
    screen.blit(overtext,(810,120))
    overtext=overfont2.render("ENEMY SPEED- : XSLOW",True,(255,255,255))
    screen.blit(overtext,(810,160))
    overtext=overfont2.render("ENEMY SPEED RESET : XRESET ",True,(255,255,255))
    screen.blit(overtext,(810,200))
    overtext=overfont2.render("CHANGE MUSIC : XM",True,(255,255,255))
    screen.blit(overtext,(810,240))
    overtext=overfont2.render("ENEMY SPEED+ : XFAST",True,(255,255,255))
    screen.blit(overtext,(810,280))

def showscor(x,y):
    showscore=font.render("SCORE : "+str(score),True,(255,255,255))
    screen.blit(showscore,(x,y))


def firebullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimg,(x,y+10))



def collision(x1,x2,y1,y2):
    distance=sqrt( ((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)) )
    if distance<27:
        return (True)
    else:
        return (False)


def player(x,y):#to blit pic on screen
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):#to blit pic on screen
    screen.blit(enemyimg[i],(x,y))



# game loop
running=True
while running:
    #RGB - RED GREEN BLUE
    screen.fill((33,0,0))

    #background image appear
    screen.blit(background,(0,0))

    #capuring all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

         
            
        #to check any key press and later left right
            
        if event.type == pygame.KEYDOWN:
            hold=(event.unicode)
            cheat=cheat+hold

            
            if event.key == pygame.K_LEFT:
                xupdate =-2.5  ###############                    #once presse its added in line and will stop if keyup
            if event.key == pygame.K_RIGHT:
                xupdate =2.5
            if event.key == pygame.K_SPACE:
                if bulletstate == "ready":
                    bullsound= mixer.Sound('req/laser.mp3')
                    bullsound.play()
                    updatebulletx=playerx
                    firebullet(updatebulletx, bullety)
            if event.key == pygame.K_y and panda==1:
                speedx,speedy=1.5,40#########
                for j in range(numenemy):
                    enemyx[j]=random.randint(0,735)
                    enemyy[j]=random.randint(50,150)

                score=0
                numenemy=6
                panda=0
            if event.key == pygame.K_x:
                cheat=""
                
            
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xupdate=0
               

    
    #player movement restriction      
    playerx+=xupdate
    
    if(playerx <0):
        playerx=0
    elif(playerx >735):
        playerx=735

    
    #enemy movement

    for i in range(numenemy):

        #game over
        if enemyy[i]>440:####
            for j in range(numenemy):
                enemyy[j]=2000
            panda=1
            speedx,speedy=0.7,40
            gameover()
            

        
        enemyx[i]+=updateenemyx[i]
        
        if(enemyx[i] <0):
            updateenemyx[i]=speedx
            enemyy[i]+=updateenemyy[i]
        elif(enemyx[i] >735):
            updateenemyx[i]=-1*speedx
            enemyy[i]+=updateenemyy[i]

            ## collision
        col=collision(enemyx[i],updatebulletx,enemyy[i],bullety)
        if col:
            blastsound= mixer.Sound('req/blast.mp3')
            blastsound.play()
            bullety=480
            bulletstate="ready"
            score+=1
            if(score%20==0 and score<150):
                numenemy+=1
            elif(score%25==0 and score>=150 and score<300):
                numenemy+=2
            elif(score >=300 and score <301):
                numenemy+=10
            elif(score >=350):
                numenemy+=1
                
            enemyx[i]=random.randint(0,735)
            enemyy[i]=random.randint(50,150)

        enemy(enemyx[i],enemyy[i],i)#enemy position sending to function
        
        


        


     #bullet control movement
    if bullety<=0:
        bullety=480
        bulletstate="ready"
        
    if bulletstate == "fire":
        firebullet(updatebulletx,bullety)
        bullety -=speedb#################



    if (len(cheat)<7):
        if(cheat==cheats[0]):
            score+=10
            cheat=""
        elif(cheat==cheats[1]):
            score+=25
            cheat=""
        elif(cheat==cheats[2]):
            if(speedx>0.2):
                speedx -=0.1
            cheat=""
        elif(cheat==cheats[3]):
            if(speedx<2):
                speedx =1.4
            cheat==""
        elif(cheat==cheats[4]):
            if(speedb<6):
                speedb+=1
            cheat=""
        elif(cheat==cheats[5]):
            cheat=""
            mixer.music.load('musics/'+musics[spot])
            mixer.music.play(-1)
            spot=spot-1
            if spot<0:
                spot=len(musics)-1
        elif(cheat==cheats[6]):
            speedx=0.8
            cheat=""
            
                
    else:
            cheat=""


        
   
    ch()
    player(playerx,playery)#always put after screen.fill
    showscor(textx,texty)
    
    
    pygame.display.update()# so that screen keeps updating
