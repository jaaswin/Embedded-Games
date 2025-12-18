# Catch the Light Game — Reaction Time Challenge
---

> Click the button below to jump straight into my project.

<p align="center">
  <a href="https://wokwi.com/projects/447241969981217793" target="_blank">
    <img src="https://img.shields.io/badge/Open%20Project-%F0%9F%9A%80-blue?style=for-the-badge" alt="Open Project Badge"/>
  </a>
</p>
<br>

- [🔗
My project](https://wokwi.com/projects/447241969981217793)

``` bash
https://wokwi.com/projects/447241969981217793

```


---
## Project Overview
Catch the Light Game is an interactive reaction-time embedded project built with the Raspberry Pi Pico (RP2040) and MicroPython. Players watch a chasing light animation across an 8-LED array and try to press a button exactly when the randomly chosen target LED lights up. Feedback is provided via a buzzer and a 16×2 I²C LCD.

Key ideas:
- Real-time reaction testing
- Multi-sensory feedback (visual + audio + display)
- Small, modular MicroPython codebase

---

## Abstract
This project demonstrates GPIO control, I²C communication, timing/interrupt handling, and a simple game state machine to evaluate human reaction time. Each round selects a random target LED; the LEDs “chase” in sequence and the user must press the button when the target LED is lit. The system provides immediate feedback, scoring, and persistent counters displayed on the LCD.

---

## Features

Gameplay
- Random target selection per round
- LED chase animation
- Real-time scoring (caught / missed)
- Instant multi-modal feedback (LCD + buzzer + LED animation)

Technical
- MicroPython on Raspberry Pi Pico
- I²C 16×2 LCD with driver
- GPIO managed LEDs and input with pull-ups
- Modular code layout for maintainability

---

## Hardware Components

Required
- Raspberry Pi Pico (1)
- LEDs (8) — different colors
- 220 Ω resistors (8)
- Push Button (1) — momentary
- Active Buzzer (1)
- 16×2 I²C LCD (1) with backpack (typ. 0x27)
- Breadboard, jumper wires, USB cable

Hardware Specs
- Operating Voltage: 3.3V
- Pico clock: 133 MHz
- MicroPython firmware recommended: 1.19+

---

## Circuit Design

GPIO pin mapping (recommended)
- LCD SDA: GP0 (I2C SDA)
- LCD SCL: GP1 (I2C SCL)
- Violet LED: GP2
- Green LED: GP3
- Yellow LED: GP4
- Blue LED: GP5
- Cyan LED: GP6
- Sandal LED: GP7
- White LED: GP8
- Red LED: GP9
- Push Button: GP15 (Input with internal pull-up; button to GND)
- Buzzer: GP16 (Active buzzer)

Connection notes
- Put a 220 Ω resistor in series with each LED.
- Button: one side to GP15, the other to GND; enable internal pull-up in code.
- I²C LCD: VCC to 3.3V, GND to GND, SDA to GP0, SCL to GP1 (ensure correct voltage tolerance).
- Active buzzer can be driven directly as a digital output (short pulses).

---



## Working Principle

Game state machine
1. Initialization
   - Initialize pins, LCD, and counters.
   - Show welcome message.

2. Gameplay loop
   - Select target LED index randomly (0..7).
   - Display “Target: <Color>” on the LCD.
   - Run LED chase sequence (e.g., 300 ms per LED).
   - Monitor button during each LED ON window.
   - Evaluate the input — success if pressed during the target LED.

3. Feedback
   - Success: increment caught counter, play success tone (3 short beeps), run success animation.
   - Failure: increment missed counter, play failure tone, run failure animation.
   - Update LCD with C: / M: counters.


---

## Demo & Results

Typical test metrics
- Reaction window: 300 ms (default)
- System latency: < 10 ms (variable by firmware & debouncing)
- Typical success rate by player skill:
  - Beginner: ~50–60%
  - Experienced: ~70–85%

Example session (LCD / console)
- Initialization: "Catch the Light! / Get Ready..."
- Gameplay: "Target: Blue / C:0 M:0"
- On success: "You caught Blue! / Awesome!" + 3 short beeps + blink animation
- On failure: "Missed Blue! / Try Again" + long buzzes + rapid flashing

---

## Applications
- Educational: teaching MicroPython, GPIO, I²C
- Research: simple psychophysics/reaction time experiments
- Training: reflex training and assessment
- Demos: maker-fair and embedded-systems showcases

---

## Future Enhancements

Difficulty & scoring
- Multiple speed levels (Easy 500ms, Medium 300ms, Hard 150ms, Expert 100ms)
- Time-based scoring (faster presses → more points)
- Combo multipliers for streaks

Hardware upgrades
- RGB LEDs for richer feedback
- Haptic motor for vibration feedback
- Multiple buttons for multiplayer

Connectivity
- Wi‑Fi / Bluetooth scoreboard (add an ESP32 companion or add USB logging)
- Data logging for analysis (CSV output over USB)

Accessibility
- Audio-only mode
- Adjustable timing windows and color-blind friendly color schemes

---

## Conclusion
Catch the Light is a compact, instructive embedded project that demonstrates MicroPython programming, I²C integration, and real-time user interaction. Its modular design makes it easy to extend with new modes, logging, or network features.

---


