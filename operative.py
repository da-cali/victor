# Returns a list of guesses given a clue, and a set of possible codenames.
def operative_guesses(model, codenames, clue):
    similarities_with_clue = [(model.similarity(w, clue), w) for w in codenames]
    return sorted(similarities_with_clue, reverse=True)