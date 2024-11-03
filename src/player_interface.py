from src.game import Game

class PlayerInterface:
    """класс взаимодействия с игроком
    
    единственное поле класса:
    1) game
    """
    
    game = None
    
    def __init__(self):
        self.game = None

    def start_game(self):
        """запускаем игру
        """
        self.game = Game()

        print(f"Hello\nTry to guess {self.game.word_length}-letter word in {self.game.num_of_tries} attempts. Good luck)")

    def get_word(self):
        """считываем слово

        Returns:
            str: считанное слово
        """
        return input("Введите слово: ").strip().lower()

    def show_result(self, result):
        """вывести результат после конца игры

        Args:
            result (void): вывести поздравление с победой/утешение по по поводу проигрыша в зависимости от result
        """
        if result:
            print("Поздравляем! Вы угадали слово!")
        else:
            print("Вы проиграли. Загаданное слово было:", self.game.word)

    def play(self):
        """основной игровой цикл
        """
        
        while not self.game.out_of_attempts():
            word = self.get_word()
            _ = self.game.guess_word(word)
            if isinstance(_, str):
                print(_)
                
            if _ == "Вы угадали слово!":
                self.show_result(True)
                return
        
        self.show_result(False)
        
if __name__ == "__main__":
    interface = PlayerInterface()
    interface.start_game()
    interface.play()