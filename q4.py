
import random
print("Winning Rules of the Rock paper scissor game as follows: \n\n"
                                +"Rock vs paper : paper wins \n"
                                + "Rock vs scissor : Rock wins \n"
                                +"paper vs scissor : scissor wins \n")
 
while True:
    print("Enter choice \n 1) Rock, \n 2) paper\n 3) scissor \n")
     
    choice = int(input("User's choice: "))
 
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))
         
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'

    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
         
    print("\nYour choice is: " + choice_name)
    print("\nComputer choice is: " + comp_choice_name)
    

    print(choice_name + " X " + comp_choice_name)
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
        print("\npaper wins ", end = "")
        result = "paper"
         
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        print("\nRock wins  ", end = "")
        result = "Rock"
    else:
        print("\nscissor wins ", end = "")
        result = "scissor"
 

    if result == choice_name:
        print("\nCongrats!!! You win.....")
    else:
        print("\nYou lost.....")
         
    print("Do you want to play again? (Y/N)")
    ans = input()
 
    if ans == 'n' or ans == 'N':
        break
     
print("\nThanks for playing")