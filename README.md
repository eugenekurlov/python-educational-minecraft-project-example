# Python Minecraft Final Project

## Overview

The project objective is to apply the concepts and skills learned throughout the course by creating a custom modification or automation script for the Minecraft game and Telegram bot using Python. In this case it is a game insided Minecraft game.

## Description

The game is a simple jump game with disappearing blocks. The higher you are the more score you get. The blocks disappear sequentially in a while. There's limitation in game duration for test puposes.

A pupil think through detalization of the game by himself.

The results of the game is saving in .csv file to make it shareable. "Database" part was written by pupil under my instructions, because pandas library is not the most required python developer tool. If you're teacher and your pupils perceive information quickly, you can go through the DBMS topic with them, so they'll be able to store the records in sql format.

The more real-life applicability is Telegram bot. The record table sending by bot mechanism was realized.

## Project Goals

- **Apply Python programming concepts**: Utilize variables, loops, functions, classes, and modules to build a functional project.
- **Integrate with Minecraft**: Use the Minecraft API to interact with the game, manipulate the environment, or automate tasks.
- **Problem-solving**: Identify a problem or a feature to implement in Minecraft and solve it using Python.
- **Creativity and originality**: Encourage creative thinking and original ideas in the context of Minecraft.

## Requirements

1. **Python Knowledge**: Basic to intermediate understanding of Python programming, telebot and mcpi libraries.
2. **Minecraft Knowledge**: Spatial thinking, understanding of Minecraft coordinate system.
3. **Minecraft Setup**: Ensure you have Minecraft installed and properly configured to work with the Minecraft API for Python (such as the Minecraft Pi Edition or Minecraft Forge with a Python modding library).
4. **IDE or Text Editor**: Use any Python-friendly integrated development environment (IDE) or text editor (e.g. PyCharm Community Edition).

## Getting Started

1. **Install Required Libraries**:
   Ensure you have the necessary Python libraries installed. You may need to install `mcpi` or another Minecraft API library. All python packages needed are in `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

2. **Connect to Minecraft**:
   Ensure your Minecraft game is running and the Python script can connect to it.

3. **Run Example Script**:
   Run the `main.py` file provided in the project folder using CLI:
   ```bash
   python main.py
   ```
   or in your IDE.

## Evaluation Criteria

Projects will be evaluated based on the following criteria:

- **Functionality**: Does the project work as intended?
- **Code Quality**: Is the code well-organized, readable, and documented?
- **Creativity**: How original and creative is the project idea?
- **Complexity**: Does the project demonstrate a good understanding of Python and its integration with Minecraft?
- **Developability**: Are any ideas to improve the project, to add new features or to provide code operability in more extreme user experience conditions?