
# 🐍 Project 20: Classic Python Snake Game

## ✨ Overview
This is a recreation of the classic **Snake Game** built in Python. The project focuses on demonstrating fundamental concepts of **Object-Oriented Programming (OOP)** and utilizing Python's built-in `turtle` library for graphical implementation.

## 🚀 Features
* **Classic Gameplay:** Control a growing snake, eat food to score, and avoid colliding with the walls or your own tail.
* **Adjustable Difficulty:** Users can select a difficulty level ('s' for easy, 'm' for median, 'h' for hard) at the start of the game, which directly controls the game speed and challenge.
* **Score Tracking:** A score system is displayed at the top of the screen.
* **Modular OOP Design:** The game logic is split into dedicated, reusable classes for clean code management.

## 🛠️ Technologies Used
* **Language:** Python 3
* **Libraries:** `turtle` (for graphics) and `time` (for controlling game speed/difficulty).

## 💻 Getting Started

### Prerequisites
You only need a modern installation of **Python 3** to run this project. No external packages are required as it uses the built-in `turtle` library.

### Installation & Execution
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git)
    cd YourRepoName
    ```
2.  **Run the Main Script:**
    The entire game can be started by executing the `main.py` file:
    ```bash
    python main.py
    ```
3.  **Choose Difficulty:** When the game starts, a prompt will appear asking you to choose a difficulty:
    * Type `s` for Easy
    * Type `m` for Medium
    * Type `h` for Hard

### Controls
The snake is controlled using the keyboard arrow keys:
* **Up Arrow**
* **Down Arrow**
* **Left Arrow**
* **Right Arrow**

## 🧩 Project File Structure
The project is divided into four main Python classes/files:

| File | Description |
| :--- | :--- |
| `main.py` | The game's entry point and main loop. Initializes the screen, handles user input, manages the game state, and controls the main game flow (e.g., collision detection). |
| `snake.py` | Defines the `Snake` class, which handles the creation, movement, and growth of the snake body. |
| `food.py` | Defines the `Food` class, which manages the food object's creation and random placement on the screen. |
| `scoreboard.py` | Defines the `ScoreBoard` class, which displays the score, updates it, and shows the "GAME OVER" message. |

## ✒️ Author
* gateri jeremiah - www.linkedin.com/in/gateri-jeremiah-ab2129320


