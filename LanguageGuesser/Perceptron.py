import os
import random
import re


class Perceptron:

    languageDir = "Languages"
    myLanguage = ""
    def __init__(self, myLanguage):
        self.alphabetDict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                    "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0,
                    "z": 0}
        self.y = 0
        self.myLanguage = myLanguage
        self.weights = []
        self.bias = 0
        self.threshold = 0
        self.assignedClass = ""
        self.realClass = myLanguage

    def readFiles(self):
        languageData = ""
        for fileName in os.listdir(self.languageDir + "/" + self.myLanguage):
            file = open(self.languageDir + "/" + self.myLanguage + "/" + fileName)
            fileData = file.read()
            for char in fileData:
                if not re.match(r'[a-zA-Z]', char):
                    fileData = fileData.replace(char, '')
            languageData += fileData.lower()
        return languageData

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
        # print(self.alphabetDict.values(), "    ", len(text))