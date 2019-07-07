


def swap_str_character(word: str, char_index: int, new_char: str):
    l = list(word)
    l[char_index] = new_char
    return "".join(l)

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