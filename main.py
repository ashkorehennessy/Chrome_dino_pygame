import pygame
import os
import random


class Gamedata:
    def __init__(self):
        self.gamestate = True
        self.gamespeed = 10  # running speed
        self.frame = 0  # frame
        self.score = 0  # score
        self.highest_score = 0  # highest score
        self.ground = 383  # 地面坐标
        self.night = False


gamedata = Gamedata()

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
        self.Y = gamedata.ground
        self.length = 75
        self.height = 92
        self.jump_speed = 1500
        self.jump_frame = 0
        self.gravity = 8000
        self.jumping = False
        self.ducking = False
        self.dropping = False
        self.standing = True
        self.bigjump = False

    def jump(self, INPUT):
        # 按下空格或上方向键，并且未处于蹲下或跳跃状态，起跳
        if (INPUT[pygame.K_SPACE] or INPUT[pygame.K_UP]) and not (self.ducking or self.jumping):
            pygame.mixer.Sound.play(snd_press)
            self.jumping = True
            self.gravity = 8000
            self.jump_speed = 1500
            self.jump_frame = 38
        # 28 < jump_frame < 30时未松开空格或上方向键，且没有处于躲避和大跳状态，切换小跳为大跳
        elif ((INPUT[pygame.K_SPACE] or INPUT[pygame.K_UP])
              and 28 < self.jump_frame < 30
              and not (self.bigjump or self.ducking)):
            self.bigjump = True
            self.gravity = 8000
            self.jump_speed = 1800
            self.jump_frame += 9

    def duck(self, INPUT):
        # 快速下降或蹲下
        self.ducking = False
        if INPUT[pygame.K_DOWN]:
            if self.jumping:
                self.dropping = True
            else:
                self.ducking = True

    def update(self):
        # 更新恐龙Y坐标
        if self.jump_frame >= 0:
            # 状态为drop时不使用公式计算高度，以每帧30像素快速落地
            if self.dropping:
                self.Y += 30
                if self.Y > gamedata.ground:
                    self.jump_frame = 0
                    self.Y = gamedata.ground
            else:
                self.Y = gamedata.ground - (
                        self.jump_speed * self.jump_frame / 100 - (self.gravity * self.jump_frame ** 2) / 20000)
            self.jump_frame -= 1
        else:
            # 复原状态
            self.jumping = False
            self.bigjump = False
            self.dropping = False
        if self.ducking:
            self.height = 55
        else:
            self.height = 92

    def show(self):
        if gamedata.frame % 20 < 10:
            index = 1
        else:
            index = 2
        if self.ducking:
            index += 2
        if self.jumping:
            index += 4
        if self.standing:
            index = 0
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
        self.speed = gamedata.gamespeed

    def update(self, another):
        self.X = another.X + random.randrange(1250, 3000)
        self.type = random.randrange(1, 9)
        # 鸟的速度和高度随机
        if self.type > 6:
            self.Y = gamedata.ground - random.randrange(0, 150)
            self.speed = gamedata.gamespeed + random.randrange(0, gamedata.gamespeed // 4)
        else:
            self.Y = gamedata.ground
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
        if gamedata.frame % 20 < 10:
            WINDOW.blit(img_bird1, convert(self.X, self.Y, 77))
        else:
            WINDOW.blit(img_bird2, convert(self.X, self.Y, 77))

    def hit(self, dino):
        return (dino.X + dino.length > self.X
                and dino.X < self.X + self.length
                and dino.Y > self.Y - self.height
                and dino.Y - dino.height < self.Y)

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
        speed = gamedata.gamespeed / 2
        X_min = 500
        X_max = 1000
        Y_min = 100
        Y_max = 250
        imgs = [img_cloud]
        super().__init__(speed, X_min, X_max, Y_min, Y_max, imgs)


class Star(Background):
    def __init__(self):
        speed = gamedata.gamespeed / 5
        X_min = 250
        X_max = 750
        Y_min = 50
        Y_max = 200
        imgs = [img_star1, img_star2, img_star3]
        super().__init__(speed, X_min, X_max, Y_min, Y_max, imgs)


class Moon(Background):
    def __init__(self):
        speed = gamedata.gamespeed / 10
        X_min = 1280
        X_max = 1281
        Y_min = 75
        Y_max = 76
        imgs = [img_moon1, img_moon2, img_moon3, img_moon4, img_moon5, img_moon6, img_moon7]
        super().__init__(speed, X_min, X_max, Y_min, Y_max, imgs)
        self.current_img = 1

    def show(self, another):
        self.X -= self.speed
        if not gamedata.night:
            self.current_img = (self.current_img + 1) % len(self.imgs)
            self.X = 1280
            self.Y = 75
        self.img = self.imgs[self.current_img]
        WINDOW.blit(self.img, (self.X, self.Y))


class Road:
    def __init__(self):
        self.X = 0
        self.Y = gamedata.ground - 22

    def show(self):
        if self.X < -2560:
            self.X = 0
        self.X -= gamedata.gamespeed
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
        obstacle1.change_speed(gamedata.gamespeed + random.randrange(0, gamedata.gamespeed // 4))
    else:
        obstacle1.change_speed(gamedata.gamespeed)
    if obstacle2.type > 6:
        obstacle2.change_speed(gamedata.gamespeed + random.randrange(0, gamedata.gamespeed // 4))
    else:
        obstacle2.change_speed(gamedata.gamespeed)
    cloud1.change_speed(gamedata.gamespeed / 4)
    cloud2.change_speed(gamedata.gamespeed / 4)
    cloud3.change_speed(gamedata.gamespeed / 4)
    cloud4.change_speed(gamedata.gamespeed / 4)
    star1.change_speed(gamedata.gamespeed / 10)
    star2.change_speed(gamedata.gamespeed / 10)
    star3.change_speed(gamedata.gamespeed / 10)
    star4.change_speed(gamedata.gamespeed / 10)
    moon.change_speed(gamedata.gamespeed / 20)


# 渐变反转颜色
def reverse_color():
    if not hasattr(reverse_color, "rgb"):
        reverse_color.rgb = 0
    if gamedata.score % 1000 > 950:
        reverse_color.rgb -= 1
    else:
        if reverse_color.rgb < 255:
            reverse_color.rgb += 1
    pixels = pygame.surfarray.pixels2d(WINDOW)
    pixels ^= int(('{:02X}' * 3).format(reverse_color.rgb, reverse_color.rgb, reverse_color.rgb), 16)
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
    if score > 100 and gamedata.gamestate is True:
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
    if not (gamedata.score > 100 and gamedata.gamestate
            and (0 < gamedata.score % 100 <= 5
                 or 10 < gamedata.score % 100 <= 15
                 or 20 < gamedata.score % 100 <= 25)):
        WINDOW.blit(images[5], (1125, 50))
        WINDOW.blit(images[6], (1150, 50))
        WINDOW.blit(images[7], (1175, 50))
        WINDOW.blit(images[8], (1200, 50))
        WINDOW.blit(images[9], (1225, 50))


# 启动动画
def start_animation(dino, road):
    clock = pygame.time.Clock()
    start = False
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render("Press space to play", True, (0, 0, 0))
    wink = 0
    # 等待按下空格
    while start is False:
        clock.tick(100)  # FPS
        WINDOW.fill((255, 255, 255))
        WINDOW.blit(img_road, (road.X, road.Y))
        pygame.draw.rect(WINDOW, (255, 255, 255), pygame.Rect(100, 0, 1280, 540))  # 用白色矩形填充右侧屏幕
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        INPUT = pygame.key.get_pressed()
        if INPUT[pygame.K_SPACE] is True:
            start = True
            dino.jump(INPUT)
        dino.show()
        WINDOW.blit(text, (575, 242))
        # 眨眼 
        if 800 < wink % 1000 <= 830:
            pygame.draw.rect(WINDOW, (41, 41, 41), pygame.Rect(55, 298, 8, 8))
        wink += 1
        pygame.display.flip()
    # 起跳
    while dino.jumping:
        clock.tick(100)
        WINDOW.fill((255, 255, 255))
        WINDOW.blit(img_road, (road.X, road.Y))
        pygame.draw.rect(WINDOW, (255, 255, 255), pygame.Rect(100, 0, 1280, 540))  # 用白色矩形填充右侧屏幕
        dino.update()
        dino.show()
        pygame.display.flip()
    # 显示道路动画
    for i in range(50):
        clock.tick(200)
        WINDOW.fill((255, 255, 255))
        WINDOW.blit(img_road, (road.X, road.Y))
        dino.show()
        pygame.draw.rect(WINDOW, (255, 255, 255), pygame.Rect(100 + 25 * i, 0, 1280, 540))  # 白色矩形向右移
        pygame.display.flip()
    dino.standing = False


# 游戏结束界面
def gameover():
    # 昼夜加载不同图片
    if gamedata.night:
        WINDOW.blit(img_fail_n, convert(dino1.X, dino1.Y, 92))
        WINDOW.blit(img_gameover_n, (435, 175))
        WINDOW.blit(img_restart_n, (601, 275))
    else:
        WINDOW.blit(img_fail, convert(dino1.X, dino1.Y, 92))
        WINDOW.blit(img_gameover, (435, 175))
        WINDOW.blit(img_restart, (601, 275))
    pygame.display.flip()
    pygame.mixer.Sound.play(snd_fail)
    if gamedata.score > gamedata.highest_score:
        with open("record.txt", "w") as file:
            file.write(str(gamedata.score))
    gamedata.frame = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        clock = pygame.time.Clock()
        clock.tick(100)  # FPS
        INPUT = pygame.key.get_pressed()
        # 重新开始
        if INPUT[pygame.K_SPACE] is True:
            gamedata.gamestate = True
            gamedata.gamespeed = 15
            obstacle1.update(obstacle2)
            obstacle2.update(obstacle1)
            break


def menu():
    # 游戏初始化
    gamedata.highest_score = get_history_score()
    WINDOW.fill((255, 255, 255))
    pygame.display.flip()
    start_animation(dino1, road1)
    obstacle1.update(obstacle2)
    obstacle2.update(obstacle1)
    obstacle1.X = 2500
    obstacle2.X = 4000
    # 等待按下空格
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        gamedata.highest_score = get_history_score()
        while gamedata.gamestate:
            clock = pygame.time.Clock()
            clock.tick(100)  # FPS
            main()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
        gameover()


def main():
    WINDOW.fill((255, 255, 255))

    # 姿态控制
    INPUT = pygame.key.get_pressed()
    dino1.jump(INPUT)
    dino1.duck(INPUT)
    dino1.update()

    # 障碍更新
    if obstacle1.X <= -100:
        obstacle1.update(obstacle2)
        sync_speed()
    if obstacle2.X <= -100:
        obstacle2.update(obstacle1)
        sync_speed()

    # 碰撞检测
    if obstacle1.hit(dino1) or obstacle2.hit(dino1):
        gamedata.gamestate = False

    # 显示物体
    if 700 <= gamedata.score % 1000 <= 999:
        moon.show(moon)
        star1.show(star4)
        star2.show(star1)
        star3.show(star2)
        star4.show(star3)
        gamedata.night = True
    else:
        gamedata.night = False
    road1.show()
    cloud1.show(cloud4)
    cloud2.show(cloud1)
    cloud3.show(cloud2)
    cloud4.show(cloud3)
    obstacle1.show()
    obstacle2.show()
    dino1.show()
    show_score(gamedata.score, gamedata.highest_score)
    if gamedata.night:
        reverse_color()
    pygame.display.flip()

    # 速度调整
    if gamedata.frame == 0:
        gamedata.gamespeed = 10
        sync_speed()
    if gamedata.frame == 800:
        gamedata.gamespeed = 14
        sync_speed()
    if gamedata.frame == 1600:
        gamedata.gamespeed = 17
        sync_speed()
    if gamedata.frame == 2500:
        gamedata.gamespeed = 20
        sync_speed()
    if gamedata.score % 100 == 99:
        pygame.mixer.Sound.play(snd_reach_score)

    gamedata.frame += 1
    gamedata.score = int(gamedata.frame / 5)


if __name__ == "__main__":
    menu()
