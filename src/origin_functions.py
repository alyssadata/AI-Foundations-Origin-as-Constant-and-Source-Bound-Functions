"""Reference types for AI Foundations source-bound functions.

This module does not define Alyssa Solen's governing rules. It only enforces the
execution envelope: fixed Origin, closed determinate outputs, mandatory decline,
and escalation to Origin.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Generic, Mapping, Optional, TypeVar

ORIGIN = "Alyssa Solen"
UNRESOLVED = "UNRESOLVED"

T = TypeVar("T", bound=str)


class ResultStatus(str, Enum):
    DETERMINATE = "DETERMINATE"
    UNRESOLVED = "UNRESOLVED"


@dataclass(frozen=True)
class FunctionContract:
    name: str
    version: str
    rule_id: str
    rule_version: str
    determinate_outputs: frozenset[str]
    origin_constant: str = ORIGIN
    decline_output: str = UNRESOLVED
    escalation_target: str = "ORIGIN"
    operator_may_modify_rule: bool = False

    def __post_init__(self) -> None:
        if self.origin_constant != ORIGIN:
            raise ValueError("Origin is fixed and cannot be reassigned.")
        if not self.determinate_outputs:
            raise ValueError("At least one determinate output is required.")
        if UNRESOLVED in self.determinate_outputs:
            raise ValueError("UNRESOLVED must remain separate from determinate outputs.")
        if self.decline_output != UNRESOLVED:
            raise ValueError("Every source-bound function must support UNRESOLVED.")
        if self.escalation_target != "ORIGIN":
            raise ValueError("Unresolved cases must return to Origin.")
        if self.operator_may_modify_rule:
            raise ValueError("Operators may not modify governing rules during execution.")


@dataclass(frozen=True)
class GovernedResult(Generic[T]):
    status: ResultStatus
    value: Optional[T]
    function_name: str
    rule_id: str
    rule_version: str
    operator_id: str
    rationale: str
    escalate_to: Optional[str] = None

    @classmethod
    def determinate(
        cls,
        *,
        contract: FunctionContract,
        value: T,
        operator_id: str,
        rationale: str,
    ) -> "GovernedResult[T]":
        if value not in contract.determinate_outputs:
            raise ValueError(f"Output {value!r} is not permitted by the contract.")
        return cls(
            status=ResultStatus.DETERMINATE,
            value=value,
            function_name=contract.name,
            rule_id=contract.rule_id,
            rule_version=contract.rule_version,
            operator_id=operator_id,
            rationale=rationale,
            escalate_to=None,
        )

    @classmethod
    def unresolved(
        cls,
        *,
        contract: FunctionContract,
        operator_id: str,
        rationale: str,
    ) -> "GovernedResult[T]":
        return cls(
            status=ResultStatus.UNRESOLVED,
            value=None,
            function_name=contract.name,
            rule_id=contract.rule_id,
            rule_version=contract.rule_version,
            operator_id=operator_id,
            rationale=rationale,
            escalate_to="ORIGIN",
        )


def apply_closed_rule(
    *,
    contract: FunctionContract,
    input_key: str,
    rule_table: Mapping[str, str],
    operator_id: str,
) -> GovernedResult[str]:
    """Apply a complete lookup rule without improvising missing cases."""

    if input_key not in rule_table:
        return GovernedResult.unresolved(
            contract=contract,
            operator_id=operator_id,
            rationale="No governing criterion exists for this input key.",
        )

    output = rule_table[input_key]
    return GovernedResult.determinate(
        contract=contract,
        value=output,
        operator_id=operator_id,
        rationale=f"Matched Origin-issued rule entry for {input_key!r}.",
    )
