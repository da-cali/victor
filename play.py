from joblib import load, dump
from gensim import downloader
from spymaster import spymaster_clue
from operative import operative_guesses

# Load local version of model. Download and store otherwise.
print("\nLoading model...")
try:
    model = load("model.pkl")
except Exception:
    model = downloader.load('word2vec-google-news-300')
    dump(model, "model.pkl")

# Initialize new game.
print("\nPlease enter the codenames (separated by spaces).")
red = input("\nRed agents:\n").split()
blue = input("\nBlue agents:\n").split()
yellow = input("\nBystanders:\n").split()
black = input("\nAssasin:\n").split()

# Play.
game_on = True
while game_on:
    for team in ["RED","BLUE"]:
        print(f"\n---------- {team} team turn ----------\n\n{team} spymaster:")
        if team == "RED":
            objective,clue = spymaster_clue(model,red,blue,yellow,black)
        else:
            objective,clue = spymaster_clue(model,blue,red,yellow,black)
        print(f"Objective: {objective} \nClue: '{clue}' for {len(objective)}.")
        print(f"\n{team} operatives:")
        guesses = operative_guesses(model,(red+blue+yellow+black),clue)
        for i in range(len(objective)):
            guess = guesses[i][1]
            print(f"Guess: {guess}")
            if guess in black:
                print(f"\n☠️ Assasin. \n{team} team loses.")
                quit()
            elif guess in yellow:
                yellow.remove(guess)
                print("✖️")
                break
            else:
                if team == "RED":
                    if guess in red:
                        print("✔️")
                        red.remove(guess)
                        if red == []:
                            print("\nRed team wins.")
                            quit()
                    else:
                        print("✖️")
                        blue.remove(guess)
                        if blue == []:
                            print("\nBlue team wins.")
                            quit()
                        break
                else:
                    if guess in blue:
                        print("✔️")
                        blue.remove(guess)
                        if blue == []:
                            print("\nBlue team wins.")
                            quit()
                    else:
                        print("✖️")
                        red.remove(guess)
                        if red == []:
                            print("\nRed team wins.")
                            quit()
                        break