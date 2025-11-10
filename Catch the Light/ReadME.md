# Catch the Light — Raspberry Pi Pico Reaction Game

Catch the Light is an interactive reaction-time game built for the Raspberry Pi Pico using MicroPython. Players try to press a button exactly when a target LED lights up in a chasing pattern. The game provides visual, auditory, and on-screen feedback and is designed to be modular and easy to extend.

---

## Table of Contents
- Abstract
- Features
- Hardware Components & Wiring
- Circuit Diagram
- Software Architecture
- Installation & Setup
- Game Logic
- Example Code Snippet
- Results & Demo
- Future Enhancements
- Contributing
- License
- Contact

---

## Abstract
This project demonstrates GPIO control, I²C LCD communication, real-time timing, and user interaction on the Raspberry Pi Pico using MicroPython. It implements a randomized target LED during a sequential light chase where players must time their button press to "catch" the target.

---

## Features

Gameplay
- Dynamic target selection (randomized)
- Real-time scoring (caught / missed)
- Light chase animation
- Button input for player reactions
- Buzzer tones for success/failure
- 16×2 I²C LCD for live messages and scores

Technical
- MicroPython implementation
- I²C LCD driver integration
- Modular code structure for easy extension
- Low-latency input handling and timing via time.ticks_ms

---

## Hardware Components
- Raspberry Pi Pico ×1
- LEDs ×8 (Violet, Green, Yellow, Blue, Cyan, Sandal, White, Red)
- 220Ω resistors ×8
- Momentary push button ×1
- Active buzzer ×1 (drive from GP16)
- 16×2 I²C LCD (SDA / SCL)
- Breadboard and jumper wires

---

## GPIO Pin Mapping
- LCD SDA: GP0
- LCD SCL: GP1
- Violet LED: GP2
- Green LED: GP3
- Yellow LED: GP4
- Blue LED: GP5
- Cyan LED: GP6
- Sandal LED: GP7
- White LED: GP8
- Red LED: GP9
- Button: GP15 (use internal pull-up; button ground to GND)
- Buzzer: GP13

---

## Circuit Diagram
(See /docs/schematic.png in the repository for a visual diagram.)

Simple ASCII overview:
+-------------------+      +-------------------+
|   Raspberry Pi    |      |    I²C LCD        |
|      Pico         |      |   Display         |
| GP0  ----------> SDA     |                   |
| GP1  ----------> SCL     |                   |
| GP2..GP9 -----> LEDs     |                   |
| GP15 <------ Button      |                   |
| GP16 ------> Buzzer      |                   |
+-------------------+      +-------------------+

---

## Software Architecture
Files in the repo:
- main.py — Main game application and loop
- lcd_api.py — LCD API (MicroPython)
- i2c_lcd.py — I²C LCD driver wrapper
- requirements.txt — Optional list (for documentation)
- docs/ — diagrams, screenshots, demo assets

Core modules:
- machine (GPIO, I²C)
- time (timing & delays)
- random (target selection)
- lcd_api / i2c_lcd (I²C LCD integration)

---

## Installation & Setup

1. Clone the repository
   git clone https://github.com/jaaswin/catch-the-light-game.git
   cd catch-the-light-game

2. Copy files to the Raspberry Pi Pico using Thonny:
   - main.py
   - lcd_api.py
   - i2c_lcd.py
   - any assets in docs/

3. Wire hardware following the pin mapping above. Use 220Ω resistors on each LED.

4. Power the Pico (via USB). Run `main.py` from Thonny or set it as `main.py` on the device filesystem so it runs on boot.

---

## Game Logic (high level)
1. Initialize hardware and LCD, display welcome message.
2. Randomly pick one LED as the target for the round.
3. Run a light-chase sequence across the 8 LEDs.
4. During each LED "on" window, check for button press.
5. If the button is pressed while the target LED is lit → success (increment caught).
   Otherwise if button pressed on a non-target → miss.
6. Provide feedback via LCD, LEDs (blink pattern), and buzzer tones.
7. Update and display running score; repeat.

---

## Future Enhancements
- Difficulty levels with progressively faster chase
- High score persistence (EEPROM / flash)
- Multiplayer / competitive modes
- Bluetooth or Wi-Fi connectivity for remote scoreboards
- Add 7-segment or more advanced displays

---

## Conclusion:

The Catch the Light Game successfully demonstrates the use of GPIO control, I²C communication, timing functions, and randomization on the Raspberry Pi Pico platform.
It’s a fun and engaging project that enhances understanding of embedded system design, real-time decision making, and human-machine interaction.
