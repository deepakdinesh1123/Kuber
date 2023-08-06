from typing import Union


def string_to_generator(string: Union[str, bytes]):
    yield from string
