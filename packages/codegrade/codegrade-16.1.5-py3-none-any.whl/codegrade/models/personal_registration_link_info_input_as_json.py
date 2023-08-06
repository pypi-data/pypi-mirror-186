"""The module that defines the ``PersonalRegistrationLinkInfoInputAsJSON`` model.

SPDX-License-Identifier: AGPL-3.0-only OR BSD-3-Clause-Clear
"""

import typing as t
from dataclasses import dataclass, field

import cg_request_args as rqa

from ..utils import to_dict


@dataclass
class PersonalRegistrationLinkInfoInputAsJSON:
    """Input data for a personal registration link."""

    #: The username for logging in of the user.
    username: "str"
    #: The full name of the user.
    name: "str"
    #: The email address of the user.
    email: "str"

    raw_data: t.Optional[t.Dict[str, t.Any]] = field(init=False, repr=False)

    data_parser: t.ClassVar = rqa.Lazy(
        lambda: rqa.FixedMapping(
            rqa.RequiredArgument(
                "username",
                rqa.SimpleValue.str,
                doc="The username for logging in of the user.",
            ),
            rqa.RequiredArgument(
                "name",
                rqa.SimpleValue.str,
                doc="The full name of the user.",
            ),
            rqa.RequiredArgument(
                "email",
                rqa.SimpleValue.str,
                doc="The email address of the user.",
            ),
        ).use_readable_describe(True)
    )

    def to_dict(self) -> t.Dict[str, t.Any]:
        res: t.Dict[str, t.Any] = {
            "username": to_dict(self.username),
            "name": to_dict(self.name),
            "email": to_dict(self.email),
        }
        return res

    @classmethod
    def from_dict(
        cls: t.Type["PersonalRegistrationLinkInfoInputAsJSON"],
        d: t.Dict[str, t.Any],
    ) -> "PersonalRegistrationLinkInfoInputAsJSON":
        parsed = cls.data_parser.try_parse(d)

        res = cls(
            username=parsed.username,
            name=parsed.name,
            email=parsed.email,
        )
        res.raw_data = d
        return res
