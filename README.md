# 🐍 Snake Game in Python (Pygame)

A classic **Snake Game** built using **Python** and **Pygame**.  
Simple, fun, and addictive — relive the nostalgia of the old-school snake game right on your computer!

---

## 🎮 Features
- Smooth snake movement with arrow keys ⬅️➡️⬆️⬇️
- Randomly generated food 🍎
- Score tracking system 🏆
- Game-over screen with replay option 🔄
- Clean and minimal UI 🎨

---

## 🖥️ Demo
- Snake moves around the grid eating food.
- Each food increases the snake’s length and your score.
- Colliding with walls or yourself ends the game.
- Press **P** to play again or **Q** to quit after losing.

---

## ⚙️ Requirements
Make sure you have the following installed:
- Python 3.x
- Pygame library

Install pygame with:
```bash
pip install pygame
```

---

## 🚀 How to Run
1. Clone this repository:
```bash
git clone https://github.com/your-username/snake-game.git
```
2. Navigate to the project folder:
```bash
cd snake-game
```
3. Run the game:
```bash
python snake.py
```

---

## 📸 Screenshots

---

## 🧩 Code Highlights
- Snake Rendering:
```bash
def game_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])
```
-Food Generation:
```bash
foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0
```

---

## 🎯 Future Improvements
- Add difficulty levels (Easy, Medium, Hard)
- Add sound effects 🎵
- High score saving system 💾
- Multiplayer mode ⚔️

---

