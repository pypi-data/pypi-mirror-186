import numpy as np

from optimizers_af.optimizers import ParticleCollisionAlgorithm
from optimizers_af.test_functions import test_func_1, de_jong_1, rosenbrock


FUNCTIONS = (
    # test_func_1,
    # de_jong_1,
    rosenbrock,
)
INITIAL_POINTS = (
    # np.array([3.10, 2.70, 4.20, 3.1, 4.1, .59]),
    # np.array([3.10, 2.70, 4.20, 3.1, 4.1, .59]),
    np.array([1.10, 2.03]),
)

test_points_rmo = []
for func, point in zip(FUNCTIONS, INITIAL_POINTS):
    PCA = ParticleCollisionAlgorithm(
        func=func,
        generations_number=10000,
        bounds=[(-2.048, 2.048) for _ in range(point.size)],
    )
    test_points_rmo.append(PCA.run(point=point)[0])

for func, point in zip(FUNCTIONS, test_points_rmo):
    print(f'PCA: Minimum of `{func.__name__}`: {str(point.round(2))}')
