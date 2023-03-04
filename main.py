import pygame ,sys, random
#Tao nen chay lien tuc
def draw_floor():
    screen.blit(floor,(floor_x_position, 650)) #set toa do floor_x_position, 600
    screen.blit(floor,(floor_x_position+423, 650)) #set toa do loor_x_position+423, 600
#Tao xuat hien ong cho game
def create_pipe():
    random_pipe_pos = random.choice(pipe_height) #chon chieu cao ngau nhien tu pipe_height
    bottom_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos-700))
    return bottom_pipe, top_pipe
#Tao cac ong
def move_pipe(pipes):
    for pipe in pipes :
        pipe.centerx -= 5
    return pipes
# di chuyen ong
def draw_pipe(pipes) :
    for pipe in pipes :
        if pipe.bottom >= 600 :
            screen.blit(pipe_surface, pipe) 
        else :
            flip_pipe = pygame.transform.flip(pipe_surface,False, True)
            screen.blit(flip_pipe, pipe) 
# Xu li va cham
def check_collosion(pipes):
    for pipe in pipes :
        if bird_rect.colliderect(pipe) : #collidrect() : ham va cham cua pygame
            hit_sound.play()
            return False
        if bird_rect.top <= -75 or bird_rect.bottom >= 650:
            hit_sound.play()
            return False
    return True
# Ham lam hieu ung xoay cho chim
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1, -bird_movement*2.5, 1)
    return new_bird
# Tao bird dap canh
def bird_animation() :
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect
# Hien thi diem
def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render("Score : " + str(int(score)),True, (255, 255, 255)) #set font chu len game
        score_rect = score_surface.get_rect(center = (218, 100))
        screen.blit(score_surface, score_rect)
    if game_state == 'main_over': #Khi game ket thuc
        score_surface = game_font.render("Score : " + str(int(score)),True, (255, 255, 255)) #set font chu len game
        score_rect = score_surface.get_rect(center = (218, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score : {int(high_score)}',True, (255, 255, 255)) #set font chu len game
        high_score_rect = high_score_surface.get_rect(center = (218, 630))
        screen.blit(high_score_surface, high_score_rect)
# Cap nhaat diem cao nhat
def update_high_score(score, high_score):
    if score > high_score:
        high_score = score
    return score

#Chinh sua am thanh thich hop
pygame.mixer.pre_init(frequency=44100, size = -16, channels = 2, buffer = 512) 
#Khoi tao pygame 
pygame.init()
# Tao man hinh chinh
screen = pygame.display.set_mode((432,768))
# Set FPS cho game
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.TTF', 40) # Font(ten font chu danh rieng cho game , size)
# Bien flag biet la game chajy
game_active = True
score = 0 #Diem
high_score = 0 #diem cao nhat
# tao bien trong luc choi
gravity = 0.20  #Luc hut trai dat
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
bird_mid = pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
bird_down = pygame.image.load('assets/yellowbird-downflap.png').convert_alpha()
bird_up = pygame.image.load('assets/yellowbird-upflap.png').convert_alpha()
bird_list = [bird_down, bird_mid, bird_up] #0 1 2
bird_index = 0
bird = bird_list[bird_index]
bird = pygame.transform.scale2x(bird) # lam cho bird x 2
bird_rect = bird.get_rect(center = (100,384)) #TAo 1 cai hinh chu nhat cho bird
    #Tao timer cho bird
birdflap = pygame.USEREVENT + 1 # USEREVENT + 1 laf cai thu 2 trong code 
pygame.time.set_timer(birdflap, 200)
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
# Screen Over
game_over_surface = pygame.image.load('assets/message.png').convert_alpha()
game_over_surface = pygame.transform.scale2x(game_over_surface) # lam cho bird x 2
game_over_rect = game_over_surface.get_rect(center = (218, 400))
# sound ............ Chen am thanh
flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
countDown_score_sound = 100
# Tao chuoi vong lap game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Tao nut thoat cho game
            pygame.quit()
            sys.exit()  #Thoat he thong
        if event.type == pygame.KEYDOWN: #Khi co phim bi nhan thi chim bay
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement =-8
                flap_sound.play() # Lenh chay tien trong tro choi
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                #Reset B & P
                pipe_list.clear() #Xoa ong, neu khong xoa khi bat dau lai bij chem ong
                bird_rect.center = (100, 384)
                bird_movement = 0
                score = 0 #set lai diem khi thua

        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
            # print(create_pipe)
        if event.type == birdflap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird, bird_rect = bird_animation()

    screen.blit(bg,(0, 0)) #set toa do 0, 0
    
    #Neu game dang chay thi chim va ong
    if game_active:
        #con chim di chuyen thi cang rot
        bird_movement += gravity
        bird_rect.centery += bird_movement
        ratated_bird = rotate_bird(bird) #Lam cho chim chuyen dong
        screen.blit(ratated_bird,bird_rect) # da set hinh chu nhat cho con chim
        

        #pipe
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        # Chay va cham cua chim
        game_active = check_collosion(pipe_list)
        score += 0.01
        # hien thi diem
        score_display('main_game')
        #Am thanh diem
        countDown_score_sound -= 1
        if countDown_score_sound < 1:
            score_sound.play()
            countDown_score_sound = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_high_score(score, high_score)
        score_display('main_over')

    #San
    floor_x_position -= 1 # NO di chuyen
    draw_floor() #goi ham
    if floor_x_position <= -432:
        floor_x_position = 0

    
    pygame.display.update()
    clock.tick(120) #FPS = 120            