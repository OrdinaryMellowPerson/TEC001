def login():
    import sys

    correct_username = "python"
    correct_password = "rules"

    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        print(f"\n--- Lần thử {attempts + 1} / {max_attempts} ---")
        username = input("Username: ")
        password = input("Password: ")

        if username == correct_username and password == correct_password:
            print("\nWelcome! 🎉")
            return

        attempts += 1

        if attempts < max_attempts:
            print(f"Sai rồi cu! Bạn còn {max_attempts - attempts} lần thử.",file=sys.stderr)

    print("\nAccess denied. ❌", file=sys.stderr)
login()