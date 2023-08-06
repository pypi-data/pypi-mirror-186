import numpy as np

from optimizers_af.optimizers import HookeJeeves, RadialMovementOptimization
from optimizers_af.test_functions import test_func_1, de_jong_1, rastrigin


FUNCTIONS = (test_func_1, de_jong_1, rastrigin)
INITIAL_POINTS = (
    np.array([3.10, 2.70, 4.20, 3.1, 4.1, .59]),
    np.array([3.10, 2.70, 4.20, 3.1, 4.1, .59]),
    np.array([3.10, 2.70, 4.20, 3.1, 4.1, .59]),
)

test_points_hj = []
for func, point in zip(FUNCTIONS, INITIAL_POINTS):
    HJ = HookeJeeves(
        func=func,
        accuracy=1e-7,
        initial_step_size=1.0,
        step_reduction_factor=0.5,
    )
    test_points_hj.append(HJ.run(point=point)[0])

test_points_rmo = []
for func, point in zip(FUNCTIONS, INITIAL_POINTS):
    RMO = RadialMovementOptimization(
        func=func,
        generations_number=10000,
        particles_number=10,
        bounds=(-5.12, 5.12),
        c_parameters=(0.6, 0.7),
        weight_limits=(0, 1),
        scale=2,
    )
    test_points_rmo.append(RMO.run(point=point)[0])

for func, point in zip(FUNCTIONS, test_points_hj):
    print(f'HJ: Minimum of `{func.__name__}`: {str(point.round(2))}')
for func, point in zip(FUNCTIONS, test_points_rmo):
    print(f'RMO: Minimum of `{func.__name__}`: {str(point.round(2))}')
