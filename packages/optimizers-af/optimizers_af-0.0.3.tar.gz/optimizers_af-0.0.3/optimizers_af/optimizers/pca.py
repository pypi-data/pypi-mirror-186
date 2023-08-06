import numpy as np

from optimizers_af.optimizers.base import Base
from optimizers_af.optimizers.bound_constrained import BoundConstrained


class ParticleCollisionAlgorithm(Base, BoundConstrained):

    def __init__(self, generations_number: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.generations_number = generations_number
        self.old_point = self._get_random_point()
        self.new_point = np.zeros(self.dimension)
        self.best_fitness = self.func(self.old_point)

    def __perturbation(self):
        rand = np.random.random(self.dimension)
        self.new_point = (
                self.old_point
                + ((self.superior_bounds - self.old_point) * rand)
                - ((self.old_point - self.inferior_bounds) * (1 - rand))
        )
        self.new_point = np.clip(
            a=self.new_point,
            a_min=self.inferior_bounds,
            a_max=self.superior_bounds,
        )

    def __small_perturbation(self):
        uppers = np.min(
            [
                (1.0 + 0.2 * np.random.random(self.dimension))
                * self.old_point,
                self.superior_bounds
            ],
            axis=0,
        )
        lowers = np.max(
            [
                (0.8 + 0.2 * np.random.random(self.dimension))
                * self.old_point,
                self.inferior_bounds
            ],
            axis=0,
        )
        rand = np.random.random(self.dimension)
        self.new_point = (
                self.old_point
                + ((uppers - self.old_point) * rand)
                - ((self.old_point - lowers) * (1 - rand))
        )

    def __exploration(self):
        for n in range(self.generations_number):
            self.__small_perturbation()
            if self.func(self.new_point) > self.func(self.old_point):
                if self.func(self.new_point) > self.best_fitness:
                    self.best_fitness = self.func(self.new_point)
                self.old_point = self.new_point

    def __scattering(self):
        p_scattering = 1 - self.func(self.new_point) / self.best_fitness
        if p_scattering > np.random.random():
            self.old_point = self._get_random_point()
        else:
            self.__exploration()

    def run_iteration(self, generation: int) -> None:
        self.__perturbation()
        if self.func(self.new_point) > self.func(self.old_point):
            if self.func(self.new_point) > self.best_fitness:
                self.best_fitness = self.func(self.new_point)
            self.old_point = self.new_point
            self.__exploration()
        else:
            self.__scattering()
        self._update_history(point=self.new_point, generation=generation)

    def fill_history(self) -> None:
        for generation in range(self.generations_number):
            self.run_iteration(generation=generation)
