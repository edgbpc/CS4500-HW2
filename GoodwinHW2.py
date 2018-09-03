'''
Eric Goodwin
09-01-2018
Version 1.0
CS 4500 Introduction to the Software Profession

Resources Used:
https://docs.python.org/3/library
https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/
https://www.geeksforgeeks.org/sum-function-python/
https://www.tutorialspoint.com/python/list_max.htm
http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
https://stackoverflow.com/questions/493386/how-to-print-without-newline-or-space
https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string

Requirements:

Design:

2D LIST

Development:

'''

# for the random number generator
import random
# time used to sleep the program during execution which allows the program to run slow enough to see the locations change
import time
outputFile = open("HW2goodwinOutfile.txt", "w")

introMessage = """Dice Rolling Simulation - 
Program simulates navigating of a pyramid of integers using a four sided die.
Number of the die indicates direction to travel on the pyramid.  If there is a valid location to travel to
then the location is updated and that location is marked as visited.  Every visit is recorded.
If a move is not valid, counts as another visit at the current location.
Game continues until all locations are visited.
When game terminates, vital statistics are reported."""

print(introMessage + "\n")
outputFile.write(introMessage + "\n\n")




# declaring the gameBoardLocation list.  Lists are index from 0. Ignoring index 0 for this project
gameBoardLocation = [[0, 0, 0, 0, 0]] * 22

# gameBoardLocation contains the game data for each position on the board.
# Data is as follows:
# index 0 - dot count
# index 1 - Valid Upper Left Movement
# index 2 - Valid Lower Left Movement
# index 3 - Valid Upper Right Movement
# index 4 - Valid Lower Right Movement
# index of gameBoardLocation cooresponds to a location on the pyramid.
# Example: gameBoardLocation[1] refers to position 1


# gameDotTracker keeps count times a location is visited.  Game ends when all locations visited.
gameDotTracker = [0] * 22
gameDotTracker[0] = 1  # declaring 0 index location as visited because this location is not used in this project
gameDotTracker[1] = 1  # location one starts as visited

# gameBoardLocation encoding
gameBoardLocation[0] = [0, None, None, None, None] # unused for this project
gameBoardLocation[1] = [0, None, 2, None, 3]  # dot count starts at 0, valid moves are lower left, lower right
gameBoardLocation[2] = [0, None, 4, 1, 5]
gameBoardLocation[3] = [0, 1, 5, None, 6]
gameBoardLocation[4] = [0, None, 7, 2, 8]
gameBoardLocation[5] = [0, 2, 8, 3, 9]
gameBoardLocation[6] = [0, 3, 9, None, 10]
gameBoardLocation[7] = [0, None, 11, 4, 12]
gameBoardLocation[8] = [0, 4, 12, 5, 13]
gameBoardLocation[9] = [0, 5, 13, 6, 14]
gameBoardLocation[10] = [0, 6, 14, None, 15]
gameBoardLocation[11] = [0, None, 16, 7, 17]
gameBoardLocation[12] = [0, 7, 17, 8, 18]
gameBoardLocation[13] = [0, 8, 18, 9, 19]
gameBoardLocation[14] = [0, 9, 19, 10, 20]
gameBoardLocation[15] = [0, 10, 20, None, 21]
gameBoardLocation[16] = [0, None, None, 11, None]
gameBoardLocation[17] = [0, 11, None, 12, None]
gameBoardLocation[18] = [0, 12, None, 13, None]
gameBoardLocation[19] = [0, 13, None, 14, None]
gameBoardLocation[20] = [0, 14, None, 15, None]
gameBoardLocation[21] = [0, 15, None, None, None]

# this variable controls if the game is continuing to play.  Once all locations have been visited once, stillPlaying
# will change to false and terminate the game
stillPlaying = True
diceRoll = 0
currentLocation = 1
print("Game Location: " + str(currentLocation), end='')
outputFile.write("Game Location: " + str(currentLocation))

while stillPlaying:

    # simulate a dice rolling by generating random value 1 to 4. Each value represents a direction to move as follows:
    # 1 = Upper Left, 2 = Lower Left, 3 = Upper Right, 4 = Lower Right
    diceRoll = random.randint(1, 4)
    # added this sleep so I could watch the program execute instead of instantly complete.
    time.sleep(0.005)

# this section checks to see if the location selected by the dice roll is valid.  if so, updates the visit counter and
# changes current location to the new location on the gameboard.
# if the move is not valid, increments the counter for the currentlocation
    if gameBoardLocation[currentLocation][diceRoll] is not None:
        currentLocation = gameBoardLocation[currentLocation][diceRoll]
        gameBoardLocation[currentLocation][0] += 1
        gameDotTracker[currentLocation] += 1
        print(",", end='')
        print(str(currentLocation), end='')
        outputFile.write("," + str(currentLocation))
        # print("Move valid.  New Location is " + str(currentLocation) + ". Incrementing count. Location " + str(currentLocation) +
        # " has been visited " + str(gameBoardLocation[currentLocation][0]) + " times")
    else:
        # print("Unable to move.  Incrementing count for location " + str(currentLocation))
        currentLocation = currentLocation
        gameDotTracker[currentLocation] += 1
        gameBoardLocation[currentLocation][0] += 1
        print(",", end='')
        print(str(currentLocation), end='')
        outputFile.write("," + str(currentLocation))


# this code checks to see if 0 does not exist in the gameDotTracker array.  If not, stillPlaying changes to False and the game ends
    if 0 not in gameDotTracker:
        stillPlaying = False
        print(".")
        outputFile.write(".\n")


# Reporting
print("\nGame Statistics:\n")
outputFile.write("\nGame Statistics:\n\n")

totalMoves = sum(gameDotTracker)
print("Total moves to complete the game: " + str(totalMoves - 1))
outputFile.write("Total moves to complete the game: " + str(totalMoves - 1) + "\n")
print("Average visits per location: " + str((totalMoves - 1)/21))
outputFile.write("Average visits per location: " + str((totalMoves - 1)/21) + "\n")
maxDots = max(gameDotTracker)
print("Maximum visits to any one location: " + str(maxDots))
outputFile.write("Maximum visits to any one location: " + str(maxDots) + "\n")

for index, dots in enumerate(gameDotTracker, start=1):
    if dots == maxDots:
        print("Location " + str(index-1) + " had most visits of " + str(dots))
        outputFile.write("Location " + str(index-1) + " had most visits of " + str(dots) + "\n")
        
outputFile.close()












