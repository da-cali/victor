# Returns a list of guesses given a clue, and a set of possible words.
def operative_guesses(model,words,clue):
    similarities_with_clue = [(model.similarity(w,clue),w) for w in words]
    return sorted(similarities_with_clue,reverse=True)