from machine import Pin, I2C
from time import sleep
from i2c_lcd import I2cLcd
import urandom

# LCD setup
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Button
button = Pin(14, Pin.IN, Pin.PULL_UP)

# Custom characters
player = [
    0b00100,
    0b01110,
    0b00100,
    0b01110,
    0b10101,
    0b00100,
    0b01010,
    0b00000
]

obstacle = [
    0b11111,
    0b11111,
    0b11111,
    0b11111,
    0b11111,
    0b11111,
    0b11111,
    0b00000
]

lcd.custom_char(0, player)
lcd.custom_char(1, obstacle)

def wait_for_button():
    while button.value() == 1:
        pass
    sleep(0.2)  # debounce

while True:
    # Game variables
    player_x = 1
    obstacle_x = 15
    obstacle_y = 1
    jump = False
    score = 0
    game_over = False

    lcd.clear()
    lcd.putstr(" LCD JUMP GAME ")
    sleep(1)

    # ------------ GAME LOOP ------------
    while not game_over:
        lcd.clear()

        # Jump input
        if button.value() == 0:
            jump = True

        # Draw player
        if jump:
            lcd.move_to(player_x, 0)
            lcd.putchar(chr(0))
            jump = False
            player_y = 0
        else:
            lcd.move_to(player_x, 1)
            lcd.putchar(chr(0))
            player_y = 1

        # Draw obstacle
        lcd.move_to(obstacle_x, obstacle_y)
        lcd.putchar(chr(1))

        # Collision detection
        if obstacle_x == player_x and obstacle_y == player_y:
            game_over = True
            break

        obstacle_x -= 1

        # Obstacle reset + score
        if obstacle_x < 0:
            obstacle_x = 15
            obstacle_y = urandom.getrandbits(1)
            score += 1

        sleep(0.25)

    # ------------ GAME OVER SCREEN ------------
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(" GAME OVER ")
    lcd.move_to(0, 1)
    lcd.putstr("Score: " + str(score))

    # Wait for restart
    wait_for_button()
