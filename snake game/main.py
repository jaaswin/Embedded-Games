from machine import Pin, SPI, ADC
import max7219
import time, random

# --- SPI for MAX7219 ---
spi = SPI(0, baudrate=10000000, polarity=0, phase=0,
          sck=Pin(2), mosi=Pin(3))
cs = Pin(5, Pin.OUT)

# Matrix display
matrix = max7219.Matrix8x8(spi, cs, 1)
matrix.brightness(1)

# --- Joystick ---
joy_x = ADC(Pin(26))
joy_y = ADC(Pin(27))
joy_btn = Pin(16, Pin.IN, Pin.PULL_UP)

# --- Snake variables ---
snake = [(3, 3), (3, 4)]   # starting body
direction = (0, -1)        # start moving up
food = (random.randint(0, 7), random.randint(0, 7))
score = 0

def draw():
    matrix.fill(0)
    # Draw food
    matrix.pixel(food[0], food[1], 1)
    # Draw snake
    for x, y in snake:
        matrix.pixel(x, y, 1)
    matrix.show()

def get_direction():
    global direction
    x_val = joy_x.read_u16()
    y_val = joy_y.read_u16()

    if x_val < 10000:
        direction = (-1, 0)   # left
    elif x_val > 55000:
        direction = (1, 0)    # right
    elif y_val < 10000:
        direction = (0, -1)   # up
    elif y_val > 55000:
        direction = (0, 1)    # down

def new_food():
    while True:
        pos = (random.randint(0, 7), random.randint(0, 7))
        if pos not in snake:
            return pos

def game_over():
    matrix.fill(0)
    for _ in range(3):
        matrix.fill(1)
        matrix.show()
        time.sleep(0.3)
        matrix.fill(0)
        matrix.show()
        time.sleep(0.3)
    return

# --- Main game loop ---
while True:
    get_direction()

    # New head position
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # Check collisions
    if (new_head in snake) or not (0 <= new_head[0] <= 7 and 0 <= new_head[1] <= 7):
        game_over()
        snake = [(6, 6), (6, 8)]
        direction = (0, -1)
        food = new_food()
        score = 0
        continue

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = new_food()
    else:
        snake.pop()  # move forward

    draw()
    time.sleep(0.3)
