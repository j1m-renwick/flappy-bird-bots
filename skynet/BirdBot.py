from assets.Bird import Bird
from skynet.PredictiveNeuralNet import PredictiveNeuralNet


class BirdBot(Bird):
    score = 0

    def __init__(self, screen, brain=None):
        super().__init__(screen)
        if brain is not None:
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
