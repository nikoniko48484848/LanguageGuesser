from Perceptron import Perceptron


class Trainer:
    def __init__(self, perceptron: Perceptron):
        self.perceptron = perceptron

    def calculateNetValue(self, inputVector):
        netValue = 0
        for i in range(len(inputVector)):
            netValue += float(inputVector[i]) * self.perceptron.weights[i]
        netValue -= self.perceptron.bias
        # print("Vector")
        # print("Net Value: ",netValue)
        return netValue

    # def calculateNetForTest(self):


    def activate(self, inputVector):
        if self.calculateNetValue(inputVector) > self.perceptron.threshold:
            self.perceptron.y = 1
        else:
            self.perceptron.y = 0

    def assignClass(self, inputVector):
        self.activate(inputVector)
        # print("Output: ",self.perceptron.y)
        if self.perceptron.y == 0:
            self.perceptron.assignedClass = ""
        else:
            self.perceptron.assignedClass = self.perceptron.myLanguage
        # print("Assigned Class: ", self.perceptron.assignedClass)

    def deltaFunction(self, inputVector, vectorRealClass):
        self.assignClass(inputVector)
        learningRate = 0.1  # 0.00001
        if self.perceptron.assignedClass == vectorRealClass:
            decision = 1
        else:
            decision = -1

        inputMultipliedByLR = []
        for val in inputVector:
            newVal = float(val) * learningRate * decision
            inputMultipliedByLR.append(newVal)

        # print(inputMultipliedByLR)
        # print("+++++++++++++++++++++++")
        # print("Weights before delta: ", self.perceptron.weights)

        for i in range(len(inputMultipliedByLR)):
            self.perceptron.weights[i] += inputMultipliedByLR[i]
        self.perceptron.bias += -1 * learningRate * decision
        # print(self.perceptron.bias)

        # print("Threshold: ", self.perceptron.threshold, " + ", learningRate * decision, end="")
        # print(" = ", self.perceptron.threshold)
        #
        # print("Weights after delta: ", self.perceptron.weights)

    def train(self):
        inputVec = self.perceptron.weights
        self.deltaFunction(inputVec, self.perceptron.myLanguage)

    def test(self, inputVector):
        print("Net value for", self.perceptron.myLanguage, ":", self.calculateNetValue(inputVector))
        self.activate(inputVector)
        return self.calculateNetValue(inputVector)
        # print()
        # if self.perceptron.y == 1:
        #     # print("Language of the text is: " + self.perceptron.myLanguage)
        # else:
        #     # print("Perceptron chose the wrong language")
