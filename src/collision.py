# 공과 벽돌 또는 패들간의 충돌 감지
# 충돌 검사
# 충돌 시 처리 관련 메서드

def detect_collision(ball, paddle, bricks):
    if ball.rect.colliderect(paddle.rect):
        ball.speed_y *= -1

    for brick in bricks:
        if brick.durability > 0 and ball.rect.colliderect(brick.rect):
            if brick.hit():
                bricks.remove(brick)
            ball.speed_y *= -1
            return True
    return False