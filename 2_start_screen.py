import pygame


# 시작화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60,5)

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

# 게임 루프
running = True # 게임이 실행중인가?
while running:
    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 전체를 까맣게
    screen.fill(BLACK)

    # 시작화면
    display_start_screen()

    # 화면 업데이트
    pygame.display.update()

pygame.quit()