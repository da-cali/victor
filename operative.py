from joblib import load, dump
from gensim import downloader

# Load local version of model. Download and store otherwise.
print("Loading model...")
try:
    model = load("model.pkl")
except Exception:
    model = downloader.load('word2vec-google-news-300')
    dump(model,"model.pkl")

# Returns a list of guesses given a clue, and a set of possible words.
def operative_guesses(words,clue):
    similarities_with_clue = [(model.similarity(w,clue),w) for w in words]
    return sorted(similarities_with_clue,reverse=True)

# Run the operative function with custom input clue set of words.
# To do: target_number = int(input("\nEnter a target number:"))
while True:
    operative_words = input("\nEnter a set of words (separated by spaces) for the operative. Press enter to use example set of words.\n")
    if operative_words == "":
        with open("words/all.txt","r") as file:
            set_of_words = [word for word in file.read().split("\n") if word != ""]
        print(f"Example clues from the set {set_of_words}:")
    else:
        set_of_words = operative_words.split()
    clue = input("\nEnter a clue:")
    print("\nOperative guesses:")
    [print(guess) for guess in operative_guesses(set_of_words,clue)]
