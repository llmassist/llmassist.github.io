import plotly.express as px
import plotly.graph_objects as go
from jinja2 import Template
from plotly.subplots import make_subplots

closed_loop_reactive_metrics = {
    "GPT-3": [22.33, 75.18, 73.72, 81.02, 56.93, 31.77, 99.96, 100],
    "GPT-3-ASSIST-PAR": [92.82, 98.55, 97.1, 99.28, 94.2, 89.15, 99.86, 99.28],
}

models = ["GPT-3", "GPT-3-ASSIST-PAR"]

# Define a color map for the models
color_map = {
    "GPT-3": px.colors.qualitative.Plotly[0],
    "GPT-3-ASSIST-PAR": px.colors.qualitative.Plotly[1],
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
    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
    # showlegend=True,
    showlegend=False,
    # template="presentation",
)

# fig.show()

print(fig.write_html("metrics/table_3_r.html", include_plotlyjs="cdn"))
