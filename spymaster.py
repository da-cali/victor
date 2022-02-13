from joblib import load, dump
from gensim import downloader
from fuzzywuzzy import fuzz

# Load local version of model. Download and store otherwise.
print("Loading model...")
try:
    model = load("model.pkl")
except Exception:
    model = downloader.load('word2vec-google-news-300')
    dump(model, "model.pkl")

# Returns a list of tuples (clue_objectives,potential_clues) given a set of words.
# This function uses word embeddings to generate objectives (iterating over every
# word to find similar words within the set) and clues for the objectives.
# To do: Refactor to consider list of negative, neutral, and assasin words.
def spymaster_clues(set_of_words):
    objectives_and_clues = []
    for word in set_of_words:
        similar_words = model.most_similar(word,topn=100000)
        similar_words_within_set = [w for w,_ in similar_words if w in set_of_words]
        clue_objectives = sorted([word]+similar_words_within_set)
        if len(clue_objectives) > 1 and clue_objectives not in [o for o,_ in objectives_and_clues]:
            potential_clues = model.most_similar(positive=clue_objectives,topn=20)
            filtered_potential_clues = [(clue,score) for clue,score in potential_clues 
                                        if "_" not in clue and all([fuzz.partial_ratio(w,clue)<65 for w in set_of_words])]
            objectives_and_clues.append((clue_objectives,filtered_potential_clues))
    return sorted(objectives_and_clues,key=(lambda tup: tup[1][0][1]),reverse=True)

# Run the spymaster function on a custom input set of words.
while True:
    spymaster_words = input("\nEnter a set of words separated by spaces, or press enter to use example set of words.\n")
    if spymaster_words == "":
        with open("words/red.txt","r") as file:
            set_of_words = [word for word in file.read().split("\n") if word != ""]
        print(f"Example clues from the set {set_of_words}:")
    else:
        set_of_words = spymaster_words.split()
    print("\nPotential clues:")
    [print(f"\nObjective: \n{objective} \nClues:\n {clues}") for objective,clues in spymaster_clues(set_of_words)]