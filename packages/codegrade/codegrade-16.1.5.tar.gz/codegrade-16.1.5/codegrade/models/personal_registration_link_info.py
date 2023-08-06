"""The module that defines the ``PersonalRegistrationLinkInfo`` model.

SPDX-License-Identifier: AGPL-3.0-only OR BSD-3-Clause-Clear
"""

import typing as t
from dataclasses import dataclass, field

import cg_request_args as rqa

from ..utils import to_dict
from .personal_registration_link_info_input_as_json import (
    PersonalRegistrationLinkInfoInputAsJSON,
)


@dataclass
class PersonalRegistrationLinkInfo(PersonalRegistrationLinkInfoInputAsJSON):
    """Serialization of the personal info for a registration link."""

    #: The id of this user info.
    id: "str"
    #: Whether this user has already used their link to enroll.
    is_used: "bool"

    raw_data: t.Optional[t.Dict[str, t.Any]] = field(init=False, repr=False)

    data_parser: t.ClassVar = rqa.Lazy(
        lambda: PersonalRegistrationLinkInfoInputAsJSON.data_parser.parser.combine(
            rqa.FixedMapping(
                rqa.RequiredArgument(
                    "id",
                    rqa.SimpleValue.str,
                    doc="The id of this user info.",
                ),
                rqa.RequiredArgument(
                    "is_used",
                    rqa.SimpleValue.bool,
                    doc=(
                        "Whether this user has already used their link to"
                        " enroll."
                    ),
                ),
            )
        ).use_readable_describe(
            True
        )
    )

    def to_dict(self) -> t.Dict[str, t.Any]:
        res: t.Dict[str, t.Any] = {
            "id": to_dict(self.id),
            "is_used": to_dict(self.is_used),
            "username": to_dict(self.username),
            "name": to_dict(self.name),
            "email": to_dict(self.email),
        }
        return res

    @classmethod
    def from_dict(
        cls: t.Type["PersonalRegistrationLinkInfo"], d: t.Dict[str, t.Any]
    ) -> "PersonalRegistrationLinkInfo":
        parsed = cls.data_parser.try_parse(d)

        res = cls(
            id=parsed.id,
            is_used=parsed.is_used,
            username=parsed.username,
            name=parsed.name,
            email=parsed.email,
        )
        res.raw_data = d
        return res


import os

if os.getenv("CG_GENERATING_DOCS", "False").lower() in ("", "true"):
    # fmt: off
    pass
    # fmt: on
