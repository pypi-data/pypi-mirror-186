from .newton import NewtonConvergenceError as NewtonConvergenceError, newton as newton
from _typeshed import Incomplete
from typing import Callable

def natural(problem, u0, lambda0: float, callback: Callable, lambda_stepsize0: float = ..., lambda_stepsize_max: float = ..., lambda_stepsize_aggressiveness: float = ..., max_newton_steps: int = ..., newton_tol: float = ..., max_steps: float = ..., verbose: bool = ..., use_first_order_predictor: bool = ..., milestones: Incomplete | None = ...): ...
