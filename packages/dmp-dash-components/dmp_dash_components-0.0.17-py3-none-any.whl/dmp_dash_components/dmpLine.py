from plotly.graph_objects import Figure, Scatter
from .plotFuncs import *
from .plotlyTemplate import *
from dash.dcc import Graph


class dmpLine(Figure):
    def __init__(
            self,
            data=None,
            dimension='',
            value='',
            groupby=None,
            name=None,
            template='plotly_white+dmp',
            margin={'l': 20, 'r': 10, 't': 10, 'b': 10, 'pad': 5},
            width=None,
            height=350,
            showLabels=True,
            xaxisTitle=None,
            yaxisTitle=None,
            title=None,
            dualYaxis=False,
            *args,
            **kwargs):
        Figure.__init__(self, *args, **kwargs)
        self.set_subplots(specs=[[{"secondary_y": dualYaxis}]])
        data = sort_df_dimension(data, dimension, reverse=False)
        if name is None:
            name = dimension.title()
        if groupby is None:
            self.add_trace(
                Scatter(
                    x=data[dimension],
                    y=data[value],
                    mode='lines',
                    name=name
                )
            )
        else:
            groups = sort_values(data[groupby].unique().tolist(), reverse=True)
            for i in range(len(groups)):
                group = groups[i]
                secondary_y = False
                data_ = data[data[groupby] == group]
                if dualYaxis is True and i == 1:
                    secondary_y = True
                self.add_trace(
                    Scatter(
                        x=data_[dimension],
                        y=data_[value],
                        name=sort_trace_name(group),
                        mode='lines'
                    ),
                    secondary_y=secondary_y
                )
        self.update_layout(template=template, margin=margin, autosize=True)
        if xaxisTitle is not None:
            self.update_xaxes(title=xaxisTitle)
        if yaxisTitle is not None:
            if type(yaxisTitle) == str:
                self.update_yaxes(title=yaxisTitle)
            elif type(yaxisTitle) == list:
                self.update_yaxes(title_text=yaxisTitle[0], secondary_y=False)
                self.update_yaxes(title_text=yaxisTitle[1], secondary_y=True)
        else:
            if groupby is not None and dualYaxis is True:
                self.update_yaxes(title_text=groups[0], secondary_y=False)
                self.update_yaxes(title_text=groups[1], secondary_y=True)
        self.update_layout(hovermode='x unified')
        if width is not None:
            self.update_layout(width=width)
        if height is not None:
            self.update_layout(height=height)
        self.update_layout(legend_traceorder="reversed")
        if title is not None:
            self.update_layout(title={'text': title,
                                      'xanchor': 'center',
                                      'yanchor': 'top',
                                      'x': 0.45 if groupby is not None else 0.5},
                               margin={'l': 20, 'r': 10,
                                       't': 35, 'b': 10, 'pad': 5},
                               title_font_family='sans-serif',
                               title_font_size=15,
                               )

    def graph(self, config=chart_config, className=None):
        return Graph(figure=self, config=chart_config, className=className)
