from assets.Bird import Bird
from skynet.PredictiveNeuralNet import PredictiveNeuralNet


class BirdBot(Bird):

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
    score = 0

    def __init__(self, screen, brain = None):
        super().__init__(screen)
        if (brain != None):
            self.net = brain
        else:
            self.net = PredictiveNeuralNet([4, 4, 1])
        self.fitness = -1

    def input_data(self, data):
        self.net.setInputData(data)

    def animate(self):
        self.score += 1
        if self.net.predict()[0][0] > 0.5:
            super().jump()
        super().animate()
