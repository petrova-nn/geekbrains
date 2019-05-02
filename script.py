# 1. Создайте класс Word.
# 2. Добавьте свойства text и part of speech.
# 3. Добавьте возможность создавать объект слово со значениями в скобках.
# 4. Создайте класс Sentence
# 5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
# 6. Добавьте метод show, составляющий предложение.
# 7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.
import random


class Word:
    text = "UN"
    part_of_speech = "UN"

    def __init__(self, text, part):
        self.text = text
        self.part_of_speech = part


class Sentence:
    content = []
    sent = ""
    parts = []

    def show(self):
        random.shuffle(self.word)
        for w in self.word:
            if w == self.word[0]:
                w = w.title()
            if w == self.word[-1]:
                w = "{}.".format(w)
            self.sent = "{0}{1} ".format(self.sent, w)
        return self.sent

    def show_parts(self):
        self.parts = set(self.part)
        return self.parts

    def __init__(self, word, part):
        self.word = word
        self.part = part
        for n in range(len(word)):
            self.content.append(n+1)

d={}

word1 = Word("компьютер", "существительное")
word2 = Word("загружен", "глагол")
word3 = Word("утром", "наречие")
word4 = Word("сегодня", "наречие")

d['w'] = [word1.text, word2.text, word4.text, word3.text]
d['ps'] = [word1.part_of_speech, word2.part_of_speech, word4.part_of_speech, word3.part_of_speech]
print("Загруженный список слов:\n{}\n".format(d))
sent = Sentence(d['w'],d['ps'])
print("Предложение:\n{}\n".format(sent.show()))
print("Части речи в предложении:\n{}\n".format(sent.show_parts()))
# я не поняла задание  - что такое "свойство content, равное списку, состоящему из номеров слов, входящих в предложение"
# поэтому в списке просто номера слов
print("Номера слов:\n{}".format(sent.content))
