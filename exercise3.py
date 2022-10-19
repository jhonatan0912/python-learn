from time import process_time_ns


num1 = int(input("Insert first number: "))
num2 = int(input("Insert second number: "))

if (num2 == 0):
    print("Error!! | Divisor can't be 0")
else:
    result = num1 / num2
    print(result)
