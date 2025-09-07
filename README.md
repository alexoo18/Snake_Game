# 🐍 Snake Game 

A modern take on the classic Snake Game, built with **Python**.  

This version features:
- A clean modular design
- Circular snake body with animated eyes 👀
- Apple-shaped food 🍎
- Score and length tracking
- Pause and restart functionality
- Game-over animation (flashing red snake)
- Dedicated UI bar (score + controls outside the play area)

---

## 🎮 How to Play

- **Arrow Keys** → Move the snake  
- **Eat apples 🍎** → Grow and earn points  
- **Avoid** → Walls and your own body  
- **P** → Pause  
- **ESC** → Quit  
- **SPACE** → Restart after Game Over  

---

## 📦 Requirements

- Python 3.9+ (tested on Python 3.11)  
- Pygame 2.6.1 or later  

Install dependencies with:

```bash
pip install -r requirements.txt
```
---
## ▶️ Run the Game

Clone the repository and run:
```bash
python main.py
```
---
## 📂 Project Structure
```bash
.
├── constants.py      # Global constants (grid size, colours, speed, etc.)
├── snake.py          # Snake class (movement, growth, collision)
├── food.py           # Food class (apple placement & respawn)
├── renderer.py       # Renderer class (graphics & UI drawing)
├── input_handler.py  # Handles keyboard input
├── game.py           # Main Game class (logic + game loop)
├── main.py           # Entry point (starts the game)
└── requirements.txt  # Dependencies
```
---
## ✨ Features

- 🟢 Circular snake with eyes
- 🍎 Apple-shaped food with stem + leaf
- 📊 UI bar at the top showing score, length, and controls
- ⏸️ Pause screen overlay
- 💀 Game Over screen with restart/quit instructions
- 🔴 Flashing red snake when dead

---

## 📸 Screenshots

Here are some screenshots of the game in action:

<img width="1336" height="1086" alt="image" src="https://github.com/user-attachments/assets/71fd32a4-a6e4-454d-9307-41b79022c1e9" />

<img width="1341" height="1086" alt="image" src="https://github.com/user-attachments/assets/6cfc92ce-dc5d-4915-b7e1-e30483a4e81d" />

<img width="1339" height="1086" alt="image" src="https://github.com/user-attachments/assets/927da38f-4bba-4fae-afec-f7d29c15e55b" />

---
## 📝 License

This project is free to use, modify, and learn from.
Built for fun with Python, with help from Claude AI for debugging! 
