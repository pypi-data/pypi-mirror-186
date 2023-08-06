from plotly.graph_objects import Figure, Bar
from .plotFuncs import *
from .plotlyTemplate import *
from dash.dcc import Graph


class dmpBar(Figure):
    def __init__(
            self,
            data=None,
            dimension='',
            value='',
            groupby=None,
            orientation='h',
            name=None,
            barmode='group',
            template='plotly_white+dmp',
            margin={'l': 20, 'r': 10, 't': 10, 'b': 10, 'pad': 5},
            width=None,
            barWidth=30,  # applies to horizontal bar only
            height=None,
            title=None,
            showLabels=True,
            xaxisTitle=None,
            yaxisTitle=None,
            *args,
            **kwargs):
        Figure.__init__(self, *args, **kwargs)
        if name is None:
            name = dimension.title()
        data = sort_df_dimension(data, dimension, reverse=True)
        if orientation == 'h':
            x, y = value, dimension
            if barWidth is not None:
                height = barWidth * data[x].nunique()
                if height < 120:
                    height = 120
            if data[x].nunique() == 1:
                height = 60
            if barmode == 'stack100':
                x = 'pert'
        else:
            y, x = value, dimension
            if barmode == 'stack100':
                y = 'pert'
        if groupby is None:
            self.add_trace(
                Bar(
                    y=data[y], x=data[x], orientation=orientation,
                    name=name, text=data[value], hovertemplate='%{text}'
                )
            )
        else:
            data['pert'] = 100 * data[value] / \
                data.groupby([dimension])[value].transform('sum')
            data['text'] = data.apply(lambda x: '{} ({}%)'.format(
                x[value], round2(x['pert'])), axis=1)
            if 'stack' in barmode:
                groups = sort_values(
                    data[groupby].unique().tolist(), reverse=True)
            else:
                groups = sort_values(
                    data[groupby].unique().tolist(), reverse=False)
            for group in groups:
                data_ = data[data[groupby] == group]
                self.add_trace(
                    Bar(
                        y=data_[y], x=data_[x],
                        orientation=orientation,
                        name=sort_trace_name(group),
                        text=data_['text'],
                        hovertemplate='%{text}'
                    )
                )
        self.update_layout(template=template, margin=margin, autosize=True)
        if width is not None:
            self.update_layout(width=width)
        if height is not None:
            self.update_layout(height=height)
        if orientation == 'h':
            self.update_xaxes(showticklabels=False, showgrid=False)
        else:
            self.update_yaxes(showticklabels=False, showgrid=False)
        if 'stack' in str(barmode):
            self.update_layout(barmode='stack')
            if orientation == 'h':
                self.update_layout(hovermode='y unified')
            else:
                self.update_layout(hovermode='x unified')
        if showLabels is False:
            self.update_traces(text=None)
        if xaxisTitle is not None:
            self.update_xaxes(title=xaxisTitle)
        if yaxisTitle is not None:
            self.update_yaxes(title=yaxisTitle)
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
