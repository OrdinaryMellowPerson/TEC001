def task_3():
    names_set = set()

    while True:
        name = input("Enter a name (or press Enter to quit): ")

        if name == "":
            break

        if name in names_set:
            print("Existing name")
        else:
            print("New name")
            names_set.add(name)

    print("\n--- List of entered names ---")
    for n in names_set:
        print(n)

task_3()