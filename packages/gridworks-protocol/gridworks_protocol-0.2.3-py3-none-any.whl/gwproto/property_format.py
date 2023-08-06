import string
import struct
from typing import Any
from typing import Callable

import pendulum
import pydantic


def predicate_validator(
    field_name: str, predicate: Callable[[Any], bool], error_format: str = "", **kwargs
) -> classmethod:  # type: ignore
    """
    Produce a pydantic validator from a function returning a bool.

    Example:

        from typing import Any
        from pydantic import BaseModel, ValidationError
        from gwproto.property_format import predicate_validator

        def is_truthy(v: Any) -> bool:
            return bool(v)

        class Foo(BaseModel):
            an_int: int

            _validate_an_int = predicate_validator("an_int", is_truthy)

        print(Foo(an_int=1))

        try:
            print(Foo(an_int=0))
        except ValidationError as e:
            print(e)

    Args:
        field_name: the name of the field to validate.
        predicate: the validation function. A truthy return value indicates success.
        error_format: Optional format string for use in exception raised by validation failure. Takes one parameter, 'v'.
        **kwargs: Passed to pydantic.validator()

    Returns:
        The passed in object v.
    """

    def _validator(v: Any) -> Any:
        if not predicate(v):
            if error_format:
                err_str = error_format.format(value=v)
            else:
                err_str = f"Failure of predicate on [{v}] with predicate {predicate}"
            raise ValueError(err_str)
        return v

    return pydantic.validator(field_name, allow_reuse=True, **kwargs)(_validator)


def is_bit(candidate: int) -> bool:
    if candidate == 0:
        return True
    if candidate == 1:
        return True
    return False


def is_64_bit_hex(candidate: str) -> bool:
    if len(candidate) != 8:
        return False
    if not all(c in string.hexdigits for c in candidate):
        return False
    return True


def is_lrd_alias_format(candidate: str) -> bool:
    """AlphanumericStrings separated by periods, with most
    significant word to the left.  I.e. `dw1.ne` is the child of `dw1`."""
    # noinspection PyBroadException
    try:
        x = candidate.split(".")
    except:
        return False
    for word in x:
        if not word.isalnum():
            return False
    return True


def is_positive_integer(candidate: Any) -> bool:
    if not isinstance(candidate, int):
        return False
    if candidate <= 0:
        return False
    return True


def is_reasonable_unix_time_ms(candidate: float) -> bool:
    if pendulum.datetime(2000, 1, 1, 0, 0, 0).int_timestamp * 1000 > candidate:
        return False
    if pendulum.datetime(3000, 1, 1, 0, 0, 0).int_timestamp * 1000 < candidate:
        return False
    return True


def is_reasonable_unix_time_s(candidate: float) -> bool:
    if pendulum.datetime(2000, 1, 1, 0, 0, 0).int_timestamp > candidate:
        return False
    if pendulum.datetime(3000, 1, 1, 0, 0, 0).int_timestamp < candidate:
        return False
    return True


def is_unsigned_short(candidate: int) -> bool:
    # noinspection PyBroadException
    try:
        struct.pack("H", candidate)
    except:
        print("requires 0 <= number <= 65535")
        return False
    return True


def is_short_integer(candidate: int) -> bool:
    # noinspection PyBroadException
    try:
        struct.pack("h", candidate)
    except:
        print("short format requires (-32767 -1) <= number <= 32767")
        return False
    return True


def is_uuid_canonical_textual(candidate: str) -> bool:
    try:
        x = candidate.split("-")
    except AttributeError:
        return False
    if len(x) != 5:
        return False
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError:
            return False
    if len(x[0]) != 8:
        return False
    if len(x[1]) != 4:
        return False
    if len(x[2]) != 4:
        return False
    if len(x[3]) != 4:
        return False
    if len(x[4]) != 12:
        return False
    return True
