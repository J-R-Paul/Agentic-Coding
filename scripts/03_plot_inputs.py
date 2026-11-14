"""Draw two plain starter plots from precomputed synthetic descriptive summaries.

These are inputs for testing a student-created plotting skill. Rebuilding the
statistics is unnecessary for this exercise. The confidence intervals have
already been computed; preserve their values and explain their assumptions.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "04-skill"
OUT.mkdir(parents=True, exist_ok=True)
for stem in ["life_satisfaction_by_status", "care_hours_by_age"]:
    table = pd.read_csv(ROOT / "data" / "fixtures" / f"{stem}.csv")
    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.errorbar(table.estimate, range(len(table)),
                xerr=[table.estimate - table.ci_low, table.ci_high - table.estimate],
                fmt="o", color="black", capsize=3)
    ax.set_yticks(range(len(table)), table.group.str.replace("_", " "))
    ax.set(xlabel=table.units.iloc[0], title=f"{table.measure.iloc[0]} — synthetic data")
    ax.invert_yaxis()
    fig.text(.5, .015, "95% t intervals for group means; independent observations assumed.",
             ha="center", fontsize=8)
    fig.tight_layout(rect=[0, .045, 1, 1])
    fig.savefig(OUT / f"{stem}.png", dpi=160)
    plt.close(fig)
    print(f"Created outputs/04-skill/{stem}.png")
