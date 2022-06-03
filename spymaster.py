from fuzzywuzzy import fuzz

# Returns a list of tuples (words_to_guess,clues) given a set of words.
# This function uses word embeddings to generate objectives (iterating over every
# word to find similar words within the set) and clues for the objectives.
def spymaster_clue(model,ally_agents,opposite_agents,bystanders,assasin):
    # Generate candidates for clues by finding groups of similar words
    # within the ally_agents and looking for related words to all of them.
    candidates = []
    MAX_WORDS_TO_CONSIDER = 100000
    THRESH = 65
    for word in ally_agents:
        similar_words = model.most_similar(word,topn=MAX_WORDS_TO_CONSIDER)
        similar_words_within_set = [w for w,_ in similar_words if w in ally_agents]
        words_to_guess = sorted([word]+similar_words_within_set)
        if words_to_guess not in [wtg for wtg,_ in candidates]:
            raw_potential_clues = model.most_similar(positive=words_to_guess,topn=50)
            legal_potential_clues = [(clue,score) for clue,score in raw_potential_clues 
                                    if "_" not in clue and all([fuzz.partial_ratio(w,clue)<THRESH for w in ally_agents])]
            refined_potential_clues = []
            for clue,score in legal_potential_clues:
                if all([fuzz.partial_ratio(clue,refined_clue)<THRESH for refined_clue in refined_potential_clues]):
                    refined_potential_clues.append((clue,score))
            candidates.append((words_to_guess,refined_potential_clues))
    # Group the candidates into groups of the same length, sorted by length.
    groups = {}
    for wtg,clues in candidates:
        length = len(wtg)
        if length in groups:
            groups[length].append((wtg,clues))
        else:
            groups[length] = [(wtg,clues)]
    sorted_groups = [groups[n] for n in sorted(groups,reverse=True)]
    # Return best clue filtering out clues for non ally agents.
    for group in sorted_groups:
        sorted_candidates = sorted(group,key=(lambda tup: tup[1][0][1]),reverse=True)
        for objective,clues in sorted_candidates:
            for clue,_ in clues:
                if all([word not in model.most_similar(clue,topn=MAX_WORDS_TO_CONSIDER) for word in (opposite_agents+bystanders+assasin)]):
                    return (objective,clue)
    first_candidate = sorted_groups[0][0]
    return (first_candidate[0],first_candidate[0][0])
