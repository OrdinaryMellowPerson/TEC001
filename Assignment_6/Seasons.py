def task_2():
    seasons = ("winter", "spring", "summer", "autumn")

    try:
        month = int(input("Enter a month number (1-12): "))

        if month == 12 or month == 1 or month == 2:
            season_name = seasons[0]
        elif month >= 3 and month <= 5:
            season_name = seasons[1]
        elif month >= 6 and month <= 8:
            season_name = seasons[2]
        elif month >= 9 and month <= 11:
            season_name = seasons[3]
        else:
            print("Invalid month! Must be between 1 and 12.")
            return

        print(f"The season is: {season_name}")

    except ValueError:
        print("Please enter an integer.")

task_2()