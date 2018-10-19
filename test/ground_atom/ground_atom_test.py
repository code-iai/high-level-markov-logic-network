from ground_atom.ground_atom import GroundAtom

TEST_GROUND_ATOM_1 = 'test(test1)'
TEST_GROUND_ATOM_2 = 'test(test1,test2)'


def test_should_return_str_representation_of_one_instance_ground_atom():
    one_instance_ground_atom = GroundAtom('test', ['test1'])
    assert str(one_instance_ground_atom) == TEST_GROUND_ATOM_1


def test_should_return_str_representation_of_two_instances_ground_atom():
    two_instances_ground_atom = GroundAtom('test', ['test1', 'test2'])
    assert str(two_instances_ground_atom) == TEST_GROUND_ATOM_2

