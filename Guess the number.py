#Guess the Nunber
import random

player_name=input("Enter the name of the player:")
upper_limit=int(input("Enter the upper limit:"))
lower_limit=int(input("Enter the lower limit:"))
n=int(input("Enter the number of rounds that u want to play:"))
players_points=100
play_again= True
while play_again:
    for i in range(1,n+1):
      print("Round",i," Remaining Points: ",players_points)
      y=random.randint(lower_limit,upper_limit)
      while True:
            user_guess_value=int(input("Enter your number for the guess:"))
            if(user_guess_value!=y):
                if(user_guess_value>y):
                    players_points-=5
                    print("Too High!")
                elif(user_guess_value<y):
                    players_points-=5
                    print("Too Low!")
            elif(user_guess_value==y):
                    print("Correct Guess,Congratulations!!!",player_name)
                    print("The points u scored: ",players_points)
                    break
            if(players_points<=0):
                    print("Oops!! U lost the game")
                    print("Sorry better luck next time",player_name)
                    print("The points u scored: ",players_points)
                    break
      print("Do u want to continue the game?")
      choice=input("Enter 'Y' For Continuing the Game and 'N' For Quiting: ")
      if(choice=='Y'):
            play_again = True
      elif(choice=='N'):
            play_again = False
print("Thanks",player_name,"for playing the game.")

