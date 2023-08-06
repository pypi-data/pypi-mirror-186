
from typing import Sequence, Tuple, Union

from pygame.math import Vector2, Vector3

Vector2Coercible = Union[float, Tuple[float, float], Sequence[float], Vector2]
Vector3Coercible = Union[float, Tuple[float, float, float], Sequence[float], Vector3]
