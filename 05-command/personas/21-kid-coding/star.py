# 거북이로 별 그리기 — 5각 별 (각도 144도)
# 4-6 학년용 첫 lesson

import turtle

t = turtle.Turtle()
t.speed(3)

# for 반복문 5번 — 한 변 그리고 144도 회전
for i in range(5):
    t.forward(120)   # 앞으로 120 픽셀
    t.right(144)     # 144도 회전 (5각 별의 외각)

turtle.done()
