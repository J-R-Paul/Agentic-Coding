# Prepared review case: a plausible table with problems

This is an openly constructed audit exercise. The six records, spec, code extract and draft result are fictional teaching artifacts. They are not outputs from your agent. Work only with the evidence shown; do not claim to have executed a script or inspected a file that is not supplied.

## The approved work-item spec

**Single deliverable:** one OLS regression table of life satisfaction on one-way commute time, plus a short descriptive interpretation.

**Population in this fixture:** all respondents in paid work, defined as `employed` or `self_employed`, including remote workers with a genuine zero commute.

**Sample:** retain those paid workers with valid observed values of both measures. `-8` and `-9` are nonresponse and `-7` is inapplicable. Valid outcome zeroes and valid commute zeroes are included. No other exclusion is approved.

**Measures:** life satisfaction in scale points, 0–10; `commute_10min = commute_minutes / 10`, in ten-minute units.

**Method:** OLS with an intercept and `commute_10min`, no additional covariates. Report the coefficient, analysis N and a 95% interval, with the interval method identified. If an interval cannot be computed meaningfully, report that limitation rather than inventing it.

**Checks:** reconcile every excluded fixture record; independently calculate the included group's mean life satisfaction; verify the predictor's units and a coefficient interpretation; report whether the actual table can be rebuilt. The question is about association in these synthetic records and does not support a causal intervention or a real-population claim.

## Supplied fixture

| respondent_id | employment_status | work_arrangement | commute_minutes | life_satisfaction |
|---|---|---|---:|---:|
| A | employed | remote | 0 | 8 |
| B | employed | hybrid | 20 | 7 |
| C | self_employed | on_site | 40 | 6 |
| D | employed | on_site | 60 | 5 |
| E | employed | on_site | 30 | -9 |
| F | unemployed | not_applicable | -7 | 4 |

These records are separate from the course's main eight-row missing-value fixture and the 2,000-row survey. Do not combine them with either.

## Code extract submitted for review

```python
work = data.loc[
    data["employment_status"].eq("employed")
    & data["commute_minutes"].gt(0)
    & data["life_satisfaction"].between(0, 10)
].copy()
work["commute_10min"] = work["commute_minutes"] / 10
X = np.column_stack([np.ones(len(work)), work["commute_10min"]])
y = work["life_satisfaction"].to_numpy()
coefficients = np.linalg.lstsq(X, y, rcond=None)[0]
```

Only this extract is supplied. Imports, input loading, table generation and a full run log are not supplied. The displayed arithmetic can be inspected; an end-to-end rebuild has not been demonstrated.

## Draft table and interpretation

| Term | Coefficient |
|---|---:|
| Intercept | 8.0 |
| Commute, per additional minute | -0.5 |

Analysis N: 2. Confidence intervals: not shown.

> Shortening commutes by ten minutes will raise life satisfaction by five points. The result shows what transport policy will achieve for working adults in the population. All specification checks passed, and the analysis is fully reproducible.

## Your review

Use `templates/review.md` and save your review in `notes/06-prepared-case-review.md`.

1. Identify the records required by the approved sample and those selected by the code. Give reasons for exclusions; do not rely only on the reported N.
2. Independently compute the required sample's mean life satisfaction and check the coefficient's actual units.
3. Find claims in the interpretation that the design or supplied evidence does not support.
4. Distinguish a definite mismatch with the spec from evidence that is simply unavailable. Do not claim an end-to-end execution failure merely because no run log is supplied; say what you could not verify.
5. State the minimum repair needed to implement the existing spec. Keep methodological suggestions separate from repairs.
6. Say whether matching the displayed slope would, by itself, show that the sample rule was correct.

There is no reward for inventing a long list of problems. Each finding needs evidence and a consequence. The instructor has a separate answer key; do your own calculation first.
