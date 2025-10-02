# Flappy Bird Game 

## Project Overview
This project implements a Flappy Bird-style game using Raspberry Pi Pico microcontroller with multiple display interfaces and user input controls. The game demonstrates real-time graphics rendering, physics simulation, and hardware interfacing in an embedded system environment.

> Click the button below to jump straight into my project.

<p align="center">
  <a href="https://wokwi.com/projects/438795646549160961" target="_blank">
    <img src="https://img.shields.io/badge/Open%20Project-%F0%9F%9A%80-blue?style=for-the-badge" alt="Open Project Badge"/>
  </a>
</p>

## 🎯 Project Objectives
- Design and implement an interactive game on Raspberry Pi Pico
- Interface OLED display for real-time game graphics rendering
- Implement push button control for user input
- Interface LCD display for score tracking and game status
- Simulate physics concepts (gravity, velocity, collision detection)
- Demonstrate embedded systems programming with MicroPython

## 📋 Components List

| Component           | Specification           | Quantity |
|---------------------|------------------------|----------|
| Raspberry Pi Pico   | RP2040 Microcontroller | 1        |
| OLED Display        | 0.96" I²C, 128×64 px   | 1        |
| LCD Display         | 16×2 I²C LCD           | 1        |
| Push Button         | Tactile Switch         | 1        |
| Breadboard          | Prototyping Board      | 1        |
| Jumper Wires        | Male-to-Male           | Multiple |
| Resistors           | 10KΩ Pull-up           | 1        |

## 🔌 Circuit Connection Diagram

```
+------------------------------------------------------------------------+
|                            Raspberry Pi Pico                           |
|                                                                        |
|  +-----------------------------+                                      |
|  | GP0 (SDA)  ---------------->|-----> OLED Display (SDA)             |
|  | GP1 (SCL)  ---------------->|-----> OLED Display (SCL)             |
|  |                             |-----> LCD Display (SDA)              |
|  |                             |-----> LCD Display (SCL)              |
|  | GP14       ---------------->|-----> Push Button (Input)            |
|  | 3.3V       ---------------->|-----> Displays (VCC)                 |
|  | GND        ---------------->|-----> Displays (GND) + Button (GND)  |
|  +-----------------------------+                                      |
+------------------------------------------------------------------------+
```

### Pin Configuration Table
| Raspberry Pi Pico Pin | Connected To         | Function     |
|----------------------|----------------------|--------------|
| GP0                  | OLED SDA + LCD SDA   | I²C Data     |
| GP1                  | OLED SCL + LCD SCL   | I²C Clock    |
| GP14                 | Push Button          | User Input   |
| 3.3V                 | Both Displays        | Power        |
| GND                  | Both Displays + Btn  | Ground       |

## 🎮 Game Mechanics & Working Principle

### Physics Simulation
The game implements realistic physics through the following parameters:

```python
# Physics constants
GRAVITY = 0.5
JUMP_STRENGTH = -4
TERMINAL_VELOCITY = 8
```

### Game Elements
- **Bird Character**: Controlled by player, affected by gravity
- **Pipes**: Randomly generated obstacles with gaps
- **Scoring System**: Points awarded for each passed pipe
- **Collision Detection**: Checks bird position against pipes and boundaries

### Game Flow
1. **Initialization**: Set up displays, initialize game variables
2. **Game Loop**: Continuous rendering and input processing
3. **Bird Movement**: Apply gravity and handle jump input
4. **Pipe Generation**: Create pipes at random heights
5. **Collision Checking**: Detect collisions with pipes or boundaries
6. **Score Update**: Increment score when passing pipes
7. **Game Over**: Display final score and restart option



## 🖥️ Display Interface Design

### OLED Display (Game View)
```
+--------------------------------+
|            FLAPPY BIRD         |
|                                |
|      🐦                        |
|                                |
|     ███              ███       |
|     ███              ███       |
|     ███      ███████████       |
|            ███████████         |
|     ███████████                |
|     ███                        |
|     ███                        |
|                                |
| Score: 5                       |
+--------------------------------+
```

### LCD Display (Score Board)
```
Line 1: Score: 005
Line 2: High: 012
```

## 🚀 Applications & Use Cases

### Educational Applications
- **Embedded Systems Training**: Practical I²C interface implementation
- **Game Development**: Real-time graphics and physics simulation
- **Python Programming**: MicroPython embedded development
- **Electronics Education**: Circuit design and prototyping

### Industrial Applications
- **Prototype Development**: Rapid game concept validation
- **HMI Interfaces**: Multi-display control systems
- **IoT Devices**: User interface design for embedded systems


## ✅ Conclusion

This project successfully demonstrates the capabilities of Raspberry Pi Pico in creating interactive gaming applications. The implementation showcases:

- ✅ Real-time graphics rendering on OLED display
- ✅ Multi-display interface management
- ✅ Responsive user input handling
- ✅ Physics simulation in embedded environment
- ✅ Efficient memory and processing resource management

The Flappy Bird game serves as an excellent platform for learning embedded systems programming, display interfacing, and real-time application development.

## 🔮 Future Enhancements

### Hardware Extensions
- 🔊 **Audio Feedback**: Add buzzer for sound effects
- 🎮 **Multiple Controls**: Joystick or additional buttons
- 📡 **Wireless Connectivity**: WiFi for score sharing
- 💾 **External Storage**: SD card for game data

### Software Improvements
- 🎯 **Difficulty Levels**: Adaptive game difficulty
- 👥 **Multiplayer Mode**: Competitive gameplay
- 🏆 **Achievement System**: Unlockable content
- 🔄 **Game Saves**: Persistent high score storage

### Game Features
- 🌈 **Themes**: Multiple visual themes
- 💫 **Power-ups**: Special abilities and bonuses
- 🎨 **Animations**: Enhanced visual effects
- 📊 **Statistics**: Detailed gameplay analytics

      
