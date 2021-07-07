import pygame

# 초기화
pygame.init()
screen_width = 1200 # 가로
screen_hight = 720 # 세로
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Memory Game")

# 게임 루프
running = True # 게임이 실행중인가?
while running:
    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()