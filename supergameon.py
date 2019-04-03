import pygame

pygame.init()


pygame.display.set_caption("Top Game")

pygame.mixer.music.load('Test.mp3')
Jumpsound = pygame.mixer.Sound('Jumpp.wav')

prav = pygame.image.load('prav.bmp')

walkRight = [pygame.image.load('right1.png'),
             pygame.image.load('right3.png'), pygame.image.load('right2.png'),
             pygame.image.load('right4.png')]

walkLeft = [pygame.image.load('left1.png'),
            pygame.image.load('left3.png'), pygame.image.load('left2.png'),
            pygame.image.load('left4.png')]

walkJump = [pygame.image.load('Jleft1.png'),
            pygame.image.load('Jright1.png'), pygame.image.load('Jleft2.png'),
            pygame.image.load('Jright2.png')]

bg = [pygame.image.load('bg.jpg'), pygame.image.load('bg2.jpg'),
      1, pygame.image.load('bg3.jpg'),
      pygame.image.load('bglvl3.jpg')]

ns = [pygame.image.load('bgst.jpg'),
      pygame.image.load('exit.jpg'), pygame.image.load('play.jpg'),
      pygame.image.load('ruls.jpg')]

life = [pygame.image.load('Life.png'), pygame.image.load('Life2.png'),
        pygame.image.load('Life3.png')]

playerStand = [pygame.image.load('stop1.png'),
               pygame.image.load('stop2.png')]

gameover = [pygame.image.load('gameover.jpg')]

win = pygame.image.load('win.jpg')

monster = [pygame.image.load('monster.png')]

heal = pygame.image.load('Heal.png')

clock = pygame.time.Clock()

x = 20
y = 390
xm = 684
ym = 77
widht = 50
height = 111
speed = 5
speedm = 5
cooldown = 1000
cooldownm = 100
lastm = 0
last = 0

blocks = [[227, [10, 235]], [390, [0, 745]], [260, [400, 600]], [235, [320, 380]], [82, [155, 305]], [42, [325, 420]],
          [20, [420, 1000]]]
blocks2 = [[248, [95, 255]], [187, [319, 480]], [185, [520, 680]], [183, [740, 890]], [47, [735, 900]],
           [-20, [365, 700]], [28, [109, 290]], [-40, [0, 140]]]
blocks3 = [[246, [775, 846]], [236, [438, 667]], [122, [835, 1000]]]

ships = [[[100, 234], [350, 392]], [[665, 800], [350, 392]], [[869, 1000], [350, 392]], [[495, 600], [-61, -20]]]
ships2 = []

jumpCount = 10
walkCount = 0

robota = True
vzal = False
vzal2 = False
vzal3 = False
Lifeschet = 6
robotan = True
Jump = False
left = False
right = False
storona = False
Jstorona = True
trata = True
dvigm = False
fon = 2
vzruv = True
uroven = 1
ddddddd = True
pravila = False


def draw():
    global walkCount
    global ddddddd
    global kek
    global now1

    if fon == 3:
        okno.blit(bg[1], (0, 0))
    elif fon == 2:
        okno.blit(bg[0], (0, 0))
    elif fon == 1:
        okno.blit(bg[2], (0, 0))
    elif fon == 4:
        okno.blit(bg[3], (0, 0))
    elif fon == 5:
        okno.blit(bg[4], (0, 0))

    if not vzal:
        okno.blit(heal, (639, 68))
    if not vzal2 and uroven == 2:
        okno.blit(heal, (639, 68))

    if walkCount + 2 >= 20:
        walkCount = 0

    if uroven == 1:
        okno.blit(monster[0], (xm, ym))

    if left:
        if not Jump:
            okno.blit(walkLeft[walkCount // 5], (x, y))
            walkCount += 1
        else:
            if Jstorona:
                okno.blit(walkJump[0], (x, y))
            else:
                okno.blit(walkJump[2], (x, y))
    elif right:
        if not Jump:
            okno.blit(walkRight[walkCount // 5], (x, y))
            walkCount += 1
        else:
            if Jstorona:
                okno.blit(walkJump[1], (x, y))
            else:
                okno.blit(walkJump[3], (x, y))
    else:
        if storona:
            okno.blit(playerStand[1], (x, y))
        else:
            okno.blit(playerStand[0], (x, y))
    if Lifeschet == 6:
        okno.blit(life[0], (850, 10))
        okno.blit(life[0], (900, 10))
        okno.blit(life[0], (950, 10))
    elif Lifeschet == 5:
        okno.blit(life[0], (850, 10))
        okno.blit(life[0], (900, 10))
        okno.blit(life[1], (950, 10))
    elif Lifeschet == 4:
        okno.blit(life[0], (850, 10))
        okno.blit(life[0], (900, 10))
        okno.blit(life[2], (950, 10))
    elif Lifeschet == 3:
        okno.blit(life[0], (850, 10))
        okno.blit(life[1], (900, 10))
        okno.blit(life[2], (950, 10))
    elif Lifeschet == 2:
        okno.blit(life[0], (850, 10))
        okno.blit(life[2], (900, 10))
        okno.blit(life[2], (950, 10))
    elif Lifeschet == 1:
        okno.blit(life[1], (850, 10))
        okno.blit(life[2], (900, 10))
        okno.blit(life[2], (950, 10))
    elif Lifeschet == 0:
        oknogg = pygame.display.set_mode((473, 441))
        oknogg.blit(gameover[0], (0, 0))
        if ddddddd:
            now1 = str(pygame.time.get_ticks())
            kek = str(int(now1)/1000) + 'ceк'
            ddddddd = False

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(kek, False, (255, 0, 0))
        okno.blit(textsurface, (0, 0))

    elif Lifeschet == 999:
        oknogg = pygame.display.set_mode((780, 461))
        oknogg.blit(win, (0, 0))
        if ddddddd:
            now1 = str(pygame.time.get_ticks())
            kek = str(int(now1)/1000) + 'ceк'
            ddddddd = False
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(kek, False, (255, 0, 0))
        okno.blit(textsurface, (0, 0))
    pygame.display.update()

oknons = pygame.display.set_mode((518, 648))

while robotan:
    clock.tick(30)


    for schet in pygame.event.get():
        if schet.type == pygame.QUIT:
            robotan = False
            robota = False

    if not pravila:
        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            if 94 < pos[1] < 156 and 110 < pos[0] < 422:
                oknons.blit(ns[2], (0, 0))
            elif 245 < pos[1] < 305 and 71 < pos[0] < 455:
                oknons.blit(ns[3], (0, 0))
            elif 557 < pos[1] < 614 and 303 < pos[0] < 500:
                oknons.blit(ns[1], (0, 0))
            else:
                oknons.blit(ns[0], (0, 0))
        else:
            oknons.blit(ns[0], (0, 0))
    else:
        okno.blit(prav, (0, 0))
    pressed = pygame.mouse.get_pressed()
    if not pravila:
        if pressed[0] and 94 < pos[1] < 156 and 110 < pos[0] < 422:
            robotan = False
            robota = True
        elif pressed[0] and 245 < pos[1] < 305 and 71 < pos[0] < 455:
            okno = pygame.display.set_mode((1000, 561))
            pravila = True
        elif pressed[0] and 557 < pos[1] < 614 and 303 < pos[0] < 500:
            robotan = False
            robota = False
    else:
        pos = pygame.mouse.get_pos()
        if pressed[0] and 0 < pos[1] < 86 and 784 < pos[0] < 1000:
            oknons = pygame.display.set_mode((518, 648))
            pravila = False
    pygame.display.update()

if Lifeschet == 0:
    robota = False

okno = pygame.display.set_mode((1000, 561))
pygame.mixer.music.play()

while robota:
    clock.tick(30)


    for schet in pygame.event.get():
        if schet.type == pygame.QUIT:
            robota = False

    keys = pygame.key.get_pressed()
    if uroven == 1:
        if 630 < x < 645 and y == 20 and not vzal:
            vzal = True
            if Lifeschet < 6:
                Lifeschet += 1
            draw()
        now = pygame.time.get_ticks()
        if now - lastm >= cooldownm:
            if xm > 700:
                dvigm = True
            elif xm < 550:
                dvigm = False
            if dvigm:
                xm -= speedm
            else:
                xm += speedm
            lastm = now
        if xm - 50 <= x <= xm + 60 and y == 20:
            if now - last >= cooldown:
                last = now
                if Lifeschet > 0:
                    Lifeschet -= 1
        if keys[pygame.K_LEFT] and x > 5:
            if not Jump:
                if (y == blocks[0][0] and x > blocks[0][1][1]) \
                        or (y == blocks[0][0] and blocks[0][1][0] > x) \
                        or (y == blocks[2][0] and blocks[2][1][0] > x) \
                        or (y == blocks[2][0] and blocks[2][1][1] < x) \
                        or (y == blocks[3][0] and blocks[3][1][1] < x) \
                        or (y == blocks[3][0] and blocks[3][1][0] > x) \
                        or (y == blocks[4][0] and blocks[4][1][1] < x) \
                        or (y == blocks[4][0] and blocks[4][1][0] > x) \
                        or (y == blocks[6][0] and blocks[6][1][1] < x) \
                        or (y == blocks[6][0] and blocks[6][1][0] > x):
                    Jump = True
                    jumpCount = -1
            x -= speed
            left = True
            right = False
            storona = False
        elif keys[pygame.K_RIGHT] and (x < 945 or (18 < y < 23)):
            if not Jump:
                if (y == blocks[0][0] and x > blocks[0][1][1]) \
                        or (y == blocks[0][0] and blocks[0][1][0] > x) \
                        or (y == blocks[2][0] and blocks[2][1][0] > x) \
                        or (y == blocks[2][0] and blocks[2][1][1] < x) \
                        or (y == blocks[3][0] and blocks[3][1][1] < x) \
                        or (y == blocks[3][0] and blocks[3][1][0] > x) \
                        or (y == blocks[4][0] and blocks[4][1][1] < x) \
                        or (y == blocks[4][0] and blocks[4][1][0] > x) \
                        or (y == blocks[6][0] and blocks[6][1][1] < x) \
                        or (y == blocks[6][0] and blocks[6][1][0] > x):
                    Jump = True
                    jumpCount = -1
                elif (18 < y < 23) and x > 945:
                    fon = 4
                    uroven = 2
                    x = 20
                    y = 395
            x += speed
            left = False
            right = True
            storona = True
        else:
            left = False
            right = False
            walkCount = 0
        if not Jump:
            if keys[pygame.K_UP]:
                Jumpsound.play()
                Jump = True
        else:

            if y != blocks[0][0] or y != blocks[1][0]:
                if jumpCount < 0:
                    y += 1
                    if vzruv:
                        fon = 2
                    for schet2 in range((jumpCount ** 2) // 2):
                        if y == blocks[0][0] and (blocks[0][1][0] < x < blocks[0][1][1]) \
                                or (y == blocks[1][0]) \
                                or (y == blocks[2][0] and (blocks[2][1][0] < x < blocks[2][1][1])) \
                                or (y == blocks[3][0] and (blocks[3][1][0] < x < blocks[3][1][1])) \
                                or (y == blocks[4][0] and (blocks[4][1][0] < x < blocks[4][1][1])) \
                                or (y == blocks[6][0] and (blocks[6][1][0] < x < blocks[6][1][1])):
                            Jump = False
                            jumpCount = 10
                        elif (y == blocks[5][0] and (blocks[5][1][0] < x < blocks[5][1][1])):
                            y += 1
                            if vzruv:
                                pass
                            else:
                                Jump = False
                            jumpCount = 10
                            fon = 3
                            vzruv = True

                        else:
                            y += 1
                    Jstorona = False
                else:
                    y -= 1
                    if vzruv:
                        fon = 2
                    for schet2 in range((jumpCount ** 2) // 2):
                        if (y == blocks[0][0] and (blocks[0][1][0] < x < blocks[0][1][1])) \
                                or (y == blocks[1][0]) \
                                or (y == blocks[2][0] and (blocks[2][1][0] < x < blocks[2][1][1])) \
                                or (y == blocks[3][0] and (blocks[3][1][0] < x < blocks[3][1][1])) \
                                or (y == blocks[4][0] and (blocks[4][1][0] < x < blocks[4][1][1])) \
                                or (y == blocks[6][0] and (blocks[6][1][0] < x < blocks[6][1][1])):
                            Jump = False
                            jumpCount = 10
                        elif (y == blocks[5][0] and (blocks[5][1][0] < x < blocks[5][1][1])):
                            y -= 1
                            if vzruv:
                                pass
                            else:
                                Jump = False
                            jumpCount = 10
                            fon = 3
                            vzruv = True

                        else:
                            y -= 1
                    Jstorona = True
                jumpCount -= 1
            else:
                Jump = False
                jumpCount = 10
    elif uroven == 2:
        now = pygame.time.get_ticks()

        if 630 < x < 645 and y == -20 and not vzal2:
            vzal2 = True
            if Lifeschet < 6:
                Lifeschet += 1
            draw()

        if ships[0][1][0] < y < ships[0][1][1] + 5 and ships[0][0][0] < x < ships[0][0][1] \
                or ships[1][1][0] < y < ships[1][1][1] + 5 and ships[1][0][0] < x < ships[1][0][1] \
                or ships[2][1][0] < y < ships[2][1][1] + 5 and ships[2][0][0] < x < ships[2][0][1] \
                or ships[3][1][0] < y < ships[3][1][1] + 5 and ships[3][0][0] < x < ships[3][0][1]:

            if now - last >= cooldown:
                last = now
                if Lifeschet > 0:
                    Lifeschet -= 1
        if keys[pygame.K_LEFT] and (x >= 5 or -100 < y < 0):
            if not Jump:
                if (y == blocks2[0][0] and x < blocks2[0][1][0]) \
                        or (y == blocks2[1][0] and blocks2[1][1][0] - 10 < x < blocks2[1][1][0]) \
                        or (y == blocks2[2][0] and blocks2[2][1][0] - 10 < x < blocks2[2][1][0]) \
                        or (y == blocks2[4][0] and blocks2[4][1][0] - 10 < x < blocks2[4][1][0]) \
                        or (y == blocks2[5][0] and blocks2[5][1][0] - 10 < x < blocks2[5][1][0]) \
                        or (y == blocks2[6][0] and blocks2[6][1][0] - 10 < x < blocks2[6][1][0]) \
                        or (y == blocks2[3][0] and blocks2[3][1][0] - 10 < x < blocks2[3][1][0]):
                    Jump = True
                    jumpCount = -1
                elif (370 < y < 420 and 375 < x < 700):
                    while x > 375:
                        x -= speed
                        draw()
                elif (y == 183 and 775 < x < 895):
                    while x > 775:
                        x -= speed
                        draw()
                elif (-100 < y < 0) and x < 10:
                    fon = 5
                    uroven = 3
                    x = 995
                    y = 395

            x -= speed
            left = True
            right = False
            storona = False
        elif keys[pygame.K_RIGHT] and (x < 945):
            if not Jump:
                if (y == blocks2[0][0] and x > blocks2[0][1][1]) \
                        or (y == blocks2[1][0] and x > blocks2[1][1][1]) \
                        or (y == blocks2[2][0] and x > blocks2[2][1][1]) \
                        or (y == blocks2[4][0] and x > blocks2[4][1][1]) \
                        or (y == blocks2[5][0] and x > blocks2[5][1][1]) \
                        or (y == blocks2[6][0] and x > blocks2[6][1][1]) \
                        or (y == blocks2[7][0] and x > blocks2[7][1][1]) \
                        or (y == blocks2[3][0] and x > blocks2[3][1][1]):
                    Jump = True
                    jumpCount = -1
                elif 370 < y < 420 and 375 < x < 700:
                    while x < 700:
                        x += speed
                        draw()
                elif (y == 183 and 775 < x < 895):
                    while x < 895:
                        x += speed
                        draw()
                    Jump = True
                    jumpCount = -1
            x += speed
            left = False
            right = True
            storona = True
        else:
            left = False
            right = False
            walkCount = 0
        if not Jump:
            if keys[pygame.K_UP]:
                Jump = True
                Jumpsound.play()
        else:
            if y != blocks[0][0] or y != blocks[1][0]:
                if jumpCount < 0:
                    y += 1
                    for schet2 in range((jumpCount ** 2) // 2):
                        if (y == blocks2[0][0] and (blocks2[0][1][0] < x < blocks2[0][1][1])) \
                                or (y == blocks[1][0]) \
                                or (y == blocks2[2][0] and (blocks2[2][1][0] < x < blocks2[2][1][1])) \
                                or (y == blocks2[3][0] and (blocks2[3][1][0] < x < blocks2[3][1][1])) \
                                or (y == blocks2[4][0] and (blocks2[4][1][0] < x < blocks2[4][1][1])) \
                                or (y == blocks2[5][0] and (blocks2[5][1][0] < x < blocks2[5][1][1])) \
                                or (y == blocks2[6][0] and (blocks2[6][1][0] < x < blocks2[6][1][1])) \
                                or (y == blocks2[7][0] and (blocks2[7][1][0] < x < blocks2[7][1][1])) \
                                or (y == blocks2[1][0] and (blocks2[1][1][0] < x < blocks2[1][1][1])):
                            Jump = False
                            jumpCount = 10
                        else:
                            y += 1
                    Jstorona = False
                else:
                    y -= 1
                    for schet2 in range((jumpCount ** 2) // 2):
                        if (y == blocks2[0][0] and (blocks2[0][1][0] < x < blocks2[0][1][1])) \
                                or (y == blocks[1][0]) \
                                or (y == blocks2[2][0] and blocks2[2][1][0] < x < blocks2[2][1][1]) \
                                or (y == blocks2[3][0] and blocks2[3][1][0] < x < blocks2[3][1][1]) \
                                or (y == blocks2[4][0] and (blocks2[4][1][0] < x < blocks2[4][1][1])) \
                                or (y == blocks2[5][0] and (blocks2[5][1][0] < x < blocks2[5][1][1])) \
                                or (y == blocks2[6][0] and (blocks2[6][1][0] < x < blocks2[6][1][1])) \
                                or (y == blocks2[7][0] and (blocks2[7][1][0] < x < blocks2[7][1][1])) \
                                or (y == blocks2[1][0] and blocks2[1][1][0] < x < blocks2[1][1][1]):
                            Jump = False
                            jumpCount = 10
                        else:
                            y -= 1
                    Jstorona = True
                jumpCount -= 1
            else:
                Jump = False
                jumpCount = 10
    elif uroven == 3:


        now = pygame.time.get_ticks()
        if 0 == 1:

            if now - last >= cooldown:
                last = now
                if Lifeschet > 0:
                    Lifeschet -= 1
        if y == 390 and (390 < x < 600):
            y += 500
            Lifeschet = 0
        elif y > 800:
            Lifeschet = 0
        if keys[pygame.K_LEFT] and x > 5 and (
            (not (760 <= x <= 860) or y < 247) and (not (600 <= x <= 665) or y < 237)):
            if not Jump:
                if (y == blocks3[0][0] and x < blocks3[0][1][0]) \
                        or (y == blocks3[1][0] and blocks3[1][1][0] - 10 < x < blocks3[1][1][0]) \
                        or (y == blocks3[2][0] and blocks3[2][1][0] - 10 < x < blocks3[2][1][0]):
                    Jump = True
                    jumpCount = -1

            x -= speed
            left = True
            right = False
            storona = False
        elif keys[pygame.K_RIGHT] and (x < 945) and (
            (not (760 < x < 860) or y < 247) and (not (600 < x < 665) or y < 237)):
            if not Jump:
                if (y == blocks3[0][0] and x > blocks3[0][1][1]) \
                        or (y == blocks3[1][0] and x > blocks3[1][1][1]) \
                        or (y == blocks3[2][0] and x > blocks3[2][1][1]) \
                        or (y == blocks[0][0] and x > 390):
                    Jump = True
                    jumpCount = -1
                elif x > 939 and y == 122:
                    x = 595
                    y = 236
                elif x > 596 and y == 236:
                    x = 937
                    y = 122
            x += speed
            left = False
            right = True
            storona = True
        else:
            left = False
            right = False
            walkCount = 0
        if not Jump:
            if keys[pygame.K_UP]:
                Jump = True
                Jumpsound.play()
        else:
            if (y != blocks[0][0] or y != blocks[1][0]) or (390 < x < 600):
                if jumpCount < 0:
                    y += 1
                    for schet2 in range((jumpCount ** 2) // 2):
                        if (y == blocks[1][0] and (x < 390 or x > 600)) \
                                or (y == blocks3[0][0] and (blocks3[0][1][0] < x < blocks3[0][1][1])) \
                                or (y == blocks3[1][0] and (blocks3[1][1][0] < x < blocks3[1][1][1])) \
                                or (y == blocks3[2][0] and (blocks3[2][1][0] < x < blocks3[2][1][1])):
                            Jump = False
                            jumpCount = 10
                        else:
                            y += 1
                    Jstorona = False
                else:
                    y -= 1
                    for schet2 in range((jumpCount ** 2) // 2):
                        if (y == blocks[1][0] and (x < 390 or x > 600)) \
                                or (y == blocks3[0][0] and blocks3[0][1][0] < x < blocks3[0][1][1]) \
                                or (y == blocks3[1][0] and blocks3[1][1][0] < x < blocks3[1][1][1]) \
                                or (y == blocks3[2][0] and blocks3[2][1][0] < x < blocks3[2][1][1]):
                            Jump = False
                            jumpCount = 10
                        else:
                            y -= 1
                    Jstorona = True
                jumpCount -= 1
            else:
                Jump = False
                jumpCount = 10

    draw()


pygame.quit()
