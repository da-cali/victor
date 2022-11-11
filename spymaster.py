from fuzzywuzzy import fuzz


# Returns a tuple (words_to_guess,clue) given a turn state and a model.
# This function uses word vectors to generate objectives (iterating over every
# word to find similar words within the set) and clues for the objectives.
def spymaster_clue(model, ally_agents, opposite_agents, bystanders, assasin):

    # Constants for model and fuzziness.
    words_to_consider = 100000
    max_similarity = 50

    # Returns a list of (similar_codenames,potential_clues) tuples given a list
    # of codenames (words), where similar_codenames is a group of semantically 
    # similar codenames in input list, and potential_clues is a list of words 
    # semantically related to the group, along with their similarity scores.
    def potential_objectives(codenames):
        candidates = []
        for codename in codenames:
            similar_words = model.most_similar(codename, topn=words_to_consider)
            similar_codenames = sorted([codename] + [w for w, _ in similar_words if w in codenames])
            if similar_codenames not in [words for words, _ in candidates]:
                raw_clues = model.most_similar(positive=similar_codenames, topn=50)
                legal_clues = [
                    (clue, score) for clue, score in raw_clues if "_" not in clue and 
                    all([fuzz.partial_ratio(w, clue) < max_similarity for w in codenames])]
                refined_clues = []
                for clue, score in legal_clues:
                    if all([fuzz.partial_ratio(clue, refined_clue) < max_similarity 
                            for refined_clue in refined_clues]):
                        refined_clues.append((clue, score))
                candidates.append((similar_codenames, refined_clues))
        return candidates
    
    # Group the candidates into groups of the same length, sorted by length.
    groups = {}
    ally_objectives = potential_objectives(ally_agents)
    for codenames, clues in ally_objectives:   
        length = len(codenames)
        if length in groups:
            groups[length].append((codenames, clues))
        else:
            groups[length] = [(codenames, clues)]
    sorted_groups = [groups[n] for n in sorted(groups, reverse=True)]
    
    # Return best candidate filtering out clues for non ally agents.
    # Return first sorted candidate if no safe clue was found.
    for group in sorted_groups:
        sorted_candidates = sorted(group, key=(lambda tup: tup[1][0][1]), reverse=True)
        for words, clues in sorted_candidates:
            for clue, _ in clues:
                if all([word not in model.most_similar(clue, topn=words_to_consider) 
                        for word in (opposite_agents + bystanders + assasin)]):
                    return (words, clue)
    first_candidate = sorted_groups[0][0]
    return (first_candidate[0], first_candidate[0][0])
