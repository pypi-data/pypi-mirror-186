import plotly.io as pio
import plotly.graph_objects as go

colorway = ['#6366f1', '#f52080', '#a056f3', '#ff7075', '#fcce25', '#1ac7c2',
            '#48a7f0', '#fc8b4e', '#7ca7eb', '#f768a1', '#ee204d', '#1f75fe',
            '#fce883', '#b5674d', '#ff7538', '#1cac78', '#926eae',  '#c0448f',
            '#ff5349', '#c5e384', '#7366bd', '#ffb653', '#199ebd', '#ededed',
            '#fdd9b5', '#5d76cd', '#1dacd6', '#95918c', '#ffcfab', '#80daeb',
            '#faa76c', '#dbd7d2', '#bab86c', '#9d81ba', '#ff9baa', '#a8e4a0',
            '#ef98aa', '#cd4a4a', '#9aceeb', '#f664af', '#c0448f', '#fc89ac',
            '#e7c697', '#77dde7', '#8e4584', '#cb4154', '#cdc5c2', '#c8385a',
            '#17806d', '#158078', '#fdfc74', '#1974d2', '#ff48d0', '#dd9475',
            '#ca3767', '#45cea2', '#7851a9', '#fc74fd', '#de5d83', '#efdbc5',
            '#414a4c', '#cc6666', '#7442c8', '#cd9575', '#71bc78', '#9f8170',
            '#e90067', '#e6335f', '#fd7c6e', '#FA9C44', '#FFDB00', '#fed8b1',
            '#ff7a00']


pio.templates['dmp'] = go.layout.Template(
    layout=go.Layout(
        colorway=colorway,
        font={'color': '#252525'},
        uniformtext_minsize=11,
        uniformtext_mode='hide',
        autosize=True,
        xaxis={
            'title_font': {"size": 11},
            'automargin': True
        },
        yaxis={
            'ticksuffix': ' ',
            'title_font': {"size": 11},
            'automargin': True
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
)

chart_config = {
    'displayModeBar': False,
    'responsive': True,
    'doubleClick': False,
    'scrollZoom': False,
    'staticPlot': False,
    'modeBarButtonsToRemove': ['zoom', 'pan']
    }
