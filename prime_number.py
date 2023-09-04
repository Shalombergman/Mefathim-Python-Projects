def is_prime(n):
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 1 and n % 1 == 0


n = input("please insert any number:")
n = int(n)
if is_prime(n):
    print(f"{n} not a natural number: ")
elif n >= 0:
        print(f"{n} is a number composite: ")
else:
    print(f"{n} very good is prime: ")
