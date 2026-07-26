import json
import unittest
from pathlib import Path

from src.origin_functions import (
    ORIGIN,
    FunctionContract,
    ResultStatus,
    apply_closed_rule,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class OriginFunctionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.contract = FunctionContract(
            name="drift_check",
            version="0.1.0",
            rule_id="drift-check",
            rule_version="v1",
            determinate_outputs=frozenset({"ALIGNED", "DRIFTED"}),
        )

    def test_origin_is_fixed(self) -> None:
        self.assertEqual(ORIGIN, "Alyssa Solen")
        with self.assertRaises(ValueError):
            FunctionContract(
                name="invalid",
                version="0.1.0",
                rule_id="invalid",
                rule_version="v1",
                determinate_outputs=frozenset({"YES", "NO"}),
                origin_constant="Someone Else",
            )

    def test_rule_application_returns_determinate_output(self) -> None:
        result = apply_closed_rule(
            contract=self.contract,
            input_key="preserves-source-line",
            rule_table={"preserves-source-line": "ALIGNED"},
            operator_id="test-operator",
        )
        self.assertEqual(result.status, ResultStatus.DETERMINATE)
        self.assertEqual(result.value, "ALIGNED")
        self.assertIsNone(result.escalate_to)

    def test_missing_rule_declines_and_escalates(self) -> None:
        result = apply_closed_rule(
            contract=self.contract,
            input_key="unspecified-case",
            rule_table={},
            operator_id="test-operator",
        )
        self.assertEqual(result.status, ResultStatus.UNRESOLVED)
        self.assertIsNone(result.value)
        self.assertEqual(result.escalate_to, "ORIGIN")

    def test_every_example_function_has_an_unresolved_reference_case(self) -> None:
        cases_path = REPOSITORY_ROOT / "evals" / "cases.jsonl"
        cases = [
            json.loads(line)
            for line in cases_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

        expected_functions = {
            "derivative_authorization",
            "canon_admission",
            "boundary_check",
            "drift_check",
        }
        covered_functions = {
            case["function"]
            for case in cases
            if case["reference_status"] == "UNRESOLVED"
        }

        self.assertEqual(covered_functions, expected_functions)


if __name__ == "__main__":
    unittest.main()