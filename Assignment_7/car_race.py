import random

class Car:
    def __init__(self, reg_num, max_speed):
        self.registration_number = reg_num
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


if __name__ == "__main__":
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(150, 200)
        cars.append(Car(f"ABC-{i}", max_speed))

    race_finished = False
    while not race_finished:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

            if car.travelled_distance >= 10000:
                race_finished = True

    header = f"{'Reg Number':<12} | {'Max Speed':<12} | {'Current Speed':<15} | {'Distance':<10}"
    print(header)
    print("-" * len(header))
    for car in cars:
        print(
            f"{car.registration_number:<12} | {car.maximum_speed:<12} | {car.current_speed:<15} | {car.travelled_distance:<10.1f} km")