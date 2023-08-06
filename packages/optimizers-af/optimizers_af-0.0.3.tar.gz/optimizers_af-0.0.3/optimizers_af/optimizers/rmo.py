"""
References
----------
2014. R.Rahmani, R.Yusof.
A New Simple, Fast And Efficient Algorithm
For Global Optimization Over Continuous Search-Space Problems.
Radial Movement Optimization.
doi:10.1016/j.amc.2014.09.102

"""


import numpy as np

from optimizers_af.optimizers.base import Base
from optimizers_af.optimizers.bound_constrained import BoundConstrained


class RadialMovementOptimization(Base, BoundConstrained):

    def __init__(
            self,
            generations_number: int,
            particles_number: int,
            scale: int,
            c_parameters: tuple[float, float],
            weight_limits: tuple[float, float] = (0, 1),
            **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.generations_number = generations_number
        self.particles_number = particles_number
        self.scale = scale
        self.c_parameters = c_parameters
        self.weight_limits = weight_limits

    def __generate_velocities(self, dimensions_number: int):
        return np.random.uniform(
            low=-1.0,
            size=(self.particles_number, dimensions_number)
        ) * (self.superior_bounds - self.inferior_bounds) / self.scale

    def __get_weight(self, generation: int) -> float:
        return (
                self.weight_limits[1]
                - (self.weight_limits[1] - self.weight_limits[0])
                * generation / self.generations_number
        )

    def run_iteration(self, generation: int) -> None:
        globally_best_point, global_minimum = self.history[-1][:2]
        radially_best_point, generation_minimum = self.history[-1][:2]
        centre = radially_best_point
        generation_minimum = self.func(centre)
        velocities = self.__generate_velocities(centre.size)
        weight = self.__get_weight(generation)
        locations = self._get_shifted_points(
            centre=centre,
            shifts=weight * velocities,
        )
        for _, location in enumerate(locations):
            if (loss := self.func(location)) < generation_minimum:
                generation_minimum = loss
                radially_best_point = location
                if generation_minimum < self.history[-1][1]:
                    global_minimum = generation_minimum
                    globally_best_point = radially_best_point
        centre += (
                self.c_parameters[0] * (self.history[-1][0] - centre)
                + self.c_parameters[1] * (radially_best_point - centre)
        )
        self._update_history(
            point=globally_best_point,
            loss=global_minimum,
            generation=generation,
        )

    def fill_history(self) -> None:
        globally_best_point, global_minimum = self.history[-1][:2]
        self._check_point_shape(point=globally_best_point)
        for generation in range(self.generations_number):
            self.run_iteration(generation=generation)
