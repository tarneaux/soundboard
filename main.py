from tkinter import Tk, Button
import os
from pygame import mixer
from functools import partial


class App:
    def __init__(self):
        mixer.init()
        self.root = Tk()
        self.buildButtons()

        self.gridElements()
        stopButton = Button(self.root, text="[Stop]", command=mixer.music.stop)
        xSize, ySize = self.root.grid_size()
        print(ySize)
        stopButton.grid(column=3, row=ySize)
        self.root.mainloop()

    def buildButtons(self):
        self.elements = []
        for file in os.listdir("sounds"):
            if file.endswith(".mp3"):
                self.elements.append(Button(self.root, text=file[:-4], command=partial(self.play, file)))
    def gridElements(self):
        x = 0
        y = 1
        for b in self.elements:
            x += 1
            if x == 4:
                x = 1
                y += 1
            b.grid(column=x, row=y)

    def play(self, file):
        mixer.music.load(os.path.join("sounds", file))
        mixer.music.play()

App()