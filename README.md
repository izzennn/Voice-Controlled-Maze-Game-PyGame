# Voice-Controlled-Maze-Game-PyGame
**Voice-Controlled Maze Game** is a simple yet innovative game implemented in Python using the Pygame, PyAudio, and threading libraries. Players navigate a ball through an obstacle course using voice commands like "go right," "go left," "up," and "down."

![Voice-Controlled Maze Game Screenshot](game.png)

## Gameplay

- The objective is to guide the ball through a maze of obstacles to reach the finish line using voice commands.
- The game listens for specific directional keywords—`left`, `right`, `up`, or `down`—within the spoken sentence.
- Example commands:
  - "Go right to avoid the wall!"
  - "Move up a little."
  - "Quickly go down!"
- The use of multi-word commands with the directional keyword ensures more accurate recognition.

## How to Run

1. Ensure you have Python and the required libraries installed (`Pygame` and `PyAudio`).
   
2. Clone this repository to your local machine.

3. Navigate to the project directory.

4. Run the game by executing the `maze.py` script:

   ```bash
   python3 maze.py
   ```

5. Use your voice to control the ball and navigate through the maze!

## Features

- **Voice-Controlled Movement**: Control the ball using voice commands with directional keywords.
- **Obstacle Course**: Navigate through a series of obstacles to complete the maze.
- **Multi-Threading**: Uses threading to handle real-time voice recognition and game mechanics smoothly.

## Customization

You can customize the game by modifying parameters in the `maze.py` script:

- Adjust the maze layout by editing the obstacle positions.
- Modify the ball's speed for easier or more challenging gameplay.
- Tweak voice recognition settings for sensitivity and accuracy.

## Dependencies

- Python 3.x
- Pygame
- PyAudio
- Threading (built-in Python library)

## Notes

- Ensure that your microphone is working correctly before running the game.
