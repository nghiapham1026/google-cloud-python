# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.cloud.websecurityscanner_v1beta.types import scan_run_error_trace
from google.cloud.websecurityscanner_v1beta.types import scan_run_warning_trace
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.websecurityscanner.v1beta", manifest={"ScanRun",},
)


class ScanRun(proto.Message):
    r"""A ScanRun is a output-only resource representing an actual
    run of the scan. Next id: 12

    Attributes:
        name (str):
            The resource name of the ScanRun. The name
            follows the format of
            'projects/{projectId}/scanConfigs/{scanConfigId}/scanRuns/{scanRunId}'.
            The ScanRun IDs are generated by the system.
        execution_state (~.scan_run.ScanRun.ExecutionState):
            The execution state of the ScanRun.
        result_state (~.scan_run.ScanRun.ResultState):
            The result state of the ScanRun. This field
            is only available after the execution state
            reaches "FINISHED".
        start_time (~.timestamp.Timestamp):
            The time at which the ScanRun started.
        end_time (~.timestamp.Timestamp):
            The time at which the ScanRun reached
            termination state - that the ScanRun is either
            finished or stopped by user.
        urls_crawled_count (int):
            The number of URLs crawled during this
            ScanRun. If the scan is in progress, the value
            represents the number of URLs crawled up to now.
        urls_tested_count (int):
            The number of URLs tested during this
            ScanRun. If the scan is in progress, the value
            represents the number of URLs tested up to now.
            The number of URLs tested is usually larger than
            the number URLS crawled because typically a
            crawled URL is tested with multiple test
            payloads.
        has_vulnerabilities (bool):
            Whether the scan run has found any
            vulnerabilities.
        progress_percent (int):
            The percentage of total completion ranging
            from 0 to 100. If the scan is in queue, the
            value is 0. If the scan is running, the value
            ranges from 0 to 100. If the scan is finished,
            the value is 100.
        error_trace (~.scan_run_error_trace.ScanRunErrorTrace):
            If result_state is an ERROR, this field provides the primary
            reason for scan's termination and more details, if such are
            available.
        warning_traces (Sequence[~.scan_run_warning_trace.ScanRunWarningTrace]):
            A list of warnings, if such are encountered
            during this scan run.
    """

    class ExecutionState(proto.Enum):
        r"""Types of ScanRun execution state."""
        EXECUTION_STATE_UNSPECIFIED = 0
        QUEUED = 1
        SCANNING = 2
        FINISHED = 3

    class ResultState(proto.Enum):
        r"""Types of ScanRun result state."""
        RESULT_STATE_UNSPECIFIED = 0
        SUCCESS = 1
        ERROR = 2
        KILLED = 3

    name = proto.Field(proto.STRING, number=1)

    execution_state = proto.Field(proto.ENUM, number=2, enum=ExecutionState,)

    result_state = proto.Field(proto.ENUM, number=3, enum=ResultState,)

    start_time = proto.Field(proto.MESSAGE, number=4, message=timestamp.Timestamp,)

    end_time = proto.Field(proto.MESSAGE, number=5, message=timestamp.Timestamp,)

    urls_crawled_count = proto.Field(proto.INT64, number=6)

    urls_tested_count = proto.Field(proto.INT64, number=7)

    has_vulnerabilities = proto.Field(proto.BOOL, number=8)

    progress_percent = proto.Field(proto.INT32, number=9)

    error_trace = proto.Field(
        proto.MESSAGE, number=10, message=scan_run_error_trace.ScanRunErrorTrace,
    )

    warning_traces = proto.RepeatedField(
        proto.MESSAGE, number=11, message=scan_run_warning_trace.ScanRunWarningTrace,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
