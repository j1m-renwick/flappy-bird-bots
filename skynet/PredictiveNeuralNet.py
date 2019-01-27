import numpy as np
from copy import deepcopy
from random import *
import pickle


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def mutate(current_value, mutation_rate):
    if random() < mutation_rate:
        offset = np.random.normal(scale=0.5)
        return current_value + offset
    else:
        return current_value


# A neural net with feedforward predictive capabilities ONLY.  Cannot be trained.
class PredictiveNeuralNet:

    # def __init__(self, numberOfInputNodes, numberOfHiddenNodes, numberOfOutputNodes):
    #     self.numI = numberOfInputNodes
    #     self.numH = numberOfHiddenNodes
    #     self.numO = numberOfOutputNodes
    #     self.createWeightMatrices();

    def __init__(self, listOfNodes):
        self.totalNodeList = listOfNodes
        self.createWeightMatrices()

    def setInputData(self, inputVector):
        # sets a numpy row vector and bias as the input vector layer.
        # append 1 to the front as a bias value - e.g. [1,x,y,z,....] )
        # print("INPUT")
        # print(inputVector)
        biasAndInputs = np.append(np.array([1]), inputVector)
        # convert the row vector to a column vector
        self.inputData = biasAndInputs[np.newaxis].T
        # print(self.inputData)

    def createWeightMatrices(self):
        # set up weight matrices with random starting values
        # input->hidden: numH x numI (+ 1 random bias weight to each row)
        self.weightsIH = np.random.uniform(low=-1, high=1, size=(self.numH, self.numI + 1))
        # self.weightsIH = np.random.random((self.numH, self.numI+1))
        # hidden->ouput: numO x numH (+ 1 random bias weight to each row)
        self.weightsHO = np.random.uniform(low=-1, high=1, size=(self.numO, self.numH + 1))
        # self.weightsHO = np.random.random((self.numO,self.numH+1))

    def createWeightMatrices(self):
        # set up weight matrices with random starting values
        # layer1->layer2: numLayer2 x numLayer1 (+ 1 random bias weight to each row)

        self.weightsList = []

        for i in range(len(self.totalNodeList) - 1):
            self.weightsList.append(
                np.random.uniform(low=-1, high=1, size=(self.totalNodeList[i + 1], self.totalNodeList[i] + 1)))

    # def predict(self):
    #     # feedforward for input->hidden layer (dot product of the weights and the inputs)
    #     self.hiddenData = self.weightsIH.dot(self.inputData)
    #     # apply activation function (sigmoid in this case)
    #     self.hiddenData = np.array(list(map(sigmoid, self.hiddenData)))
    #     # add a bias of 1 to the hiddenData before feeding forward again
    #     self.hiddenData = np.append(np.array([1]), self.hiddenData)[np.newaxis].T
    #     # feedforward for hidden->output layer (dot product of the weights and the hidden inputs)
    #     self.outputData = self.weightsHO.dot(self.hiddenData)
    #     # apply activation function (sigmoid in this case)
    #     self.outputData = np.array(list(map(sigmoid, self.outputData)))
    #     # print("OUTPUT")
    #     # print(self.outputData)
    #     # return a column vector of N outputs
    #     return self.outputData

    def predict(self):

        # initialise current data to be the supplied inputs
        currentData = self.inputData
        # feed the data forward for each layer
        for i in range(len(self.totalNodeList) - 2):
            # - multiply the weight matrix by the data
            weightedData = self.weightsList[i].dot(currentData)
            # - run the result through the activation function
            activatedData = np.array(list(map(sigmoid, weightedData)))
            # - add a new bias to the matrix
            biasedData = np.append(np.array([1]), activatedData)[np.newaxis].T
            # - set matrix as the currentData
            currentData = biasedData

        # for the last hidden layer to output layer mapping, only multiply by the weights and
        # run through the activation function - no bias
        weightedData = self.weightsList[-1].dot(currentData)
        # - run the result through the activation function
        activatedData = np.array(list(map(sigmoid, weightedData)))
        return activatedData

    def copy(self):
        copiedSelf = deepcopy(self)
        # clear the input data, just in case...
        copiedSelf.inputData = None
        return copiedSelf

    # def mutate(self, mutationRate):
    #     # mutate the brain!!....nerg....argh.....kill all humans...etc
    #     self.weightsIH = np.array(list(map(lambda p: mutate(p, 0.1), self.weightsIH)))
    #     self.weightsHO = np.array(list(map(lambda p: mutate(p, 0.1), self.weightsHO)))
    #     return self

    def mutate(self, mutationRate):
        # mutate the brain!!....nerg....argh.....kill all humans...etc
        for mat in self.weightsList:
            for i in range(len(mat) - 1):
                mat[i] = np.array(list(map(lambda p: mutate(p, mutationRate), mat[i])))

        return self

    def persist(self, fileName):
        binary_file = open(fileName, mode='wb')
        pickle.dump(self, binary_file)
        binary_file.close()
        return

    @staticmethod
    def load(fileName):
        binary_file = open(fileName, "rb")
        loadedNeuralNet = pickle.load(binary_file)
        binary_file.close()
        return loadedNeuralNet

# nn = PredictiveNeuralNet([2,10,5,2])
#
# # get the computed actions based on the inputs
# nn.setInputData(np.array([1.2,0.4]))
#
# print(nn.predict())
# aa = nn.copy()
# aa = aa.mutate(1)
# aa.setInputData(np.array([1.2,0.4]))
# print(aa.predict())
