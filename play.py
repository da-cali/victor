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

# Simulates a Codenames game and returns the result as a string.
def play(t1_agents,t1_name,t2_agents,t2_name,bystanders,assasin):
    result = "Next turn."
    print(f"\n--------- {t1_name} team turn ---------\n")
    print(f"{t1_name} spymaster:")
    objective,clue = spymaster_clue(model,t1_agents,t2_agents,bystanders,assasin)
    objective_size = len(objective)
    print(f"Objective: {objective} \nClue: '{clue}' for {objective_size}.")
    print(f"\n{t1_name} operatives:")
    guesses = operative_guesses(model,(t1_agents+t2_agents+bystanders+assasin),clue)
    for i in range(objective_size):
        guess = guesses[i][1]
        print(f"Guess: {guess}")
        if guess in assasin:
            result = f"☠️ Assasin. {t1_name} team loses."
            break
        elif guess in bystanders:
            bystanders.remove(guess)
            print("✖️")
            break
        elif guess in t2_agents:
            print("✖️")
            t2_agents.remove(guess)
            if t2_agents == []:
                result = f"{t2_name} team wins."
            break
        else:
            print("✔️")
            t1_agents.remove(guess)
            if t1_agents == []:
                result = f"{t1_name} team wins."
                break
            if objective_size - 1 == i:
                break
    if result == "Next turn.":
        return play(t2_agents,t2_name,t1_agents,t1_name,bystanders,assasin)
    else:
        return result

# Set up game and play.
print("\nPlease enter the codenames (separated by spaces).")
red = input("\nRed agents:\n").split()
blue = input("\nBlue agents:\n").split()
yellow = input("\nBystanders:\n").split()
black = input("\nAssasin:\n").split()
result = play(red,"RED",blue,"BLUE",yellow,black)
print(f"\nGame over. {result}")
