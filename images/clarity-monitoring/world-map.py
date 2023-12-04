import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

# Read data
countries = pd.read_csv("clarity-countries.csv", index_col=0)
countries = countries.to_dict()["No. of sessions"]
countries = {k: [v] for k, v in sorted(countries.items(), key=lambda item: item[1])}
browsers = pd.read_csv("clarity-browsers.csv")
os = pd.read_csv("clarity-os.csv")

# COLORBLIND PALETTE
COLORBLIND = [
    "#377eb8",  # blue
    "#ff7f00",  # orange
    "#4daf4a",  # green
    "#f781bf",  # pink
    "#a65628",  # brown
    "#984ea3",  # purple
    "#999999",  # gray
    "#e41a1c",  # red
    "#dede00",  # yellow
]

# [Plot 1] Chropopleth map for countries

# Prepare data
raw = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv"
)
raw.columns = ["country", "GDP", "code"]
antarctica = ["Antarctica", 0, "ATA"]
raw.loc[len(raw)] = antarctica
data = pd.DataFrame(countries).T.reset_index()
data.columns = ["country", "count"]
df = pd.merge(raw, data, how="left", on="country")
df["count"] = df["count"].replace(np.nan, 0)

# Plot
fig = px.choropleth(
    df,
    locations="code",
    color="count",
    color_continuous_scale=["#FFFFFF", "#377eb8"],
    labels={"count": "Visitors"},
    range_color=(0, round(df["count"].max())),
    projection="equirectangular",  # miller
    width=1200,
    height=700,
)

fig.update_layout(
    coloraxis_colorbar=dict(
        thicknessmode="pixels",
        thickness=40,
        lenmode="pixels",
        len=520,
        yanchor="top",
        y=0.97,
        ticks="outside",
        tickwidth=1,
        ticklen=10,
        dtick=1,
        outlinecolor="black",
        outlinewidth=1,
    )
)

fig.update_coloraxes(
    colorbar_title_font_size=30,
    colorbar_tickfont_size=16
)

plt.tight_layout()
fig.write_image("clarity-countries.png", engine="auto")

# [Plot 2] Pie chart for browsers

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

wedges, texts = ax.pie(
    browsers["No. of sessions"],
    colors=COLORBLIND,
    wedgeprops=dict(width=0.5, edgecolor="black"),
    startangle=-40,
)

bbox_props = dict(boxstyle="square, pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1) / 2.0 + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(
        browsers["Browsers"][i] + " (" + browsers["% of sessions"][i] + ")",
        xy=(x, y),
        xytext=(1.35 * np.sign(x), 1.4 * y),
        horizontalalignment=horizontalalignment,
        **kw
    )

plt.tight_layout()
plt.savefig("clarity-browsers.png", dpi=300)

# [Plot 3] Pie chart for Operating systems
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

wedges, texts = ax.pie(
    os["No. of sessions"],
    colors=COLORBLIND,
    wedgeprops=dict(width=0.5, edgecolor="black"),
    startangle=-40,
)

bbox_props = dict(boxstyle="square, pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1) / 2.0 + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(
        os["Operating systems"][i] + " (" + os["% of sessions"][i] + ")",
        xy=(x, y),
        xytext=(1.35 * np.sign(x), 1.4 * y),
        horizontalalignment=horizontalalignment,
        **kw
    )

plt.tight_layout()
plt.savefig("clarity-os.png", dpi=300)
