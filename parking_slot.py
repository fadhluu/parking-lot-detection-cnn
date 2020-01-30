class parking_slot():
    def __init__(self, pos_x, pos_y, number):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.number = 0
        self.status = False  # True = occupied, False = empty
        self.car_id = 0

    def assign_spot(self, car_list):
        for car in car_list:
            car_center = [(car.pos_x[1] - car.pos_x[0]) + car.pos_x[0],
                          (car.pos_y[1] - car.pos_y[0]) + car.pos_y[0]]
            if car_center[0] in range(self.pos_x[0], self.pos_x[1]) and car_center[1] in range(self.pos_y[0], self.pos_y[1]):
                self.status = True
                self.set_car_id(car.number)

    def scan_spot(self, car_list):
        for car in car_list:
            car_center = [(car.pos_x[1] - car.pos_x[0]) + car.pos_x[0],
                          (car.pos_y[1] - car.pos_y[0]) + car.pos_y[0]]
            if car_center[0] in range(self.pos_x[0], self.pos_x[1]) and car_center[1] in range(self.pos_y[0], self.pos_y[1]):
                self.status = False

    def set_car_id(self, car_id):
        self.car_id = car_id
