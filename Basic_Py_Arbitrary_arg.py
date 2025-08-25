# def printFamily(*first_name, last_name):
#     for name in first_name :
#         print(name +" "+ last_name)
# printFamily("John","Bob",last_name="Sample")

################################################

# def list_of_names(*names):
#     for name in names:
#         print("Hello", name)

# list_of_names("Raf", "Ryan", "Kenneth")

##############################################################

# # Function with *args for exam scores
# def calculate_total(*scores):
#     if len(scores) == 0:
#         return 0, 0
#     total = sum(scores)
#     average = total / len(scores)
#     return total, average


# # Function with **kwargs for student details
# def print_student_details(name, **details):
#     print(f"\nStudent: {name}")
#     for key, value in details.items():
#         print(f"{key} : {value}")


# # ---- Main Program ----
# # Ask for student details
# name = input("Enter student name: ")
# age = input("Enter student age: ")
# course = input("Enter student course: ")

# # Ask for 3 exam scores
# scores = []
# for i in range(1, 4):
#     score = int(input(f"Enter exam score {i}: "))
#     scores.append(score)

# # Call functions
# total, average = calculate_total(*scores)
# print_student_details(name, age=age, course=course)

# # Print results
# print(f"Total Score: {total}")
# print(f"Average Score: {average:.2f}")


#########################################################################

def names(firstname, lastname):
    print(firstname + " " + lastname)

names(firstname=input("Enter your Firstname: "), lastname=input("Enter your Lastname: "))


#################################################################################

# Defines a function calculate_bill(*prices) that accepts any number of food item prices and returns the total bill amount.
# Defines another function print_order_details(customer, **details) that prints the customer’s name and any extra order details (like address, payment_method, delivery_time).
# In the main program:
# Ask the user for their name, address, and payment method.
# Ask the user how many items they want to order.
# For each item, ask for its price and store it.
# Use calculate_bill() to compute the total bill.
# Use print_order_details() to display the order summary.

# Function with *args for item prices
def calculate_bill(*prices):
    if len(prices) == 0:
        return 0
    return sum(prices)


# Function with **kwargs for order details
def print_order_details(customer, **details):
    print(f"\nOrder Summary for {customer}")
    for key, value in details.items():
        print(f"{key} : {value}")


# ---- Main Program ----
# Ask for customer details
name = input("Enter customer name: ")
address = input("Enter customer address: ")
payment = input("Enter payment method: ")

# Ask for number of items
num_items = int(input("\nHow many items are you ordering? "))

# Collect prices of each item
prices = []
for i in range(1, num_items + 1):
    price = float(input(f"Enter price of item {i}: "))
    prices.append(price)

# Calculate total bill
total = calculate_bill(*prices)

# Print order details
print_order_details(name, address=address, payment_method=payment, total_bill=total)


#########################################################################################################

# Defines a function borrowed_books(*books) that accepts any number of book titles and prints them as the list of borrowed books.
# Defines another function print_member_details(member, **details) that prints the library member’s name and any extra details (like member_id, membership_type, expiry_date).
# In the main program:
# Ask the user for their name, member ID, and membership type.
# Ask how many books they want to borrow.
# For each book, ask for its title and store it.
# Use borrowed_books() to print the list of borrowed books.
# Use print_member_details() to display the member’s details.

# def borrowed_books(*books):
#     if len(books) == 0:
#         return 0
#     return sum(books)

# def print_memer_details(member, **details):
#     print(f"\nMembers Name: {member}")
#     for key, value in details.items():
#         print(f"{key} : {value}")
# #Main Program
# #Details
# name = input("Enter your Name: ")
# mem_id = input("Enter Your member ID: ")
# type = input("Membership Type: ")
# #How Many Books You want to Borrow
# books = int(input("How Many Books You want to Borrow: "))
# title = input("Title of the Books: ")

# for i in books:



