import pygame
pygame.mixer.init()

pygame.mixer.music.load("audio.mp3")

pygame.mixer.music.set_volume(0.3)

pygame.mixer.music.play()