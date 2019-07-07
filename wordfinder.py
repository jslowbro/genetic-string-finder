import random


class Candidate:

    def __init__(self, word):
        self.word = word
        self.truth_list = len(word) * [0]

    def __repr__(self):
        return "\n" + self.word + "\n" + self.truth_list.__str__() + "\n"


def evaluate_candidate(candidate: Candidate, target: str):
    for i in range(0, len(target)):
        if candidate.word[i] == target[i]:
            candidate.truth_list[i] = 1
        else:
            candidate.truth_list[i] = 0

    return candidate


def fitness_score(candidate: Candidate):
    score = 0
    for i in candidate.truth_list:
        if i == 1:
            score = score + 1

    return score


def random_fixed_size_candidates(word_set, length: int, no_candidates: int):
    candidate_list = []
    for i in range(0, no_candidates):
        word = ''
        for j in range(0, length):
            word = word + random.choice(word_set)

        candidate_list.append(Candidate(word))
    return candidate_list


def write_candidates_to_file(file_name: str, candidate_list: []):
    with open(file_name, 'w+') as f:
        for candidate in candidate_list:
            f.write(candidate.word + '\n')


def read_candidates_from_file(file_name: str):
    candidate_list = []
    with open(file_name, 'r') as f:
        contents = f.readlines()
    for i in contents:
        candidate_list.append(Candidate(i.replace('\n', '')))
    return candidate_list


def fittest_candidates(candidates: [], no_alpha_specimen, target):
    fittest = sorted(candidates, key=lambda x: fitness_score(evaluate_candidate(x, target)), reverse=True)
    return fittest[:no_alpha_specimen]


def breed_pair(mother: Candidate, father: Candidate, word_set, one_pair_offspring: int):
    offspring = []
    for i in range(0, one_pair_offspring):
        offspring.append(single_breeding(mother, father, word_set))
    return offspring


def single_breeding(mother: Candidate, father: Candidate, word_set):
    child = Candidate(mother.word)
    for i in range(0, len(mother.truth_list)):
        if father.truth_list[i] == 1:
            child.word = swap_str_character(child.word, i, father.word[i])
        elif mother.truth_list[i] == 1:
            child.word = swap_str_character(child.word, i, mother.word[i])
        else:
            child.word = swap_str_character(child.word, i, random.choice(word_set))

    return child


def breed(candidates: [], word_set: str, one_pair_offspring: int):
    offspring = []
    for i in range(0, len(candidates)):
        for j in range(i, len(candidates)):
            if i != j:
                offspring.extend(breed_pair(candidates[i], candidates[j], word_set, one_pair_offspring))

    return offspring


def swap_str_character(word: str, char_index: int, new_char: str):
    l = list(word)
    l[char_index] = new_char
    return "".join(l)
