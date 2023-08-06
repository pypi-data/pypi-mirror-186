"""gt.sh.telemetry.from.multipurpose.sensor.100 type"""

from gwproto.errors import MpSchemaError
from gwproto.gt.gt_sh_telemetry_from_multipurpose_sensor.gt_sh_telemetry_from_multipurpose_sensor_base import (
    GtShTelemetryFromMultipurposeSensorBase,
)


class GtShTelemetryFromMultipurposeSensor(GtShTelemetryFromMultipurposeSensorBase):
    def check_for_errors(self):
        errors = self.derived_errors() + self.hand_coded_errors()
        if len(errors) > 0:
            raise MpSchemaError(
                f" Errors making making gt.sh.telemetry.from.multipurpose.sensor.100 for {self}: {errors}"
            )

    def hand_coded_errors(self):
        return []
