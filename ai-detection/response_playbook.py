#!/usr/bin/env python3

import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_alerts(filepath="active_alerts.json"):
    with open(filepath, "r") as f:
        return json.load(f)


def respond_to_alert(alert):
    severity = alert["severity"]
    timestamp = alert["timestamp"]

    if severity == "critical":
        action = "BLOCK IP + ISOLATE HOST"
    elif severity == "high":
        action = "BLOCK IP"
    elif severity == "medium":
        action = "MONITOR"
    else:
        action = "IGNORE"

    logger.warning(f"[{severity.upper()}] {timestamp} → Åtgärd: {action}")


def main():
    alerts = load_alerts()

    for alert in alerts:
        respond_to_alert(alert)


if __name__ == "__main__":
    main()
