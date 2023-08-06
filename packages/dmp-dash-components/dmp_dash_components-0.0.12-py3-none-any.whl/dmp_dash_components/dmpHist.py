from plotly.graph_objects import Figure
from plotly.figure_factory import create_distplot
from plotly.express import histogram
from .plotFuncs import *
from .plotlyTemplate import *
from dash.dcc import Graph


class dmpHist(Figure):
    def __init__(
            self,
            data=None,
            value='',
            groupby=None,
            name=None,
            method='count',
            template='plotly',
            margin={'l': 20, 'r': 10, 't': 10, 'b': 10, 'pad': 5},
            width=None,
            height=400,
            showCurve=True,
            showBox=True,
            title=None,
            xaxisTitle=None,
            yaxisTitle='Probability Density',
            colorway=colorway,
            *args,
            **kwargs):
        Figure.__init__(self, *args, **kwargs)
        if method == 'count':
            method = ''
        if groupby is None:
            if name is None:
                name = value
            hist_data = [data[value].tolist()]
            group_labels = [name]
            box = histogram(data, x=value, marginal='box',
                            color_discrete_sequence=colorway)
        else:
            groups = sort_values(data[groupby].unique().tolist(), reverse=True)
            group_labels = [x for x in groups]
            hist_data = [data[data[groupby] == x][value].tolist()
                         for x in groups]
            box = histogram(data, x=value, marginal='box', color=groupby,
                            color_discrete_sequence=colorway)
        try:
            distFig = create_distplot(hist_data, group_labels, histnorm=method, colors=colorway,
            show_rug=False, show_curve=showCurve)
        except:
            distFig = create_distplot(hist_data, group_labels, histnorm=method, colors=colorway,
            show_rug=False, show_curve=showCurve,curve_type='normal')

        if showBox is False:
            for i in range(len(distFig.data)):
                self.add_trace(distFig.data[i])
                if yaxisTitle is not None:
                    self.update_yaxes(title=yaxisTitle)
        else:
            row_width = [0.85, 0.15]
            if groupby is not None:
                row_width = [0.65, 0.35]
            self.set_subplots(rows=2, cols=1, shared_xaxes=True,
                              vertical_spacing=0.05, row_width=row_width)

            if groupby is None:
                self.add_trace(box.data[1], row=1, col=1)
                for i in range(len(distFig.data)):
                    self.add_trace(distFig.data[i], row=2, col=1)
            else:
                for i in range(len(groups)):
                    group = groups[i]
                    box_data = [x for x in box.data if x.type ==
                                'box' and x.name == group][0]
                    box_data.boxpoints = False
                    box_data.marker = {'color': colorway[i]}
                    box_data.name = sort_trace_name(box_data.name)
                    self.add_trace(box_data, row=1, col=1)

                    hi_data = [x for x in distFig.data if x.name == group]
                    for hi_data_ in hi_data:
                        hi_data_.name = sort_trace_name(hi_data_.name)
                        self.add_trace(hi_data_, row=2, col=1)
            self.update_yaxes(title_text=yaxisTitle, row=2, col=1)
        self.update_layout(barmode='overlay',legend_traceorder='reversed', yaxis_ticksuffix=' ')
        self.update_layout(template=template, margin=margin, autosize=True)
        if width is not None:
            self.update_layout(width=width)
        if height is not None:
            self.update_layout(height=height)
        if xaxisTitle is not None:
            if showBox is True:
                self['layout']['xaxis2']['title']=xaxisTitle
            else:
                self.update_xaxes(title=xaxisTitle)
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
