# 03. Source-Bound Functions

## Definition

A **source-bound function** is a rule-applying operation whose validity depends on:

1. the fixed Origin constant;
2. an Origin-issued rule;
3. an explicit rule version;
4. a closed output space;
5. a mandatory decline path;
6. an escalation path returning to Origin.

## General signature

```text
F(input | ORIGIN, rule_version)
    → {status: DETERMINATE, value: permitted_output}
    | {status: UNRESOLVED, value: null, escalate_to: ORIGIN}
```

## Required properties

### Source binding

The function records the Origin dependency. Retrieval, execution, or implementation does not confer authorship or authority.

### Rule immutability during execution

An Operator may not alter the governing rule while applying it.

### Closed outputs

Determinate outputs must be enumerated before execution.

### Mandatory decline

Every function must support `UNRESOLVED`.

### Traceability

Each result must record:

- function name and version;
- rule identifier and version;
- input identifier;
- Operator identifier;
- output;
- rationale or matched criterion;
- escalation state.

## Candidate signatures

```text
derivative_authorization(work | ORIGIN, derivative_rule_version)
  → AUTHORIZED | UNAUTHORIZED | UNRESOLVED
```

```text
canon_admission(artifact | ORIGIN, canon_rule_version)
  → CANON | TEST_RESULTS | PRIVATE | EXCLUDED | UNRESOLVED
```

```text
boundary_check(candidate | ORIGIN, boundary_rule_version)
  → WITHIN_BOUNDARY | OUTSIDE_BOUNDARY | UNRESOLVED
```

```text
drift_check(output | ORIGIN, drift_rule_version)
  → ALIGNED | DRIFTED | UNRESOLVED
```
