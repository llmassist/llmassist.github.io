import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

closed_loop_non_reactive_metrics = {
    "PDM-Closed": [92.51, 98.05, 93.11, 99.55, 95.19, 91.75, 99.83, 99.95],
    "GPT-3-ASSIST-UNC": [90.11, 96.19, 92.55, 98.91, 93.37, 91.05, 99.83, 99.91],
    "GPT-3-ASSIST-PAR": [93.05, 98.31, 93.69, 99.54, 95.61, 92.16, 99.83, 99.95],
}

models = ["PDM-Closed", "GPT-3-ASSIST-UNC", "GPT-3-ASSIST-PAR"]

# Define a color map for the models
color_map = {
    "GPT-3": px.colors.qualitative.Plotly[0],
    "GPT-3-ASSIST-PAR": px.colors.qualitative.Plotly[1],
    "PDM-Closed": px.colors.qualitative.Plotly[2],
    "GPT-3-ASSIST-UNC": px.colors.qualitative.Plotly[3],
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

fig = make_subplots(
    rows=2,
    cols=1,
    subplot_titles=("Overall Score", "Sub-Metrics"),
    specs=[[{"type": "bar"}], [{"type": "polar"}]],
)

for model in models:
    fig.add_trace(
        go.Bar(
            name=model,
            x=[model],
            y=[closed_loop_non_reactive_metrics[model][0]],
            marker_color=color_map[model],  # Use color from the map
            showlegend=True,
        ),
        row=1,
        col=1,
    )

for model in models:
    fig.add_trace(
        go.Scatterpolar(
            r=closed_loop_non_reactive_metrics[model][1:],
            theta=metric_names[1:],
            fill="toself",
            name=model,
            marker_color=color_map[model],  # Use color from the map
            showlegend=True,
        ),
        row=2,
        col=1,
    )

fig.update_layout(
    title="Closed Loop Non-Reactive Metrics",
    polar=dict(radialaxis=dict(visible=True, range=[90, 100])),
    # showlegend=True,
    showlegend=False,
    # template="presentation",
)
fig.update_yaxes(range=[85, 100], row=1, col=1)

# fig.show()

print(fig.write_html("metrics/table_2_nr.html", include_plotlyjs="cdn"))
