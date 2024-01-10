import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

closed_loop_reactive_metrics = {
    "PDM-Closed": [91.79, 97.91, 93.29, 99.37, 94.65, 89.92, 99.83, 99.95],
    "GPT-3-ASSIST-UNC": [90.32, 96.82, 93.1, 98.73, 92.92, 89.01, 99.83, 99.86],
    "GPT-3-ASSIST-PAR": [92.2, 98.18, 93.62, 99.64, 94.72, 90.07, 99.83, 99.95],
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
            y=[closed_loop_reactive_metrics[model][0]],
            marker_color=color_map[model],  # Use color from the map
            showlegend=True,
        ),
        row=1,
        col=1,
    )

for model in models:
    fig.add_trace(
        go.Scatterpolar(
            r=closed_loop_reactive_metrics[model][1:],
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
    title="Closed Loop Reactive Metrics",
    polar=dict(radialaxis=dict(visible=True, range=[90, 100])),
    # showlegend=True,
    showlegend=False,
    # template="presentation",
)
fig.update_yaxes(range=[85, 100], row=1, col=1)

# fig.show()

print(fig.write_html("metrics/table_2_r.html", include_plotlyjs="cdn"))
