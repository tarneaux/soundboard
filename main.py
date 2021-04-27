import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import os
from pygame import mixer
from functools import partial


class App:
    def __init__(self):
        mixer.init()
        win = Gtk.Window()
        win.connect("destroy", Gtk.main_quit)
        self.grid = Gtk.Grid()
        win.add(self.grid)
        self.buildButtons()
        self.gridElements()
        stopButton = Gtk.Button(label="[Stop]")
        stopButton.connect("clicked", self.stopMusic)
        self.grid.attach(stopButton, 2, self.height, 1, 1)
        win.show_all()
        Gtk.main()
    def stopMusic(self, junk):
        mixer.music.stop()
    def buildButtons(self):
        self.elements = []
        for file in os.listdir("."):
            if file.endswith(".mp3"):
                self.elements.append(Gtk.Button(label=file[:-4]))
                self.elements[len(self.elements) - 1].connect("clicked", partial(self.play, file))
    def gridElements(self):
        x = 0
        y = 1
        for b in self.elements:
            x += 1
            if x == 3:
                x = 1
                y += 1
            self.grid.attach(b, x, y, 1, 1)
        self.height = y+1

    def play(self, file, junk):
        mixer.music.load(os.path.join(".", file))
        mixer.music.play()

App()
