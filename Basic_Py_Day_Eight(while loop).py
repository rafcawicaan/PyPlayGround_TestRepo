# While Loop Activity

# Stores a secret number (for example, 7).
# Asks the user to guess the number using input().
# Keeps asking until the user guesses correctly.
# If the guess is too high, print "Too high! Try again."
# If the guess is too low, print "Too low! Try again."
# When the user guesses correctly, print "Correct! You guessed it."

# secret_num = 7

# while True :
#     guess_num = int(input("Guess the Number from 1 to 10: "))

#     if guess_num > secret_num :
#         print("Too high! Try again.")
#     elif guess_num < secret_num :
#         print("Too low! Try again.")
#     else :
#         if guess_num == secret_num :
#             print("Correct! You guessed it.")
#         break

################################################################################################

# You have a car with 50 liters of fuel.
# Each trip consumes 7 liters of fuel.
# Ask the user if they want to take a trip (yes or no).
# If yes, subtract 7 liters from the fuel and display the remaining fuel.
# If fuel goes below 7 liters, stop the loop and print "Not enough fuel for another trip!".
# If no, stop the loop and print "Trip ended. Safe travels!".

# fuel = 50

# while True:
#     isTripContinue = input("You want to take a trip (yes or no): ").lower()

#     if isTripContinue == "yes":
#         if fuel >= 7:  # only take a trip if enough fuel
#             fuel -= 7
#             print("The remaining fuel:", fuel)
#         else:
#             print("Not enough fuel for another trip!")
#             break

#     elif isTripContinue == "no":
#         print("Trip ended. Safe travels!")
#         break

#     else:
#         print("Invalid input, please type 'yes' or 'no'.")


################################################################################################

# While loop
# Cheking the age if the age is legal or minor

# age = 12

# while age < 18:
#     print("Too young" + str(age))
#     age = age + 1 
# else :
#     print("Legal Age" + str(age))

################################################################################################

# WHile Loop in Collection

# variable
# names = [
#       # index positions
#       #  0       1        2        3        4         5       6
#       'Raf', 'Randy', 'Rodel', 'Ryan', 'Kenneth', 'Mark', 'Danica']

# i = 0  # starting index (first position in the list)

# # while loop will run as long as i <= 4 (so only the first 5 names will print)
# while i <= 4:
#     # access list element using index
#     print("Hello", names[i])
#     i = i + 1  # move to the next index

# # else part of while runs only when the loop condition becomes False
# else:
#     print("No names found in the list")

############################################################################################

# WHile loop

# list of numbers from 1 to 10
# numbers = [1,2,3,4,5,6,7,8,9,10]

# # starting index at 0 (first element in the list)
# i = 0

# # loop continues while i is less than the length of the list
# while i < len(numbers) :
#     # check if the current number is even (divisible by 2)
#     if (numbers[i] % 2 == 0 ):
#         print("Even Number : " + str(numbers[i]))
#     # if not even, then it's odd
#     else :
#         print("ODD Number : " + str(numbers[i]))
    
#     # move to the next index
#     i = i + 1


#######################################################################################
#WHile loop Math Game

# Problem Statement:
# Write a Python program that:
# Randomly chooses a number between 1 and 50.
# The player keeps guessing until they find the correct number.
# The program should give hints:
# “Too High!” if the guess is higher.
# “Too Low!” if the guess is lower.
# Count how many tries it takes.
# When the player guesses correctly, display:
# The number of attempts
# A “You Win!” message

lives = 3
answer = 12

while lives > 0 :
    number = (int(input("Enter a Number from 1 to 50: ")))

    if number > answer :
        print("Your answer is high")
    elif number < answer :
        print("Your Answer is low")
    elif number == answer :
        print("Your answer is correct!")
        break
    else :
        print("Enter a valid number")

    if number != answer :
        lives -= 1
        print("Your Remaining lives is", lives)
    else :
        print("sample")