from sklearn import svm  # Import the Support Vector Machine (SVM) module from scikit-learn

history = [1, 2, 3, 2]  # Initialize a list to store the history of player moves

input_data = [  # Initialize a list to store the input data for the SVM model
    [1, 1],  # Input data for first game
    [1, 3],  # Input data for second game
    [3, 2],  # Input data for third game
    [2, 1]   # Input data for fourth game
]

output_data = [3, 2, 1, 1]  # Initialize a list to store the output data for the SVM model

model = svm.SVC()  # Initialize an SVM model

model.fit(input_data, output_data)  # Train the SVM model with the input and output data

def getPlayer2():  # Define a function to get the player's move
    choice = int(input("Please select one of the following 1) Rock, 2) Paper, 3) Scissors: "))  # Prompt the user for input
    return choice  # Return the user's choice



def getPlayer1():  # Define a function to determine the computer's move
    data_record = [history[-2], history[-1]]  # Get the player's last two moves
    current = model.predict([data_record])[0]  # Determine the computer's next move using the trained model

    # Return the move that will beat the predicted move
    if current == 1:
        return 2
    elif current == 2:
        return 3
    else:
        return 1


wins_player1 = 0  # Initialize a variable to store the number of wins for the computer
wins_player2 = 0  # Initialize a variable to store the number of wins for the player
total_ties = 0  # Initialize a variable to store the total number of ties

for i in range(1, 15):  # Iterate over a range of 1 to 14 (15 games)
    print("Game: ", i)  # Print the current game number

    comp = getPlayer1()  # Get the computer's move
    user = getPlayer2()  # Get the player's move
    print("Computer: ", comp, "vs Player: ", user)  # Print the computer's and player's moves

    # Determine the outcome of the game and update the scores
    if comp == 1 and user == 1:
        print("It's a tie!")
        total_ties += 1
    elif comp == 1 and user == 2:
        print("The user wins!")
        wins_player2 += 1
    # Continue similar comparisons for all possible combinations of moves

    # As the game progresses, we want the model to be able to see the patterns/habits of the player. To do this, we will need to update our model. If we add the user's most recent move to their history, we can then add more data to our input and output, which trains our model. By taking the 3rd and 2nd most recent game as our input, we can see what the actual result would be from the 1st most recent game. Just like what we did when we came up with patterns in our input and output data, we are getting live results as to what the player will commonly choose after looking at the player's choices for the previous 2 games.
  
    print("Updating the training model...")  # Print a message indicating the model update
    history.append(user)  # Append the player's move to the history list

    input_data.append([history[-3], history[-2]])  # Update the input data with the new historical data
    output_data.append(history[-1])  # Update the output data with the new historical data

    model.fit(input_data, output_data)  # Retrain the SVM model with the updated data
    print("Finished updating the training model")  # Print a message indicating the completion of model update

print("Computer: ", wins_player1)  # Print the total number of wins for the computer
print("Player: ", wins_player2)  # Print the total number of wins for the player
print("Total ties: ", total_ties)  # Print the total number of ties
