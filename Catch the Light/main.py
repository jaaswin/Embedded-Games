from machine import Pin, I2C
import time, random
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

# ---------------- LCD SETUP ----------------
I2C_ADDR = 0x27  # Use 0x3F if your LCD uses that address
I2C_ROWS = 2
I2C_COLS = 16

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_ROWS, I2C_COLS)

# ---------------- HARDWARE SETUP ----------------
led_colors = ["Violet", "Green", "Yellow", "Blue", "Cyan", "Sandal", "White", "Red"]
led_pins = [2, 3, 4, 5, 6, 7, 8, 9]  # Adjust pins as per your wiring
leds = [Pin(p, Pin.OUT) for p in led_pins]

button = Pin(15, Pin.IN, Pin.PULL_UP)
buzzer = Pin(16, Pin.OUT)

# ---------------- GAME VARIABLES ----------------
caught = 0
missed = 0
speed = 100   # LED change speed in milliseconds
target_index = 0

# ---------------- HELPER FUNCTIONS ----------------
def beep(duration=0.1, repeat=1, gap=0.05):
    for _ in range(repeat):
        buzzer.value(1)
        time.sleep(duration)
        buzzer.value(0)
        time.sleep(gap)

def show_status(message1, message2=""):
    lcd.clear()
    lcd.putstr(message1)
    lcd.move_to(0, 1)
    lcd.putstr(message2)

def all_leds(state):
    for l in leds:
        l.value(state)

# ---------------- MAIN GAME LOOP ----------------
show_status("Catch the Light!", "Get Ready...")
time.sleep(2)

while True:
    # Choose new target LED randomly
    target_index = random.randint(0, len(leds)-1)
    target_color = led_colors[target_index]

    show_status(f"Target: {target_color}", f"score:{caught} Missed:{missed}")
    time.sleep(1)

    pressed = False
    hit = False

    # LEDs chase effect
    for i in range(5):  # run through 3 cycles of LEDs
        for j in range(len(leds)):
            all_leds(0)
            leds[j].value(1)
            if button.value() == 0:
                pressed = True
                time.sleep(0.2)
                if j == target_index:
                    hit = True
                break
            time.sleep_ms(speed)
        if pressed:
            break

    # Turn off all LEDs
    all_leds(0)

    # Evaluate result
    if hit:
        caught += 1
        show_status(f"You caught {target_color}!", "One Point..!")
        beep(0.1, 3, 0.05)
        # Celebration: blink LEDs
        for _ in range(3):
            all_leds(1)
            time.sleep(0.1)
            all_leds(0)
            time.sleep(0.1)
    else:
        missed += 1
        show_status(f"Missed {target_color}!", "Try Again 😅")
        # Error buzzer + flash
        beep(0.3, 2, 0.1)
        for _ in range(3):
            all_leds(1)
            time.sleep(0.05)
            all_leds(0)
            time.sleep(0.05)

    # Short delay before next round
    time.sleep(1)
