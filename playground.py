from car import car
from parking_slot import parking_slot

parking_list = []
car_list = []

parking_slot_1 = parking_slot(pos_x=[200, 400], pos_y=[200, 400], number=1)
parking_slot_2 = parking_slot(pos_x=[400, 600], pos_y=[400, 600], number=2)

parking_list.append(parking_slot_1)
parking_list.append(parking_slot_2)


car_1 = car(number=1, pos_x=[450, 550], pos_y=[450, 550])
car_2 = car(number=2, pos_x=[300, 500], pos_y=[250, 350])

car_list.append(car_1)
car_list.append(car_2)

for car in car_list:
    car_center = car.get_car_center()
    print(car_center)

for parking_slot in parking_list:
    parking_slot.scan_spot(car_list)
    parking_slot.assign_spot(car_list)
    print(parking_slot.status, parking_slot.pos_x,
          parking_slot.pos_y, parking_slot.car_id)
