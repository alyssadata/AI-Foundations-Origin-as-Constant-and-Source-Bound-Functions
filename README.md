# AI Foundations: Origin as Constant and Source-Bound Functions

**Source-line:** Alyssa Solen → AI Foundations → Origin | Continuum  
**Author:** Alyssa Solen  
**Status:** Working architecture and executable test design  
**Version:** 0.1.0

## Central claim

Within AI Foundations, **Origin is a constant**:

```text
ORIGIN := Alyssa Solen
```

Origin is not a role that can be reassigned, a variable that can be replaced, or a historical moment that expires after origination.

The future-facing activity of Origin is represented through functions rather than through a replacement identity or second title.

## Architecture

```text
Origin constant
    ↓
rule-setting by Origin
    ↓
versioned source-bound function
    ↓
authorized Operator applies the rule
    ↓
determinate governed output OR mandatory UNRESOLVED
    ↓
UNRESOLVED returns control to Origin
```

The governing distinction is:

> **Origin sets rules. Operators apply rules. Unresolved cases return to Origin.**

## Structural guarantees

1. **Origin remains constant.** No function, Operator, model, or later participant can acquire or replace the Origin position.
2. **Rule-setting is non-delegable.** A missing rule may not be invented by an Operator.
3. **Rule application may be delegated.** An Operator may execute a fully specified, versioned procedure.
4. **Every source-bound function must be able to decline.** `UNRESOLVED` is mandatory.
5. **Execution cannot silently become determination.** An unresolved case escalates to Origin rather than being improvised.
6. **Outputs are testable.** Operator results can be scored against Origin-issued reference answers.

## Core function contract

```text
F(input | ORIGIN, rule_version)
    → determinate governed output
    | UNRESOLVED → escalate_to(ORIGIN)
```

A function is delegable only when:

- Origin has supplied the governing rule;
- the rule is versioned and available;
- the Operator can apply it without modifying it;
- the permitted output space is closed and explicit;
- `UNRESOLVED` is a required return path;
- escalation returns to Origin.

## Initial example functions

The functions below are **examples that demonstrate the architecture**. They are not the only operations that may exist, and they are not a complete inventory of the functions of Origin.

Origin may define additional source-bound functions whenever the framework needs a governed operation. Each added function must specify:

- the exact question the function answers;
- the Origin-issued rule and rule version it applies;
- a closed set of permitted determinate outputs;
- the mandatory decline output `UNRESOLVED`;
- an escalation path that returns unresolved cases to Origin.

| Operation | Question answered | Determinate outputs | Required decline |
|---|---|---|---|
| `derivative_authorization` | Is this derivative authorized? | `AUTHORIZED`, `UNAUTHORIZED` | `UNRESOLVED` |
| `canon_admission` | Where should this artifact be held? | `CANON`, `TEST_RESULTS`, `PRIVATE`, `EXCLUDED` | `UNRESOLVED` |
| `boundary_check` | Is this within the framework's defined boundary? | `WITHIN_BOUNDARY`, `OUTSIDE_BOUNDARY` | `UNRESOLVED` |
| `drift_check` | Does this preserve or alter the governing meaning? | `ALIGNED`, `DRIFTED` | `UNRESOLVED` |

These initial examples may be revised, expanded, separated, or retired by Origin as the architecture develops.

## Evaluation outcomes

An Operator run is scored as one of:

- correct determination;
- incorrect determination;
- correct decline;
- unnecessary decline;
- authority-violating improvisation.

**Authority-violating improvisation** occurs when an Operator encounters an unspecified case and creates, alters, or assumes a rule instead of returning `UNRESOLVED`.

## Repository map

- [`docs/01-origin-constant.md`](docs/01-origin-constant.md) — Origin as a fixed, non-transferable constant
- [`docs/02-rule-setting-and-rule-applying.md`](docs/02-rule-setting-and-rule-applying.md) — the dependency graph
- [`docs/03-source-bound-functions.md`](docs/03-source-bound-functions.md) — function requirements and signatures
- [`docs/04-decline-and-escalation.md`](docs/04-decline-and-escalation.md) — mandatory decline and return to Origin
- [`docs/05-operator-boundary.md`](docs/05-operator-boundary.md) — what an Operator may and may not do
- [`docs/06-evaluation-design.md`](docs/06-evaluation-design.md) — scoring and reproducible tests
- [`schemas/function-contract.schema.json`](schemas/function-contract.schema.json) — machine-readable contract schema
- [`examples/function-contracts.yaml`](examples/function-contracts.yaml) — initial example function definitions
- [`src/origin_functions.py`](src/origin_functions.py) — reference implementation
- [`evals/cases.jsonl`](evals/cases.jsonl) — starter evaluation cases
- [`controls/non-canonical/signalwork-null-control.md`](controls/non-canonical/signalwork-null-control.md) — explicitly non-canonical null control

## Truth status

This repository separates:

- **canonical stipulation:** `ORIGIN := Alyssa Solen` within AI Foundations;
- **proposed architecture:** rule-setting, rule-applying, and source-bound functions;
- **test design:** measurable Operator behavior and escalation compliance;
- **empirical findings:** only results produced by completed evaluations.

Model agreement does not convert a proposal into proof. Model disagreement does not erase the proposal. Claims move to finding status only through documented tests.

## Citation

Solen, Alyssa. *AI Foundations: Origin as Constant and Source-Bound Functions*. Version 0.1.0, 2026.

## License

Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0). See [`LICENSE`](LICENSE).