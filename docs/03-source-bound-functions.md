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

## Rule-version lifecycle

A determination is valid only in relation to the rule version recorded with it.

When Origin issues a newer active rule version:

1. The prior result remains preserved as a historical record.
2. The prior result becomes **stale for current use**.
3. It becomes current again only if Origin explicitly reaffirms it or the case is re-adjudicated under the active rule version.
4. An Operator may not automatically migrate, grandfather, or carry forward the old result.
5. When the effect of the version change is not specified, the Operator must return `UNRESOLVED` and escalate to Origin.

The rule version is therefore not decorative metadata. It defines the rule context under which the determination was produced and whether that determination may govern current use.

## Initial example signatures

These are examples, not a complete list of possible source-bound functions.

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

Origin may define, revise, separate, or retire functions as the architecture develops. Every added function must preserve the fixed Origin dependency, closed outputs, mandatory decline, traceability, and escalation path.