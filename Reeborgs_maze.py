"""
For this project, we are going to complete [Reeborg's Maze challange](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)
Lost in a maze
Reeborg was exploring a dark maze and the battery in its flashlight ran out.

Write a program  so Reeborg can find the exit. THe map of the maze is the same each time, but the robot's location and facing direction is unknown.
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        if front_is_clear():
            move()
    else:
        turn_left()