import tkinter as tk
import json
import serial
import time

class SerialCommunicator:
    """Handles serial communication with the Pico."""
    
    def __init__(self, port='COM6', baud_rate=115200):
        self.serialPath = serial.Serial(port, baud_rate)

    def send_command(self, command):
        sentData = command
        x = sentData.encode()
        self.serialPath.write(x)

class Multi_StateCommands:

    def wave(self):
        QuadrupedGUI.load_state(self, "Waving1.json")
        QuadrupedGUI.update_pico(self)
        time.sleep(1)
        QuadrupedGUI.load_state(self, "Waving2.json")
        QuadrupedGUI.update_pico(self)
        time.sleep(1)
        QuadrupedGUI.load_state(self, "Waving1.json")
        QuadrupedGUI.update_pico(self)
        time.sleep(1)
        QuadrupedGUI.load_state(self, "Waving2.json")
        QuadrupedGUI.update_pico(self)
        time.sleep(1)
        QuadrupedGUI.load_state(self, "Standing.json")
        QuadrupedGUI.update_pico(self)
        time.sleep(1)

class QuadrupedGUI:
    """Main GUI class for controlling the quadruped robot."""
    
    def __init__(self, root):
        """Initialize the GUI."""
        self.forwardRightHip = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL)
        self.forwardRightFoot = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL)
        self.forwardLeftHip = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL)
        self.forwardLeftFoot = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL)
        self.backwardRightHip = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL)
        self.backwardRightFoot = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL)
        self.backwardLeftHip = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL)
        self.backwardLeftFoot = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL)
        
        
        
    def create_gui(self):
        """Create the GUI elements."""
        
        self.forwardRightHip.pack()
        self.forwardRightFoot.pack()
        self.forwardLeftHip.pack()
        self.forwardLeftFoot.pack()
        self.backwardRightHip.pack()
        self.backwardRightFoot.pack()
        self.backwardLeftHip.pack()
        self.backwardLeftFoot.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        tk.Button(root, text="Save", command= lambda : QuadrupedGUI.save_state(self, self.entry.get())).pack()
        tk.Button(root, text="Load", command= lambda : QuadrupedGUI.load_state(self, self.entry.get())).pack()
        tk.Button(root, text="Update Positions", command= lambda : QuadrupedGUI.update_pico(self)).pack()
        tk.Button(root, text="Wave", command= lambda : Multi_StateCommands.wave(self)).pack()
        

        


    def update_pico(self):
        sentData = (f"{self.forwardRightHip.get()},{self.forwardRightFoot.get()},{self.forwardLeftHip.get()},{self.forwardLeftFoot.get()},{self.backwardRightHip.get()},{self.backwardRightFoot.get()},{self.backwardLeftHip.get()},{self.backwardLeftFoot.get()}\n")

        sc = SerialCommunicator()
        sc.send_command(sentData)
        #SerialCommunicator.send_command(sentData)

    def save_state(self, fileName):
        """Save the current state of the robot."""
        print("saved")
        with open(fileName, "w") as file:
            file.write(f"{self.forwardRightHip.get()},{self.forwardRightFoot.get()},{self.forwardLeftHip.get()},{self.forwardLeftFoot.get()},{self.backwardRightHip.get()},{self.backwardRightFoot.get()},{self.backwardLeftHip.get()},{self.backwardLeftFoot.get()}")


    def load_state(self, fileName):
        """Load the last saved state of the robot."""
        print("loaded")
        index = 0
        with open(fileName, "r") as file:
            for line in file:
                hip1, foot1, hip2, foot2, hip3, foot3, hip4, foot4 = line.rstrip().split(",")
                self.forwardRightHip.set(hip1)
                self.forwardRightFoot.set(foot1)
                self.forwardLeftHip.set(hip2)
                self.forwardLeftFoot.set(foot2)
                self.backwardRightHip.set(hip3)
                self.backwardRightFoot.set(foot3)
                self.backwardLeftHip.set(hip4)
                self.backwardLeftFoot.set(foot4)
                


if __name__ == "__main__":
    root = tk.Tk()
    app = QuadrupedGUI(root)
    app.create_gui()
    root.mainloop()
    
