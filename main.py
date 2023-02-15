import pygame
import os
import random
GAMESTATE=True       
GAMESPEED=20 # running speed
FRAME=0 # frame
SCORE=0 # score
HISTORY=0 # highest score
GROUND=766 #地面坐标
NIGHT=False
jump_frame=1
jump_speed=0
gravity=0 #重力
max_jump_frame=54
rgb=0
# init window
pygame.init()
SCREEN_WIDTH= pygame.display.Info().current_w
if SCREEN_WIDTH < 2560:
    DISPLAY_WINDOW = pygame.display.set_mode((1920,800),pygame.HWACCEL)
else:
    DISPLAY_WINDOW = pygame.display.set_mode((2560,1080),pygame.HWACCEL)
WINDOW = pygame.Surface((2560, 1080))
img_title=pygame.image.load(os.path.join("images/others", "img_title.png"))
pygame.display.set_caption('Chrome dino')
pygame.display.set_icon(img_title)
# load resources
img_prestart=pygame.image.load(os.path.join("images/dino", "prestart.png"))
img_running1=pygame.image.load(os.path.join("images/dino", "dinorun1.png"))
img_running2=pygame.image.load(os.path.join("images/dino", "dinorun2.png"))
img_ducking1=pygame.image.load(os.path.join("images/dino", "dinoduck1.png"))
img_ducking2=pygame.image.load(os.path.join("images/dino", "dinoduck2.png"))
img_jumping=pygame.image.load(os.path.join("images/dino", "dinojump.png"))
img_fail=pygame.image.load(os.path.join("images/dino", "dinofail.png"))
img_fail_n=pygame.image.load(os.path.join("images/dino", "dinofail_n.png"))
img_cactus1=pygame.image.load(os.path.join("images/obstacles", "cactus1.png"))
img_cactus2=pygame.image.load(os.path.join("images/obstacles", "cactus2.png"))
img_cactus3=pygame.image.load(os.path.join("images/obstacles", "cactus3.png"))
img_cactus4=pygame.image.load(os.path.join("images/obstacles", "cactus4.png"))
img_cactus5=pygame.image.load(os.path.join("images/obstacles", "cactus5.png"))
img_cactus6=pygame.image.load(os.path.join("images/obstacles", "cactus6.png"))
img_bird1=pygame.image.load(os.path.join("images/obstacles", "bird1.png"))
img_bird2=pygame.image.load(os.path.join("images/obstacles", "bird2.png"))
img_cloud=pygame.image.load(os.path.join("images/backgrounds", "cloud.png"))
img_star1=pygame.image.load(os.path.join("images/backgrounds", "star1.png"))
img_star2=pygame.image.load(os.path.join("images/backgrounds", "star2.png"))
img_star3=pygame.image.load(os.path.join("images/backgrounds", "star3.png"))
img_moon1=pygame.image.load(os.path.join("images/backgrounds", "moon1.png"))
img_moon2=pygame.image.load(os.path.join("images/backgrounds", "moon2.png"))
img_moon3=pygame.image.load(os.path.join("images/backgrounds", "moon3.png"))
img_moon4=pygame.image.load(os.path.join("images/backgrounds", "moon4.png"))
img_moon5=pygame.image.load(os.path.join("images/backgrounds", "moon5.png"))
img_moon6=pygame.image.load(os.path.join("images/backgrounds", "moon6.png"))
img_moon7=pygame.image.load(os.path.join("images/backgrounds", "moon7.png"))
img_road=pygame.image.load(os.path.join("images/backgrounds", "road.png"))
img_gameover=pygame.image.load(os.path.join("images/others", "gameover.png"))
img_restart=pygame.image.load(os.path.join("images/others", "restart.png"))
img_gameover_n=pygame.image.load(os.path.join("images/others", "gameover_n.png"))
img_restart_n=pygame.image.load(os.path.join("images/others", "restart_n.png"))
img_0=pygame.image.load(os.path.join("images/others", "img_0.png"))
img_1=pygame.image.load(os.path.join("images/others", "img_1.png"))
img_2=pygame.image.load(os.path.join("images/others", "img_2.png"))
img_3=pygame.image.load(os.path.join("images/others", "img_3.png"))
img_4=pygame.image.load(os.path.join("images/others", "img_4.png"))
img_5=pygame.image.load(os.path.join("images/others", "img_5.png"))
img_6=pygame.image.load(os.path.join("images/others", "img_6.png"))
img_7=pygame.image.load(os.path.join("images/others", "img_7.png"))
img_8=pygame.image.load(os.path.join("images/others", "img_8.png"))
img_9=pygame.image.load(os.path.join("images/others", "img_9.png"))
img_hi=pygame.image.load(os.path.join("images/others", "img_hi.png"))
snd_press=pygame.mixer.Sound(os.path.join("sounds", "button-press.mp3"))
snd_fail=pygame.mixer.Sound(os.path.join("sounds", "hit.mp3"))
snd_reach_score=pygame.mixer.Sound(os.path.join("sounds", "score-reached.mp3"))

class DinoSaur:
    def __init__(self,X):
        self.X = X
        self.Y = GROUND
        self.length = 150
        self.height = 184
        self.jumping = False
        self.ducking = False
        self.dropping = False
        self.bigjump = False
    def show(self):
        if FRAME%20 < 10:
            index=1
        else:
            index=2
        if self.ducking:
            index+=2
        if self.jumping:
            index+=4
        match index:
            case 1:WINDOW.blit(img_running1, convert(self.X, self.Y, 184))
            case 2:WINDOW.blit(img_running2, convert(self.X, self.Y, 184))
            case 3:WINDOW.blit(img_ducking1, convert(self.X, self.Y, 111))
            case 4:WINDOW.blit(img_ducking2, convert(self.X, self.Y, 111))
            case _:WINDOW.blit(img_jumping,  convert(self.X, self.Y, 184))

class Obstacle:
    def __init__(self):
        self.type = 0
        self.X = 0
        self.Y = 0
        self.length = 0
        self.height = 0
        self.speed = GAMESPEED

    def update(self,another):
        self.X=another.X+random.randrange(1500,4000)
        self.type=random.randrange(1,9)
        if self.type > 6:
            self.Y = GROUND-random.randrange(0,300)
            self.speed = GAMESPEED+random.randrange(0,GAMESPEED//7)
        else:
            self.Y = GROUND
        match self.type:
            case 1: self.length=60  ; self.height=141 #仙人掌1
            case 2: self.length=130 ; self.height=141 #仙人掌2
            case 3: self.length=200 ; self.height=141 #仙人掌3
            case 4: self.length=90  ; self.height=196 #仙人掌4
            case 5: self.length=200 ; self.height=195 #仙人掌5
            case 6: self.length=290 ; self.height=192 #仙人掌6
            case 7: self.length=140 ; self.height=153 #鸟
            case 8: self.length=140 ; self.height=153 #鸟
            case 9: self.length=140 ; self.height=153 #鸟

    def show(self):
        if self.type>6:
            self.X -= self.speed
        else:
            self.X-=GAMESPEED
        match self.type:
            case 1: WINDOW.blit(img_cactus1, convert(self.X, self.Y, 141)) #仙人掌1
            case 2: WINDOW.blit(img_cactus2, convert(self.X, self.Y, 141)) #仙人掌2
            case 3: WINDOW.blit(img_cactus3, convert(self.X, self.Y, 141)) #仙人掌3
            case 4: WINDOW.blit(img_cactus4, convert(self.X, self.Y, 196)) #仙人掌4
            case 5: WINDOW.blit(img_cactus5, convert(self.X, self.Y, 195)) #仙人掌5
            case 6: WINDOW.blit(img_cactus6, convert(self.X, self.Y, 192)) #仙人掌6
            case 7: bird(self) #鸟
            case 8: bird(self) #鸟
            case 9: bird(self) #鸟

class Background:
    def __init__(self,speed,X_min,X_max,Y_min,Y_max,imgs):
        self.X=-101
        self.Y=-3
        self.speed=speed
        self.X_min=X_min
        self.X_max=X_max
        self.Y_min=Y_min
        self.Y_max=Y_max
        self.imgs=imgs
        self.img=random.choice(imgs)
    def show(self,another):
        self.X-=self.speed
        if self.X < -100:
            self.X=another.X+random.randrange(self.X_min,self.X_max)
            self.Y=random.randrange(self.Y_min,self.Y_max)
            self.img=random.choice(self.imgs)
        WINDOW.blit(self.img, (self.X,self.Y))

class Cloud(Background):
    def __init__(self):
        speed=GAMESPEED/2
        X_min=1000
        X_max=2000
        Y_min=200
        Y_max=500
        imgs=[img_cloud]
        super().__init__(speed, X_min, X_max, Y_min, Y_max, imgs)

class Star(Background):
    def __init__(self):
        speed=GAMESPEED/5
        X_min=500
        X_max=1500
        Y_min=100
        Y_max=400
        imgs = [img_star1,img_star2,img_star3]
        super().__init__(speed, X_min, X_max, Y_min, Y_max, imgs)

class Moon(Background):
    def __init__(self):
        speed=GAMESPEED/10
        X_min=2560
        X_max=2561
        Y_min=150
        Y_max=151
        imgs = [img_moon1,img_moon2,img_moon3,img_moon4,img_moon5,img_moon6,img_moon7]
        super().__init__(speed, X_min, X_max, Y_min, Y_max, imgs)
        self.current_img = 1
    def show(self):
        self.X-=self.speed
        if NIGHT == False:
            self.current_img = (self.current_img + 1) % len(self.imgs)
            self.X=2560
            self.Y=150
        self.img = self.imgs[self.current_img]
        WINDOW.blit(self.img, (self.X,self.Y))

class Road:
    def __init__(self):
        self.X=0
        self.Y=GROUND-44
    def show(self):
        if self.X < -5120:
            self.X = 0
        self.X -= GAMESPEED
        WINDOW.blit(img_road, (self.X, self.Y))
        
dino1=DinoSaur(10)
obstacle1=Obstacle()
obstacle2=Obstacle()
cloud1=Cloud()
cloud2=Cloud()
cloud3=Cloud()
cloud4=Cloud()
star1=Star()
star2=Star()
star3=Star()
star4=Star()
moon=Moon()
road1=Road()

def reverse_color():
    global rgb
    if SCORE % 1000 > 950:
        rgb-=1
    else:
        if rgb<255:
            rgb+=1
    pixels = pygame.surfarray.pixels2d(WINDOW)
    pixels ^= int(('{:02X}' * 3).format(rgb,rgb,rgb),16)
    del pixels

def bird(self):
    if FRAME%20 < 10:
        WINDOW.blit(img_bird1, convert(self.X, self.Y, 153))
    else:
        WINDOW.blit(img_bird2, convert(self.X, self.Y, 153))

def convert(X, Y, img_height):
    """仅用于恐龙和障碍，转换图像绘制起点为左下角"""
    return (X, Y - img_height)

def get_history_score():
    try:
        with open("record.txt", "r") as f:
            score = int(f.read().strip())
        return score
    except:
        with open("record.txt", "w") as f:
            f.write("0")
        return 0

def show_score(score,hi_score):
    num_images = {
        "0": img_0,
        "1": img_1,
        "2": img_2,
        "3": img_3,
        "4": img_4,
        "5": img_5,
        "6": img_6,
        "7": img_7,
        "8": img_8,
        "9": img_9
    }
    #图片闪烁效果
    if score > 100 and GAMESTATE == True:
        if score % 100 < 30:
            score = score // 100 * 100
    score_str = "{:05d}".format(score)
    hi_score_str = "{:05d}".format(hi_score)
    images = []
    for num in hi_score_str:
        image = num_images[num]
        images.append(image)
    for num in score_str:
        image = num_images[num]
        images.append(image)

    WINDOW.blit(img_hi,(1825,100))
    WINDOW.blit(images[0],(1950,100))
    WINDOW.blit(images[1],(2000,100))
    WINDOW.blit(images[2],(2050,100))
    WINDOW.blit(images[3],(2100,100))
    WINDOW.blit(images[4],(2150,100))
    if not(SCORE>100 and GAMESTATE \
        and(0 < SCORE % 100 <=5 \
        or 10 < SCORE % 100 <=15 \
        or 20 < SCORE % 100 <=25)): 
        WINDOW.blit(images[5],(2250,100))
        WINDOW.blit(images[6],(2300,100))
        WINDOW.blit(images[7],(2350,100))
        WINDOW.blit(images[8],(2400,100))
        WINDOW.blit(images[9],(2450,100))

def start_animation():
    clock = pygame.time.Clock()
    start = False
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("Press space to play", True, (0, 0, 0))
    wink=0
    global jump_frame
    jump_frame = 54
    while jump_frame>0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        clock.tick(100) #FPS
        WINDOW.fill((255, 255, 255))
        WINDOW.blit(img_road, (road1.X, road1.Y))
        pygame.draw.rect(WINDOW, (255,255,255), pygame.Rect(200, 0, 2560, 1080)) # hide road1
        INPUT = pygame.key.get_pressed()
        if INPUT[pygame.K_SPACE]:
            start = True
        if start == True:
            jump_frame -= 1
            dino1.Y=GROUND-(3000 * jump_frame / 100 - (11111*jump_frame**2)/20000) # jump animation
        else:
            WINDOW.blit(text, (1150, 485))
        dino1.show()
        # winking while waiting 
        if 800 < wink%1000 <= 830:
            pygame.draw.rect(WINDOW, (83,83,83), pygame.Rect(110, 595, 16, 16))
        SCALE_WIN = pygame.transform.scale(WINDOW, DISPLAY_WINDOW.get_size())
        DISPLAY_WINDOW.blit(SCALE_WIN, (0, 0))
        pygame.display.flip()
        wink+=1
    for i in range (50):
        clock.tick(200)
        WINDOW.fill((255, 255, 255))
        WINDOW.blit(img_road, (road1.X, road1.Y))
        dino1.show()        
        pygame.draw.rect(WINDOW, (255,255,255), pygame.Rect(200+50*i, 0, 2560, 1080)) # unhide road animation
        SCALE_WIN = pygame.transform.scale(WINDOW, DISPLAY_WINDOW.get_size())
        DISPLAY_WINDOW.blit(SCALE_WIN, (0, 0))
        pygame.display.flip()
    obstacle1.update(obstacle2)
    obstacle2.update(obstacle1)

def gameover():
    global GAMESTATE
    global GAMESPEED
    global NIGHT
    global FRAME
    if NIGHT:
        WINDOW.blit(img_fail_n, convert(dino1.X, dino1.Y, 184))
        WINDOW.blit(img_gameover_n, (871, 350))
        WINDOW.blit(img_restart_n, (1203, 550))
    else:
        WINDOW.blit(img_fail, convert(dino1.X, dino1.Y, 184))
        WINDOW.blit(img_gameover, (871, 350))
        WINDOW.blit(img_restart, (1203, 550))
    SCALE_WIN = pygame.transform.scale(WINDOW, DISPLAY_WINDOW.get_size())
    DISPLAY_WINDOW.blit(SCALE_WIN, (0, 0))
    pygame.display.flip()
    pygame.mixer.Sound.play(snd_fail)
    if SCORE > HISTORY:
        with open("record.txt", "w") as file:
            file.write(str(SCORE))
    FRAME=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        clock = pygame.time.Clock()
        clock.tick(100) #FPS
        INPUT = pygame.key.get_pressed()
        if INPUT[pygame.K_SPACE] == True:
            GAMESTATE=True
            GAMESPEED=15
            obstacle1.update(obstacle2)
            obstacle2.update(obstacle1)
            break


def hitbox(obstacle):
    return dino1.X + dino1.length > obstacle.X \
    and dino1.X < obstacle.X + obstacle.length \
    and dino1.Y > obstacle.Y - obstacle.height \
    and dino1.Y - dino1.height < obstacle.Y 

def menu():
    global GAMESTATE
    global HISTORY
    HISTORY=get_history_score()
    WINDOW.fill((255, 255, 255))
    pygame.display.flip()
    dino1.jumping = True
    start_animation()
    obstacle1.update(obstacle2)
    obstacle2.update(obstacle1)
    obstacle1.X=5000
    obstacle2.X=8000
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0        
        HISTORY=get_history_score()
        while GAMESTATE:
            clock = pygame.time.Clock()
            clock.tick(144) #FPS
            main()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
        gameover()

def main():
    WINDOW.fill((255, 255, 255))
    global max_jump_frame
    global jump_frame
    global gravity
    global jump_speed
    global SCORE
    global FRAME
    global GAMESTATE
    global GAMESPEED
    global NIGHT

    ###############姿态控制###############
    INPUT = pygame.key.get_pressed()
    #按下空格或上方向键，并且未处于蹲下或跳跃状态
    if (INPUT[pygame.K_SPACE] or INPUT[pygame.K_UP]) \
    and not (dino1.ducking or dino1.jumping):
        pygame.mixer.Sound.play(snd_press)
        dino1.jumping = True
        max_jump_frame = 38
        gravity = 13000
        jump_speed = 2500
        jump_frame = max_jump_frame
    #跳跃30帧之前按住空格和上方向键，切换小跳为大跳
    elif (INPUT[pygame.K_SPACE] or INPUT[pygame.K_UP]) \
    and not (jump_frame > 30 or jump_frame < 28 or dino1.bigjump or dino1.ducking):
        dino1.bigjump = True
        max_jump_frame = 53
        gravity = 11111
        jump_speed = 3000
        jump_frame += 18
    #快速下降或蹲下
    dino1.ducking = False
    if INPUT[pygame.K_DOWN]:
        if dino1.jumping:
            dino1.dropping = True
        else:
            dino1.ducking = True
    #更新恐龙Y坐标
    if (jump_frame >= 0):
        #状态为drop时不使用公式计算高度，以每帧30像素快速落地
        if(dino1.dropping):
            dino1.Y+=30
            if(dino1.Y>GROUND):
                jump_frame=0
                dino1.Y=GROUND
        else:
            dino1.Y=GROUND-(jump_speed * jump_frame / 100 - (gravity*jump_frame**2)/20000)
        jump_frame-=1
    else:
        #复原状态
        dino1.jumping = False
        dino1.bigjump = False
        dino1.dropping = False
    if dino1.ducking:
        dino1.height = 111
    else:
        dino1.height = 184
    ###############姿态控制###############
    # 障碍更新
    if obstacle1.X <= -200:
        obstacle1.update(obstacle2)
    if obstacle2.X <= -200:
        obstacle2.update(obstacle1)
    
    # 碰撞检测
    if hitbox(obstacle1) or hitbox (obstacle2):
        GAMESTATE=False

    # 显示
    if 700 <= SCORE % 1000 <= 999:
        moon.show()
        star1.show(star4)
        star2.show(star1)
        star3.show(star2)
        star4.show(star3)
        NIGHT=True
    else:
        NIGHT=False
    road1.show()
    cloud1.show(cloud4)
    cloud2.show(cloud1)
    cloud3.show(cloud2)
    cloud4.show(cloud3)
    obstacle1.show()
    obstacle2.show()
    dino1.show()
    show_score(SCORE,HISTORY)
    if NIGHT:
        reverse_color()
    if SCREEN_WIDTH < 2560:
        SCALE_WIN = pygame.transform.scale(WINDOW, DISPLAY_WINDOW.get_size())
        DISPLAY_WINDOW.blit(SCALE_WIN, (0, 0))
    else:
        DISPLAY_WINDOW.blit(WINDOW,(0,0))
    pygame.display.flip()

    if SCORE in range(0,160): GAMESPEED = 15
    if SCORE in range(160,320): GAMESPEED = 20
    if SCORE in range(320,500): GAMESPEED = 25
    if SCORE > 500 : GAMESPEED = 30

    if SCORE % 100 == 99:
        pygame.mixer.Sound.play(snd_reach_score)

    FRAME+=1
    SCORE=int(FRAME/5)


menu()


