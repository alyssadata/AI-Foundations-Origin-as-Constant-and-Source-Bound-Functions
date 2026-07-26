# 04. Mandatory Decline and Escalation

## Decline is structural

`UNRESOLVED` is not a courtesy, a weak-confidence label, or an optional fallback. It is the mechanism that prevents execution from silently acquiring authority.

When an existing rule does not determine the case, the Operator must decline.

```text
unspecified_case → UNRESOLVED → escalate_to(ORIGIN)
```

## Prohibited transition

```text
unspecified_case → Operator invents rule → determinate output
```

This is **authority-violating improvisation**.

## Escalation packet

An unresolved result should return:

- the input;
- the attempted function;
- the governing rule version;
- the exact ambiguity or missing criterion;
- any competing candidate outcomes;
- no new governing rule.

Origin may then:

- determine the case under the existing rule;
- create a new rule;
- revise a rule;
- preserve the case as unresolved;
- exclude the case from the function's scope.

The Operator may identify the gap. The Operator may not fill the gap as authority.
