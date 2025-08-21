# Dictionary
# person_details = {
#     # 'first_name' : str(input('Enter you first name: ')),
#     # 'last_name' : str(input('Enter you last name: ')),
#     'first_name' : 'raf',
#     'last_name' : 'cawi',
#     'email' : 'sampleemail@gmail.com',
#     'contact_no' : '09123456789'
# }
# person_details['name' ]
# other_person = person_details.copy() #copying person_details data
# # other_person.pop('email') #deleting email in the person_details using the other_persons
# other_person.update({'email' : 'sampleemailnew@gmail.com'}) #Updating data inside a dict uisng update
# print(other_person)

# print(f"Hello", person_details.get('first_name'), person_details.get('last_name'))
# print(len(person_details)) #Get the lenght of the person_details which is 4(firstname,lastname,email,contact_no)

###########################################################################################################

#Dictionaries Nested
# person_other_details = {
#     'birthdate' : 'January-08-2025',
#     'height' : 155,
#     'sex' : 'Male'
# }
# person_details = {
#     'firstname' : 'raf',
#     'lastname' : 'cawi',
#     'contact_no' : '09123456789',
#     'other_details' : person_other_details
# }
# print(person_details.get('other_details').get('birthdate'))

#####################################################################################################
# Nestted IF Else Condition

# student_name = "Raf"
# grade = int(input("Enter your Grade: "))

# if grade <  0 or grade >= 101 :
#     print("Enter a Correct Number between 0 - 100")
# elif 90 <= grade <= 100 :
#     if 95 <= grade <= 100 :
#         print("Good Job! your qualified for Scholarship")
#     else : # IF the Grades is 94 to 90
#         print("Good Job! but your not qualified for Scholarship")
# elif 80 <= grade <= 89 :
#         print("Great!")
# elif 75 <= grade <= 79 :
#         print("Keep It Great!")
# elif 60 <= grade <= 74 :
#         print("Fail!")
# else :
#     print("Hello, World!")
# print(f"Hello {student_name} Your Grade is {grade}")

######################################################################

# Two Nested If Else COndition

# ammount = int(input("enter an ammount: "))
# if ammount >= 1000 :
#     print("You are eligible for a discount!")
#     if ammount >= 5000 :
#         print("You get a 20% discount!")
#     else :
#         print("You get a 10% discount!")
# elif ammount >= 500 :
#     print("You get a free gift!")
# else : 
#     print("Better luck next time!")

##################################################################################

# multiple nested if-else

# exam_results = int(input("Enter your Exam Score: "))
# attendance = int(input("Enter your attendance: "))

# if exam_results >= 75 :
#     if attendance >= 80 :
#         print("You passed with good standing!")
#     else:
#         print("You passed, but your attendance is low.")
# else :
#     if attendance >= 80 :
#         print("You failed, but your attendance is good.")
#     else :
#         print("You failed and your attendance is poor.")

##########################################################################

#multiple three nested if else 

# exam_results = int(input("Enter your Exam Score: "))
# attendance = int(input("Enter your attendance: "))

# if exam_results >= 90 and attendance >= 80 :
#     print("You are qualifies for a scholarship.")
# else :
#     if exam_results >= 90 and attendance >= 79 :
#         print("passes but without scholarship.")
#     else:
#         if exam_results >= 75 :
#             print("passes normally.")
#         else :
#             if attendance >= 80 :
#                 print("can take a remedial exam")
#             else :
#                 print("The application is not additted")


# Best Practices Three Nested If else

# exam_results = int(input("Enter your Exam Score: "))
# attendance = int(input("Enter your attendance: "))

# if exam_results >= 90 and attendance >= 80:
#     print("scholarship")
# elif exam_results >= 90:
#     print("pass but no scholarship")
# elif exam_results >= 75:
#     print("pass normally")
# elif attendance >= 80:
#     print("remedial")P
# else:
#     print("not admitted")

#######################################################################################

# collection conditionals using IN
# course_name = str(input("Enter your Course: ")).capitalize()
# science_courses = ["Biology", "Chemistry", "Physics"]
# tech_courses = ["Programming", "Networking", "Database"]
# arts_courses = ["Painting", "Music", "Theater"]

# if course_name in science_courses :
#     print ("You enrolled in a Science course.")
# elif course_name in tech_courses :
#     print("You Enrolled in tech course")
# elif course_name in arts_courses :
#     print("You Enrolled in arts course")
# else :
#     print("Hello World")

#####################################################################################

# collection conditionals getting specific Value
# course_name = str(input("Enter your Course: ")).capitalize()

# science_courses = ["Biology", "Chemistry", "Physics"]
# tech_courses = ["Programming", "Networking", "Database"]
# arts_courses = ["Painting", "Music", "Theater"]

# if "Biology" in course_name :
#     print("You enroll in the biology course")
# elif "Programming" in course_name :
#     print("You enroll in the Programming course")
# elif "Painting" in course_name :
#     print("You enroll in the Painting course")
# else :
#     print("Hello World")

#####################################################################################

# While Loop Activity

# A user has a balance of ₱10,000.
# Create a program using a while loop that:
# Continuously asks the user to enter an amount to withdraw.
# If the entered amount is greater than the balance, print "Insufficient funds.".
# If the entered amount is 0 or negative, print "Invalid amount.".
# Otherwise, subtract it from the balance and print the updated balance.
# The loop should keep running until the balance is 0 or the user enters "exit".
# At the end, print "Thank you for using our ATM!".


user_balance = 10000

while True :
    amount = int(input("Enter an Amount to withdraw: "))
    if amount > user_balance :
            print("Insufficient funds.")
    elif amount < 0 :
        print("Invalid amount.")
    else :
        user_balance -= amount 
        print("Your Balance now is", user_balance)
    print("Thank you for using our ATM")

    ##################################################################################