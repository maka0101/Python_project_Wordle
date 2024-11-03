import random
import nltk
from nltk.corpus import words
from xtermcolor import colorize

nltk.download('words')
ENGLISH_WORDS = set(words.words())

class Game:
    """собственно, основной класс Game

    главные поля:
    1) длина слова
    2) число использованных попыток
    3) загаданное слово
    4) лист для хранения уже использованных слов
    """
    word_length = 5,
    num_of_tries = 6,
    word = "", 
    words = []
    
    def __init__(self):
        self.word_length = 5
        self.num_of_tries = 6
        self.word = self.generate_word()
        self.words = []
    
    def generate_word(self):
        """Генерируем слово, которое предстоит отгадывать игроку

        Returns:
            str: собственно, сама строка
        """
        valid_words = [word for word in ENGLISH_WORDS if len(word) == self.word_length]
        return random.choice(valid_words).lower()

    def check_word_exist(self, word):
        """проверяем, существует ли слово(в нашем словаре)

        Args:
            word (str): слово, которое проверяем

        Returns:
            bool: существует/не существует
        """
        return word in ENGLISH_WORDS

    def check_word_already_been(self, word):
        """проверка, на то, что слово уже было введено

        Args:
            word (str): слово, которое проверяем

        Returns:
            bool: уже было/ещё не было
        """
        return word in self.words

    def guess_word(self, word):
        """основной обработчик слова, предыдущие функции - подфункции этой

        Args:
            word (str): слово, которое проверяем

        Returns:
            str/bool: если, слово некорректно -> выводим стрингу с описанием ошибки
            если слово отгадали -> выводим стрингу с поздравлением
            иначе - 1
        """
        if len(word) != self.word_length:
            return "Некорректная длина слова."
        if not self.check_word_exist(word):
            return "Слово не найдено в словаре."
        if self.check_word_already_been(word):
            return "Слово уже было введено."
        
        self.words.append(word)
        
        for i in range(self.word_length):
            if word[i] == self.word[i]:
                print(colorize(word[i], ansi = 2), end = "")
            elif word[i] in self.word:
                print(colorize(word[i], ansi = 3), end = "")
            else:
                print(colorize(word[i], ansi = 1), end = "")
        print("\n")
        
        if word == self.word:
            return "Вы угадали слово!"
        
        return 1

    def out_of_attempts(self):
        """отслеживаем момент, когда завершить игру

        Returns:
            bool: собственно, проверяем, что количество использованных попыток не больше оговоренного
        """
        return len(self.words) >= self.num_of_tries