## Pong Game on Raspberry Pi Pico using Grove OLED SH1107 (128×128)
> Click the button below to jump straight into my project.

<p align="center">
  <a href="https://wokwi.com/projects/450221015009910785" target="_blank">
    <img src="https://img.shields.io/badge/Open%20Project-%F0%9F%9A%80-blue?style=for-the-badge" alt="Open Project Badge"/>
  </a>
</p>

<br>

- [🔗
My project](https://wokwi.com/projects/450221015009910785)

``` bash
https://wokwi.com/projects/450221015009910785

```

### Project Overview

This project demonstrates the design and implementation of a classic **Pong game** using a **Raspberry Pi Pico** and a **Grove OLED SH1107 display (128×128)**.
The game showcases real-time graphics rendering, GPIO-based user input, and embedded system programming using **MicroPython**.

The objective of this project is to apply embedded systems concepts such as display interfacing, input handling, game logic, and timing control in a practical and interactive manner.

---

### Hardware Components

* Raspberry Pi Pico
* Grove OLED SH1107 Display (128×128)
* Push buttons (for paddle control)
* Breadboard and jumper wires
* USB cable for programming and power


---

### System Description

The OLED display is interfaced with the Raspberry Pi Pico using the **I²C protocol**.
A custom MicroPython driver is used to control the SH1107 OLED and render graphics on a 128×128 pixel screen.

Two paddles are controlled using push buttons, while a moving ball follows predefined physics rules. Collision detection is implemented for:

* Paddle hits
* Top and bottom screen boundaries

The game runs in a continuous loop with controlled refresh timing to ensure smooth animation.

---

### Game Features

* 128×128 pixel graphical display
* Real-time paddle movement using GPIO inputs
* Ball movement with collision detection
* Center divider line rendering
* Game-over condition handling
* Optimized refresh rate for smooth gameplay

---

### Working Principle

1. The Pico initializes the OLED display and clears the screen.
2. Button inputs are read to move paddles up or down.
3. The ball position updates based on velocity values.
4. Collision logic checks for wall and paddle contact.
5. Graphics are updated using a frame buffer and rendered to the OLED.
6. The loop repeats until a game-over condition is met.



---

### Conclusion

This project successfully demonstrates how a Raspberry Pi Pico can be used to create an interactive graphical application using an OLED display.
It highlights key embedded system skills such as hardware interfacing, graphics handling, real-time logic, and MicroPython programming, making it a strong addition to an embedded systems portfolio.


