# results = lambda num1,num2:num1 + num2
# print(results(num1 = int(input("Enter a 1st number")), 
#               num2 = int(input("Enter a 2nd number"))))

################################################################################
# Uses a lambda function to calculate the square of a number.
# Ask the user to enter a number.
# Use the lambda to compute its square and print the result.

# num = int(input("Enter a Number: "))
# results = lambda num: num * num
# print(f"The square of {num} is {results(num)}")

################################################################################
# Has a list of numbers from 1 to 20.
# Uses a lambda function with filter() to get only the even numbers from the list.
# Prints the even numbers.

# numbers = list(range(1, 21))
# results = filter(lambda x: x % 2 == 0, numbers)
# even_numbers = list(results)   # what should wrap results to show the values?
# print("Even numbers from 1 to 20:", even_numbers)

################################################################################
results = lambda val1: val1 * 2
print(results(val1 = int(input("NUmber: "))))