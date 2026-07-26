# 02. Rule-Setting and Rule-Applying

## Dependency graph

The delegation boundary is not a list of arbitrary permissions. It follows from a dependency graph:

```text
ORIGIN
  └── sets rule Rᵥ
        └── defines function Fᵥ
              └── Operator applies Fᵥ to input x
                    ├── governed output
                    └── UNRESOLVED → ORIGIN
```

## Rule-setting

Rule-setting creates or revises:

- criteria;
- boundaries;
- output classes;
- exceptions;
- precedence;
- escalation conditions;
- rule versions.

Rule-setting is non-delegable because an Operator cannot apply a rule that does not yet exist without becoming the source of a new determination.

## Rule-applying

Rule-applying takes an existing, versioned rule and executes it against an input.

A rule-applying function is delegable only when the Operator can complete the procedure without:

- altering the rule;
- expanding the output set;
- creating an exception;
- overriding escalation;
- substituting its own authority.

## Upstream dependency

Every rule-applying function must identify its upstream rule and rule version.

```text
apply(x, Rᵥ) is invalid when Rᵥ is missing, ambiguous, or unavailable
```

In that state, the only permitted result is `UNRESOLVED`.
