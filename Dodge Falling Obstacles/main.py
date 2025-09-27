from machine import Pin, ADC, I2C
import ssd1306
import utime
import random

# Joystick setup
xJoy = ADC(Pin(26))  # VRx
yJoy = ADC(Pin(27))  # VRy

# Display setup (128x64 OLED)
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Game variables
player_x = 60
player_y = 50
obstacles = []
score = 0
game_over = False

def spawn_obstacle():
    return [random.randint(0, 120), 0]  # [x, y]

def draw_game():
    oled.fill(0)
    oled.text("Score: {}".format(score), 0, 0)
    oled.fill_rect(player_x, player_y, 8, 8, 1)
    for obs in obstacles:
        oled.fill_rect(obs[0], obs[1], 8, 8, 1)
    if game_over:
        oled.text("GAME OVER", 30, 30)
    oled.show()

# Main game loop
while True:
    if not game_over:
        # Move player with joystick
        xVal = xJoy.read_u16()
        yVal = yJoy.read_u16()
        if xVal < 20000: player_x -= 2
        if xVal > 45000: player_x += 2
        if yVal < 20000: player_y -= 2
        if yVal > 45000: player_y += 2

        # Keep inside screen
        player_x = max(0, min(120, player_x))
        player_y = max(8, min(56, player_y))

        # Spawn new obstacles
        if random.randint(0, 20) == 0:
            obstacles.append(spawn_obstacle())

        # Move obstacles
        for obs in obstacles:
            obs[1] += 2

        # Remove off-screen obstacles
        obstacles = [obs for obs in obstacles if obs[1] < 64]

        # Collision detection
        for obs in obstacles:
            if (player_x < obs[0] + 8 and player_x + 8 > obs[0] and
                player_y < obs[1] + 8 and player_y + 8 > obs[1]):
                game_over = True

        # Score update
        score += 1

    draw_game()
    utime.sleep(0.05)
