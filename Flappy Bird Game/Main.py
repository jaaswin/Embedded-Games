from machine import Pin, I2C
import ssd1306
import utime
from i2c_lcd import I2cLcd
import random

# --- I2C for both displays ---
i2c = I2C(0, scl=Pin(1), sda=Pin(0))

# OLED setup
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# LCD setup (change 0x27 if needed)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Push button setup
button = Pin(14, Pin.IN, Pin.PULL_UP)

# Bird settings
bird_y = 30
velocity = 0
gravity = 0.5
jump_strength = -4

# Pipe settings
pipe_x = 128
pipe_gap = 20
pipe_width = 15
pipe_height = random.randint(10, 40)

# Score
score = 0
game_over = False

def draw_bird():
    oled.fill_rect(10, int(bird_y), 5, 5, 1)

def draw_pipe():
    oled.fill_rect(pipe_x, 0, pipe_width, pipe_height, 1)
    oled.fill_rect(pipe_x, pipe_height + pipe_gap, pipe_width, 64, 1)

def check_collision():
    global game_over
    if bird_y <= 0 or bird_y >= 64:
        game_over = True
    if 10 + 5 > pipe_x and 10 < pipe_x + pipe_width:
        if bird_y < pipe_height or bird_y > pipe_height + pipe_gap:
            game_over = True

# --- Game Loop ---
while True:
    if not game_over:
        # Bird jump
        if button.value() == 0:
            velocity = jump_strength

        # Physics
        velocity += gravity
        bird_y += velocity

        # Move pipe
        pipe_x -= 2
        if pipe_x < -pipe_width:
            pipe_x = 128
            pipe_height = random.randint(10, 40)
            score += 1

        # Collision
        check_collision()

        # Draw
        oled.fill(0)
        draw_bird()
        draw_pipe()
        oled.text("Score: {}".format(score), 50, 0)
        oled.show()

        # LCD updates
        lcd.clear()
        lcd.putstr("Score: {}".format(score))

        utime.sleep(0.05)
    else:
        oled.fill(0)
        oled.text("GAME OVER", 20, 30)
        oled.show()

        lcd.clear()
        lcd.putstr("Game Over!\nScore: {}".format(score))
        break
