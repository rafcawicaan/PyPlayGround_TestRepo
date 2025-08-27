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

# def names(firstname, lastname):
#     print(firstname + " " + lastname)

# names(firstname=input("Enter your Firstname: "), lastname=input("Enter your Lastname: "))


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
# def calculate_bill(*prices):
#     if len(prices) == 0:
#         return 0
#     return sum(prices)


# # Function with **kwargs for order details
# def print_order_details(customer, **details):
#     print(f"\nOrder Summary for {customer}")
#     for key, value in details.items():
#         print(f"{key} : {value}")


# # ---- Main Program ----
# # Ask for customer details
# name = input("Enter customer name: ")
# address = input("Enter customer address: ")
# payment = input("Enter payment method: ")

# # Ask for number of items
# num_items = int(input("\nHow many items are you ordering? "))

# # Collect prices of each item
# prices = []
# for i in range(1, num_items + 1):
#     price = float(input(f"Enter price of item {i}: "))
#     prices.append(price)

# # Calculate total bill
# total = calculate_bill(*prices)

# # Print order details
# print_order_details(name, address=address, payment_method=payment, total_bill=total)


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
#         print("No books borrowed.")
#     else:
#         print("\nList of borrowed books:")
#         for book in books:
#             print(f"- {book}")

# def print_member_details(member, **details):
#     print(f"\nMember's Name: {member}")
#     for key, value in details.items():
#         print(f"{key} : {value}")

# # Main Program
# # Details
# name = input("Enter your Name: ")
# mem_id = input("Enter Your member ID: ")
# type = input("Membership Type: ")

# # How Many Books You want to Borrow
# num_books = int(input("How Many Books You want to Borrow: "))

# books = []
# for i in range(1, num_books + 1):
#     book_title = input(f"Enter the title of book {i}: ")
#     books.append(book_title)

# borrowed_books(*books)
# print_member_details(name, member_id=mem_id, membership_type=type)

########################################################################################################
# sample *args
# def add_numbers(*args):
#     return sum(args)

# result = add_numbers(1, 2, 3)
# print("The sum is:", result)
# #kwargs
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)
# # print_info(name="Raf", course="BIST", age=23)
# print_info(name=input("Enter your name: "), course=input("Enter Course: "), age=input("Enter your age: "))

###########################################################################################
# Write a function multiply_numbers(*args) that accepts any number of numbers and returns their product (multiplication result).
# Then call it with different sets of numbers and print the results.

# def multiply_numbers(*args):
#     results = 1
#     for x in args:
#         results *= x
#         print("The results is ", results)
# multiply_numbers(2, 3)
####################################################################################################

# def multiply_numbers(**num):
#     result = 1
#     for value in num.values():   # use .values() to get 2, 3 instead of "first_num", "second_num"
#         result *= value
#     print("The result is", result)
# multiply_numbers(first_num=int(input("Enter first num: ")), second_num=int(input("Enter second num: ")))


###################################################################################################
# Defines a function checkout(*items, **customer) that:
# Uses *items to accept prices of any number of items.
# Uses **customer to accept customer details like name, address, and payment_method.
# Inside the function:
# Calculate the total cost of the items.
# Print the customer’s details.
# Print the total amount.
# def checkout(*items, **customer):
#     if len(items) > 0:
#         print("Total amount is", sum(items))
    
#     for key, value in customer.items():
#             print(f"{key} : {value}")

# checkout(20, 30, 50, name = input("Name: "), address = input("Address: "), method = input("Payment Method: "))

###############################################################################
# Write a function student_report(*grades, **student) that:
# Accepts any number of grades as *args.
# Accepts student details (name, course, year) as **kwargs.
# Prints the average grade and the student’s details.

# def student_report(*grades, **student):
#     if len(grades):
#         print("Your Grade is", grades)
    
#     for key, value in student.items():
#         print(f"{key} : {value}")
# student_report(90, 95, 90, name=input("Name: "), course=input("Enter course: "), year=input("Enter Year: "))

#############################################################################
# Problem Statement:
# Write a function book_trip(*places, **details) that:
# Accepts multiple travel destinations as *args.
# Accepts booking details (traveler name, payment_method, date) as **kwargs.
# Prints the list of destinations and the booking details.

# def book_trip(*places, **details):
#     print("\nYour Travel Destinations:")
#     for p in places:
#         print("-", p)

#     print("\nBooking Details:")
#     for key, value in details.items():
#         print(f"{key.capitalize()}: {value}")

# # User decides how many places to enter
# destinations = []
# num = int(input("How many destinations do you want to add? "))

# for i in range(num):
#     destinations.append(input(f"Enter destination {i+1}: "))

# # Pass list using * to unpack it into *args
# book_trip(*destinations,
#           name=input("Enter Your Name: "),
#           method=input("Payment Method: "),
#           date=input("Date of Travel: "))

################################################################################################

def greetings(name):
    print(print(f"Hello {name} welcome to python."))
greetings("Raf")
greetings("Ryan")
greetings("Kenneth")