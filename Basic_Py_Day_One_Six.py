#DAY 1
# print ("Hello, World!")

##################################################################################################

# DAY 2
# sample data inputs

##################################################################################################

# first_name = str(input("Enter your name: "))
# last_name = str(input("Enter your last name: "))
# age = int(input("Enter your age: "))

# # print a greeting message
# print(f"Hello, {first_name} {last_name}! You are {age} years old.")

##################################################################################################

#DAY 3
#Simple calculator

# num1 = float(input("Enter you First Number: "))
# num2 = float(input("Enter your Second Number: "))

# operation = input("Enter the operation you want to perform (+, -, *, /): ")

# if operation == '+':
#     result = num1 + num2
# elif operation == '-':
#     result = num1 - num2
# elif operation == '*':
#     result = num1 * num2
# elif operation == '/':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error: Division by zero is not allowed."
# print(f"The result of {num1} {operation} {num2} is: {result}")

##################################################################################################

#DAY 4
# Comparison Activity (== != > < >= <=)

# name = str(input("Enter your Name: "))
# age = int(input("Enter your Age: "))
# grade = float(input("Enter your Grade: "))

# if age == 18:
#     print("Are you a 18 years old? ", age == 18 )
# elif age != 18:
#     print("Your are NOT 18 years old? ", age != 18 )
# elif age > 18:
#     print("Your age is GREATER THAN 18? ", age > 18 )
# elif age < 18:
#     print("Your age is LESS THAN 18? ", age < 18 )
# elif age >= 18:
#     print("Your age is GREATER THAN or EQUAL to 18? ", age >= 18 )
# elif age <= 18:
#     print("Your age is LESS THAN or EQUAL to 18? ", age <= 18 )
# print(f"Your name is {name} \n and you're {age} years old" )
# print("Your Grade is Grade One? ", grade == 1 )
# print("Your Grade is NOT Grade One? ", grade != 1 )
# print("Your Grade is Higher than Grade One", grade >= 1)
# print("Your Grade is Kinder", grade <= 1)

##################################################################################################

# DAY 5
# Logical Operators (and or not) WITH IF ELSE/ELIF

# name = str(input("Enter your Name: "))
# age = int(input("Enter your Age: "))
# id_type = input("You want to avail discount? (yes/no/senior)").lower()

# # Teen discount: must be between 13 and 19
# teen_discount = age >= 13 and age <= 19

# # Student discount: either has student ID or below 12
# student_discount = (id_type == "yes") or age <= 12

# # Senior discount: not younger than 60

# # senior_discount = not (age >= 60)
# senior_discount = age >= 60

# # print("\n---RESULTS---")
# if teen_discount == True:
#     print(f"Hello {name} You can avail teen discount", teen_discount)
# elif student_discount:
#     print(f"Hello {name} You can avail student discount", student_discount)
# elif id_type == "no":
#     print("You can't avail discount ")
# elif age >= 60 and id_type == "senior":
#     print(f"Hello {name} You can avail senior discount", senior_discount)
# elif senior_discount and id_type == "senior":
#     print(f"Hello {name} You can't avail senior discount", senior_discount)
# print("Done")

##################################################################################################

# DAY 6 Conditions (if-else)
# gender = input("Enter your Gender: ").upper()

# if gender == "BOY":
#     print("Your Gender is BOY")
# elif gender == "GIRL":
#     print("Your Gender is GIRL")
# else :
#     print("Enter a valid Gender")

##################################################################################################





