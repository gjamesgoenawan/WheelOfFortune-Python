# Wheel Of Fortune Implementation in Python
Built for NTU MA1080 Mini Project by [Gabriel James Goenawan](https://www.linkedin.com/in/gjamesgoenawan/)

## Requirements and Running The Code
1. Formatting only supported in Windows & through commandline Interface (cmd). 
2. Debug Mode will always print the answer on top of the screen. (Useful for testing purposes)
4. On weaker hardware, the game may struggle to run. (low frames per second on animations)

Clone the Repository using:
```
git clone https://github.com/gabrieljames01/WheelOfFortune-Python.git
cd WheelOfFortune-Python
py app.py
```
No Additional Libraries needed.

FeatureTest Folder consists of first successful test code for most features included in this project.

## Implemented Features:
1. User-friendly GUI
2. A wheel that actually charges, turns, decelerates and stops at the selected value.
3. Natural turning animation. (the pointer can stop anywhere on the circle. not just the center)
4. A dynamic scoreboard that adjusts its own size based on the numbers of player and their balance.
5. Phrases are randomly selected & displayed properly in the GUI.
6. Properly implemented player action function. So it's easy to add new features.
7. Some input proofing. (Decided to took the first character if the input length is more than 1 character & skipped the person who gives empty input or " ")
8. Working input timer with a graphical indicator. (with Threading)
9. Proper ending screen.
10. Player number can be customized. The default max player is 3, but you can change it by changing the maxplayer variable in line 3.
    However, each player needed a custom asset (pX.gif and endbgX.gif). I've only included the asset for player 1-5, so errors will occur if maxplayer is more than 5. 
    This is just a proof of concept of the neat implementation of the player turn and action based system.
11. When a player is choosing action, the default answer is spin (selected when the answer is empty or something else)


