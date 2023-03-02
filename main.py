import pygame ,sys, random
#Tao nen chay lien tuc
def draw_floor():
    screen.blit(floor,(floor_x_position, 600)) #set toa do floor_x_position, 600
    screen.blit(floor,(floor_x_position+423, 600)) #set toa do loor_x_position+423, 600
#Tao xuat hien ong cho game
def create_pipe():
    random_pipe_pos = random.choice(pipe_height) #chon chieu cao ngau nhien tu pipe_height
    bottom_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos-600))
    return bottom_pipe, top_pipe
#Tao cac ong
def move_pipe(pipes):
    for pipe in pipes :
        pipe.centerx -= 5
    return pipes
# di chuyen ong
def draw_pipe(pipes) :
    for pipe in pipes :
        if pipe.bottom >= 768 :
            screen.blit(pipe_surface, pipe) 
        else :
            flip_pipe = pygame.transform.flip(pipe_surface,False, True)
            screen.blit(flip_pipe, pipe) 

pygame.init() #Khoi tao pygame

# Tao man hinh chinh
screen = pygame.display.set_mode((432,768))
# Set FPS cho game
clock = pygame.time.Clock() 
# tao bien trong luc
gravity = 0.25
# di chuyen cua chim, bat dau = 0
bird_movement = 0 
# set background for screen
bg = pygame.image.load('assets/background-night.png').convert() #convert giong file game load nhanh hon
bg = pygame.transform.scale2x(bg) # lam cho bg x 2
# set them anh floor: san cho screen
floor = pygame.image.load('assets/floor.png').convert()
floor = pygame.transform.scale2x(floor) # lam cho floor x 2
floor_x_position = 0 # vi tri floor
#init bird
bird = pygame.image.load('assets/yellowbird-midflap.png')
bird = pygame.transform.scale2x(bird) # lam cho bird x 2
bird_rect = bird.get_rect(center = (100,384)) #TAo 1 cai hinh chu nhat cho bird
#Tao ong cho game
pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface) # lam cho bipipe_surfacerd x 2
#Tao list ong
pipe_list = []

#Tao rieng chieu dai cho ong
pipe_height = [350,450,500]
#Tao timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)

# Tao chuoi vong lap game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Tao nut thoat cho game
            pygame.quit()
            sys.exit()  #Thoat he thong
        if event.type == pygame.KEYDOWN: #Khi co phim bi nhan thi chim bay
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement =-8
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
            # print(create_pipe)


    screen.blit(bg,(0, 0)) #set toa do 0, 0
    
    #con chim di chuyen thi cang rot
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird,bird_rect) # da set hinh chu nhat cho con chim
    #pipe
    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)
    #San
    floor_x_position -= 1 # NO di chuyen
    draw_floor() #goi ham
    if floor_x_position <= -432:
        floor_x_position = 0
    pygame.display.update()
    clock.tick(120) #FPS = 120            