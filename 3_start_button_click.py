import pygame
from pygame import display


# 시작화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60,5)

# 게임화면 보여주기
def display_game_screen():
    print("Game start")

# pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True

# 초기화
pygame.init()
screen_width = 1200 # 가로
screen_hight = 720 # 세로
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Memory Game")

# 시작버튼
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120, screen_hight - 120)

# 색
BLACK = (0,0,0)
WHITE = (255,255,255)

# 게임 시작여부
start = False

# 게임 루프
running = True # 게임이 실행중인가?
while running:
    click_pos = None

    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    # 화면 전체를 까맣게
    screen.fill(BLACK)

    if start :
        # 게임 화면 표시
        display_game_screen()
    else:
        # 시작화면
        display_start_screen()

    if click_pos:
        check_buttons(click_pos)

    # 화면 업데이트
    pygame.display.update()



pygame.quit()