from plotly.graph_objects import Figure, Pie
from .plotFuncs import *
from .plotlyTemplate import *
from dash.dcc import Graph

class dmpPie(Figure):
    def __init__(
            self,
            data=None,
            dimension='',
            value='',
            hole=0.4,
            template='plotly_white+dmp',
            margin={'l': 20, 'r': 10, 't': 10, 'b': 10, 'pad': 5},
            width=None,
            height=None,
            showLabels=True,
            title=None,
            *args,
            **kwargs):
        Figure.__init__(self, *args, **kwargs)
        data = sort_df_dimension(data, dimension, reverse=False)
        if data[dimension].nunique() <= 5:
            textinfo = 'percent+label'
        else:
            textinfo = 'percent'
        self.add_trace(
                Pie(
                    labels=data[dimension].tolist(),
                    values=data[value].tolist(),
                    textinfo=textinfo
                   )
            )
        self.update_layout(template=template, margin=margin, autosize=True)
        if width is not None:
            self.update_layout(width=width)
        if height is not None:
            self.update_layout(height=height)
        if hole is not None:
            self.update_traces(hole=hole)
        self.update_layout(legend_traceorder="reversed")
        if title is not None:
            self.update_layout(title={'text': title,
                                      'xanchor': 'center',
                                      'yanchor': 'top',
                                      'x': 0.45},
                               margin={'l': 20, 'r': 10,
                                       't': 35, 'b': 10, 'pad': 5},
                               title_font_family='sans-serif',
                               title_font_size=15,
                               )
    def graph(self, config=chart_config, className=None):
        return Graph(figure=self, config=chart_config, className=className)
