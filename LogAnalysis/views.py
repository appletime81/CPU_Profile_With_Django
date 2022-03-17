from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import pandas as pd


# Create your views here.
def index(request, **kwargs):
    data = {
        "Topic": "Analysis",
        "Des.": "A site for analysis CPU performance"
    }
    return render(request, 'index.html', context=data)


def plot_chart(request, **kwargs):
    x_data = [0, 1, 2, 3]
    y_data = [x ** 2 for x in x_data]
    plot_div1 = plot([Scatter(x=x_data, y=y_data,
                             mode='lines', name='test',
                             opacity=0.8, marker_color='green')],
                    output_type='div')
    plot_div2 = plot([Scatter(x=x_data, y=y_data,
                             mode='lines', name='test',
                             opacity=0.8, marker_color='green')],
                    output_type='div')
    return render(request, 'index.html', context={'plot_div1': plot_div1, 'plot_div2': plot_div2})
