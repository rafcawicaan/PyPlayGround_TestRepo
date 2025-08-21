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

age = 12

while age < 18:
    print("Too young" + str(age))
    age = age + 1 
else :
    print("Legal Age" + str(age))