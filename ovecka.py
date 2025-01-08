import time
import random
import pygame
import os

#krouzit
def circle_text(text, width=10, height=5, speed=0.2):
    for i in range(width + height):
        os.system('cls' if os.name == 'nt' else 'clear')
        if i < width:  # Posun doprava
            print(" " * i + text)
        elif i < width + height:  # Posun dolů
            print("\n" * (i - width) + " " * width + text)
        time.sleep(speed)




# ovecka.py
from ovecka_splash import SplashScreen

# Zobrazení splash screenu
splash = SplashScreen(title="Ovečka Počítání", bg_color=(50, 50, 200))  # Modré pozadí
splash.show(message="Ovečka Počítání... 🐑", font_size=50, duration=5)

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

    # Animace
    for i in range(20):
        os.system('cls' if os.name == 'nt' else 'clear')

        # Odsazení pro pohyb
        print(" " * i + sheep_art2)

        time.sleep(0.2)



# prehraje ovecku
def ovecka():
    # Inicializace mixeru
    pygame.mixer.init()
    # Načtení hudebního souboru
    pygame.mixer.music.load("ovecka.mp3")  # Nahraď cestu svým souborem
    # Přehrávání hudby
    pygame.mixer.music.play()
    # Udržení programu spuštěného, dokud se hudba nepřehraje
   # while pygame.mixer.music.get_busy():
    #    pass  # Čekej, dokud hudba hraje

def chrapani():
        # Inicializace mixeru
        pygame.mixer.init()
        # Načtení hudebního souboru
        pygame.mixer.music.load("chrap.mp3")  # Nahraď cestu svým souborem
        # Přehrávání hudby
        pygame.mixer.music.play()
        # Udržení programu spuštěného, dokud se hudba nepřehraje
        while pygame.mixer.music.get_busy():
            pass  # Čekej, dokud hudba hraje


def predchrap():
    # Inicializace mixeru
    pygame.mixer.init()
    # Načtení hudebního souboru
    pygame.mixer.music.load("predchrap.mp3")  # Nahraď cestu svým souborem
    # Přehrávání hudby
    pygame.mixer.music.play()
    # Udržení programu spuštěného, dokud se hudba nepřehraje
    while pygame.mixer.music.get_busy():
        pass  # Čekej, dokud hudba hraje




def nahodny_pes():
    characters = ('pes zeryk', 'pes alik', 'kocour_v_botach', 'mickey_mouse', 'koucour_mikes', 'sponge_bob')
    random_char = random.choice(characters)
    return (f" {random_char}")

def smilik():
    sheep_emojis = ["!!!","normalne mi hrabe" ,"🐏","???" ,"🦙", "🐂" ,"jakto ze nechrapes" ,"🚀", "😄", "🤪", "🤓"]
    random_emoji = random.choice(sheep_emojis)
    return random_emoji

def count_sheep(n):
    print("Začínáme počítat ovečky...")
    if n == 0:
        return ""
    result = ""
    for i in range(1, n + 1):

        print(f"{i} ovecka..." , end=" ", flush=True)  # Vypiš okamžitě
        time.sleep(2)  # Pauza na 1 sekundu

        #result += (f"{i}  ovecka... ")
        if (i % 3 == 0):
         predchrap()

        #result += f"{nahodny_pes()} \n "
         print(f"{nahodny_pes()} \n ")
         print(f'{smilik()}', end=" ")
         ovecka()
    return result

nakreslena_ovecka()
j= (input("jak moc se ti chce spat ? malo , dost , strasne ?" ))


if (j == "malo"):
    i = 10
elif (j == "dost"):
     i = 20
elif (j == "strasne"):
      i = 30

print(count_sheep(i))
print (f"a ... nakonec {(nahodny_pes())}")
print (f"takovych ovecek ..uz koukej chrapat ")
chrapani()
print('🐑 🚀 😄 🤪 🤓')
nakreslena_ovecka()
circle_text("Dobrou noc", width=20, height=5, speed=0.1)



