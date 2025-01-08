import time
import random
import pygame
import os

#krouzit
def circle_text(text, width=10, height=5, speed=0.2):
    for i in range(width + height):
        os.system('cls' if os.name == 'nt' else 'clear')
        if i < width:  # GO rght
            print(" " * i + text)
        elif i < width + height:  # Go DOwn
            print("\n" * (i - width) + " " * width + text)
        time.sleep(speed)




# ovecka.py
from ovecka_splash import SplashScreen

# Splash screen
splash = SplashScreen(title="Counting Sheeps", bg_color=(50, 50, 200))  # Modré pozadí
splash.show(message="Counting Sheeps... 🐑", font_size=50, duration=5)

def nakreslena_ovecka():
    sheep_art = """
       __  _
      (oo)\\_______
      (__)\\       )\\/\\
          ||----w |
          ||     ||
    """
    print(sheep_art)


def nakreslena_ovecka2():
    sheep_art2 = """""
          __  _
         (oo)\\_______
         (__)\\       )\\/\\
             ||----w |
             ||     ||
       """

    # Animation
    for i in range(20):
        os.system('cls' if os.name == 'nt' else 'clear')

        # move
        print(" " * i + sheep_art2)

        time.sleep(0.2)



# sound
def ovecka():
    # Inicializace mixeru
    pygame.mixer.init()
    # Načtení hudebního souboru
    pygame.mixer.music.load("ovecka.mp3")  # You can modify whatever you want
    # Music Play
    pygame.mixer.music.play()
   

def chrapani():
        # Mixer
        pygame.mixer.init()
        # Sound Loading
        pygame.mixer.music.load("chrap.mp3")  # You can modify whatever you want
        # Music Play
        pygame.mixer.music.play()
        # Keep stay until play stop
        while pygame.mixer.music.get_busy():
            pass  # Wait


def predchrap():
    # Inicializace mixeru
    pygame.mixer.init()
    # Načtení hudebního souboru
    pygame.mixer.music.load("predchrap.mp3")  # You can choose what ever you want
    # Music play
    pygame.mixer.music.play()
    # Keep stay until play stop
    while pygame.mixer.music.get_busy():
        pass  # Wait till play




def nahodny_pes():
    characters = ('dog zeryk', 'dog alik', 'cat_in_boots', 'mickey_mouse', 'cat_mikes', 'sponge_bob')
    random_char = random.choice(characters)
    return (f" {random_char}")

def smilik():
    sheep_emojis = ["!!!","Im really really crazy" ,"🐏","???" ,"🦙", "🐂" ,"sleep NOW" ,"🚀", "😄", "🤪", "🤓"]
    random_emoji = random.choice(sheep_emojis)
    return random_emoji

def count_sheep(n):
    print("Start Counting Sheeps...")
    if n == 0:
        return ""
    result = ""
    for i in range(1, n + 1):

        print(f"{i} sheeps..." , end=" ", flush=True)  # Write
        time.sleep(2)  # Pause 1 sec

       
        if (i % 3 == 0):
         predchrap()

        
         print(f"{nahodny_pes()} \n ")
         print(f'{smilik()}', end=" ")
         ovecka()
    return result

nakreslena_ovecka()
j= (input("How much you want to sleep? little , more , lot ?" ))


if (j == "little"):
    i = 10
elif (j == "more"):
     i = 20
elif (j == "lot"):
      i = 30

print(count_sheep(i))
print (f"and ... last {(nahodny_pes())}")
print (f"sooo much sheeps  ..GO sleep GO GO GO  ")
chrapani()
print('🐑 🚀 😄 🤪 🤓')
nakreslena_ovecka()
circle_text("Good Night", width=20, height=5, speed=0.1)



