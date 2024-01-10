import plotly.express as px
import plotly.graph_objects as go
from jinja2 import Template
from plotly.subplots import make_subplots

closed_loop_non_reactive_metrics = {
    "GPT-3": [18.08, 63.04, 60.14, 78.26, 57.97, 31.3, 99.93, 98.91],
    "GPT-3-ASSIST-PAR": [94.8, 100, 94.89, 100, 97.81, 90.18, 99.86, 99.64],
}
models = ["GPT-3", "GPT-3-ASSIST-PAR"]

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
    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
    # showlegend=True,
    showlegend=False,
    # template="presentation",
)

# fig.show()

print(fig.write_html("metrics/table_3_nr.html", include_plotlyjs="cdn"))
