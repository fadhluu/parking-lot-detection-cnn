class car():
    def __init__(self, number, pos_x, pos_y):
        self.number = number
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_car_center(self):
        cc = [(self.pos_x[1] - self.pos_x[0]) + self.pos_x[0],
              (self.pos_y[1] - self.pos_y[0]) + self.pos_y[0]]
        return cc
