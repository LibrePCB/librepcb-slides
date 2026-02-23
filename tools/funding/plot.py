# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "kaleido",
#     "numpy",
#     "pandas",
#     "plotly",
# ]
# ///
import plotly.graph_objects as go
labels = ['NLnet Grant','Sponsorings','Donations']
values = [35850, 5000, 1750]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

fig.update_layout(
    template='plotly_white',
    margin=dict(l=20, r=20, t=20, b=20),
)

fig.write_image("funding.svg", width=300, height=200)
