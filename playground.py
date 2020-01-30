from car import car
from parking_slot import parking_slot
import random
import time

parking_list = []
car_list = []

parking_slot_1 = parking_slot(pos_x=[200, 400], pos_y=[200, 400], number=1)
parking_slot_2 = parking_slot(pos_x=[400, 600], pos_y=[400, 600], number=2)
parking_slot_3 = parking_slot(pos_x=[600, 800], pos_y=[600, 800], number=3)

parking_list.append(parking_slot_1)
parking_list.append(parking_slot_2)
parking_list.append(parking_slot_3)


car_1 = car(number=1, pos_x=[0, 0], pos_y=[0, 0])
car_2 = car(number=2, pos_x=[0, 0], pos_y=[0, 0])
car_3 = car(number=3, pos_x=[0, 0], pos_y=[0, 0])
car_4 = car(number=4, pos_x=[0, 0], pos_y=[0, 0])
car_5 = car(number=5, pos_x=[0, 0], pos_y=[0, 0])

car_list.append(car_1)
car_list.append(car_2)
car_list.append(car_3)
car_list.append(car_4)
car_list.append(car_5)

# for car in car_list:
#     car_center = car.get_car_center()
#     print(car.number, car_center)

# for parking_slot in parking_list:
#     parking_slot.scan_spot(car_list)
#     parking_slot.assign_spot(car_list)
#     print(parking_slot.status, parking_slot.pos_x,
#           parking_slot.pos_y, parking_slot.car.number)

# pos_x = [[450, 550], [300, 500], [400, 250], [700, 500], [530, 120]]
# pos_y = [[450, 550], [250, 350], [600, 400], [900, 200], [650, 350]]

while True:

    # car_1.pos_x[0] = random.randint(200, 700)
    # car_1.pos_x[1] = random.randint(200, 700)
    # car_1.pos_y[0] = random.randint(200, 700)
    # car_1.pos_y[0] = random.randint(200, 700)

    for car in car_list:
        car.pos_x = [random.randint(200, 800), random.randint(200, 800)]
        car.pos_y = [random.randint(200, 800), random.randint(200, 800)]
        car_center = car.get_car_center()
        print('Car:', car.number, 'Position:', car_center)

    print('********************************')

    for parking_slot in parking_list:
        parking_slot.scan_spot(car_list)
        parking_slot.assign_spot(car_list)
        status = parking_slot.get_status()
        box = parking_slot.get_pos_x_and_y()
        try:
            car_center = parking_slot.car.get_car_center()
            print('Slot:', parking_slot.number,
                  status, 'Car: ', parking_slot.car.number, box, car_center)
        except AttributeError as e:
            print('Slot:', parking_slot.number,
                  status, parking_slot.car, box)

    print('-----------------------------------------\n')
    time.sleep(1)
