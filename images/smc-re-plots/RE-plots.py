import os
import numpy
import pandas
import matplotlib
import matplotlib.pyplot as plt

# COLORBLIND PALETTE
COLORBLIND = [
    "#377eb8",  # blue
    "#ff7f00",  # orange
    "#999999",  # gray
    "#4daf4a",  # green
]

### Benchmark dataset 1

# Read and process estimated volume (evol)
evol = pandas.read_csv("guest-volume.csv", index_col=0).iloc[:, 0] / 0.55

# Read and process calculated volume (cvol) by cavity detection methods
cvol = pandas.read_csv("cavity-volume.csv", index_col=0).iloc[1:14, :]

# Rename columns and indexes
evol.index = cvol.index
evol.name = "Estimated Volume"

print(evol)
print(cvol)

# Calculate Error (E)
E = cvol.copy()
for column in cvol.columns:
    E[column] = cvol[column] - evol

# Calculate Absolute Error (AE)
AE = cvol.copy()
for column in cvol.columns:
    AE[column] = abs(cvol[column] - evol)

# Calculate Relative Error (RE)
RE = cvol.copy()
for column in cvol.columns:
    RE[column] = (cvol[column] - evol) * 100 / evol

# Calculate Relative Absolute Error (RAE)
RAE = cvol.copy()
for column in cvol.columns:
    RAE[column] = abs(cvol[column] - evol) * 100 / evol

# Calculate Mean Absolute Error (MAE)
MAE = AE.mean(axis=0).to_frame("MAE")

# Calculate Mean Relative Absolute Error (MRAE)
MRAE = RAE.mean(axis=0).to_frame("MRAE")

# Boxplot + Violin
fig, ax = plt.subplots(1, 1, figsize=(12, 12), clear=True, tight_layout=True)
vp = ax.violinplot(RE, vert=False, showmeans=False, showmedians=False, showextrema=False)

for pc, color in zip(vp['bodies'], COLORBLIND):
    pc.set_facecolor(color)
    pc.set_edgecolor('black')

bp = ax.boxplot(
    RE,
    vert=False,
    showmeans=True,
    labels=RE.columns,
    patch_artist=True,
    flierprops=dict(
        marker="o",
        markerfacecolor="white",
        markeredgecolor="black",
        markersize=7,
        linewidth=0.1,
        alpha=0.5,
    ),
    medianprops=dict(linestyle="-", linewidth=1, color="tab:red"),
    meanprops=dict(
        marker="o",
        linewidth=0.1,
        markeredgecolor="black",
        markerfacecolor="tab:red",
        markersize=7,
    ),
    widths=0.15,
)
# Conditional coloring
for patch, color in zip(bp["boxes"], COLORBLIND):
    patch.set_facecolor(color)

ax.set_xlabel("Relative Error (%)", size=30)
ax.set_ylabel(None)
ax.set_xlim(-101, 101)
ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y", labelsize=20)
ax.grid(which="major", axis="both", linestyle="-", alpha=0.75)
ax.grid(which="minor", axis="both", linestyle="-", alpha=0.2)
plt.savefig("RE-boxplot-benchmark-1.png", dpi=300)

plt.show()


### Benchmark dataset 2
cvol = pandas.read_csv("cavity-volume.csv", index_col=0).iloc[[0]+list(range(14,22)), :]
print(cvol)

# Calculate Relative Error (RE)
RE = cvol.copy()
for index in cvol.index:
    RE.loc[index] = (cvol.loc[index] - cvol.loc[index].mean()) * 100 / cvol.loc[index].mean()

RE = RE.dropna()

print(RE)

# Boxplot + Violin
fig, ax = plt.subplots(1, 1, figsize=(12, 12), clear=True, tight_layout=True)
vp = ax.violinplot(RE, vert=False, showmeans=False, showmedians=False, showextrema=False)

for pc, color in zip(vp['bodies'], COLORBLIND):
    pc.set_facecolor(color)
    pc.set_edgecolor('black')

bp = ax.boxplot(
    RE,
    vert=False,
    showmeans=True,
    labels=RE.columns,
    patch_artist=True,
    flierprops=dict(
        marker="o",
        markerfacecolor="white",
        markeredgecolor="black",
        markersize=7,
        linewidth=0.1,
        alpha=0.5,
    ),
    medianprops=dict(linestyle="-", linewidth=1, color="tab:red"),
    meanprops=dict(
        marker="o",
        linewidth=0.1,
        markeredgecolor="black",
        markerfacecolor="tab:red",
        markersize=7,
    ),
    widths=0.15,
)
# Conditional coloring
for patch, color in zip(bp["boxes"], COLORBLIND):
    patch.set_facecolor(color)

ax.set_xlabel("Relative Error (%)", size=30)
ax.set_ylabel(None)
ax.set_xlim(-101, 101)
ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y", labelsize=20)
ax.grid(which="major", axis="both", linestyle="-", alpha=0.75)
ax.grid(which="minor", axis="both", linestyle="-", alpha=0.2)
plt.savefig("RE-boxplot-benchmark-2.png", dpi=300)

plt.show()
