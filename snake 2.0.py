import pgzrun
import random
#speed1 = 4
bush = Actor("bushpy2.gif")
bush2 = Actor("bushpy2.gif")
bush3 = Actor("bushpy2.gif")
bush4 = Actor("bushpy2.gif")
bush5 = Actor("bushpy2.gif")
bush6 = Actor("bushpy2.gif")
enemy = Actor("tank_huge.png")
backforest = Actor("back forest.png")
tank = Actor('tank_red.png')
tank2 = Actor("tank_sand.png")
crate = Actor('crate.png')
#powerup = Actor ("luma boi2 (2).png")
tank.pos = 100, 56
tank2.pos = 175, 56
crate.y = random.randint(0,450)
crate.x = random.randint(0,450)
enemy.pos = 250,450
enemyX = random.randint(0,450)
enemyY = random.randint(0,450)
bush.pos = 100, 180
bush2.pos = 230, 250
bush3.pos = 400, 160
bush4.pos =  300, 350
bush5.pos =  150, 400
bush6.pos = 450, 300
#powerup.pos = 300,250
safespot = Rect((70,30), (150,50))
green = 34,139,34

WIDTH = 500
HEIGHT = 500
points = 0
points2 = 0

backforest = Actor('back forest.png', (WIDTH/2, HEIGHT/2))
scboard = Rect((20, 20),(50, 50))
scboard2 = Rect((420, 20),(50, 50))

def draw():
    screen.clear()
    backforest.draw()
    bush.draw()
    bush2.draw()
    bush3.draw()
    bush4.draw()
    bush5.draw()
    bush6.draw()
    tank.draw()
    tank2.draw()
    enemy.draw()
    crate.draw()
    #powerup.draw()
    screen.draw.rect(safespot,green)

    screen.draw.textbox(str(points), scboard)
    screen.draw.textbox(str(points2), scboard2)

def update():
    global points
    global points2
    global enemyX
    global enemyY
    go()
    go2()
    if enemy.x < enemyX:
        enemy.x += 1
    if enemy.x > enemyX:
        enemy.x -= 1

    if enemy.y < enemyY:
        enemy.y += 1

    if enemy.y > enemyY:
        enemy.y -= 1

    if enemy.x == enemyX and enemy.y == enemyY:
        enemyX = random.randint(0, 450)
        enemyY = random.randint(0, 450)

    if tank2.colliderect(enemy):
        if enemy.colliderect(safespot):
            print("i am safetank2")
        else:
            points2 -= 5
            tank2.pos = 175, 56

    if tank.colliderect(enemy):
        if enemy.colliderect(safespot):
            print("i am safe tank1")
        else:
            points -= 5
            tank.pos = 100, 56


    #if tank.colliderect(powerup):
        speed1 = 20








    if tank.colliderect(crate):  #ger poäng till spelaren
        points = points + 1
        restart()

    if tank2.colliderect(crate):
        points2 = points2 + 1
        restart()


    if tank.colliderect(bush):# ser tiil att man inte kan köra över ett hinder.
        tank.pos = 100, 56

    if tank2.colliderect(bush):
        tank2.pos = 175, 56

    if tank.colliderect(bush2):
        tank.pos = 100, 56

    if tank2.colliderect(bush2):
        tank2.pos = 175, 56


    if tank.colliderect(bush3):
        tank.pos = 100, 56
    if tank2.colliderect(bush3):
        tank2.pos = 175, 56

    if tank.colliderect(bush4):
        tank.pos = 100, 56

    if tank2.colliderect(bush4):
        tank2.pos = 175, 56

    if tank.colliderect(bush4):
        tank.pos = 100, 56

    if tank2.colliderect(bush4):
        tank2.pos = 175, 56

    if tank.colliderect(bush5):
        tank.pos = 100, 56

    if tank2.colliderect(bush5):
        tank2.pos = 175, 56

    if tank.colliderect(bush6):
        tank.pos = 100, 56

    if tank2.colliderect(bush6):
        tank2.pos = 175, 56



    if ((crate.colliderect(bush)) or (crate.colliderect(bush2)) or (crate.colliderect(bush3)) or (crate.colliderect(bush4)) or (crate.colliderect(bush5)) or (crate.colliderect(bush6))):
        restart()


    if tank.y > 500:
        tank.y -= random.randint(5, 8) #ser till att tanken inte åker ur skärmen. nedre
    if tank.y < 0:
        tank.y += random.randint(5, 8) #ser till att tanken inte åker ur skärmen. övre
    if tank.x > 500:
        tank.x -= random.randint(5, 8)  # ser till att tanken inte åker ur skärmen. höger
    if tank.x < 0:
        tank.x += random.randint(5, 8)  # ser till att tanken inte åker ur skärmen. vänster


    if tank2.y > 500:
        tank2.y -= random.randint(5, 8) #ser till att tanken inte åker ur skärmen. nedre
    if tank2.y < 0:
        tank2.y += random.randint(5, 8) #ser till att tanken inte åker ur skärmen. övre
    if tank2.x > 500:
        tank2.x -= random.randint(5, 8)  # ser till att tanken inte åker ur skärmen. höger
    if tank2.x < 0:
        tank2.x += random.randint(5, 8)  # ser till att tanken inte åker ur skärmen. vänster




def go():
 #global speed1
 if keyboard.left == True:
     tank.x += -4

 if keyboard.right == True:
     tank.x += 4

 if keyboard.up == True:
     tank.y += -4

 if keyboard.down == True:
     tank.y += 4




def go2():
 if keyboard.a == True:
     tank2.x += -4

 if keyboard.d == True:
     tank2.x += 4

 if keyboard.w == True:
     tank2.y += -4

 if keyboard.s == True:
     tank2.y += 4

def restart():
    tank.pos = 100, 56
    tank2.pos = 175, 56
    crate.y = random.randint(0, 450)
    crate.x = random.randint(0, 450)







pgzrun.go()