# Copyright 2023 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
# pylint:disable=missing-module-docstring
from enum import Enum


class VerbosityEnum(Enum):
    """Defines the verbosity modes in Boulder Opal."""

    VERBOSE = "VERBOSE"
    QUIET = "QUIET"


def parse_verbosity(verbosity: str) -> VerbosityEnum:
    """
    Parse a string representing a verbosity mode.

    Parameters
    ----------
    verbosity : str
        The value of the enum member to be retrieved from `VerbosityEnum`.

    Returns
    -------
    VerbosityEnum
        The member of `VerbosityEnum` corresponding to value.

    Raises
    ------
    ValueError
        If `verbosity` is not a valid value for any member of `VerbosityEnum`.
    """

    try:
        return VerbosityEnum(verbosity)

    except ValueError as err:
        raise ValueError(
            "Invalid verbosity mode "
            f"(valid modes are {list(VerbosityEnum.__members__)})",
            {"verbosity": verbosity},
        ) from err
