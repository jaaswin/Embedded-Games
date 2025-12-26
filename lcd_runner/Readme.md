# LCD Runner Game using Raspberry Pi Pico

> Click the button below to jump straight into my project.

<p align="center">
  <a href="https://wokwi.com/projects/438795646549160961" target="_blank">
    <img src="https://img.shields.io/badge/Open%20Project-%F0%9F%9A%80-blue?style=for-the-badge" alt="Open Project Badge"/>
  </a>
</p>
<br>

- [🔗
My project](https://wokwi.com/projects/438795646549160961)

``` bash
https://wokwi.com/projects/438795646549160961

```
## 📌 Project Overview
**LCD Runner** is a simple runner-style game built using a **Raspberry Pi Pico**, a **16x2 LCD display**, and **push buttons**.  
The player controls a character on the LCD screen and uses buttons to jump or move to avoid obstacles.

This project demonstrates:
- Embedded programming with Raspberry Pi Pico
- Interfacing an LCD display
- Using push buttons for user input
- Basic game logic on microcontrollers

---

## 🧰 Components Used
- Raspberry Pi Pico
- 16x2 LCD (with or without I2C)
- Push Buttons (1–2)
- Breadboard
- Jumper Wires
- USB Cable

---

## 🔌 Circuit Connections

### LCD Connections (Example – I2C)
| LCD Pin | Pico Pin |
|--------|----------|
| VCC    | 3.3V / 5V |
| GND    | GND |
| SDA    | GP0 |
| SCL    | GP1 |

### Button Connections
| Button | Pico Pin |
|-------|----------|
| Button 1 (Jump) | GP15 |
| Button 2 (Optional) | GP14 |
| Other side | GND |

> ⚠️ Make sure pull-up or pull-down resistors are configured (internal or external).

---

## 🎮 Game Description
- The player character stays on the left side of the LCD.
- Obstacles move from right to left.
- Press the button to **jump** and avoid obstacles.
- The game ends if the player collides with an obstacle.
- Score increases as obstacles are avoided.

---

## 🧠 Working Principle
1. The LCD continuously updates the game frame.
2. Buttons are read using GPIO inputs.
3. Game logic checks for collisions.
4. Score is updated and displayed.
5. Game resets after a collision.

---

## 💻 Software & Tools
- Programming Language: **MicroPython / C (choose one)**
- IDE: Thonny / Arduino IDE
- Libraries:
  - LCD library
  - GPIO handling library

---

## ▶️ How to Run
1. Connect the components as per the circuit diagram.
2. Upload the code to the Raspberry Pi Pico.
3. Power the Pico using USB.
4. Press the button to start playing.

---


