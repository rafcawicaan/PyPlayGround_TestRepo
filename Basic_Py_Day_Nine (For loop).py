# Differences between every functions 
# For loop → repeat a known number of times or iterate items.

# While loop → repeat until a condition is false.

# If/Else → make decisions.

# Functions / Collections → organize and reuse data or code.

#For Loop

# fruits = ["Apple", "Banana", "Orange", "Mango"]

# for x in fruits :
#     print("The list of the Fruits is", x)
# else :
#     print("No more fruits")

##########################################################################################################

# Asks the user 5 multiplication questions (random numbers between 1 and 10).
# Uses a for loop to repeat the questions.
# Keeps track of the score (1 point per correct answer).
# At the end, display the final score.

# Multiplication quiz with for loop

# List of (question, correct_answer) pairs
# questions = [
#     ("What is 3 * 2? ", 6),
#     ("What is 2 * 2? ", 4),
#     ("What is 3 * 3? ", 9),
#     ("What is 4 * 2? ", 8),
#     ("What is 2 * 1? ", 2)
# ]

# points = 0  # Track score

# # Loop through each question
# for x, correct_answer in questions:
#     answer = int(input(x))   # Ask question
#     if answer == correct_answer:  # Check correctness
#         print("Correct!")
#         points += 1
#     else:
#         print("Wrong! Try again.")

# # Final score after loop ends
# print("Your final score is:", points, "out of", len(questions))


######################################################################################################
# For loop using Vowels
# Ask the user for a word in lowercase, then use a for loop to count how many vowels (a, e, i, o, u) it contains.
# Input: hello
# Output: The word has 2 vowels.

# vowels = [
#     ("a"), ("e"), ("i"), ("o"), ("u")
# ]
# count = 0
# word = str(input("Enter a word: " )).lower()
# for x in word :
#     if x in vowels :
#         count += 1
# print("The total vowels in your word is", count)


###################################################################################################
# Account Authentication using For Loop

# username = ["admin", "client1", "client2"]
# password = ["abc123", "pass123", "123cdf"]

# user = str(input("Enter a username: "))
# enter_pass = str(input("Enter a Password: "))

# for x in range(len(username)) :
#     if user == username[x] and enter_pass == password[x] :
#         print("Hello", user)
#         break
#     else :
#         print("Wrong Username or Password Please Try again!")
#         break
# print("Welcome have a nice day!")

#########################################################################################
# Asks the user to enter a lowercase word.
# Uses a for loop to go through each character.
# Counts how many times each letter appears.
# Prints the result.
# lowercase_word = input("Enter a lowercase word: ")

# counts = {}
# for x in lowercase_word.items():
#     if x in counts:
#         counts[x] += 1
#     else :
#         counts[x] = 1
# print("Letter" + counts)

#######################################################################################3
# Asks the user to enter a word.
# Prints each character of the word on a separate line.
# At the end, also print how many characters the word has.

# enter_word = input()
# for x in enter_word:
#     print(x)
# print("The word has", len(enter_word), "characters.")

##########################################################################################
# Write a Python program that:
# Asks the user to enter a number.
# Prints the multiplication table for that number from 1 to 10.

# num1 = int(input("Enter a Number: "))
# for x in range(1, 11):
#     result = num1 * x
#     print(num1, "x", x, "=", result)

##############################################################################################
# Asks the user to enter a number n.
# Prints all even numbers from 1 to n.
# At the end, prints how many even numbers were found.

# num = int(input("Enter a number: "))
# count = 0
# for n in range(1, num + 1):
#     if n % 2 == 0:
#         print(n)
#     count += 1
# print(f"There are {count} even numbers")


########################################################################################################
# Asks the user to enter a positive number n.
# Uses a for loop to calculate the factorial of that number.
# Prints the result.

num = int(input("Enter a positive number: "))
fact = 1
for n in range(1, num + 1):
    fact *= n
    print(n)
print(f"The factorial of {num} is {fact}")