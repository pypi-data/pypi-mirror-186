from typing import Any, Callable

Encoder = Callable[[Any], str | bytes]
Dencoder = Callable[[str | bytes], Any]

Data = list | dict | str | float | int | None
