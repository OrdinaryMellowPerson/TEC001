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

class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        header = f"{'Reg Number':<12} | {'Max Speed':<12} | {'Current Speed':<15} | {'Distance':<10}"
        print(header)
        print("-" * len(header))
        for car in self.cars:
            print(
                f"{car.registration_number:<12} | {car.maximum_speed:<12} | {car.current_speed:<15} | {car.travelled_distance:<10.1f} km")
        print("\n")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

if __name__ == "__main__":
    participants = []
    for i in range(1, 11):
        max_speed = random.randint(150, 200)
        participants.append(Car(f"ABC-{i}", max_speed))

    derby = Race("Grand Demolition Derby", 8000, participants)

    print(f"--- WELCOME TO {derby.name.upper()} ---")

    hours_passed = 0

    while not derby.race_finished():
        derby.hour_passes()
        hours_passed += 1

        if hours_passed % 10 == 0:
            print(f"--- STATUS AT HOUR {hours_passed} ---")
            derby.print_status()

    print(f"--- FINAL STATUS AT HOUR {hours_passed} (RACE FINISHED) ---")
    derby.print_status()