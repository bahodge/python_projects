list = range(1, 100)
fizz_counter = 0
buzz_counter = 0
fizzbuzz_counter = 0


for num in list:
    if num % 15 == 0:
        print(str(num) + " fizzbuzz")
        fizzbuzz_counter += 1
    elif num % 5 == 0:
        print(str(num), " buzz")
        buzz_counter += 1
    elif num % 3 == 0:
        print(str(num), " fizz")
        fizz_counter += 1
    else:
        print(str(num))

print("Fizzbuzz Count: " + str(fizzbuzz_counter))
print("Fizz Count: " + str(fizz_counter))
print("Buzz Count: " + str(buzz_counter))