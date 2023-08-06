"""gt.dispatch.boolean.local.100 type"""

from gwproto.errors import MpSchemaError
from gwproto.gt.gt_dispatch_boolean_local.gt_dispatch_boolean_local_base import (
    GtDispatchBooleanLocalBase,
)


class GtDispatchBooleanLocal(GtDispatchBooleanLocalBase):
    def check_for_errors(self):
        errors = self.derived_errors() + self.hand_coded_errors()
        if len(errors) > 0:
            raise MpSchemaError(
                f" Errors making making gt.dispatch.boolean.local.100 for {self}: {errors}"
            )

    def hand_coded_errors(self):
        return []
