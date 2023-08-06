from plotly.graph_objects import Figure
from plotly.express import scatter
from .plotFuncs import *
from .plotlyTemplate import *
from dash.dcc import Graph
from dash.html import Li, Ul, Sup
from numpy import log

class dmpScatter(Figure):
    def __init__(
            self,
            data=None,
            x='',
            y='',
            size=None,
            color=None,
            name=None,
            showLabels=True,
            xName=None,
            yName=None,
            sizeName=None,
            xaxisTitle=None,
            yaxisTitle=None,
            showscale=False,
            trendline=False,
            title=None,
            template='plotly_white+dmp',
            margin={'l': 20, 'r': 10, 't': 10, 'b': 10, 'pad': 5},
            width=None,
            height=350,
            colorway=colorway,
            *args,
            **kwargs):
        Figure.__init__(self, *args, **kwargs)
        groupby = False
        if xName is None:
            xName = x
        if yName is None:
            yName = y
        if sizeName is None:
            sizeName = size
        if size is None:
            tp = '{}: {}<br>{}: {}'
            data['text'] = data.apply(lambda df: tp.format(
                xName, df[x], yName, df[y]), axis=1)
        else:
            tp = '{}: {}<br>{}: {}<br>{}: {}'
            data['text'] = data.apply(lambda df: tp.format(xName, df[x], yName, df[y], sizeName,
                                                           df[size]), axis=1)
        if size is not None:
            data['size'] = log(data[size]) * 100
        if color is not None:
            if data[color].dtype == 'O':
                groupby = True
                data = sort_df_dimension(data, color, reverse=True)
                data['color'] = data[color]
                colors = colorway[:(data[color].nunique())]
                if trendline is True:
                    colors = [y for x in colors for y in [x] * 2]
            else:
                data['color'] = (data[color] - data[color].min()) / \
                    (data[color].max() - data[color].min())
        if groupby is True:
            showscale=False
        fig = scatter(
            data,
            x=x,
            y=y,
            color='color' if color is not None else None,
            size='size' if size is not None else None,
            color_continuous_scale='viridis_r',
            trendline='ols' if trendline is True else None,
            custom_data=['text']
        )
        self.update_layout(template=template, margin=margin, autosize=True)
        for i in range(len(fig.data)):
            fig_data = fig.data[i]
            fig_marker = fig_data.marker
            fig_data.marker = dict(
                color=fig_marker.color if groupby is False else colors[i],
                colorscale='Viridis_r',
                size=fig_marker.size,
                sizemode=fig_marker.sizemode,
                sizeref=fig_marker.sizeref,
                symbol='circle',
                showscale=showscale
            )
            self.add_trace(fig_data)
        if width is not None:
            self.update_layout(width=width)
        if height is not None:
            self.update_layout(height=height)
        # self.update_traces(hovertemplate='%{customdata[0]}')
        for i in range(len(self.data)):
            if self.data[i].mode == 'markers':
                self.data[i].hovertemplate='%{customdata[0]}'
        if xaxisTitle is not None:
            self.update_xaxes(title=xaxisTitle)
        if yaxisTitle is not None:
            self.update_yaxes(title=yaxisTitle)
        if title is not None:
            self.update_layout(title={'text': title, 'xanchor': 'center',
                                      'yanchor': 'top', 'x': 0.45 if color is not None and showscale is True else 0.5},
                               margin={'l': 20, 'r': 10,
                                       't': 35, 'b': 10, 'pad': 5},
                               title_font_family='sans-serif',
                               title_font_size=15,
                               )

    def graph(self, config=chart_config, className=None):
        return Graph(figure=self, config=chart_config, className=className)
    @property
    def olsLines(self):
        olsLines = []
        for i in range(len(self.data)):
            if self.data[i].mode == 'lines':
                try:
                    olsLine = self.data[i].hovertemplate
                    olsLine = olsLine.split('</b><br>')[1].split('<br><br>')[0]
                    r2 = olsLine.split('<br>R<sup>2</sup>')[1]
                    olsLine = olsLine.split('<br>R<sup>2</sup>')[0] + ', R'
                    olsLine = Li([olsLine.upper(), Sup('2'), r2.replace('=', ' = ')])
                    olsLines.append(olsLine)
                except:
                    pass
        olsLines = Ul(olsLines)
        return olsLines
