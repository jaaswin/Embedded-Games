# Maze Runner – Embedded Game using Raspberry Pi Pico

![Platform - Raspberry Pi Pico](https://img.shields.io/badge/Platform-Raspberry_Pi_Pico-red?style=for-the-badge) ![Language - MicroPython](https://img.shields.io/badge/Language-MicroPython-blue?style=for-the-badge)

## 🎯 Project Overview
The Maze Runner Game is an interactive embedded system project that combines hardware control, sensor interfacing, and real-time programming. Players navigate a "runner" (a glowing LED dot) through a maze displayed on an 8×8 LED matrix using a joystick controller, with audio feedback provided through a buzzer.

This project demonstrates integration of hardware control, sensor interfacing, and embedded logic programming — a compact, fun, and educational platform for learning embedded systems.

---

## 📋 Abstract
The Maze Runner Game uses a Raspberry Pi Pico, MAX7219-driven 8×8 LED matrix, a joystick module, and a buzzer. The objective is to move the runner from a start point to a goal while avoiding maze walls. The system includes collision detection, audio feedback, and multiple maze layout support.

---

## 🛠️ Components Required

| Component | Quantity | Description |
|---|---:|---|
| Raspberry Pi Pico | 1 | Main microcontroller |
| MAX7219 8×8 LED Matrix | 1 | Maze display |
| Joystick Module | 1 | Analog directional control (X/Y + button) |
| Buzzer | 1 | Audio feedback |
| Connecting Wires | As needed | For wiring |
| Breadboard / PCB | 1 | Prototyping platform |
| Power Supply | 1 | 5V DC (or via USB) |

---

## 🔌 Circuit Diagram & Connections

Pin Configuration (Raspberry Pi Pico GPIO numbering):

| Component | Pico Pin | Function |
|---|---:|---|
| MAX7219 DIN | GP19 | SPI MOSI |
| MAX7219 CLK | GP18 | SPI SCK |
| MAX7219 CS  | GP17 | Chip Select |
| Joystick VRx | GP26 | ADC0 (X-axis) |
| Joystick VRy | GP27 | ADC1 (Y-axis) |
| Joystick SW  | GP16 | Digital input (button) |
| Buzzer        | GP15 | PWM output |

Schematic Description:
- MAX7219 is connected via SPI for efficient display control.
- Joystick uses Pico ADC channels for analog position readings and a digital line for the press button.
- Buzzer is driven with PWM for tones.

(Include or attach a hardware diagram in `hardware/` to match these pin connections.)

---

## ⚡ Working Principle

System Flow:
Power On → Initialize Components → Display Maze → Read Joystick → Update Position → Check Collisions → Audio Feedback → Check Win Condition

Detailed Operation:
1. Initialization
   - Boot the Pico and initialize SPI, MAX7219 driver, ADCs, and PWM for the buzzer.
   - Load and render the maze layout on the LED matrix.
   - Set the player start position.

2. Gameplay Loop
   - Continuously read joystick analog values (X, Y).
   - Convert ADC readings to movement directions using thresholding and debouncing.
   - Attempt moves, validate against maze walls and boundaries.
   - On collision: emit buzzer beep, optionally reset or nudge back.
   - On goal reached: play victory tone and run a celebration animation.

3. Event Handling
   - Wall Collision: Short beep and visual feedback.
   - Goal Reached: Victory melody and LED pattern celebration.
   - Boundary Check: Prevent moving off the 8×8 grid.

---

## 💻 Software Implementation

- Language: MicroPython
- IDE: Thonny IDE or Wokwi Simulator
- Key Libraries:
  - `max7219.py` — MAX7219 LED matrix driver
  - `machine` — GPIO, SPI, ADC, PWM access
  - `utime` / `time` — delays and timestamps

Suggested repository layout:
```
maze-runner-pico/
├── docs/
├── hardware/
├── software/
│   ├── lib/
│   │   └── max7219.py
│   ├── src/
│   │   ├── main.py
│   │   ├── maze.py
│   │   ├── player.py
│   │   └── joystick.py
│   └── examples/
├── images/
└── README.md
```

---

## 🎮 Game Features

Core Mechanics:
- Intuitive joystick mapping for movement
- Pixel-accurate collision detection
- Visual clarity between walls, path, player, and goal
- Audio feedback for collisions and victory

Player Experience:
- Real-time responsiveness
- Progressive challenge with multiple maze layouts
- Replayability with different mazes or timed runs

---

## 📊 Applications & Educational Value

- Hands-on embedded systems learning (SPI, ADC, PWM)
- Real-time software design and event handling
- Hardware interfacing and prototyping
- Great for classroom demonstrations, maker workshops, and hobbyist projects

---

## ✅ Advantages
- Low-cost components
- Open-source and modular design
- Portable and expandable
- Easy to extend: more matrices, score tracking, saved levels

---

## 🔮 Future Enhancements
Short-term:
- Multiple maze levels
- Score and timer display (e.g., on an OLED)
- Power management improvements

Advanced:
- Procedural maze generator
- Bluetooth control / mobile app
- Multiplayer support with additional hardware
- Cloud leaderboards

Hardware expansions:
- Add more LED matrices for larger mazes
- RGB LED feedback
- Haptic vibration motor
- SD card for storing mazes

---

## 🚀 Getting Started

Prerequisites:
- Basic Python knowledge
- Understanding of electronics and safe wiring practices
- Raspberry Pi Pico with MicroPython firmware installed
- Components listed above

Setup Instructions:

1. Hardware Assembly
   - Wire the MAX7219, joystick, and buzzer to the Pico as shown in the Pin Configuration table.
   - Verify the wiring before powering the board.

2. Software Setup
   - Install Thonny (recommended) and configure it to use the Pico.
   - Flash MicroPython firmware to the Pico.
   - Upload the `software/lib/` drivers (e.g., `max7219.py`) and `software/src/` source files.

3. Testing
   - Power on the Pico and run `main.py`.
   - Verify the LED matrix initializes and displays the maze.
   - Move the joystick and confirm the runner responds.
   - Test buzzer responses by colliding with walls and reaching the goal.

---


## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with a clear description

Please check the issues page for existing tasks or request new features.

---
