import dash
import dash_core_components as dcc
from dash import html
import plotly.io as pio

app = dash.Dash(__name__)

# Define your layout and callbacks here
app.layout = html.Div([
    dcc.Graph(id='example-graph', figure={'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Example'}]})
])

# Export the app to an HTML file
pio.write_html(app.to_html(), file='index.html')
