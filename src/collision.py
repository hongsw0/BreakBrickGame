def detect_collision(ball, paddle, bricks):
    #공이 패들과 충돌하는지 확인
    if ball.rect.colliderect(paddle.rect):
        ball.speed_y *= -1  #공의 y축 속도를 반전

    for brick in bricks:
        #벽돌의 내구도가 0보다 크고, 공이 벽돌과 충돌하는지 확인
        if brick.durability > 0 and ball.rect.colliderect(brick.rect):
            if brick.hit(): #벽돌이 맞으면 내구도를 감소시킴
                bricks.remove(brick)    #내구도가 0이 되면 벽돌을 리스트에서 제거
            ball.speed_y *= -1  #공의 y축 속도를 반전
            return True #충돌이 발생했음을 나타내기 위해 true를 반환
    return False    #충돌이 발생하지 않았음을 나타내기 위해 false를 반환