"""The module that defines the ``RegisterUserWithBulkLinkCourseData`` model.

SPDX-License-Identifier: AGPL-3.0-only OR BSD-3-Clause-Clear
"""

import typing as t
from dataclasses import dataclass, field

import cg_request_args as rqa

from ..utils import to_dict


@dataclass
class RegisterUserWithBulkLinkCourseData:
    """Input data required for the `Course::RegisterUserWithBulkLink`
    operation.
    """

    #: Id of the user info
    user_info_id: "str"
    #: Password of the new user.
    password: "str"

    raw_data: t.Optional[t.Dict[str, t.Any]] = field(init=False, repr=False)

    data_parser: t.ClassVar = rqa.Lazy(
        lambda: rqa.FixedMapping(
            rqa.RequiredArgument(
                "user_info_id",
                rqa.SimpleValue.str,
                doc="Id of the user info",
            ),
            rqa.RequiredArgument(
                "password",
                rqa.SimpleValue.str,
                doc="Password of the new user.",
            ),
        ).use_readable_describe(True)
    )

    def to_dict(self) -> t.Dict[str, t.Any]:
        res: t.Dict[str, t.Any] = {
            "user_info_id": to_dict(self.user_info_id),
            "password": to_dict(self.password),
        }
        return res

    @classmethod
    def from_dict(
        cls: t.Type["RegisterUserWithBulkLinkCourseData"],
        d: t.Dict[str, t.Any],
    ) -> "RegisterUserWithBulkLinkCourseData":
        parsed = cls.data_parser.try_parse(d)

        res = cls(
            user_info_id=parsed.user_info_id,
            password=parsed.password,
        )
        res.raw_data = d
        return res
