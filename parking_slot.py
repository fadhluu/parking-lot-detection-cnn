from car import car
from datetime import datetime
from dateutil import relativedelta


class parking_slot():
    def __init__(self, pos_x, pos_y, number):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.number = number
        self.status = False  # True = occupied, False = empty
        self.car_id = 0
        self.car = None
        self.occupied_at = None
        self.empty_at = datetime.now()

    def assign_spot(self, car_list):
        for car in car_list:
            car_center = car.get_car_center()
            if car_center[0] in range(self.pos_x[0], self.pos_x[1]) and car_center[1] in range(self.pos_y[0], self.pos_y[1]):
                self.status = True
                self.set_car(car)
                self.occupied_at = self.get_time_now()

    def scan_spot(self, car_list):
        for car in car_list:
            car_center = car.get_car_center()
            if car_center[0] not in range(self.pos_x[0], self.pos_x[1]) and car_center[1] not in range(self.pos_y[0], self.pos_y[1]):
                self.status = False
                self.set_car(None)
                self.empty_at = self.get_time_now()

    def set_car(self, car):
        self.car = car

    def get_status(self):
        if self.status:
            return '| Occupied |'
        else:
            return '| Empty |'

    def get_pos_x_and_y(self):
        return [self.pos_x[0], self.pos_y[1]]

    def get_time_now(self):
        return datetime.now()

    def get_empty_time(self):
        diff = relativedelta.relativedelta(self.empty_at, self.occupied_at)
        time_diff = [diff.hours, diff.minutes, diff.seconds]
        return time_diff
