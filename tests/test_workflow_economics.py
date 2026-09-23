import importlib.util
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).parents[1]
    / "plugins"
    / "workflow-opportunity-auditor"
    / "scripts"
    / "workflow_economics.py"
)
SPEC = importlib.util.spec_from_file_location("workflow_economics", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class WorkflowEconomicsTests(unittest.TestCase):
    def test_calculates_supplied_labor_case(self):
        result = MODULE.calculate(
            {
                "workflow_name": "Lead follow-up",
                "frequency_per_month": 4,
                "minutes_per_run": 180,
                "people_per_run": 1,
                "hourly_cost_usd": 40,
                "target_minutes_per_run": 60,
                "tool_cost_monthly_usd": 30,
                "implementation_cost_usd": 600,
                "current_error_rate_pct": 12,
                "target_error_rate_pct": 5,
            }
        )
        self.assertEqual(result["metrics"]["current_monthly_labor_hours"], 12.0)
        self.assertEqual(result["metrics"]["gross_monthly_labor_hours_saved"], 8.0)
        self.assertEqual(result["metrics"]["net_monthly_labor_savings_usd"], 290.0)
        self.assertEqual(result["metrics"]["simple_payback_months"], 2.07)
        self.assertEqual(result["metrics"]["error_rate_reduction_percentage_points"], 7.0)

    def test_preserves_unknowns_instead_of_assuming_values(self):
        result = MODULE.calculate({"workflow_name": "Unknown baseline"})
        self.assertEqual(result["metrics"], {})
        self.assertIn("current_monthly_labor_hours", result["unknown"])
        self.assertIn("error_rate_reduction_percentage_points", result["unknown"])

    def test_rejects_invalid_percentage(self):
        with self.assertRaisesRegex(ValueError, "between 0 and 100"):
            MODULE.calculate({"current_error_rate_pct": 101})

    def test_labor_capacity_is_not_claimed_as_cash(self):
        result = MODULE.calculate(
            {
                "frequency_per_month": 10,
                "minutes_per_run": 30,
                "target_minutes_per_run": 15,
                "hourly_cost_usd": 20,
                "tool_cost_monthly_usd": 5,
            }
        )
        self.assertIn("not guaranteed cash savings", result["note"])


if __name__ == "__main__":
    unittest.main()
