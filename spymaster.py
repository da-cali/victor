from fuzzywuzzy import fuzz

# Returns a tuple (words_to_guess,clue) given a turn state and a model.
# This function uses word vectors to generate objectives (iterating over every
# word to find similar words within the set) and clues for the objectives.
def spymaster_clue(model,ally_agents,opposite_agents,bystanders,assasin):
    # Find groups of related words and generate potential clues for them.
    # Candidates are stored as tuples (words_to_guess,potential_clues).
    WORDS_TO_CONSIDER = 100000
    MAX_SIMILARITY= 50
    candidates = []
    for codename in ally_agents:
        similar_words = model.most_similar(codename,topn=WORDS_TO_CONSIDER)
        similar_ally_codenames = [w for w,_ in similar_words if w in ally_agents]
        words_to_guess = sorted([codename]+similar_ally_codenames)
        if words_to_guess not in [words for words,_ in candidates]:
            raw_clues = model.most_similar(positive=words_to_guess,topn=50)
            legal_clues = [(clue,score) for clue,score in raw_clues if "_" not in clue and 
                           all([fuzz.partial_ratio(w,clue)<MAX_SIMILARITY for w in ally_agents])]
            refined_clues = []
            for clue,score in legal_clues:
                if all([fuzz.partial_ratio(clue,refined_clue)<MAX_SIMILARITY 
                        for refined_clue in refined_clues]):
                    refined_clues.append((clue,score))
            candidates.append((words_to_guess,refined_clues))
    # Group the candidates into groups of the same length, sorted by length.
    groups = {}
    for words,clues in candidates:   
        length = len(words)
        if length in groups:
            groups[length].append((words,clues))
        else:
            groups[length] = [(words,clues)]
    sorted_groups = [groups[n] for n in sorted(groups,reverse=True)]
    # Return best candidate filtering out clues for non ally agents.
    # Return first sorted candidate if no safe clue was found.
    for group in sorted_groups:
        sorted_candidates = sorted(group,key=(lambda tup: tup[1][0][1]),reverse=True)
        for words,clues in sorted_candidates:
            for clue,_ in clues:
                if all([word not in model.most_similar(clue,topn=WORDS_TO_CONSIDER) 
                        for word in (opposite_agents+bystanders+assasin)]):
                    return (words,clue)
    first_candidate = sorted_groups[0][0]
    return (first_candidate[0],first_candidate[0][0])
