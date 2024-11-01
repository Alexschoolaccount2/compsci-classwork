import pygame

pygame.init()

game_clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))



ground = pygame.Rect(0,350,800,300)
houseBase = pygame.Rect(305,170,180,250)
roofpoints= [(260,170),(393,100),(526,170)]
OFloorRoof = [(260,310),(305,265),(485,265),(528,310)]
door = pygame.Rect(366,340,60,80)
doorWindow = pygame.Rect(379,348,35,17)
floorwindow = pygame.Rect(341,190,106,57)
bar1 = pygame.Rect(379,355.5,35,3)
bar2 = pygame.Rect(394,345.5,3,35)
bar3 = pygame.Rect(341,217,106,5)
bar4 = pygame.Rect(392,190,5,58)

head_y = 436
head_direction = 9


witch_x = -50

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    head_y -= head_direction * 2
    if head_y <= 420 or head_y >= 436:
        head_direction *= -1  

    
    witch_x += 5
    if witch_x-18 > 800:
        witch_x = -50
    
    
    screen.fill((0,0,75))  
    
    
    
    pygame.draw.rect(screen, (33,64, 26), ground)
    
    #pumpkin parts and code:
    pygame.draw.rect(screen, (3, 138, 18), (104, 320, 12, 45))

    # Draw pumpkin head (moving)
    pygame.draw.circle(screen, (235, 123, 5), (110, 436), 78)

    # Draw pumpkin jaw (stays on the ground)
    pygame.draw.rect(screen, (33, 64, 26), (67, 508, 85, 37))

    # Draw pumpkin mouth with dynamic opening
    pygame.draw.polygon(screen, (0, 0, 0), [
    (85, head_y + 15), (135, head_y + 15),  # Wider at the top
    (130, head_y + 65), (110, head_y + 45),  # Increased height
    (90, head_y + 65), (85, head_y + 15)     # Left point matches right point
])
    
    
    
#orag
    pygame.draw.rect(screen, (235, 123, 5), (67, 436-20, 85, 33))

    # Draw pumpkin eyes
    pygame.draw.polygon(screen, (0, 0, 0), ((65, 436 - 16), (80, 436 - 36), (95, 436 - 16)))
    pygame.draw.polygon(screen, (0, 0, 0), ((125, 436 - 16), (140, 436 - 36), (155, 436 - 16)))

    
    
    

    #moon parts
    pygame.draw.circle(screen,(237, 240, 245),(624,97),83)
    pygame.draw.circle(screen,(217, 219, 222),(580,120),16)
    pygame.draw.ellipse(screen,(217, 219, 222),(578,120,35,17),16)
    pygame.draw.circle(screen,(217, 219, 222),(620,40),16)
    pygame.draw.ellipse(screen,(217, 219, 222),(615,26,35,17),16)
    pygame.draw.ellipse(screen,(217, 219, 222),(618,70,55,37))
    pygame.draw.ellipse(screen,(217, 219, 222),(638,110,27,45))
    pygame.draw.ellipse(screen,(217, 219, 222),(567,50,27,45))

    #witch:
    pygame.draw.ellipse(screen,(0,0,0),(witch_x+9,147,16,25))
    
    pygame.draw.polygon(screen, (0, 0, 0), [
        (witch_x+3, 150), (witch_x + 15, 138), (witch_x + 30, 150)  # Head and hat
    ])
    pygame.draw.polygon(screen, (0, 0, 0), [
        (witch_x + 10, 157), (witch_x + 20, 152), (witch_x + 35, 157), (witch_x + 20, 162)  # Body
    ])
    
    pygame.draw.polygon(screen, (0, 0, 0), [
        (witch_x-8, 165), (witch_x-18, 169), (witch_x-15, 158)  # broom-straw (in prog)
    ])
    
    pygame.draw.line(screen, (0, 0, 0), (witch_x - 10, 165), (witch_x + 50, 170), 3)  # Broomstick

    #house parts
    pygame.draw.rect(screen,(69,46,94),houseBase)
    pygame.draw.polygon(screen,(0,0,0),roofpoints)
    pygame.draw.polygon(screen,(0,0,0),OFloorRoof)
    pygame.draw.rect(screen, (0,0,0), door)
    pygame.draw.rect(screen, (200,200,0), floorwindow)
    pygame.draw.circle(screen,(200,200,0),(412,386),5)
    pygame.draw.rect(screen, (200,200,0), doorWindow)
    pygame.draw.rect(screen, (0,0,0), bar1)
    pygame.draw.rect(screen, (0,0,0), bar2)
    pygame.draw.rect(screen, (0,0,0), bar3)
    pygame.draw.rect(screen, (0,0,0), bar4)

    

    game_clock.tick(10)
    pygame.display.flip()
    