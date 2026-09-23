#!/usr/bin/env python3
"""Calculate workflow economics from explicit user-supplied inputs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


NON_NEGATIVE_FIELDS = (
    "frequency_per_month",
    "minutes_per_run",
    "hourly_cost_usd",
    "target_minutes_per_run",
    "tool_cost_monthly_usd",
    "implementation_cost_usd",
)
PERCENT_FIELDS = ("current_error_rate_pct", "target_error_rate_pct")


def _number(data: dict[str, Any], key: str) -> float | None:
    value = data.get(key)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{key} must be a number or null")
    return float(value)


def calculate(data: dict[str, Any]) -> dict[str, Any]:
    for key in NON_NEGATIVE_FIELDS:
        value = _number(data, key)
        if value is not None and value < 0:
            raise ValueError(f"{key} must be greater than or equal to zero")

    people = _number(data, "people_per_run")
    if people is not None and people <= 0:
        raise ValueError("people_per_run must be greater than zero")

    for key in PERCENT_FIELDS:
        value = _number(data, key)
        if value is not None and not 0 <= value <= 100:
            raise ValueError(f"{key} must be between 0 and 100")

    frequency = _number(data, "frequency_per_month")
    minutes = _number(data, "minutes_per_run")
    people = people if people is not None else 1.0
    hourly_cost = _number(data, "hourly_cost_usd")
    target_minutes = _number(data, "target_minutes_per_run")
    tool_cost = _number(data, "tool_cost_monthly_usd")
    implementation_cost = _number(data, "implementation_cost_usd")

    metrics: dict[str, float] = {}
    unknown: list[str] = []
    assumptions = {"people_per_run": people}

    if frequency is None or minutes is None:
        unknown.append("current_monthly_labor_hours")
    else:
        metrics["current_monthly_labor_hours"] = frequency * minutes * people / 60

    if "current_monthly_labor_hours" in metrics and hourly_cost is not None:
        metrics["current_monthly_labor_cost_usd"] = (
            metrics["current_monthly_labor_hours"] * hourly_cost
        )
    else:
        unknown.append("current_monthly_labor_cost_usd")

    if frequency is not None and target_minutes is not None:
        metrics["target_monthly_labor_hours"] = frequency * target_minutes * people / 60
    else:
        unknown.append("target_monthly_labor_hours")

    if {
        "current_monthly_labor_hours",
        "target_monthly_labor_hours",
    }.issubset(metrics):
        hours_saved = max(
            0.0,
            metrics["current_monthly_labor_hours"]
            - metrics["target_monthly_labor_hours"],
        )
        metrics["gross_monthly_labor_hours_saved"] = hours_saved
        if hourly_cost is not None:
            gross_savings = hours_saved * hourly_cost
            metrics["gross_monthly_labor_savings_usd"] = gross_savings
            if tool_cost is not None:
                net_savings = gross_savings - tool_cost
                metrics["net_monthly_labor_savings_usd"] = net_savings
                metrics["annualized_net_labor_savings_usd"] = net_savings * 12
                if implementation_cost is not None and net_savings > 0:
                    metrics["simple_payback_months"] = implementation_cost / net_savings
                elif implementation_cost is not None:
                    unknown.append("simple_payback_months_non_positive_net_savings")
            else:
                unknown.extend(
                    ["net_monthly_labor_savings_usd", "annualized_net_labor_savings_usd"]
                )
        else:
            unknown.extend(
                ["gross_monthly_labor_savings_usd", "net_monthly_labor_savings_usd"]
            )
    else:
        unknown.append("gross_monthly_labor_hours_saved")

    current_error = _number(data, "current_error_rate_pct")
    target_error = _number(data, "target_error_rate_pct")
    if current_error is not None and target_error is not None:
        metrics["error_rate_reduction_percentage_points"] = max(
            0.0, current_error - target_error
        )
    else:
        unknown.append("error_rate_reduction_percentage_points")

    rounded = {key: round(value, 2) for key, value in metrics.items()}
    return {
        "workflow_name": data.get("workflow_name") or "unknown",
        "currency": data.get("currency") or "USD",
        "metrics": rounded,
        "assumptions": assumptions,
        "unknown": sorted(set(unknown)),
        "note": (
            "Labor-capacity estimates are not guaranteed cash savings. "
            "Validate realized results after the experiment."
        ),
    }


def to_markdown(result: dict[str, Any]) -> str:
    lines = [
        f"# Workflow economics: {result['workflow_name']}",
        "",
        f"Currency: {result['currency']}",
        "",
        "## Calculated metrics",
        "",
    ]
    metrics = result["metrics"]
    if metrics:
        lines.extend(f"- {key}: {value}" for key, value in metrics.items())
    else:
        lines.append("- No metrics could be calculated from the supplied inputs.")
    lines.extend(["", "## Unknown", ""])
    unknown = result["unknown"]
    lines.extend(f"- {item}" for item in unknown) if unknown else lines.append("- None")
    lines.extend(["", result["note"]])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Path to a workflow JSON file")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args()

    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("input must be a JSON object")
        result = calculate(data)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.format == "markdown":
        print(to_markdown(result), end="")
    else:
        print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
