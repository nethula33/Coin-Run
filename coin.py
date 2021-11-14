import pygame

#pygame initionization
pygame.init()

#game window
scr = pygame.display.set_mode((1200,700))

#logo 
logo = pygame.image.load("img/galaxy.png")
pygame.display.set_icon(logo)

#caption
pygame.display.set_caption("COIN RUN")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
#background image
bgmage = pygame.image.load("img/brick-wall.jpg")

#player
playerimage = pygame.image.load("img/man.png")

#boxes 
boxes_qty = 16
boximage = pygame.image.load("img/wooden-box.png")
boxes_x_list = [10 , 138, 266, 394, 394, 394, 394, 394, 10 , 138, 138, 138, 590, 680, 860, 970]
boxes_y_list = [600, 600, 600, 600, 510, 420, 330, 240, 420, 420, 330, 240, 420, 150, 300, 100]

boxes_ranges = []

def boxes(x,y):
        scr.blit(boximage,(x,y))

player_move_h = 0
player_move_v = 10
playerx = 20
playery = 540
height_y = 10 
jump = False

def player(x,y):
    scr.blit(playerimage,(x,y))

loop_run = True
while loop_run:   
    scr.blit(bgmage,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop_run = False
#Jumping
    jump_move = pygame.key.get_pressed()
    if jump_move[pygame.K_SPACE] and jump is False:
            jump = True
    if jump is True:
            playery -= height_y*7
            height_y -= 1
            if height_y <-10:
                    jump = False 
                    height_y = 10

#Player Handle
    if event.type == pygame.KEYDOWN:
#DETECT LEFT ARROW KEY
        if event.key == pygame.K_LEFT:
            print("LEFT")
            player_move_h = -10
#DETECT RIGHT ARROW KEY
        if event.key == pygame.K_RIGHT:
            print("RIGHT")
            player_move_h = 10

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            player_move_v = 0
        elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player_move_h = 0

#player go to HORIZONTAL
    playerx += player_move_h

#Y LIMITATION-/-/-/-/-/-/
    if playery <= 30:
        playery = 30
    if playery >= 595:
        playery = 595
        
#X LIMITATION-/-/-/-/-/-/
    if playerx <= 10:
        playerx = 10
    if playerx >= 1100:
        playerx = 1100

#boxes
    for x in range(16):
        boxes(boxes_x_list[x],boxes_y_list[x])
        
#call to player 
    player(playerx,playery)

#call to boxes
    pygame.time.delay(20)
    pygame.display.update()
