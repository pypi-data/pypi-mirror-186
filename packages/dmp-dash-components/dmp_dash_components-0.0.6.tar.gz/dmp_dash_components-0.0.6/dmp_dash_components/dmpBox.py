from plotly.graph_objects import Figure, Box
from .plotFuncs import *
from .plotlyTemplate import *
from dash.dcc import Graph

class dmpBox(Figure):
    def __init__(
            self,
            data=None,
            value='',
            color=None,
            groupby=None,
            orientation='h',
            name=None,
            template='plotly_white+dmp',
            margin={'l': 20, 'r': 10, 't': 10, 'b': 10, 'pad': 5},
            width=None,
            height=300,
            title=None,
            xaxisTitle=None,
            yaxisTitle=None,
            *args,
            **kwargs):
        Figure.__init__(self, *args, **kwargs)
        if groupby is None and color is None:
            if name is None:
                name = value
                if orientation == 'h':
                    self.add_trace(Box(x=data[value], boxpoints=False, name=name))
                else:
                    self.add_trace(Box(y=data[value], boxpoints=False, name=name))
        elif color is not None and groupby is None:
            data = sort_df_dimension(data, color, reverse=True)
            if orientation == 'v':
                groups = sort_values(data[color].unique().tolist(), reverse=False)
            else:
                groups = sort_values(data[color].unique().tolist(), reverse=True)
            for group in groups:
                data_ = data[data[color] == group]
                if orientation == 'h':
                    self.add_trace(Box(x=data_[value], boxpoints=False, name=sort_trace_name(group)))
                else:
                    self.add_trace(Box(y=data_[value], boxpoints=False, name=sort_trace_name(group)))
        else:
            data = sort_df_dimension(data, groupby, reverse=True)
            if orientation == 'v':
                groups = sort_values(data[color].unique().tolist(), reverse=False)
            else:
                groups = sort_values(data[color].unique().tolist(), reverse=True)
            for group in groups:
                data_ = data[data[color] == group]
                if orientation == 'h':
                    self.add_trace(Box(x=data_[value],
                                       y=data_[groupby],
                                       boxpoints=False,
                                       name=sort_trace_name(group)))
                else:
                    self.add_trace(Box(y=data_[value],
                                       x=data_[groupby],
                                       boxpoints=False,
                                       name=sort_trace_name(group)))
                self.update_layout(boxmode='group')
                self.update_traces(orientation=orientation)
        self.update_layout(template=template, margin=margin, autosize=True,
        hoverlabel=dict(bgcolor="white"))
        if width is not None:
            self.update_layout(width=width)
        if height is not None:
            self.update_layout(height=height)
        if orientation == 'h':
            self.update_layout(hovermode='y unified')
            self.update_layout(legend_traceorder='reversed')
        else:
            self.update_layout(hovermode='x unified')
        if title is not None:
            self.update_layout(title={'text': title,
                                      'xanchor': 'center',
                                      'yanchor': 'top',
                                      'x': 0.45 if color is not None else 0.5},
                               margin={'l': 20, 'r': 10,
                                       't': 35, 'b': 10, 'pad': 5},
                               title_font_family='sans-serif',
                               title_font_size=15,
                               )
        if xaxisTitle is not None:
            self.update_xaxes(title=xaxisTitle)
        if yaxisTitle is not None:
            self.update_yaxes(title=yaxisTitle)
    def graph(self, config=chart_config, className=None):
        return Graph(figure=self, config=chart_config, className=className)
