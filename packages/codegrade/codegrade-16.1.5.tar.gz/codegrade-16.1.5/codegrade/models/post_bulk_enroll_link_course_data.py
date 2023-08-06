"""The module that defines the ``PostBulkEnrollLinkCourseData`` model.

SPDX-License-Identifier: AGPL-3.0-only OR BSD-3-Clause-Clear
"""

import datetime
import typing as t
from dataclasses import dataclass, field

import cg_request_args as rqa

from .. import parsers
from ..utils import to_dict
from .user_info_with_role import UserInfoWithRole


@dataclass
class PostBulkEnrollLinkCourseData:
    """Input data required for the `Course::PostBulkEnrollLink` operation."""

    #: The date this link should stop working.
    expiration_date: "datetime.datetime"
    #: List of user information to pre-compile the registration form on the
    #: enroll page.
    users: "t.Sequence[UserInfoWithRole]"

    raw_data: t.Optional[t.Dict[str, t.Any]] = field(init=False, repr=False)

    data_parser: t.ClassVar = rqa.Lazy(
        lambda: rqa.FixedMapping(
            rqa.RequiredArgument(
                "expiration_date",
                rqa.RichValue.DateTime,
                doc="The date this link should stop working.",
            ),
            rqa.RequiredArgument(
                "users",
                rqa.List(parsers.ParserFor.make(UserInfoWithRole)),
                doc=(
                    "List of user information to pre-compile the registration"
                    " form on the enroll page."
                ),
            ),
        ).use_readable_describe(True)
    )

    def to_dict(self) -> t.Dict[str, t.Any]:
        res: t.Dict[str, t.Any] = {
            "expiration_date": to_dict(self.expiration_date),
            "users": to_dict(self.users),
        }
        return res

    @classmethod
    def from_dict(
        cls: t.Type["PostBulkEnrollLinkCourseData"], d: t.Dict[str, t.Any]
    ) -> "PostBulkEnrollLinkCourseData":
        parsed = cls.data_parser.try_parse(d)

        res = cls(
            expiration_date=parsed.expiration_date,
            users=parsed.users,
        )
        res.raw_data = d
        return res
