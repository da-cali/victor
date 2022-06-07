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

def play(t1,t1_name,t2,t2_name,b,a):
    result = "Next turn."
    print(f"\n--------- {t1_name} team turn ---------\n\n{t1_name} spymaster:")
    objective,clue = spymaster_clue(model,t1,t2,b,a)
    print(f"Objective: {objective} \nClue: '{clue}' for {len(objective)}.")
    print(f"\n{t1_name} operatives:")
    guesses = operative_guesses(model,(t1+t2+b+a),clue)
    for i in range(len(objective)):
        guess = guesses[i][1]
        print(f"Guess: {guess}")
        if guess in a:
            result = f"{t1_name} team loses."
            break
        elif guess in b:
            b.remove(guess)
            print("✖️")
            break
        elif guess in t2:
            print("✖️")
            t2.remove(guess)
            if t2 == []:
                result = f"{t2_name} team wins."
            break
        else:
            print("✔️")
            t1.remove(guess)
            if t1 == []:
                result = f"{t1_name} team wins."
                break
            if len(objective)-1 == i:
                break
    if result == "Next turn.":
        return play(t2,t2_name,t1,t1_name,b,a)
    else:
        return result

# Play.
print("\nPlease enter the codenames (separated by spaces).")
red = input("\nRed agents:\n").split()
blue = input("\nBlue agents:\n").split()
yellow = input("\nBystanders:\n").split()
black = input("\nAssasin:\n").split()
result = play(red,"RED",blue,"BLUE",yellow,black)
print(f"\nGame over. {result}")
