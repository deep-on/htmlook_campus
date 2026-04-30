# 거북이로 별 그리기 — 10각 별 (각도 72도)
# 4-6 학년용 첫 lesson

import turtle

t = turtle.Turtle()
t.speed(3)

# for 반복문 10번 — 한 변 그리고 72도 회전
for i in range(10):
    t.forward(120)   # 앞으로 120 픽셀
    t.right(72)      # 72도 회전 (10각 별)

turtle.done()
