"""Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)"""

player1 = raw_input("Player 1: Enter your choice:")
player2 = raw_input("Player 2: Enter your choice: ")

if (player1 == "rock" and player2 == "paper"):
        print "Player 2 wins!"
elif (player1 == "rock" and player2 == "scrissors"):
        print "Player 1 wins!"
        
