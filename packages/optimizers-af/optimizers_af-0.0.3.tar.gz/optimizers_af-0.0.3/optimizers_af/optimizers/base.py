from datetime import datetime

import numpy as np

from optimizers_af.logs.logged_object import LoggedObject


class Base(LoggedObject):
    """

    Parameters
    ----------
    func : callable
       An objective function with 1D-array as an argument.

    """

    def __init__(self, func: callable, **kwargs) -> None:
        super().__init__(**kwargs)
        self.history = []
        self.start = datetime.now()
        self.func = func

    def _get_time_from_start(self) -> int:
        return (datetime.now() - self.start).microseconds

    def _update_history(
            self,
            point: np.ndarray,
            loss: float = None,
            generation: int = None,
    ):
        _loss = loss if loss is not None else self.func(point)
        _generation = generation if generation else len(self.history)
        self.history.append(
            (point, _loss, self._get_time_from_start())
        )
        self.logger.info(
            f'Generation: {_generation}.'
            f' Loss: {self.history[-1][1]}.'
            f' Optimization Time: {self.history[-1][2]} msec.'
            f' Point: {str(self.history[-1][0])}.'
        )

    def fill_history(self) -> None:
        pass

    def run(self, point: np.ndarray):
        """

        Parameters
        ----------
        point : array-like
            An argument of the objective function
            that is 1D-array to be optimized.

        Returns
        -------
        parameters : array-like
            The optimized argument of the objective function.

        """
        self.start = datetime.now()
        self.history = [
            (point, self.func(point), self._get_time_from_start())
        ]
        try:
            self.fill_history()
        except (KeyboardInterrupt, SystemError):
            pass
        point, loss, optimization_time = self.history[-1]
        return point, loss, optimization_time
