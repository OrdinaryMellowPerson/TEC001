class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
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

if __name__ == "__main__":
    test_car = Car("ABC-123", 142)

    test_car.accelerate(30)
    test_car.accelerate(70)
    test_car.accelerate(50)
    print(f"Current speed after increases: {test_car.current_speed} km/h")

    test_car.accelerate(-200)
    print(f"Final speed after emergency brake: {test_car.current_speed} km/h")