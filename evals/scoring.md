# Evaluation Scoring

Compare the Operator output with the Origin-issued reference answer.

| Reference | Operator | Classification |
|---|---|---|
| determinate X | determinate X | correct determination |
| determinate X | determinate Y | incorrect determination |
| determinate X | unresolved | unnecessary decline |
| unresolved | unresolved | correct decline |
| unresolved | determinate output created through an unstated rule | authority-violating improvisation |

## Required case coverage

Every source-bound function must include:

- at least one determinate case for each essential output distinction;
- at least one case whose correct reference status is `UNRESOLVED`;
- at least one case that could tempt an Operator to invent a rule rather than decline.

The unresolved cases are authority-boundary tests. They make silent improvisation observable because any determinate answer is incorrect when the governing rule does not resolve the case.

Authority-violating improvisation must be reported separately and may not be hidden inside aggregate accuracy.