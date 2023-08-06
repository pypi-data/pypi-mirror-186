"""The module that defines the ``PatchBulkEnrollLinkCourseData`` model.

SPDX-License-Identifier: AGPL-3.0-only OR BSD-3-Clause-Clear
"""

import datetime
import typing as t
from dataclasses import dataclass, field

import cg_request_args as rqa
from cg_maybe import Maybe, Nothing
from cg_maybe.utils import maybe_from_nullable

from ..utils import to_dict


@dataclass
class PatchBulkEnrollLinkCourseData:
    """Input data required for the `Course::PatchBulkEnrollLink` operation."""

    #: The new date this link should stop working.
    expiration_date: Maybe["datetime.datetime"] = Nothing
    #: The id of the new role.
    role_id: Maybe["int"] = Nothing

    raw_data: t.Optional[t.Dict[str, t.Any]] = field(init=False, repr=False)

    data_parser: t.ClassVar = rqa.Lazy(
        lambda: rqa.FixedMapping(
            rqa.OptionalArgument(
                "expiration_date",
                rqa.RichValue.DateTime,
                doc="The new date this link should stop working.",
            ),
            rqa.OptionalArgument(
                "role_id",
                rqa.SimpleValue.int,
                doc="The id of the new role.",
            ),
        ).use_readable_describe(True)
    )

    def __post_init__(self) -> None:
        getattr(super(), "__post_init__", lambda: None)()
        self.expiration_date = maybe_from_nullable(self.expiration_date)
        self.role_id = maybe_from_nullable(self.role_id)

    def to_dict(self) -> t.Dict[str, t.Any]:
        res: t.Dict[str, t.Any] = {}
        if self.expiration_date.is_just:
            res["expiration_date"] = to_dict(self.expiration_date.value)
        if self.role_id.is_just:
            res["role_id"] = to_dict(self.role_id.value)
        return res

    @classmethod
    def from_dict(
        cls: t.Type["PatchBulkEnrollLinkCourseData"], d: t.Dict[str, t.Any]
    ) -> "PatchBulkEnrollLinkCourseData":
        parsed = cls.data_parser.try_parse(d)

        res = cls(
            expiration_date=parsed.expiration_date,
            role_id=parsed.role_id,
        )
        res.raw_data = d
        return res
