import json

from app.main import log_event


def test_log_event_emits_json(caplog) -> None:
    with caplog.at_level("INFO", logger="pipeline-demo"):
        log_event("unit_test", result="passed")
    payload = json.loads(caplog.records[-1].message)
    assert payload == {"event": "unit_test", "result": "passed"}
