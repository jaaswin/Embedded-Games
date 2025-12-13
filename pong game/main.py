from machine import Pin, I2C
import time
from sh1107_128 import SH1107

# I2C setup
i2c = I2C(0, scl=Pin(9), sda=Pin(8))
oled = SH1107(128, 128, i2c)

# Buttons
left_btn = Pin(14, Pin.IN, Pin.PULL_UP)
right_btn = Pin(15, Pin.IN, Pin.PULL_UP)

# Paddle settings
paddle_h = 24
paddle_w = 4
left_y = 52
right_y = 52

# Ball settings
ball_x = 64
ball_y = 64
dx = 3
dy = 2

while True:
    oled.fill(0)

    # Paddle control
    if not left_btn.value():
        left_y -= 4
    else:
        left_y += 2

    if not right_btn.value():
        right_y -= 4
    else:
        right_y += 2

    # Keep paddles on screen
    left_y = max(0, min(128 - paddle_h, left_y))
    right_y = max(0, min(128 - paddle_h, right_y))

    # Move ball
    ball_x += dx
    ball_y += dy

    # Wall collision
    if ball_y <= 0 or ball_y >= 127:
        dy = -dy

    # Paddle collision
    if ball_x <= 6 and left_y <= ball_y <= left_y + paddle_h:
        dx = -dx

    if ball_x >= 118 and right_y <= ball_y <= right_y + paddle_h:
        dx = -dx

    # Game over
    if ball_x < 0 or ball_x > 128:
        oled.fill(0)
        oled.text("GAME OVER", 32, 60)
        oled.show()
        break

    # Draw paddles
    oled.fill_rect(2, left_y, paddle_w, paddle_h, 1)
    oled.fill_rect(122, right_y, paddle_w, paddle_h, 1)

    # Draw center line
    for y in range(0, 128, 6):
        oled.pixel(64, y, 1)

    # Draw ball
    oled.pixel(ball_x, ball_y, 1)

    oled.show()
    time.sleep(0.03)
