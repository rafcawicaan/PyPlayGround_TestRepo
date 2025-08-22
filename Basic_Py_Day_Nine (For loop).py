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
