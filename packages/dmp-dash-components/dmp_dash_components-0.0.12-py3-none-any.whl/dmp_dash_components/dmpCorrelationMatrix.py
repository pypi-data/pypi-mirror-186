from plotly.graph_objects import Figure
from scipy.stats import pearsonr, spearmanr, kendalltau
from plotly.figure_factory import create_annotated_heatmap
from .plotFuncs import *
from .plotlyTemplate import *
from dash.dcc import Graph
import numpy as np

class dmpCorrelationMatrix(Figure):
    def __init__(
            self,
            data=None,
            columns=[],
            method='pearson', #{‘pearson’, ‘kendall’, ‘spearman’}
            template='plotly_white+dmp',
            margin={'l': 20, 'r': 10, 't': 10, 'b': 10, 'pad': 0},
            width=None,
            height=300,
            title=None,
            *args,
            **kwargs):
        Figure.__init__(self, *args, **kwargs)
        if len(columns) > 0:
            data = data[columns]
        df_corr = data.corr(method=method).round(2)
        x, y = list(df_corr.columns), list(df_corr.index)
        z = np.array(df_corr)
        if method == 'pearson':
            pval = data.corr(method=lambda x, y: pearsonr(x, y)[1]) - np.eye(*df_corr.shape)
        if method == 'spearman':
            pval = data.corr(method=lambda x, y: spearmanr(x, y)[1]) - np.eye(*df_corr.shape)
        if method == 'kendall':
            pval = data.corr(method=lambda x, y: kendalltau(x, y)[1]) - np.eye(*df_corr.shape)
        p = pval.applymap(lambda x: ''.join(['*' for t in [.05, .01] if x<=t]))
        df_corr = df_corr.astype(str) + p
        zp = np.array(df_corr)
        fig = create_annotated_heatmap(
            z,
            x = x,
            y = y ,
            annotation_text = zp,
            hoverinfo='z',
            colorscale='purples',
            showscale=True
            )
        self.add_trace(fig.data[0])
        self.layout.annotations = fig.layout.annotations
        self.update_layout(template=template, margin=margin, autosize=True)
        if width is not None:
            self.update_layout(width=width)
        if height is not None:
            self.update_layout(height=height)
        if title is not None:
            self.update_layout(title={'text': title+'<br><br>', 'xanchor': 'center',
                                      'yanchor': 'top', 'x':0.5},
                               margin={'l': 20, 'r': 10,
                                       't': 30, 'b': 10, 'pad': 0},
                               title_font_family='sans-serif',
                               title_font_size=15,
                               )
    def graph(self, config=chart_config, className=None):
        return Graph(figure=self, config=chart_config, className=className)
