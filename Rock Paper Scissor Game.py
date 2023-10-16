import random
list = ["Rock","Paper","Scissor"]

while True:
     usercount = 0
     compcount = 0
     users_choice = int(input('''
Let's start the game...
Press 1 for Start
Press 0 for Exit
 '''))
     if users_choice == 1:
          for a in range(1,6):
               users_input = int(input('''
1. Rock
2. Paper
3. Scissor
          '''))
               
               if users_choice == 1:
                ur_choice = "Rock"
               elif users_choice == 2:
                ur_choice = "Paper"
               elif users_choice == 3:
                ur_choice = "Scissor"

               comp_choice = random.choice(list)

               if comp_choice == ur_choice:
                    print("You Choose",ur_choice)
                    print("Computer Choose",comp_choice)
                    print("Draw")
                    usercount = usercount+1
                    compcount = compcount+1
               elif (ur_choice == "Rock" and comp_choice == "Scissor") or (ur_choice == "Paper" and comp_choice == "Rock") or (ur_choice == "Scissor" and comp_choice == "Paper"):
                    print("You Choose",ur_choice)
                    print("Computer Choose",comp_choice)
                    print("You Win")
                    usercount+=1
               else: 
                    print("You Choose",ur_choice)
                    print("Computer Choose",comp_choice)
                    print("You Lose")
                    compcount+=1
          print("\n")
          if usercount == compcount:
              print("Hence, The Game Is Draw...")
              print("Your Score",usercount)
              print("Computer Score",compcount)
          elif usercount > compcount:
              print("Hence, You Win The Game...")
              print("Your Score",usercount)
              print("Computer Score",compcount)
          else:
              print("Hence, You Loose The Game")
              print("Your Score",usercount)
              print("Computer Score",compcount)

     else:
          break