# main.py
from machine import Pin, ADC, SPI
from time import sleep
from max7219_matrix import MAX7219

# --- SPI + MAX7219 setup ---
# SPI0: SCK=GP18, MOSI=GP19 (these are defaults used below)
spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19))
matrix = MAX7219(spi, cs_pin=17, n=1)  # n=number of cascaded modules

# --- Joystick + button + buzzer ---
x_adc = ADC(26)   # GP26
y_adc = ADC(27)   # GP27
btn = Pin(15, Pin.IN, Pin.PULL_UP)
buzzer = Pin(14, Pin.OUT)

# --- Maze: 1 = wall, 0 = path
maze = [
    [0,1,0,0,0,1,0,0],
    [0,1,0,1,0,1,0,1],
    [0,0,0,1,0,0,0,1],
    [1,1,0,0,0,1,0,0],
    [0,0,0,1,0,1,1,0],
    [0,1,1,0,0,0,0,0],
    [0,0,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0]
]

player_x, player_y = 0, 0
goal_x, goal_y = 7, 7

# display buffer helper: convert maze + player to 8-byte array
def build_buffer():
    buf = [0]*8
    for y in range(8):
        row_byte = 0
        for x in range(8):
            if maze[y][x] == 1:
                row_byte |= (1 << x)   # wall
        buf[y] = row_byte
    # set player pixel (override walls visually if needed)
    if 0 <= player_x < 8 and 0 <= player_y < 8:
        buf[player_y] |= (1 << player_x)
    # optional: mark goal with top bit of that column (we'll draw goal as another bit)
    # Here we leave goal as path — player reaching it wins.
    return buf

def show():
    matrix.draw_buffer(build_buffer())

def beep(ms=80):
    buzzer.value(1)
    sleep(ms/1000)
    buzzer.value(0)

def read_joystick_thresholds():
    x = x_adc.read_u16()
    y = y_adc.read_u16()
    # threshold tuning
    right = x < 14000
    left = x > 52000
    up = y < 14000
    down = y > 52000
    return left, right, up, down

def can_move(nx, ny):
    return 0 <= nx < 8 and 0 <= ny < 8 and maze[ny][nx] == 0

# main loop
matrix.clear()
show()
sleep(0.1)

last_move_time = 0
move_delay = 0.18  # seconds between moves to avoid oversampling

import time
while True:
    show()
    # read joystick
    l, r, u, d = read_joystick_thresholds()

    moved = False
    nx, ny = player_x, player_y

    if l:
        nx = player_x - 1
    elif r:
        nx = player_x + 1
    if u:
        ny = player_y - 1
    elif d:
        ny = player_y + 1

    # only perform move if changed
    if (nx, ny) != (player_x, player_y):
        if can_move(nx, ny):
            player_x, player_y = nx, ny
            moved = True
        else:
            # hit wall
            beep(50)
            # flash that wall pixel quickly
            matrix.pixel(nx, ny, True)
            sleep(0.08)
            matrix.pixel(nx, ny, False)
            show()

    # check goal
    if player_x == goal_x and player_y == goal_y:
        # win animation
        for i in range(6):
            matrix.clear()
            sleep(0.12)
            # fill display
            for y in range(8):
                matrix._buf = [0xFF]*8
                matrix._write(0x01+y, 0xFF)
            beep(60)
            sleep(0.12)
        # reset or break
        matrix.clear()
        print("You Win!")
        # reset player to start
        player_x, player_y = 0, 0
        show()
        sleep(0.5)

    # small debounce/delay so single tilt moves once
    sleep(move_delay)
