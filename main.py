import random
print("Hello this is a random number guessing game")
print("")
attempts = 0
low = int(input("What do you want your lowest number to be: "))
high = int(input("What do you want your highest number to be: "))
num = random.randint(low, high)
while True:
    guess = int(input("Guess the number: "))
    if num == guess:
      attempts += 1
      print("You got it in", attempts, "attempts!")
      again = input("Do you want to play again? ")
      if again == "yes" or again == "Yes":
        attempts = 0
        num = random.randint(low, high)
        continue
      else:
        print("Thanks for playing!")
        break
    elif num > guess:
      print("You guessed too low! Try again.")
      attempts += 1
    elif num < guess:
      print("You guessed too high! Try again.")
      attempts += 1
  
 
     