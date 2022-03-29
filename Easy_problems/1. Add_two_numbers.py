# Getting input from users in integer form
number_1 = int(input("Enter number: 1 -> "))
number_2 = int(input("Enter number: 2 -> "))

# Result of sum in integer form.
result = number_1 + number_2

# Result of sum in float form
result_in_float = float(number_1) + float(number_2)

# Simply printing result in number form
print(result)

# Result using format method
print("Sum of {0} and {1} is {2}".format(number_1, number_2, result))

# Result using f string in integer form
print(f"Sum of {number_1} and {number_2} is {result}")

# Result using f string in float form
print(f"Sum of {number_1} and {number_2} in Float is {result_in_float}")





