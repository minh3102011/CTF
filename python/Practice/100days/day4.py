import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
try:
    choice = int(input("Choose 1: Rock, 2: Page, 3: Scissors\n"))
    computer = random.randint(0, 2)
    if choice == 1 or choice ==2 or choice ==3:
        if choice == 1:
            print(f"You choice : {rock}")
        elif choice == 2:
            print(f"You choice: {paper}")
        else:
            print(f"You choice: {scissors}")
        if computer == 0:
            print(f"Computer choice: {rock}")
            if choice == 1:
                print("draw!")
            elif choice == 2:
                print("You win!")
            else:
                print("You lose!")
        elif computer == 1:
            print(f"Computer choice: {paper}")
            if choice == 1:
                print("You lose!")
            elif choice == 2:
                print("draw!")
            else:
                print("You win!")
        else:
            print(f"Computer choice: {scissors}")
            if choice == 1:
                print("You win!")
            elif choice == 2:
                print("You lose!")
            else:
                print("draw!")
    else:
        print("Invalid input! Please enter 1, 2 or 3.")
except ValueError:
    print("Invalid input! Please enter a number.")
        