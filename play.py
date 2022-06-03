from joblib import load, dump
from gensim import downloader
from spymaster import spymaster_clue
from operative import operative_guesses

# Load local version of model. Download and store otherwise.
print("Loading model...")
try:
    model = load("model.pkl")
except Exception:
    model = downloader.load('word2vec-google-news-300')
    dump(model, "model.pkl")

# Initialize new game.
red = input("\nEnter the red agents' codenames (separated by spaces).\n").split()
blue = input("\nEnter the blue agents' codenames.\n").split()
yellow = input("\nEnter the bystanders' codenames.\n").split()
black = input("\nEnter the assasin's codename.\n").split()

# Play.
game_on = True
while game_on:
    for team in ["Red","Blue"]:
        print(f"\n---------- {team} team turn. ----------")
        print(f"\n{team} spymaster:")
        if team == "Red":
            objective,clue = spymaster_clue(model,red,blue,yellow,black)
        else:
            objective,clue = spymaster_clue(model,blue,red,yellow,black)
        print(f"Objective: \n{objective} \nClue:\n {clue}")
        print(f"\n{team} operatives:")
        guesses = operative_guesses(model,(red+blue+yellow+black),clue)
        for i in range(len(objective)):
            guess = guesses[i][1]
            print(f"Guess: {guess}")
            if guess in black:
                print(f"Guess is assasin. {team} team loses.")
                quit()
            elif guess in yellow:
                yellow.remove(guess)
                print("Incorrect guess. End of turn.")
                break
            else:
                if team == "Red":
                    if guess in red:
                        print("Correct guess.")
                        red.remove(guess)
                        if red == []:
                            print("Red team wins.")
                            quit()
                    else:
                        print("Incorrect guess. End of turn.")
                        blue.remove(guess)
                        if blue == []:
                            print("Blue team wins.")
                            quit()
                else:
                    if guess in blue:
                        print("Correct guess.")
                        blue.remove(guess)
                        if blue == []:
                            print("Blue team wins.")
                            quit()
                    else:
                        print("Incorrect guess. End of turn.")
                        red.remove(guess)
                        if red == []:
                            print("Red team wins.")
                            quit()
print("Game over.")
