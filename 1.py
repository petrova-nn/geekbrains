# 1. Создайте класс Word.
# 2. Добавьте свойства text и part of speech.
# 3. Добавьте возможность создавать объект слово со значениями в скобках.
# 4. Создайте класс Sentence
# 5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
# 6. Добавьте метод show, составляющий предложение.
# 7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.

# 1. Создайте классы Noun и Verb.
# 2. Настройте наследование от Word.
# 3. Добавьте защищенное свойство «Грамматические характеристики».
# 4. Перестройте работу метода show класса Sentence.
# 5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.

from random import shuffle

class Word:

     def get_types(self):
        return self.__grammar_types

     def __init__(self, text="", part="", grammar_types=""):
        self.text = text
        self.part_of_speech = part
        self.__grammar_types = grammar_types

class Noun(Word):

# если не переопределять get_types(self), возникает ошибка AttributeError: 'Noun' object has no attribute '_Word__grammar_types'
# тоже самое, если убрать строку self.__grammar_types = grammar_types
# не понимаю, почему

    def get_types(self):
        return self.__grammar_types

    def __init__(self, text="", grammar_types=""):
        self.text = text
        self.part_of_speech="существительное"
        self.__grammar_types = grammar_types

class Verb(Word):

    def get_types(self):
        return self.__grammar_types

    def __init__(self, text="", grammar_types=""):
        self.text = text
        self.part_of_speech="глагол"
        self.__grammar_types = grammar_types

class Sentence:
    content = []
    sent = ""

    def show(self):
        shuffle(self.word)
        for i, w in enumerate(self.word):
            if w == self.word[0]:
                w = w.title()
            if w == self.word[-1]:
                w = "{}.".format(w)
            self.sent = "{0}{1} ".format(self.sent, w)
            self.content.append(i)
        return self.sent.rstrip()

    def show_parts(self):
        self.parts = filter(None, set(", ".join(self.types).split(', ')))
        return list(self.parts)

    def __init__(self, word, part, types):
        self.word = word
        self.part = part
        self.types = types


word5 = Noun("снег", "мужской род, единственное число, именительный падеж")
word6 = Verb("идет", "мужской род, единственное число, настоящее время")
word3 = Word("утром", "наречие")
word4 = Word("сегодня", "наречие")

d={}
#
# word1 = Word("компьютер", "существительное")
# word2 = Word("загружен", "глагол")
# word3 = Word("утром", "наречие")
# word4 = Word("сегодня", "наречие")
#
d['w'] = [word5.text, word6.text, word4.text, word3.text]
d['ps'] = [word5.part_of_speech, word6.part_of_speech, word4.part_of_speech, word3.part_of_speech]
d['types'] = [word5.get_types(), word6.get_types(), word4.get_types(), word3.get_types()]
#print("Загруженный список слов:\n{}\n".format(d))
sent = Sentence(d['w'],d['ps'],d['types'])
print("Предложение:\n{}\n".format(sent.show()))
print("Грамматические характеристики:\n{}\n".format(sent.show_parts()))
# я поняла, что content надо передавать на вход, но так пока и оставила - на выход
print("Номера слов:\n{}".format(sent.content))

