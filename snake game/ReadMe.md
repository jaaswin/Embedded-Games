# Snake Game using Raspberry Pi Pico
---
> Click the button below to jump straight into my project.

<p align="center">
  <a href="https://wokwi.com/projects/443720747988473857" target="_blank">
    <img src="https://img.shields.io/badge/Open%20Project-%F0%9F%9A%80-blue?style=for-the-badge" alt="Open Project Badge"/>
  </a>
</p>
---
<br>

- [🔗
My project](https://wokwi.com/projects/443720747988473857)

``` bash
https://wokwi.com/projects/450221015009910785

```

## 📋 Project Overview

This project implements the classic Snake Game on an 8×8 LED matrix controlled by the MAX7219 driver IC and a Raspberry Pi Pico. A joystick module provides user input to control the snake's movement. The snake grows in size each time it eats food, and the game ends when it collides with the wall or with itself.

This project demonstrates embedded systems design, SPI communication, real-time gaming logic, and hardware-software integration using MicroPython.



## 🛠 Hardware Components

| Component | Quantity | Purpose |
|-----------|----------|---------|
| Raspberry Pi Pico | 1 | Main microcontroller board |
| MAX7219 8×8 LED Matrix | 1 | Dot matrix display module |
| Joystick Module | 1 | User input for direction control |
| Breadboard | 1 | Prototyping circuit |
| Jumper Wires | Several | Component connections |
| Micro USB Cable | 1 | Power and programming |

---

## 🔌 Circuit Connections

### MAX7219 ↔ Raspberry Pi Pico

| MAX7219 Pin | Pico Pin | Function |
|-------------|----------|----------|
| VCC | 3.3V | Power supply |
| GND | GND | Ground |
| DIN | GP3 (MOSI) | SPI Data Input |
| CS | GP5 | Chip Select |
| CLK | GP2 (SCK) | SPI Clock |

### Joystick ↔ Raspberry Pi Pico

| Joystick Pin | Pico Pin | Function |
|--------------|----------|----------|
| VRx (X-axis) | GP26 (ADC0) | Analog X-position |
| VRy (Y-axis) | GP27 (ADC1) | Analog Y-position |
| SW (Button) | GP16 | Push button |
| VCC | 3.3V | Power supply |
| GND | GND | Ground |

---

## 🎮 Working Principle

### Display Control
- The MAX7219 chip communicates with the Pico via SPI protocol
- Controls individual pixels on the 8×8 LED matrix
- Efficient display refresh using hardware SPI

### Game Logic
- Snake starts with a length of 2-3 pixels
- Food is randomly placed on available positions
- Continuous snake movement in current direction
- Joystick input changes movement direction
- Score increases when snake eats food
- Game ends on collision with walls or self

### Joystick Input Handling
- Analog-to-Digital Conversion (ADC) readings from GP26 and GP27
- **Move Left**: VRx low (< 16,000)
- **Move Right**: VRx high (> 48,000)
- **Move Up**: VRy low (< 16,000)
- **Move Down**: VRy high (> 48,000)

---

## 💻 Code Implementation

### Library & Hardware Setup
```python
from machine import Pin, SPI, ADC
import max7219
import random
import time

# SPI and MAX7219 initialization
spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3))
cs = Pin(5, Pin.OUT)
matrix = max7219.Matrix8x8(spi, cs, 1)
matrix.brightness(5)

# Joystick setup
joy_x = ADC(26)
joy_y = ADC(27)
joy_btn = Pin(16, Pin.IN, Pin.PULL_UP)
```

### Game State Variables
```python
# Snake initialization
snake = [(3, 3), (3, 4)]  # List of (x,y) coordinates
direction = (0, -1)       # Initial direction: up
food = None
score = 0
game_active = True
```

### Main Game Loop
```python
def game_loop():
    global snake, direction, food, score, game_active
    
    while True:
        if game_active:
            # Read joystick and update direction
            read_joystick()
            
            # Move snake
            move_snake()
            
            # Check for food collision
            check_food()
            
            # Check for game over conditions
            if check_collision():
                game_over()
            
            # Update display
            update_display()
            
            time.sleep(0.3)  # Game speed
        else:
            # Game over state - wait for restart
            if joy_btn.value() == 0:
                reset_game()
```

### Core Game Functions
```python
def move_snake():
    head_x, head_y = snake[0]
    dir_x, dir_y = direction
    new_head = ((head_x + dir_x) % 8, (head_y + dir_y) % 8)
    snake.insert(0, new_head)
    snake.pop()  # Remove tail unless food eaten

def generate_food():
    while True:
        food_pos = (random.randint(0, 7), random.randint(0, 7))
        if food_pos not in snake:
            return food_pos

def check_food():
    global food, score
    if snake[0] == food:
        # Grow snake by not removing tail
        snake.append(snake[-1])
        score += 1
        food = generate_food()

def check_collision():
    head = snake[0]
    # Check self-collision (head in body)
    return head in snake[1:]

def game_over():
    global game_active
    game_active = False
    # Blink animation
    for _ in range(3):
        matrix.fill(1)
        matrix.show()
        time.sleep(0.3)
        matrix.fill(0)
        matrix.show()
        time.sleep(0.3)
```

---

## 🎯 Features & Gameplay

### Game Features
- **Smooth Controls**: Responsive joystick input
- **Score Tracking**: Visual score indication
- **Random Food Generation**: Ensures fair gameplay
- **Collision Detection**: Wall and self-collision
- **Game Over Animation**: Blinking LED pattern
- **Auto-restart**: Press joystick button to restart

### Game Rules
1. Control the snake using the joystick
2. Eat food to grow longer and increase score
3. Avoid colliding with walls or yourself
4. Game ends on collision
5. Press joystick button to restart after game over

---

## 🔧 Setup Instructions

### 1. Hardware Assembly
1. Place Raspberry Pi Pico on breadboard
2. Connect MAX7219 to Pico as per pin mapping
3. Connect joystick module to Pico
4. Ensure all ground connections are common

### 2. Software Setup
1. Install MicroPython on Raspberry Pi Pico
2. Upload required libraries (max7219.py)
3. Upload the main game code
4. Reset Pico to start the game

### 3. Calibration (if needed)
```python
# Adjust these values based on your joystick
JOY_THRESHOLD_LOW = 16000
JOY_THRESHOLD_HIGH = 48000
```

---

## 📊 Technical Specifications

| Parameter | Specification |
|-----------|---------------|
| Microcontroller | Raspberry Pi Pico (RP2040) |
| Display | 8×8 LED Matrix (MAX7219 driven) |
| Communication | SPI @ 10MHz |
| Input | Analog Joystick (2-axis + button) |
| Power | 3.3V via USB |
| Code | MicroPython |
| Refresh Rate | ~3 FPS (adjustable) |

---

## 🚀 Applications & Learning Outcomes

### Educational Value
- **Embedded Systems**: Hands-on microcontroller programming
- **SPI Protocol**: Understanding serial communication
- **Game Development**: Real-time game logic implementation
- **Hardware Interfacing**: ADC, digital I/O, and display control
- **Algorithm Design**: Snake movement and collision detection

### Practical Applications
- Learning platform for embedded gaming
- Prototype for arcade game systems
- Demonstration of real-time control systems
- Foundation for more complex matrix-based projects

---

## 🔍 Troubleshooting

### Common Issues & Solutions

| Problem | Possible Cause | Solution |
|---------|----------------|----------|
| No display | Wiring incorrect | Check SPI connections |
| Flickering display | Low brightness | Increase matrix brightness |
| Unresponsive controls | ADC range issues | Calibrate joystick thresholds |
| Snake not moving | Direction logic error | Verify joystick reading logic |
| Food spawning on snake | Random generation bug | Check food placement algorithm |

### Debugging Tips
1. Use serial output to print game state
2. Test joystick values separately
3. Verify each game function individually
4. Check for off-by-one errors in coordinate math

---

## 📈 Future Enhancements

### Potential Improvements
- **Multiple Difficulty Levels**: Adjustable speed
- **High Score Tracking**: EEPROM storage
- **Sound Effects**: Buzzer for audio feedback
- **Menu System**: Game settings and modes
- **Larger Display**: Multiple matrix cascading
- **Wireless Control**: Bluetooth or WiFi input

### Code Optimizations
- Object-oriented design
- Interrupt-based input handling
- Frame rate optimization
- Memory usage optimization

---

## 🎓 Conclusion

The Snake Game project successfully demonstrates how classic gaming concepts can be implemented in embedded hardware systems. Using the Raspberry Pi Pico, MAX7219 LED matrix, and joystick module, we've recreated the timeless Snake game in a compact 8×8 display format.

This project strengthens fundamental concepts including:
- Hardware interfacing and protocol implementation
- Real-time control systems
- Game logic and state management
- Analog-to-digital conversion
- Embedded programming with MicroPython

The implementation serves as an excellent foundation for further exploration in embedded systems development, gaming applications, and interactive hardware projects.

---

## 📁 Repository Structure

```
Snake-Game-Pico/
├── Documentation/
│   ├── README.md
│   ├── schematics.png
│   └── wiring_diagram.fzz
├── Source Code/
│   ├── main.py
│   └── max7219.py
├── Images/
│   ├── circuit.jpg
│   ├── gameplay.jpg
│   └── components.jpg
└── Additional Resources/
    ├── datasheets/
    └── references.md
```

---

## 👨‍💻 Author & Acknowledgments

**Project Developer**: [Your Name]  
**Institution**: [Your Institution/Organization]  
**Date**: [Project Date]

### Acknowledgments
- Raspberry Pi Foundation for Pico hardware
- MicroPython community for development framework
- Open-source contributors for MAX7219 library

---


*This project is open-source and available for educational and personal use. Feel free to modify and enhance according to your requirements.*

