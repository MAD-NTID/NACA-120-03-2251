"""
@author: <Your name>
date: <today's date>
Project code name: HandBattle
Purpose:
    A program that plays Morra
"""

import datetime
import random

# PREDEFINED BELOW, DO NOT MODIFY ANY CODE
LINE_SEPARATOR = "=============================="
HAND_MIN = 1
HAND_MAX = 3

"""
    This function will print the header containing 
    the game name, version number, and today's date and time
"""


def get_game_header():
    now = datetime.datetime.now()

    return \
        f"{LINE_SEPARATOR}" \
        "\nMorra" \
        "\n\tGame Version 1.0" \
        f"\n{LINE_SEPARATOR}" \
        f"\nDate and Time: {now.strftime('%d/%m/%Y %H:%M:%S')}\n"


"""
    This function generate an xp.
    The function first generate an xp
    then multiply that by the round number

    Parameter:
        game_round: The current round in the game

    returns the xp for the round
"""


def generate_xp(game_round):
    if game_round < 1:
        game_round = 1

    return random.randint(HAND_MIN, HAND_MAX) * game_round


"""
    This function will randomly pick a hand for the computer.
    This will return a hand from HAND_MIN (1) to HAND_MAX (3)
"""


def get_computer_hand():
    return random.randint(HAND_MIN, HAND_MAX)


"""
    This function will return a random hand sum guess for the computer.
    This will return a hand sum from HAND_MIN * 2 + HAND_MIN * 2
"""


def get_computer_guess():
    return random.randint(HAND_MIN, HAND_MAX) + random.randint(HAND_MIN, HAND_MAX)
# PREDEFINED ABOVE, DO NOT MODIFY ANY CODE


# STUDENT CODE HERE
def determine_winner(player_hand, player_guess, computer_hand, computer_guess):
    # Returns “tie”, “player”, “computer”, “no winner”
    hand_sum = player_hand + computer_hand

    if player_guess == hand_sum and computer_guess == hand_sum:
        return "tie"
    elif player_guess == hand_sum and computer_guess != hand_sum:
        return "player"
    elif player_guess != hand_sum and computer_guess == hand_sum:
        return "computer"
    else:
        return "no winner"

def get_player_hand():
    while True:
        try:
            # player_hand = int(input("Enter a hand between " + str(HAND_MIN) + " and " +  str(HAND_MAX) + ": "))
            player_hand = int(input(f"Enter a hand between {HAND_MIN} and {HAND_MAX}: "))

            if player_hand >= HAND_MIN and player_hand <= HAND_MAX:
                return player_hand
        except:
            print("Invalid Hand\n")


def get_player_guess():
    while True:
        try:
            # player_guess = int(input("Enter a guess between", (HAND_MIN + 1), " and", (HAND_MAX * 2), ": "))
            player_guess = int(input(f"Enter a guess between {HAND_MIN + 1} and {HAND_MAX * 2}: "))

            if player_guess >= (HAND_MIN + 1) and player_guess <= (HAND_MAX * 2):
                return player_guess
        except:
            print("Invalid Guess\n")

def get_stats(player_score, player_wins, computer_score, computer_wins):
    return \
        f"Player Score: {player_score}\n" \
        f"Player Wins: {player_wins}\n" \
        f"Computer Score: {computer_score}\n" \
        f"Computer Wins: {computer_wins}\n"

def get_play_again_prompt():
    player_choice = None

    while True:
        player_choice = input("Would you like to play another round? (yes or quit): ")
        if player_choice.lower() in ['yes', 'quit']:
            break
        else:
            print("That's not a valid choice. Try again. \n")

    return player_choice

def main():
    player_score = 0
    player_wins = 0
    computer_score = 0
    computer_wins = 0
    game_round = 1

    # STUDENT CODE HERE
    print(get_game_header())

    while True:
        # 1.	Display the statistics only after round 1
        if game_round > 1:
            print(get_stats(player_score, player_wins, computer_score, computer_wins))

        # 2.	Display the current game round
        print(f"Game Round {game_round}")

        """
        3.	Call the appropriate function to get the computer's hand. 
            Store in a variable for use later. This should be kept secret 
            and not displayed to the user
        """
        computer_hand = get_computer_hand()

        """
        4.	Call the appropriate function to get the computer’s guess. 
            Store in a variable for use later. This should be kept secret 
            and not displayed to the user
        """
        computer_guess = get_computer_guess()

        """
        5.	Call the appropriate function to prompt the player for their hand, 
            and store in a variable for use later.
        """
        player_hand = get_player_hand()

        """
        6.	Call the appropriate function to prompt the player for their guess, 
            and store in a variable for use later.
        """
        player_guess = get_player_guess()

        print(f"\nComputer's Hand: {computer_hand}")
        print(f"Computer's Guess: {computer_guess}\n")

        """
        7.	Determine the winner of the round based on the computer and the user’s 
            hand, and guessed number, by calling the appropriate function
        """
        winner = determine_winner(player_hand, player_guess, computer_hand, computer_guess)

        """
        8.	Display the winner of the round, if any:
            •	Update the user's total score, and XP
        """
        print(f"The sum of both hands is {player_hand + computer_hand}")

        if winner == "player":
            player_wins += 1
            player_score += generate_xp(game_round)
            print("Player won the round")
        elif winner == "computer":
            computer_wins += 1
            computer_score += generate_xp(game_round)
            print("Computer won the round")
        else:
            # display 'tie' or 'no winner'
            print(f"{winner}")
        

        """
        9.	Ask if the user wants to play another round, and proceed accordingly:
            •	If the user chooses to “quit”, thank them for playing and gracefully 
                terminate the program. 
            •	If the user chooses “yes”, repeat the game for a new round. 
                Increment the round by 1.

        """
        play_again = get_play_again_prompt()

        if play_again == "yes":
            game_round += 1
        
        if play_again == "quit":
            break

    print("Thank you for playing Morra!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram was ended abruptly by the user\n")