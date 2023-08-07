from .errors import JacobianSolverError as JacobianSolverError
from .newton import NewtonConvergenceError as NewtonConvergenceError, newton as newton
from typing import Callable
from typing_extensions import Literal

def tangent(*_) -> None: ...
def euler_newton(problem, u0, lmbda0: float, callback: Callable, max_steps: float = ..., max_num_retries: float = ..., verbose: bool = ..., newton_tol: float = ..., max_newton_steps: int = ..., predictor_variant: Union[Literal['tangent'], Literal['secant']] = ..., stepsize0: float = ..., stepsize_max: float = ..., stepsize_aggressiveness: int = ..., cos_alpha_min: float = ..., theta0: float = ..., adaptive_theta: bool = ..., converge_onto_zero_eigenvalue: bool = ..., termination_criterion: Union[Callable, None] = ...): ...
