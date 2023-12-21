import pygame
import os
import random

GAMESTATE = True
GAMESPEED = 10  # running speed
FRAME = 0  # frame
SCORE = 0  # score
HISTORY = 0  # highest score
GROUND = 383  # 地面坐标
NIGHT = False
jump_frame = 1
jump_speed = 0
gravity = 0  # 重力
max_jump_frame = 54
rgb = 0
# init window
pygame.init()
SCREEN_WIDTH = pygame.display.Info().current_w
WINDOW = pygame.display.set_mode((1280, 540), pygame.HWACCEL)
img_title = pygame.image.load(os.path.join("images/others", "img_title.png"))
pygame.display.set_caption('Chrome dino')
pygame.display.set_icon(img_title)
# load resources
img_prestart = pygame.image.load(os.path.join("images/dino", "prestart.png"))
img_running1 = pygame.image.load(os.path.join("images/dino", "dinorun1.png"))
img_running2 = pygame.image.load(os.path.join("images/dino", "dinorun2.png"))
img_ducking1 = pygame.image.load(os.path.join("images/dino", "dinoduck1.png"))
img_ducking2 = pygame.image.load(os.path.join("images/dino", "dinoduck2.png"))
img_jumping = pygame.image.load(os.path.join("images/dino", "dinojump.png"))
img_fail = pygame.image.load(os.path.join("images/dino", "dinofail.png"))
img_fail_n = pygame.image.load(os.path.join("images/dino", "dinofail_n.png"))
img_cactus1 = pygame.image.load(os.path.join("images/obstacles", "cactus1.png"))
img_cactus2 = pygame.image.load(os.path.join("images/obstacles", "cactus2.png"))
img_cactus3 = pygame.image.load(os.path.join("images/obstacles", "cactus3.png"))
img_cactus4 = pygame.image.load(os.path.join("images/obstacles", "cactus4.png"))
img_cactus5 = pygame.image.load(os.path.join("images/obstacles", "cactus5.png"))
img_cactus6 = pygame.image.load(os.path.join("images/obstacles", "cactus6.png"))
img_bird1 = pygame.image.load(os.path.join("images/obstacles", "bird1.png"))
img_bird2 = pygame.image.load(os.path.join("images/obstacles", "bird2.png"))
img_cloud = pygame.image.load(os.path.join("images/backgrounds", "cloud.png"))
img_star1 = pygame.image.load(os.path.join("images/backgrounds", "star1.png"))
img_star2 = pygame.image.load(os.path.join("images/backgrounds", "star2.png"))
img_star3 = pygame.image.load(os.path.join("images/backgrounds", "star3.png"))
img_moon1 = pygame.image.load(os.path.join("images/backgrounds", "moon1.png"))
img_moon2 = pygame.image.load(os.path.join("images/backgrounds", "moon2.png"))
img_moon3 = pygame.image.load(os.path.join("images/backgrounds", "moon3.png"))
img_moon4 = pygame.image.load(os.path.join("images/backgrounds", "moon4.png"))
img_moon5 = pygame.image.load(os.path.join("images/backgrounds", "moon5.png"))
img_moon6 = pygame.image.load(os.path.join("images/backgrounds", "moon6.png"))
img_moon7 = pygame.image.load(os.path.join("images/backgrounds", "moon7.png"))
img_road = pygame.image.load(os.path.join("images/backgrounds", "road.png"))
img_gameover = pygame.image.load(os.path.join("images/others", "gameover.png"))
img_restart = pygame.image.load(os.path.join("images/others", "restart.png"))
img_gameover_n = pygame.image.load(os.path.join("images/others", "gameover_n.png"))
img_restart_n = pygame.image.load(os.path.join("images/others", "restart_n.png"))
img_0 = pygame.image.load(os.path.join("images/others", "img_0.png"))
img_1 = pygame.image.load(os.path.join("images/others", "img_1.png"))
img_2 = pygame.image.load(os.path.join("images/others", "img_2.png"))
img_3 = pygame.image.load(os.path.join("images/others", "img_3.png"))
img_4 = pygame.image.load(os.path.join("images/others", "img_4.png"))
img_5 = pygame.image.load(os.path.join("images/others", "img_5.png"))
img_6 = pygame.image.load(os.path.join("images/others", "img_6.png"))
img_7 = pygame.image.load(os.path.join("images/others", "img_7.png"))
img_8 = pygame.image.load(os.path.join("images/others", "img_8.png"))
img_9 = pygame.image.load(os.path.join("images/others", "img_9.png"))
img_hi = pygame.image.load(os.path.join("images/others", "img_hi.png"))
snd_press = pygame.mixer.Sound(os.path.join("sounds", "button-press.mp3"))
snd_fail = pygame.mixer.Sound(os.path.join("sounds", "hit.mp3"))
snd_reach_score = pygame.mixer.Sound(os.path.join("sounds", "score-reached.mp3"))


class DinoSaur:
    def __init__(self, X):
        self.X = X
        self.Y = GROUND
        self.length = 75
        self.height = 92
        self.jumping = False
        self.ducking = False
        self.dropping = False
        self.bigjump = False

    def show(self):
        if FRAME % 20 < 10:
            index = 1
        else:
            index = 2
        if self.ducking:
            index += 2
        if self.jumping:
            index += 4
        match index:
            case 1:
                WINDOW.blit(img_running1, convert(self.X, self.Y, 92))
            case 2:
                WINDOW.blit(img_running2, convert(self.X, self.Y, 92))
            case 3:
                WINDOW.blit(img_ducking1, convert(self.X, self.Y, 56))
            case 4:
                WINDOW.blit(img_ducking2, convert(self.X, self.Y, 56))
            case _:
                WINDOW.blit(img_jumping, convert(self.X, self.Y, 92))


class Obstacle:
    def __init__(self):
        self.type = 0
        self.X = 0
        self.Y = 0
        self.length = 0
        self.height = 0
        self.speed = GAMESPEED

    def update(self, another):
        self.X = another.X + random.randrange(1250, 3000)
        self.type = random.randrange(1, 9)
        # 鸟的速度和高度随机
        if self.type > 6:
            self.Y = GROUND - random.randrange(0, 150)
            self.speed = GAMESPEED + random.randrange(0, GAMESPEED // 4)
        else:
            self.Y = GROUND
        match self.type:
            case 1:
                self.length = 30
                self.height = 71  # 仙人掌1
            case 2:
                self.length = 65
                self.height = 71  # 仙人掌2
            case 3:
                self.length = 100
                self.height = 71  # 仙人掌3
            case 4:
                self.length = 45
                self.height = 98  # 仙人掌4
            case 5:
                self.length = 100
                self.height = 98  # 仙人掌5
            case 6:
                self.length = 145
                self.height = 96  # 仙人掌6
            case 7:
                self.length = 70
                self.height = 77  # 鸟
            case 8:
                self.length = 70
                self.height = 77  # 鸟
            case 9:
                self.length = 70
                self.height = 77  # 鸟

    def show(self):
        self.X -= self.speed
        match self.type:
            case 1:
                WINDOW.blit(img_cactus1, convert(self.X, self.Y, 71))  # 仙人掌1
            case 2:
                WINDOW.blit(img_cactus2, convert(self.X, self.Y, 71))  # 仙人掌2
            case 3:
                WINDOW.blit(img_cactus3, convert(self.X, self.Y, 71))  # 仙人掌3
            case 4:
                WINDOW.blit(img_cactus4, convert(self.X, self.Y, 98))  # 仙人掌4
            case 5:
                WINDOW.blit(img_cactus5, convert(self.X, self.Y, 98))  # 仙人掌5
            case 6:
                WINDOW.blit(img_cactus6, convert(self.X, self.Y, 96))  # 仙人掌6
            case 7:
                self.bird()  # 鸟
            case 8:
                self.bird()  # 鸟
            case 9:
                self.bird()  # 鸟

    def bird(self):
        if FRAME % 20 < 10:
            WINDOW.blit(img_bird1, convert(self.X, self.Y, 77))
        else:
            WINDOW.blit(img_bird2, convert(self.X, self.Y, 77))

    def hitbox(self, dino):
        return dino.X + dino.length > self.X \
            and dino.X < self.X + self.length \
            and dino.Y > self.Y - self.height \
            and dino.Y - dino1.height < self.Y

    def change_speed(self, speed):
        self.speed = speed


class Background:
    def __init__(self, speed, X_min, X_max, Y_min, Y_max, imgs):
        self.X = -51
        self.Y = -2
        self.speed = speed
        self.X_min = X_min
        self.X_max = X_max
        self.Y_min = Y_min
        self.Y_max = Y_max
        self.imgs = imgs
        self.img = random.choice(imgs)

    def show(self, another):
        self.X -= self.speed
        if self.X < -5:
            self.X = another.X + random.randrange(self.X_min, self.X_max)
            self.Y = random.randrange(self.Y_min, self.Y_max)
            self.img = random.choice(self.imgs)
        WINDOW.blit(self.img, (self.X, self.Y))

    def change_speed(self, speed):
        self.speed = speed


class Cloud(Background):
    def __init__(self):
        speed = GAMESPEED / 2
        X_min = 500
        X_max = 1000
        Y_min = 100
        Y_max = 250
        imgs = [img_cloud]
        super().__init__(speed, X_min, X_max, Y_min, Y_max, imgs)


class Star(Background):
    def __init__(self):
        speed = GAMESPEED / 5
        X_min = 250
        X_max = 750
        Y_min = 50
        Y_max = 200
        imgs = [img_star1, img_star2, img_star3]
        super().__init__(speed, X_min, X_max, Y_min, Y_max, imgs)


class Moon(Background):
    def __init__(self):
        speed = GAMESPEED / 10
        X_min = 1280
        X_max = 1281
        Y_min = 75
        Y_max = 76
        imgs = [img_moon1, img_moon2, img_moon3, img_moon4, img_moon5, img_moon6, img_moon7]
        super().__init__(speed, X_min, X_max, Y_min, Y_max, imgs)
        self.current_img = 1

    def show(self, another):
        self.X -= self.speed
        if not NIGHT:
            self.current_img = (self.current_img + 1) % len(self.imgs)
            self.X = 1280
            self.Y = 75
        self.img = self.imgs[self.current_img]
        WINDOW.blit(self.img, (self.X, self.Y))


class Road:
    def __init__(self):
        self.X = 0
        self.Y = GROUND - 22

    def show(self):
        if self.X < -2560:
            self.X = 0
        self.X -= GAMESPEED
        WINDOW.blit(img_road, (self.X, self.Y))


# 创建实例
dino1 = DinoSaur(10)
obstacle1 = Obstacle()
obstacle2 = Obstacle()
cloud1 = Cloud()
cloud2 = Cloud()
cloud3 = Cloud()
cloud4 = Cloud()
star1 = Star()
star2 = Star()
star3 = Star()
star4 = Star()
moon = Moon()
road1 = Road()


def sync_speed():
    if obstacle1.type > 6:
        obstacle1.change_speed(GAMESPEED + random.randrange(0, GAMESPEED // 4))
    else:
        obstacle1.change_speed(GAMESPEED)
    if obstacle2.type > 6:
        obstacle2.change_speed(GAMESPEED + random.randrange(0, GAMESPEED // 4))
    else:
        obstacle2.change_speed(GAMESPEED)
    cloud1.change_speed(GAMESPEED / 4)
    cloud2.change_speed(GAMESPEED / 4)
    cloud3.change_speed(GAMESPEED / 4)
    cloud4.change_speed(GAMESPEED / 4)
    star1.change_speed(GAMESPEED / 10)
    star2.change_speed(GAMESPEED / 10)
    star3.change_speed(GAMESPEED / 10)
    star4.change_speed(GAMESPEED / 10)
    moon.change_speed(GAMESPEED / 20)


# 渐变反转颜色
def reverse_color():
    global rgb
    if SCORE % 1000 > 950:
        rgb -= 1
    else:
        if rgb < 255:
            rgb += 1
    pixels = pygame.surfarray.pixels2d(WINDOW)
    pixels ^= int(('{:02X}' * 3).format(rgb, rgb, rgb), 16)
    del pixels


def convert(X, Y, img_height):
    """仅用于恐龙和障碍，转换图像绘制起点为左下角"""
    return X, Y - img_height


# 获取历史最高分
def get_history_score():
    try:
        with open("record.txt", "r") as f:
            score = int(f.read().strip())
        return score
    except FileNotFoundError:
        with open("record.txt", "w") as f:
            f.write("0")
        return 0


# 显示分数
def show_score(score, hi_score):
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
    # 满足条件时score向下取整百
    if score > 100 and GAMESTATE is True:
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

    WINDOW.blit(img_hi, (913, 50))
    WINDOW.blit(images[0], (975, 50))
    WINDOW.blit(images[1], (1000, 50))
    WINDOW.blit(images[2], (1025, 50))
    WINDOW.blit(images[3], (1050, 50))
    WINDOW.blit(images[4], (1075, 50))
    # 满足条件时闪烁
    if not (SCORE > 100 and GAMESTATE
            and (0 < SCORE % 100 <= 5
                 or 10 < SCORE % 100 <= 15
                 or 20 < SCORE % 100 <= 25)):
        WINDOW.blit(images[5], (1125, 50))
        WINDOW.blit(images[6], (1150, 50))
        WINDOW.blit(images[7], (1175, 50))
        WINDOW.blit(images[8], (1200, 50))
        WINDOW.blit(images[9], (1225, 50))


# 启动动画
def start_animation():
    clock = pygame.time.Clock()
    start = False
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render("Press space to play", True, (0, 0, 0))
    wink = 0
    global jump_frame
    jump_frame = 54
    while jump_frame > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        clock.tick(100)  # FPS
        WINDOW.fill((255, 255, 255))
        WINDOW.blit(img_road, (road1.X, road1.Y))
        pygame.draw.rect(WINDOW, (255, 255, 255), pygame.Rect(100, 0, 1280, 540))  # 用白色矩形填充右侧屏幕
        INPUT = pygame.key.get_pressed()
        # 等待，直到按下空格
        if INPUT[pygame.K_SPACE]:
            start = True
        if start is True:
            jump_frame -= 1
            dino1.Y = GROUND - (2100 * jump_frame / 100 - (8000 * jump_frame ** 2) / 20000)  # 跳跃动画
        else:
            WINDOW.blit(text, (575, 242))
        dino1.show()
        # 眨眼 
        if 800 < wink % 1000 <= 830:
            pygame.draw.rect(WINDOW, (41, 41, 41), pygame.Rect(55, 298, 8, 8))
        pygame.display.flip()
        wink += 1
    for i in range(50):
        clock.tick(200)
        WINDOW.fill((255, 255, 255))
        WINDOW.blit(img_road, (road1.X, road1.Y))
        dino1.show()
        pygame.draw.rect(WINDOW, (255, 255, 255), pygame.Rect(100 + 25 * i, 0, 1280, 540))  # 白色矩形向右移
        pygame.display.flip()
    obstacle1.update(obstacle2)
    obstacle2.update(obstacle1)


# 游戏结束界面
def gameover():
    global GAMESTATE
    global GAMESPEED
    global NIGHT
    global FRAME
    # 昼夜加载不同图片
    if NIGHT:
        WINDOW.blit(img_fail_n, convert(dino1.X, dino1.Y, 92))
        WINDOW.blit(img_gameover_n, (435, 175))
        WINDOW.blit(img_restart_n, (601, 275))
    else:
        WINDOW.blit(img_fail, convert(dino1.X, dino1.Y, 92))
        WINDOW.blit(img_gameover, (435, 175))
        WINDOW.blit(img_restart, (601, 275))
    pygame.display.flip()
    pygame.mixer.Sound.play(snd_fail)
    if SCORE > HISTORY:
        with open("record.txt", "w") as file:
            file.write(str(SCORE))
    FRAME = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        clock = pygame.time.Clock()
        clock.tick(100)  # FPS
        INPUT = pygame.key.get_pressed()
        # 重新开始
        if INPUT[pygame.K_SPACE] is True:
            GAMESTATE = True
            GAMESPEED = 15
            obstacle1.update(obstacle2)
            obstacle2.update(obstacle1)
            break


def menu():
    # 游戏初始化
    global GAMESTATE
    global HISTORY
    HISTORY = get_history_score()
    WINDOW.fill((255, 255, 255))
    pygame.display.flip()
    dino1.jumping = True
    start_animation()
    obstacle1.update(obstacle2)
    obstacle2.update(obstacle1)
    obstacle1.X = 2500
    obstacle2.X = 4000
    # 等待按下空格
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        HISTORY = get_history_score()
        while GAMESTATE:
            clock = pygame.time.Clock()
            clock.tick(100)  # FPS
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

    # 姿态控制
    INPUT = pygame.key.get_pressed()
    # 按下空格或上方向键，并且未处于蹲下或跳跃状态，起跳
    if (INPUT[pygame.K_SPACE] or INPUT[pygame.K_UP]) \
            and not (dino1.ducking or dino1.jumping):
        pygame.mixer.Sound.play(snd_press)
        dino1.jumping = True
        max_jump_frame = 38
        gravity = 8000
        jump_speed = 1500
        jump_frame = max_jump_frame
    # 28 < jump_frame < 30时未松开空格或上方向键，且没有处于躲避和大跳状态，切换小跳为大跳
    elif (INPUT[pygame.K_SPACE] or INPUT[pygame.K_UP]) \
            and not (jump_frame > 30 or jump_frame < 28 or dino1.bigjump or dino1.ducking):
        dino1.bigjump = True
        max_jump_frame = 53
        gravity = 8000
        jump_speed = 2150
        jump_frame += 18
    # 快速下降或蹲下
    dino1.ducking = False
    if INPUT[pygame.K_DOWN]:
        if dino1.jumping:
            dino1.dropping = True
        else:
            dino1.ducking = True
    # 更新恐龙Y坐标
    if jump_frame >= 0:
        # 状态为drop时不使用公式计算高度，以每帧30像素快速落地
        if dino1.dropping:
            dino1.Y += 30
            if dino1.Y > GROUND:
                jump_frame = 0
                dino1.Y = GROUND
        else:
            dino1.Y = GROUND - (jump_speed * jump_frame / 100 - (gravity * jump_frame ** 2) / 20000)
        jump_frame -= 1
    else:
        # 复原状态
        dino1.jumping = False
        dino1.bigjump = False
        dino1.dropping = False
    if dino1.ducking:
        dino1.height = 55
    else:
        dino1.height = 92

    # 障碍更新
    if obstacle1.X <= -100:
        obstacle1.update(obstacle2)
        sync_speed()
    if obstacle2.X <= -100:
        obstacle2.update(obstacle1)
        sync_speed()

    # 碰撞检测
    if obstacle1.hitbox(dino1) or obstacle2.hitbox(dino1):
        GAMESTATE = False

    # 显示物体
    if 700 <= SCORE % 1000 <= 999:
        moon.show(moon)
        star1.show(star4)
        star2.show(star1)
        star3.show(star2)
        star4.show(star3)
        NIGHT = True
    else:
        NIGHT = False
    road1.show()
    cloud1.show(cloud4)
    cloud2.show(cloud1)
    cloud3.show(cloud2)
    cloud4.show(cloud3)
    obstacle1.show()
    obstacle2.show()
    dino1.show()
    show_score(SCORE, HISTORY)
    if NIGHT:
        reverse_color()
    pygame.display.flip()

    # 速度调整
    if FRAME == 0:
        GAMESPEED = 10
        sync_speed()
    if FRAME == 800:
        GAMESPEED = 14
        sync_speed()
    if FRAME == 1600:
        GAMESPEED = 17
        sync_speed()
    if FRAME == 2500:
        GAMESPEED = 20
        sync_speed()
    if SCORE % 100 == 99:
        pygame.mixer.Sound.play(snd_reach_score)

    FRAME += 1
    SCORE = int(FRAME / 5)


if __name__ == "__main__":
    menu()
