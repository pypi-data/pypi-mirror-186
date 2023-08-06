import numpy as np


class BoundConstrained:

    def __init__(
            self,
            bounds: list[tuple[float, float]],
            **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.dimension = len(bounds)
        self.inferior_bounds, self.superior_bounds = np.array(bounds).T

    def _check_point_shape(
            self,
            point: np.ndarray,
            arg_name: str = 'point',
    ) -> None:
        _required_shape = (self.dimension,)
        if point.shape != _required_shape:
            raise ValueError(
                f'Wrong shape of `{arg_name}`: {point.shape}.'
                f' Required shape: {_required_shape}.'
            )

    def _get_random_point(self) -> np.ndarray:
        return (
                self.inferior_bounds
                + (self.superior_bounds - self.inferior_bounds)
                * np.random.random(self.dimension)
        )

    def _get_shifted_points(
            self,
            centre: np.ndarray,
            shifts: np.ndarray,
    ) -> np.ndarray:
        _required_shape = (self.dimension,)
        self._check_point_shape(point=centre, arg_name='centre')
        self._check_point_shape(point=shifts[0], arg_name='shift')
        return np.clip(
            a=centre + shifts,
            a_min=self.inferior_bounds,
            a_max=self.superior_bounds,
        )
