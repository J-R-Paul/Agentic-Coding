# Small inputs for checking and plotting

All values are synthetic course data, release 1.0.0.

## Hand-check fixture

`missing_values_example.csv` is an eight-row table for hand checks (card 05, *If ahead*). Work out the number of valid life
satisfaction responses and their mean using the codebook before asking an
agent to check the calculation. A commute of `0` for a remote worker, `-7` for
a nonworker, and `-8`/`-9` for nonresponse have different meanings.

`missing_values.csv` is an additional five-row worked check. Its valid responses
are 7, 8 and 5: count 3, missing count 2, mean 20/3. These results are also in
`expected_missing_values.json` for a simple reproducible check.

## Inputs for your plotting skill (card 04)

Card 04 uses `care_hours_by_age.csv`, and `life_satisfaction_by_status.csv` if you're ahead. The
first describes life satisfaction by employment status; the second describes
weekly unpaid care by age group. Both were computed from the main raw survey
after excluding only `-8` and `-9` in the summarised outcome. A respondent
with a valid outcome is retained even if another response is missing.

| Column | Meaning |
|---|---|
| `group` | Group label. Preserve the supplied order unless your spec explains a change. |
| `estimate` | Arithmetic mean of valid responses within the group |
| `ci_low`, `ci_high` | Lower and upper endpoints of the supplied interval |
| `n` | Number of valid responses used for the group mean |
| `measure`, `units` | Labels to use when constructing a title/axis |
| `ci_method` | Method behind the uncertainty interval |

Intervals are **95% Student t intervals for group means**, using the sample
standard deviation and `n-1` degrees of freedom. They assume independent
observations and are a teaching approximation for these bounded/skewed
outcomes. They are not ranges containing 95% of individuals, causal intervals,
or measures of uncertainty about a real population. Do not recompute them from
the small summary table or clamp them to the outcome bounds without stating
what changed. Values are rounded to six decimals for portability.

Create a reusable figure procedure from your visual decisions. Apply it to
both inputs without hard-coding the first outcome, units or number of groups.
Mark every figure as synthetic. The summary files exist so you can work on
the skill without first writing two cleaning pipelines.
