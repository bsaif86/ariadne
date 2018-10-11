# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_query_is_executed_for_post_json_request 1"] = [
    b'{"data": {"status": true}}'
]

snapshots["test_complex_query_is_executed_for_post_json_request 1"] = [
    b'{"data": {"hello": "Hello, Bob!"}}'
]

snapshots["test_attempt_execute_complex_query_without_variables 1"] = [
    b'{"errors": [{"message": "Variable \\"$name\\" of required type \\"String!\\" was not provided.", "locations": [{"line": 2, "column": 18}]}]}'
]

snapshots["test_execute_complex_query_without_operation_name 1"] = [
    b'{"data": {"hello": "Hello, Bob!"}}'
]

snapshots["test_attempt_execute_query_without_query_entry 1"] = [
    b'{"errors": [{"message": "The query must be a string"}]}'
]

snapshots["test_attempt_execute_query_with_invalid_operation_name 1"] = [
    b'{"errors": [{"message": "Unknown operation named \\"[1, 2, 3]\\"."}]}'
]

snapshots["test_attempt_execute_query_with_invalid_variables 1"] = [
    b"query variables should be an object"
]
