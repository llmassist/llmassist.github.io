import pandas as pd
import plotly
import plotly.graph_objs as go

# Data
data = {
    "Method": ["PDMClosed", "GPT-3-ASSISTUNC", "GPT-3-ASSISTPAR"],
    "Score": [92.51, 90.11, 93.05],
    "Collisions": [98.05, 96.19, 98.31],
    "TTC": [93.11, 92.55, 93.69],
    "Drivable": [99.55, 98.91, 99.54],
    "Comfort": [95.19, 93.37, 95.61],
    "Progress": [91.75, 91.05, 92.16],
    "Speed Limit": [99.83, 99.83, 99.83],
    "Direction": [99.95, 99.91, 99.95],
}

# Create DataFrame
df = pd.DataFrame(data)

# Categories
categories = list(df.columns[1:])

# Create traces
traces = []
for i in range(df.shape[0]):
    traces.append(go.Scatterpolar(r=df.iloc[i, 1:].values, theta=categories, fill="toself", name=df.iloc[i, 0]))

# Layout
layout = go.Layout(polar=dict(radialaxis=dict(visible=True, range=[90, 100])), showlegend=True)

# Figure
fig = go.Figure(data=traces, layout=layout)

# Plot
fig.show()

fig.write_html("metrics/play.html", include_plotlyjs="cdn")
# print(plotly.offline.plot(fig, include_plotlyjs=False, output_type="div"))
