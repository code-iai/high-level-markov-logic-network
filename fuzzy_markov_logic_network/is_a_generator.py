from word_net import determine_path_similarity_between_two_concepts
from ground_atom.ground_atom_builder import get_is_a


def get_is_a_ground_atoms(object, concepts):
    is_a_ground_atoms = {}

    for concept in concepts:
        similarity = determine_path_similarity_between_two_concepts(object, concept)
        ground_atom = get_is_a(object, concept)
        is_a_ground_atoms[ground_atom] = similarity

    return is_a_ground_atoms