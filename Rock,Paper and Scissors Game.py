import random

def determine_winner(user_choice, computer_choice):
  
  if user_choice == 'r' and computer_choice == 's':
    return "You win!"
  elif user_choice == 'p' and computer_choice == 'r':
    return "You win!"
  elif user_choice == 's' and computer_choice == 'p':
    return "You win!"
  elif user_choice == computer_choice:
    return "Tie"
  else:
    return "You lose!"

player_points = 0
computer_points = 0
max_points = 3  

while True:
  print("Comp turn: Rock(r), Paper(p) or Scissors(s)?")
  randNo = random.randint(1, 3)
  if randNo == 1:
    comp = 'r'
  elif randNo == 2:
    comp = 'p'
  elif randNo == 3:
    comp = 's'

  you = input("Your turn: Rock(r), Paper(p) or Scissors(s)?")

  valid_choices = ['r', 'p', 's']
  while you not in valid_choices:
    you = input("Invalid choice. Please enter rock(r), paper(p), or scissors(s): ")

  result = determine_winner(you, comp)

  print(f"Computer chose {comp}")
  print(f"You chose {you}")
  print(result)

  
  if result == "You win!🥳🥳":
    player_points += 1
  elif result == "Tie🤞🤞":
    player_points += 1
    computer_points += 1
  else:
    computer_points += 1

  
  if player_points == max_points:
    print("You win the game!")
    break
  elif computer_points == max_points:
    print("Computer wins the game!")
    break

  
  play_again = input("Do you want to play again? (y/n): ")
  if play_again.lower() != 'y':
    break

print(f"Final Scores: Player - {player_points}, Computer - {computer_points}")
print("Thanks for playing!")











