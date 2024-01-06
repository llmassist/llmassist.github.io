"""
Closed Loop Non-Reactive Metrics
Method	Score	Collisions	TTC	Drivable	Comfort	Progress	Speed Limit	Direction
GPT-3	18.08	63.04	60.14	78.26	57.97	31.3	99.93	98.91
GPT-3-ASSIST-PAR	94.8	100	94.89	100	97.81	90.18	99.86	99.64

Closed Loop Reactive Metrics
Method	Score	Collisions	TTC	Drivable	Comfort	Progress	Speed Limit	Direction
GPT-3	22.33	75.18	73.72	81.02	56.93	31.77	99.96	100
GPT-3-ASSIST-PAR	92.82	98.55	97.1	99.28	94.2	89.15	99.86	99.28
"""

import pandas as pd
import plotly.express as px

closed_loop_non_reactive_metrics = {
    "GPT-3": [18.08, 63.04, 60.14, 78.26, 57.97, 31.3, 99.93, 98.91],
    "GPT-3-ASSIST-PAR": [94.8, 100, 94.89, 100, 97.81, 90.18, 99.86, 99.64],
}

closed_loop_reactive_metrics = {
    "GPT-3": [22.33, 75.18, 73.72, 81.02, 56.93, 31.77, 99.96, 100],
    "GPT-3-ASSIST-PAR": [92.82, 98.55, 97.1, 99.28, 94.2, 89.15, 99.86, 99.28],
}

metric_names = [
    "Score",
    "Collisions",
    "TTC",
    "Drivable",
    "Comfort",
    "Progress",
    "Speed Limit",
    "Direction",
]

df = pd.DataFrame.from_dict(closed_loop_non_reactive_metrics, orient="index")
df = df.transpose()
df.columns = ["GPT-3", "GPT-3-ASSIST-PAR"]
df["Metric"] = metric_names
df = df.melt(id_vars=["Metric"], var_name="Method", value_name="Value")

fig = px.line_polar(
    df,
    r="Value",
    theta="Metric",
    color="Method",
    line_close=True,
    color_discrete_sequence=px.colors.sequential.Plasma_r,
    template="plotly_dark",
)
fig.show()
