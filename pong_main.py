from pong_helper import *


ans = input('Single player: (s) || Two players (t)      ')
while True:
    if ans.lower() == 's':
        spl = True
        break
    elif ans.lower() == 't':
        spl = False
        break
    else:
        print("Invalid choice, try again: ")
        ans = input('Single player: (s) || Two players (t)      ')


def draw_win(char1, char2, ball):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, char1)
    pygame.draw.rect(WIN, BLACK, char2)
    pygame.draw.rect(WIN, BLACK, ball)

    pygame.display.update()


def main(single_player):
    run = True
    char1 = pygame.Rect(210, HEIGHT - 50, 50, 20)
    char2 = pygame.Rect(210, 50, 50, 20)
    ball = pygame.Rect(210, 200, 7, 7)
    while run:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_win(char1, char2, ball)
        movement(char1, char2)
        handle_ball(ball, char1, char2)
        if single_player:
            run_ai1(char1, ball)


if __name__ == '__main__':
    main(spl)


