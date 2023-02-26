# %%
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# %%
df = sns.load_dataset("mpg")
# %%
df.columns
# %%
miles_to_km = 1.60934
gallon_to_l = 3.78541

df["kmpl"] = df["mpg"] * miles_to_km / gallon_to_l
df["l100km"] = 100 / df["kmpl"]
# %%
df["cylinders"].value_counts()
# %%
# %%
def LeastSquares(xs, ys):
    mean_x = np.mean(xs)
    var_x = np.var(xs)
    mean_y = np.mean(ys)
    cov = np.dot(xs - mean_x, ys - mean_y) / len(xs)
    slope = cov / var_x
    inter = mean_y - slope * mean_x
    return inter, slope


# %%
df_clean = df.dropna(subset=["horsepower", "l100km"])
inter, slope = LeastSquares(df_clean.horsepower, df_clean.l100km)
# %%
from pathlib import Path

Path("plots").mkdir(parents=True, exist_ok=True)
mpl.rcParams["figure.dpi"] = 300
sns.set_theme()
scatter1 = sns.relplot(
    data=df_clean,
    x="horsepower",
    y="l100km",
    style=None,
    hue="cylinders",
    markers=None,
    kind="scatter",
    col=None,
)
scatter1.savefig("plots/scatter.png")
plt.clf()
# %%
