import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
data = ROOT / "data" / "interim" / "df.csv"

df = pd.read_csv(data)

plt.rc({"pgf.rcfonts": False})

# plt.hist(df.L_PREOVULATION, bins=40)
sns.violinplot(df.L_PREOVULATION, inner='box', saturation=0.3)

plt.title("Distribution of pre-ovulation date")
plt.xlabel("Day in cycle")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig(str(ROOT / "reports" / "figures" / "l_preov_distribution.png"))
