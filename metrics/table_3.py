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

import plotly.graph_objects as go

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

fig = go.Figure()
fig.add_trace(
    go.Scatterpolar(
        r=closed_loop_non_reactive_metrics["GPT-3"][1:],
        theta=metric_names[1:],
        fill="toself",
        name="GPT-3",
    )
)
fig.add_trace(
    go.Scatterpolar(
        r=closed_loop_non_reactive_metrics["GPT-3-ASSIST-PAR"][1:],
        theta=metric_names[1:],
        fill="toself",
        name="GPT-3-ASSIST-PAR",
    )
)

fig.update_layout(
    title="Closed Loop Non-Reactive Metrics",
    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
    showlegend=True,
)

# fig.update_layout(
#     title={"text": "Closed Loop Non-Reactive Metrics", "x": 0.5, "xanchor": "center", "yanchor": "top"},
#     polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
#     legend=dict(x=0.5, y=-0.1, xanchor="center", yanchor="top"),
#     showlegend=True,
#     template="presentation",
# )

fig.show()
