"""The module that defines the ``ResultDataGetCourseGetPersonalizedRegistrationLink`` model.

SPDX-License-Identifier: AGPL-3.0-only OR BSD-3-Clause-Clear
"""

import typing as t
from dataclasses import dataclass, field

import cg_request_args as rqa

from .. import parsers
from ..utils import to_dict
from .extended_bulk_course_registration_link import (
    ExtendedBulkCourseRegistrationLink,
)
from .personal_registration_link_info import PersonalRegistrationLinkInfo


@dataclass
class ResultDataGetCourseGetPersonalizedRegistrationLink:
    """A registration link with some attached information about the user that
    will be enrolled, which the user is not allowed to override during the
    enrollment process.
    """

    #: The base enroll link.
    link: "ExtendedBulkCourseRegistrationLink"
    #: The personal info.
    user_info: "PersonalRegistrationLinkInfo"

    raw_data: t.Optional[t.Dict[str, t.Any]] = field(init=False, repr=False)

    data_parser: t.ClassVar = rqa.Lazy(
        lambda: rqa.FixedMapping(
            rqa.RequiredArgument(
                "link",
                parsers.ParserFor.make(ExtendedBulkCourseRegistrationLink),
                doc="The base enroll link.",
            ),
            rqa.RequiredArgument(
                "user_info",
                parsers.ParserFor.make(PersonalRegistrationLinkInfo),
                doc="The personal info.",
            ),
        ).use_readable_describe(True)
    )

    def to_dict(self) -> t.Dict[str, t.Any]:
        res: t.Dict[str, t.Any] = {
            "link": to_dict(self.link),
            "user_info": to_dict(self.user_info),
        }
        return res

    @classmethod
    def from_dict(
        cls: t.Type["ResultDataGetCourseGetPersonalizedRegistrationLink"],
        d: t.Dict[str, t.Any],
    ) -> "ResultDataGetCourseGetPersonalizedRegistrationLink":
        parsed = cls.data_parser.try_parse(d)

        res = cls(
            link=parsed.link,
            user_info=parsed.user_info,
        )
        res.raw_data = d
        return res
