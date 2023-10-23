import pygame

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Example usage
mp3_file = "./audio/concat.mp3"
play_mp3(mp3_file)


import visceralscrape
import infotransmitor

