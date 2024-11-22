# Quadruped Project
this project aims to make the Quadruped (named leggy) save multiple different states in files, then load those files as commands causing it to move in specific ways

## Setup
the Quadruped starts with the basic files Standing.json, Lying.json, Waving1 and Waving2. By entering the name of a file (including .json) and pressing the load button in the GUI, it will set the slider values to the entered files values, showing the state that file recorded, by pressing save, it will overwrite the entered state or create a file named after your entry (again, ensure that .json is at the end). Pressing Update Positions will send the current state of the sliders to the robot, moving it. you can test the positions before saving a file, and when you are happy with the positions, press save to load it again in the future.

## Commands
Once you have set states for the Quadruped, you can then program a button to run a command. there is a demonstration caled wave() in Multi_StateCommands. you can load and send states to the robot in sequence and delay them by fractions of a second to ensure the motors get to their states. by loading each state the motors will attempt to reach that position and wait for their next command to once again move.

To create a command you must create a function in Multi_StateCommands, from there in the QuadrupedGUI you can create a button that calls that function, then you can have a fixed set of commands you can call from the GUI.
