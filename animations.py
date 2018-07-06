import pygame

def animateVertically(pl, st, tab):
    while pl.xIncrement != 0:
        if int(pl.xIncrement/7)%len(tab) == 0:
            screen.blit()