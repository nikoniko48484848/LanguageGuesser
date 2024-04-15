import re


class Tester(object):
    alphabetDict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                    "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                    "y": 0,
                    "z": 0}
    weights = []

    def readText(self, text):
        for char in text:
            if not re.match(r'[a-zA-Z]', char):
                text = text.replace(char, '')
        return text.lower()

    def countLetters(self, text):
        for char in text:
            self.alphabetDict[char] += 1

    def setWeights(self, text):
        self.countLetters(text)
        for weight in self.alphabetDict.values():
            self.weights.append(weight / len(text))
        print(self.weights)