import evolution_chamber as evo
from evolution_chamber_util import write_candidates_to_file

available_characters = "ABCDEFGHIJKLMNOPRSTUWXYZ "
target_word = "GIMME GIMME GIMME A MAN AFTER MIDNIGHT"


def evolve(target, character_set, max_iterations, parent_group_size, one_pair_offspring, save_dir_path):
    # init
    candidates = evo.random_fixed_size_candidates(character_set, len(target), parent_group_size)
    write_candidates_to_file(f'{save_dir_path}/ancestors', candidates)
    # main loop
    for i in range(0, max_iterations):
        fittest = evo.fittest_candidates(candidates, parent_group_size, target)
        if fittest[0].word == target:
            print(f"In {i} iterations found the perfect specimen :")
            print(fittest[0].word)
            return 0
        candidates = evo.breed(fittest, character_set, one_pair_offspring)
        write_candidates_to_file(f'{save_dir_path}/generation{i}', candidates)

    print("Failed to find a perfect specimen ")
    return -1


evolve(target_word, available_characters, 100, 5, 5, 'candidates')
