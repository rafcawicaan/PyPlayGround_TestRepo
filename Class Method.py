# Define a class named Student
# class Student:
#     # constructor to initialize attributes
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     # method to display student info
#     def display_info(self):
#         print("Name:", self.name, ", Grade:", self.name)

#     # method to check if passed
#     def is_passed(self):
#         if self.grade >= 75:
#             return "You Passed"
#         else:
#             return "You Failed"


# # --- Main Program ---
# # create 3 students
# student1 = Student("Alice", 85)
# student2 = Student("Bob", 72)
# student3 = Student("Charlie", 90)

# # call methods
# student1.display_info()
# print("Passed?", student1.is_passed())

# student2.display_info()
# print("Passed?", student2.is_passed())

# student3.display_info()
# print("Passed?", student3.is_passed())

##############################################################################################################################

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


#####################################################################################33
# Write a Python program that:
# Creates a class BankAccount.
# The class should have:
# Attribute: balance (default 0).
# Method deposit(amount) → adds money to the balance.
# Method withdraw(amount) → subtracts money if there’s enough balance, otherwise print “Insufficient funds”.
# Method display_balance() → prints the current balance.
# In your main program:
# Create one account.
# Deposit 1000.
# Withdraw 500.
# Withdraw 700 (should show “Insufficient funds”).
# Display the final balance.
# Class definition

# class BankAccount:
#     # constructor to initialize balance
#     def __init__(self, balance=0):
#         self.balance = balance

#     # deposit method
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited: {amount}")

#     # withdraw method
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawn: {amount}")
#         else:
#             print("Insufficient funds")

#     # display balance method
#     def display_balance(self):
#         print(f"Current Balance: {self.balance}")


# Main Program
# account = BankAccount()  # create one account with default 0 balance

# account.deposit(1000)    # deposit 1000
# account.withdraw(500)    # withdraw 500
# account.withdraw(700)    # attempt withdraw 700 (should show insufficient funds)

# account.display_balance()  # display final balance/

###############################################################################################################################

class MyName():
    def __init__(self, name):
        self.name = name
        print(name)

NameOne = MyName("Raf")