import pygame
from FpsTimer import FpsTimer

# TODO: should probably move al logical to seperate file. Keep this one for initialisation/debugging/other purposes

fps = 60
fps_timer = FpsTimer(fps)

cntr = 0
while True:
    cntr += 1

    if cntr == 3 * fps + 1:
        break

    fps_timer.endFrame()
