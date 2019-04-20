# # import plotly
# import cufflinks as cf
#
# cf.datagen.lines(5).resample('M').iplot(kind='bar', xTitle='Dates',
#                                         yTitle='Return',
#                                         title='Cufflinks - Bar Chart')
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

py.sign_in('SofiaPetryshyn', 'A5zjy19FoSbB3cZ3dZgm')


def company_middle_plot(x, y, ticker):
    '''
        Function to visualize plot of stock of company

        :param df: pandas DataFrame
        :return: None
        '''
    trace_close = go.Scatter(
        x=x,
        y=y,
        name="close",
        line=dict(color='#17BECF'),
        opacity=0.8
    )

    data = [trace_close]

    layout = dict(
        title='Time Series of ' + ticker,
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1m',
                         step='month',
                         stepmode='backward'),
                    dict(count=6,
                         label='6m',
                         step='month',
                         stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type='date'
        )
    )

    fig = dict(data=data, layout=layout)
    py.plot(fig, filename="Time Series with Rangeslider")
