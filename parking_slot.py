class parking_slot():
    def __init__(self, pos_x, pos_y, number):
        self.pos_x = [0, 0]
        self.pos_y = [0, 0]
        self.number = 0
        self.status = False  # True = occupied, False = empty

    def assign_spot(self, car_list):
        for car in car_list:
            car_center = [(car.x[1] - car.x[0]) + car.x[0],
                          (car.y[1] - car.y[0]) + car.y[0]]
            if car_center[0] in range(self.pos_x[0], self.pos_x[1]) and car_center[1] in range(self.pos_y[0], self.pos_y[1]):
                self.status = True

    def scan_spot(self, car_list):
        for car in car_list:
            car_center = [(car.x[1] - car.x[0]) + car.x[0],
                          (car.y[1] - car.y[0]) + car.y[0]]
            if car_center[0] in range(self.pos_x[0], self.pos_x[1]) and car_center[1] in range(self.pos_y[0], self.pos_y[1]):
                self.status = False
