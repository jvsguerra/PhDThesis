# Data from 01/03/2023 to 31/01/2024
import pandas as pd
import matplotlib.pyplot as plt

# Colorblind palette
COLORBLIND = [
    "#377eb8",  # blue
    "#ff7f00",  # orange
    "#4daf4a",  # green
    "#f781bf",  # pink
    "#a65628",  # brown
    "#984ea3",  # purple
    "#999999",  # gray
    "#dede00",  # yellow
    "#e41a1c",  # red
]

# Open raw usage data
with open("kvweb-usage.txt", "r") as f:
    lines = f.readlines()

# Process
dates = []
for line in lines:
    # Long ISO format (%Y-%m-%d)
    line = line.split()[5]    
    dates.append(line)

# Convert to DataFrame and export to csv
data = pd.DataFrame(dates, columns=["Data"])
data.Data = pd.to_datetime(data.Data)
data.to_csv("kvweb-usage.csv", index=False, header=False)

# Plot KVFinder-web usage over time
fig, ax = plt.subplots(1, 1, figsize=(12, 9), clear=True, tight_layout=True)

# Histogram
x1 = data.groupby([data["Data"].dt.year, data["Data"].dt.month]).count()
print(x1)
rects = ax.bar(
    x=["Mar-23", "Apr-23", "May-23", "Jun-23", "Jul-23", "Aug-23", "Sep-23", "Oct-23", "Nov-23", "Dec-23", "Jan-24"],
    height=x1.Data.values,
    align="center",
    ecolor="black",
    capsize=5,
    width=0.5,
    edgecolor="black",
    color="#377eb8",
    alpha=0.8,
)

# Annotate bars
for rect in rects:
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2.0,
        1.05 * height,
        "%d" % int(height),
        ha="center",
        va="bottom",
        size=20
    )

# Cumulative sum
x2 = data.groupby([data["Data"].dt.year, data["Data"].dt.month]).count().cumsum()
print(x2)
ax.plot(
    ["Mar-23", "Apr-23", "May-23", "Jun-23", "Jul-23", "Aug-23", "Sep-23", "Oct-23", "Nov-23", "Dec-23", "Jan-24"],
    x2.Data.values,
    color="black",
    label="Cumulative sum",
    marker="o",
)

# Customize
ax.grid(which="major", axis="y", linestyle="--")
ax.set_ylabel("Jobs", size=20)
ax.set_ylim(0, 1400)
ax.tick_params(axis="x", labelsize=15)
ax.tick_params(axis="y", labelsize=15)
ax.yaxis.set_ticks([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400])

# Legend
ax.legend(loc="upper left", fontsize=20)

plt.savefig("jobs-executed-per-month.png", dpi=300)
