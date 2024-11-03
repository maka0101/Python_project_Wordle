import unittest
from src.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        """набор команд, которые надо выполнить перед каждым тестом
        """
        self.game = Game()
        self.game.word = "apple"

    def test_generate_word(self):
        """проверяем, что генерируется строка нужной длины
        """
        word = self.game.generate_word()
        self.assertEqual(len(word), self.game.word_length)
        self.assertIsInstance(word, str)

    def test_word_exist(self):
        """проверяем, что сгенерированное слово реально существует
        """
        self.assertTrue(self.game.check_word_exist("apple"))
        self.assertFalse(self.game.check_word_exist("bzbzb"))

    def test_word_already_been(self):
        """проверяем, было ли слово уже использовано
        """
        self.game.words.append("apple")
        self.assertTrue(self.game.check_word_already_been("apple"))
        self.assertFalse(self.game.check_word_already_been("money"))

    def test_guess_word_guessed(self):
        """функция guess_word
        сценарий:
        угадали загаданное слово
        """
        result = self.game.guess_word("apple")
        self.assertEqual(result, "Вы угадали слово!")

    def test_guess_word_incorrect_length(self):
        """функция guess_word
        сценарий:
        некорректная длина слова
        """
        result = self.game.guess_word("pd")
        self.assertEqual(result, "Некорректная длина слова.")

    def test_guess_word_not_exist(self):
        """функция guess_word
        сценарий:
        слово не существует
        """
        result = self.game.guess_word("bzbzb")
        self.assertEqual(result, "Слово не найдено в словаре.")

    def test_guess_word_already_been(self):
        """функция guess_word
        сценарий:
        слово уже вводилось
        """
        self.game.words.append("apple")
        result = self.game.guess_word("apple")
        self.assertEqual(result, "Слово уже было введено.")

if __name__ == "__main__":
    unittest.main()