from pprint import pprint

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names
        self.file_name = 'test_file.txt'
        file_name = open(self.file_name, 'w', encoding='utf-8')
        file_name.write(f"It's a text for task Найти везде,\n"
                        f"Используйте его для самопроверки.\n"
                        f"Успехов в решении задачи!\n"
                        f"text text text")
        file_name.close()

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(i, '')
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1
            else:
                result[file_name] = None
        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего