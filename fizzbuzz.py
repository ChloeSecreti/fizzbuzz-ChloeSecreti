# add your code here

for num in range(1,101):
    if num % 3 == 0:
        print("Fizz")
    if num % 5 == 0:
        print("Buzz")
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    if num % 3 != 0 and num % 5 != 0:
        print(num)
