import numpy as np
from symeess.molecule.geometry import Geometry
from symeess.shape import get_test_structure, _get_symmetry_angle


def get_shape_map(shape_label1, shape_label2, central_atom=None, num_points=50):
    ideal_structure = get_test_structure(shape_label1, central_atom)
    ideal_label_structure = []
    symbol = []
    for idx, atom in enumerate(ideal_structure):
        if idx == 0:
            atom = np.ndarray.tolist(atom)
            symbol.append('M')
        else:
            atom = np.ndarray.tolist(atom)
            symbol.append('L')
        ideal_label_structure.append(atom)
    ideal_label_structure = [symbol, ideal_label_structure]

    geometry = Geometry(ideal_label_structure)
    S_label1 = [0]
    S_label2 = [geometry.get_shape_measure(shape_label2, 0)]
    theta = _get_symmetry_angle(shape_label1, shape_label2)
    dtheta = np.linspace(0, theta, num_points)
    for angle in dtheta[1:]:
        a_label1 = angle
        a_label2 = theta - a_label1
        S_label1.append(100 * (np.sin(np.radians(a_label1)) ** 2))
        S_label2.append((100 * (np.sin(np.radians(a_label2)) ** 2)))
    return S_label1, S_label2