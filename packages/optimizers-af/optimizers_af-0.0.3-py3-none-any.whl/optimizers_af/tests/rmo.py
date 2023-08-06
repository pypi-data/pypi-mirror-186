import numpy as np

from optimizers_af.optimizers import RadialMovementOptimization
from optimizers_af.test_functions import test_func_1, de_jong_1, rastrigin


FUNCTIONS = (
    test_func_1,
    de_jong_1,
    rastrigin,
)
INITIAL_POINTS = (
    np.array([3.10, 2.70, 4.20, 3.1, 4.1, .59]),
    np.array([3.10, 2.70, 4.20, 3.1, 4.1, .59]),
    np.array([3.10, 2.70, 4.20, 3.1, 4.1, .59]),
)

test_points_rmo = []
for func, point in zip(FUNCTIONS, INITIAL_POINTS):
    RMO = RadialMovementOptimization(
        func=func,
        generations_number=20000,
        particles_number=100,
        bounds=[(-5.12, 5.12) for _ in range(point.size)],
        c_parameters=(0.7, 0.8),
        weight_limits=(0, .5),
        scale=1,
    )
    test_points_rmo.append(RMO.run(point=point)[0])

for func, point in zip(FUNCTIONS, test_points_rmo):
    print(f'RMO: Minimum of `{func.__name__}`: {str(point.round(2))}')
