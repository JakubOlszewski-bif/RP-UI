"""Define the Character class with stats, equipment, stuff"""

class Character:
    def __init__(self) -> None:
        self.level = 1
        self.name = ''
        self.char_class = ''

        # Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma
        self.stats = [0,0,0,0,0,0]

    def setup_character(self):
        pass

if __name__ == "__main__":
    a = Character()