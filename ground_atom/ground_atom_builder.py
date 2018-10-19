__FACING_ROBOT_FACE__ = 'facing_robot_face'
__BOTTOM_FACE__ = 'bottom_face'
__OBJ_TO_BE_GRASPED__ = 'obj_to_be_grasped'
__IS_ROTATIONALLY_SYMMETRIC__ = 'is_rotationally_symmetric'
__IS_A__ = 'is_a'
__GRASP_TYPE__ = 'grasp_type'


def get_is_a(arg0, arg1):
    return __get_ground_atom_with_two_args__(__IS_A__, arg0, arg1)


def __get_ground_atom_with_two_args__(ground_atom_name, arg0, arg1):
    parameters = '({},{})'.format(arg0, arg1)
    return ground_atom_name + parameters


def __get_ground_atom_with_one_arg__(ground_atom_name, arg):
    parameter = '({})'.format(arg)
    return ground_atom_name + parameter
