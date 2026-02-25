cities = []

for i in range(5):
    name = input(f"Enter city {i+1}: ")
    cities.append(name)

print("\n--- Your cities ---")
for city in cities:
    print(city)