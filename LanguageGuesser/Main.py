import os

from Perceptron import Perceptron
from Tester import Tester
from Trainer import Trainer

tester = Tester()

perceptrons = []
trainers = []


for lang in os.listdir("Languages"):
    perceptrons.append(Perceptron(lang))

n = 500 # how many trainings

for p in perceptrons:
    trainer = Trainer(p)
    trainer.perceptron.setWeights(trainer.perceptron.readFiles())
    i = 0
    while i != n:
        trainer.train()
        i += 1
    trainers.append(trainer)

inputText = input("Paste a long text")
tester.setWeights(tester.readText(inputText))
inputVec = tester.weights

result = {}

for trainer in trainers:
    result[trainer.perceptron.myLanguage] = trainer.test(inputVec)  #(trainer.perceptron.myLanguage, trainer.test(inputVec))
    # result.append(trainer.perceptron.y)
    # if trainer.perceptron:
    #     print("Language of the text is ", trainer.perceptron.myLanguage)

print("Language of the given text is: ", max(result, key=result.get))

# p.setWeights(p.readFiles())