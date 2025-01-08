# splash_screen.py
import pygame
import time

class SplashScreen:
    def __init__(self, width=600, height=400, title="Splash Screen", bg_color=(30, 30, 30)):
        pygame.init()
        self.width = width
        self.height = height
        self.title = title
        self.bg_color = bg_color
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def show(self, message="Welcome!", font_size=60, duration=3):
        self.screen.fill(self.bg_color)  # Nastavíme barvu pozadí

        # Přidáme text
        font = pygame.font.Font(None, font_size)
        text = font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)

        # Aktualizace obrazovky
        pygame.display.flip()

        # Zobrazení splash screenu na danou dobu
        time.sleep(duration)

        # Ukončení pygame
        pygame.quit()
