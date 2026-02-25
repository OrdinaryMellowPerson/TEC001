import math

n = int(input("Enter a PRIME number: "))
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{n} IS A PRIME NUMBER .")
else:
    print(f"{n} IS NOT A PRIME NUMBER .")