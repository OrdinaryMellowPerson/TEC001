class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moving UP. Now on floor: {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moving DOWN. Now on floor: {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor:
            target_floor = self.top_floor
        elif target_floor < self.bottom_floor:
            target_floor = self.bottom_floor

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

if __name__ == "__main__":
    print("--- TASK 1: ELEVATOR TEST ---")
    h = Elevator(1, 10)

    print("Moving to floor 5:")
    h.go_to_floor(5)

    print("\nReturning to bottom floor:")
    h.go_to_floor(1)