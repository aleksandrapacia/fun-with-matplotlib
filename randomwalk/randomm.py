from random import choice

class RandomWalk():  # page/407
    def __init__(self, numberOfPoints=400):
        self.numberOfPoints = numberOfPoints
        self.xs = [0]
        self.ys = [0]

    def walkk(self):
        while len(self.xs) < self.numberOfPoints:

            x_direction = choice([1,2,3]) # 1: right / -1: left
            x_distance = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.xs[-1] + x_step
            y = self.ys[-1] + y_step

            self.xs.append(x)
            self.ys.append(y)
