from datetime import datetime, timedelta
class Boat:
    def __init__(self, boat_number):
        self.boat_number = boat_number
        self.money_taken = 0
        self.total_hours_hired = 0
        self.next_available_time = datetime(2023, 1, 1, 10, 0)

    def hire_boat(self, hours):
        current_time = datetime.now()
        if current_time < self.next_available_time:
            print(f"Boat {self.boat_number} is not available until {self.next_available_time.strftime('%H:%M')}")
            return

        if hours == 0.5:
            cost = 12
        elif hours == 1:
            cost = 20
        else:
            print("Invalid hire duration. Please choose 0.5 or 1 hour.")
            return

        self.money_taken += cost
        self.total_hours_hired += hours
        return_time = current_time + timedelta(hours=hours)
        if return_time.hour > 17:
            return_time = datetime(current_time.year, current_time.month, current_time.day, 17, 0)
        self.next_available_time = return_time
        print(f"Boat {self.boat_number} hired for {hours} hours. Return by {return_time.strftime('%H:%M')}")

def calculate_daily_summary(boats):
    total_money_taken = 0
    total_hours_hired = 0
    unused_boats = []
    most_used_boat = None
    max_hours = 0

    for boat in boats:
        total_money_taken += boat.money_taken
        total_hours_hired += boat.total_hours_hired

        if boat.total_hours_hired == 0:
            unused_boats.append(boat.boat_number)

        if boat.total_hours_hired > max_hours:
            max_hours = boat.total_hours_hired
            most_used_boat = boat.boat_number

    print("\n--- Daily Summary ---")
    print(f"Total money taken: ${total_money_taken}")
    print(f"Total hours hired: {total_hours_hired} hours")
    print(f"Boats not used: {unused_boats}")
    print(f"Boat {most_used_boat} was used the most ({max_hours} hours)")

def main():
    boats = [Boat(i) for i in range(1, 11)]

    # Task 1 - Calculate money taken for one boat
    boat_number = int(input("Enter boat number (1-10): "))
    hours = float(input("Enter number of hours to hire (0.5 or 1): "))
    boats[boat_number - 1].hire_boat(hours)

    # Task 2 - Find the next available boat
    print("\n--- Boat Availability ---")
    available_boats = [boat.boat_number for boat in boats if datetime.now() >= boat.next_available_time]
    print(f"Available boats: {available_boats}")

    # Task 3 - Calculate money taken for all boats at the end of the day
    for boat in boats:
        boat.hire_boat(0)  # Set all boats as returned

    calculate_daily_summary(boats)

if __name__ == "__main__":
    main()
