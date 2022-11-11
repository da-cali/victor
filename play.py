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
def play(t1_agents, t1_name, t2_agents, t2_name, bystanders, assasin):
    result = "Next turn."
    print(f"\n<= {t1_name} team turn =>\n{t1_name} spymaster:")
    objective, clue = spymaster_clue(model, t1_agents, t2_agents, bystanders, assasin)
    objective_size = len(objective)
    print(f"Objective: {objective}\n"
          + f"Clue: '{clue}' for {objective_size}."
          + f"\n{t1_name} operatives:")
    guesses = operative_guesses(model, (t1_agents + t2_agents + bystanders + assasin), clue)
    end_of_turn, ith_guess = False, 0
    while not end_of_turn:
        guess = guesses[ith_guess][1]
        print(f"Guess: {guess}")
        if guess in assasin:
            result, end_of_turn = f"☠️ Assasin. {t1_name} team loses.", True
        elif guess in bystanders:
            bystanders.remove(guess)
            print("✖️ Bystander.")
            end_of_turn = True
        elif guess in t2_agents:
            print(f"✖️ {t2_name} team agent.")
            t2_agents.remove(guess)
            if t2_agents == []:
                result = f"{t2_name} team wins."
            end_of_turn = True
        else:
            print("✔️ Correct!")
            t1_agents.remove(guess)
            if t1_agents == []:
                result, end_of_turn = f"{t1_name} team wins.", True
            if objective_size - 1 == ith_guess:
                end_of_turn = True
        ith_guess += 1
    if result == "Next turn.":
        return play(t2_agents, t2_name, t1_agents, t1_name, bystanders, assasin)
    else:
        return result


# Set up game and play.
print("\nPlease enter the codenames (separated by spaces).")
red = input("\nRed agents:\n").split()
blue = input("\nBlue agents:\n").split()
yellow = input("\nBystanders:\n").split()
black = input("\nAssasin:\n").split()
result = play(red, "RED", blue, "BLUE", yellow, black)
print(f"\nGame over. {result}")
