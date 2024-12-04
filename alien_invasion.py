import sys

import pygame


class AlienInvasion:
    """zarzadzanie zasobami"""

    def __init__(self):
        "inicalizacja"
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Inwazja obcych")

    def run_game(self):
        """pętla główna"""
        while True:
            # Oczekiwanie na naciśniecie klawisza lub przycisku
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                pygame.display.flip()


if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie
    ai = AlienInvasion()
    ai.run_game()