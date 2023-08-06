import json
from typing import Any, Dict, List

import pendulum
from pendulum.datetime import DateTime
from swimlane import Swimlane
from swimlane.core.resources.record import Record
from typing_extensions import Literal

_LEVELS = ["debug", "info", "warning", "error", "critical"]


class UseCaseOutcome:
    def __init__(
        self, sl: Swimlane, app_name: str, integration_name: str, **default_fields
    ) -> None:
        self.sl = sl
        self.app_name = app_name
        self.integration_name = integration_name
        self.default_fields = default_fields
        self.logs: List[Dict[str, str]] = []
        self.metrics: List[Dict[str, str]] = []
        self.fields_changed: List[Dict[str, str]] = []

        # these are strings due to the limitation in Swimlane with the date/time object. It only has second precision
        self.use_case_started: DateTime
        self.arbitrary_record_fields: Dict[str, str] = {}

    def start(self):
        self.use_case_started = pendulum.now()

    def update_field(self, field_name: str, field_value: str):
        self.arbitrary_record_fields[field_name] = field_value

    def submit(
        self,
        status: Literal["Success", "Failed"],
        siem_record: Record,
        auto_closed: bool = False,
    ):
        """
        responsible for taking all of the data we have collected within this object over the course of a use case and
        submitting it to Swimlane
        """
        et: DateTime = pendulum.now()
        self._normalise_logs()

        # we need to change the fields_changed datetimes to the current date/time as it is only saved now.
        p_load: Dict[str, Any] = {
            "status": status,
            "application_name": self.app_name,
            "integration_name": self.integration_name,
            **self.arbitrary_record_fields,
            "raw_metrics": json.dumps(self.metrics),
            "raw_logs": json.dumps(self.logs),
            "raw_fields_changed": json.dumps(
                [
                    field_changed
                    for field_changed in self.fields_changed
                    if "timestamp" in field_changed
                ]
            ),
            "auto_close": "YES" if auto_closed else "NO",
            "start_time": self.use_case_started.to_iso8601_string().replace(":", "-"),
            "end_time": et.to_iso8601_string().replace(":", "-"),
            "duration_(seconds)": self.duration(et),
        }
        self.create_uco_record(self._normalise_keys(p_load), siem_record)

    def duration(self, end_time: DateTime) -> float:
        return (end_time - self.use_case_started).total_seconds()

    def create_uco_record(self, data: Dict[str, Any], siem_record: Record):
        app = self.sl.apps.get(name="Use Case Outcome")
        resp = app.records.create(**data)
        record = app.records.get(tracking_id=resp.tracking_id)
        record["SIEM Ref"].add(siem_record)
        record.patch()

    def log(self, level: str, **kwargs):
        if level not in _LEVELS:
            raise ValueError(
                f"level must be one of the following : {','.join(_LEVELS)}"
            )

        self.logs.append(
            {
                **kwargs,
                "level": level,
                **self.default_fields,
                "timestamp": pendulum.now().to_iso8601_string(),
            }
        )

    def metric(self, metric_name: str, metric_value: Any):
        self.metrics.append({"metric_name": metric_name, "metric_value": metric_value})

    def record_saved(self):
        # when the records saved, can we update all the entries in field_changed with the current date_time?
        for field_changed in self.fields_changed:
            field_changed["timestamp"] = pendulum.now().to_iso8601_string()

    def field_changed(
        self, field_name: str, old_field_value: str, new_field_value: str
    ):
        self.fields_changed.append(
            {
                "field_name": field_name,
                "old_field_name": old_field_value,
                "new_field_value": new_field_value,
            }
        )

    def _normalise_logs(self):
        # returns the list of logs that are passed in, with each dict containing the same keys. Required for UI widget
        keys = set([key for item in self.logs for key in item.keys()])

        for log in self.logs:
            for key in keys:
                if key not in log:
                    log[key] = ""

    @staticmethod
    def _normalise_keys(d: dict) -> dict:
        # returns the dict with _ replaced with spaces and each word capitalised.
        return {key.replace("_", " ").title(): value for key, value in d.items()}
