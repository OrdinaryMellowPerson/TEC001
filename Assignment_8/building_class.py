class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Moving UP -> Floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Moving DOWN -> Floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor:
            target_floor = self.top_floor
        elif target_floor < self.bottom_floor:
            target_floor = self.bottom_floor

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for _ in range(num_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        index = elevator_number - 1
        if 0 <= index < len(self.elevators):
            print(f"\n--- Running Elevator {elevator_number} to floor {destination_floor} ---")
            self.elevators[index].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number.")


if __name__ == "__main__":
    print("--- TASK 2: BUILDING TEST ---")
    my_building = Building(1, 20, 3)

    my_building.run_elevator(1, 5)
    my_building.run_elevator(2, 12)
    my_building.run_elevator(3, 8)