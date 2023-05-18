import os
import random
import pygame
import sys
import select

dir_songs = "./Playlist"

while True:
	# Get a list of all songs in the directory
 songs = os.listdir(dir_songs)

	# Shuffle the list of songs
 random.shuffle(songs)

	# Initialize pygame and the mixer
 pygame.mixer.init()

# Play the songs in the shuffled order
 for file in songs:
    # Construct the path to the song file
    song_path = os.path.join(dir_songs, file)

    # Load the song
    pygame.mixer.music.load(song_path)

    # Play the song
    pygame.mixer.music.play()

    paused = False
    song_timer = 0
    max_timer = 29
    print("Options:")
    print("p. Pause")
    print("r. Resume")
    print("n. Next")
    print("q. Quit")
    # Wait for user input or song completion
    while pygame.mixer.music.get_busy() or paused:
        
        if sys.stdin in select.select([sys.stdin], [], [], max_timer-song_timer)[0]:
            

            choice = input(" ")

            if choice == "p":
                if not paused:
                    # Pause the song
                    pygame.mixer.music.pause()
                    song_timer=pygame.mixer.music.get_pos()//1000
                    paused = True
            elif choice == "r":
                if paused:
                    # Unpause the song
                    pygame.mixer.music.unpause()
                    paused = False
            elif choice == "n":
            # Stop the current song and move to the next one
                pygame.mixer.music.stop()
                break
            elif choice == "q":
                # Stop the music and quit the program
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                exit()
            
        else :
            break
 pygame.mixer.quit()       
