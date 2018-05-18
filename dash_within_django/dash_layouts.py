from random import randint
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from .dash_custom_functions import *

from .models import Author
from django.shortcuts import get_object_or_404


def dashboard_example1(pathname):
    ''' '''

    # *** LINE AREA PLOT ***#
    trace1 = go.Scatter(
        x=[1, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0],
        y=[0, 1.3, 2.0, 3.0, 3.5, 4.5, 5.0, 3.5, 3.8, 3.5, 2.6, 2.4, 2.2, 2.8, 3.2, 3.5],
        fillcolor='rgba(127, 209, 214, 1.0)',
        fill='tonexty',
        mode= 'none'
    )

    data = [trace1]

    layout = dict(title='',
              yaxis = dict(zeroline = False),
              xaxis = dict(zeroline = False),
              margin=dict(t=10, b=50, l=20, r=10),
             )


    fig = dict(data=data, layout=layout)
    line_graph = dcc.Graph(id='line-area-graph', figure=fig, style={'display':'inline-block', 'width':'100%',
                                                                    'height': '100%;'} )

    # *** END OF LINE AREA PLOT ***#

    # *** TABLE  ***#
    df = pd.DataFrame(data={'id': [1,2,3,4,5], 'First Name': ['Joe', 'Jane', 'John', 'Julia', 'Jason'],
                            'Last Name': ['Alela', 'Bella', 'Cellar', 'Dollar', 'Ever'],
                            'data':[1,2,3,4,5]})

    Dash_table = makeBootStrapTable(df, dict(zip(df.columns, df.columns)))
    bootstrap_table = wrap_bootstrap_table(Dash_table, title='Table Summary', subtitle='Hover mouse to highlight row')
    # *** END OF TABLE  ***#


    # *** CHOROPLETH ***#
    df = loadDemoData('2014_world_gdp_with_codes.csv', encoding='latin-1')

    data = [ dict(
            type = 'choropleth',
            locations = df['CODE'],
            z = df['GDP (BILLIONS)'],
            text = df['COUNTRY'],
            # colorscale = [[0,"rgb(249, 207, 207)"],[0.5,"rgb(249, 174, 174)"],
            #                       [1,"rgb(255, 119, 119)"]],
            colorscale = [[0,"rgb(234, 253, 255)"],[0.3,"rgb(191, 239, 242)"],\
                [0.6,"rgb(153, 227, 232)"],[0.7,"rgb(127, 209, 214)"],[1,"rgb(79, 192, 198)"]],
            autocolorscale = False,
            #reversescale = True,
            marker = dict(
                line = dict (
                    color = 'rgb(180,180,180)',
                    width = 0.5
                ) ),
            colorbar = dict(
                autotick = False,
                tickprefix = '$',
                title = 'GDP<br>Billions US$'),
          ) ]

    layout = dict(
                    #title = '',
                    geo = dict(
                                showframe = False,
                                showcountries=True,
                                showcoastlines = True,
                                #scope='europe',
                                #height=800,
                                        margin=go.Margin(
                                                            l=0,
                                                            r=0,
                                                            b=0,
                                                            t=0,
                                                            pad=0
                                                        ),
                                projection = dict(
                                    type = 'Mercator'
                                                 )
                               ),
                    margin=dict(t=0, b=0, l=0, r=0),

                )

    fig = dict(data=data, layout=layout)
    world_map = dcc.Graph(id='target_results', figure=fig, style={'display':'inline-block', 'width':'100%', 'height': '250px'})
    print(world_map)

    # *** END OF CHOROPLETH ***#


    page_layout =  html.Div(className="dash_layout",
                            children=[
                                      #<!-- top tiles -->
                                      html.Div(className="row tile_count",
                                               children=[html.Div(className="col-md-3 col-sm-3 col-xs-6 tile_stats_count",
                                                                  children=[html.Span(className="count_top",
                                                                                      children=[html.I(className="fa fa-user"),
                                                                                                'Total Users',
                                                                                               ]), # end of Span

                                                                            html.Div(className="count", children=[2500]),
                                                                            html.Span(className="count_bottom",
                                                                                      children=[html.I(className="green", children=['4%']),
                                                                                                'From last Week']),
                                                                            ]), # end of tile_stats_count div

                                                        html.Div(className="col-md-3 col-sm-3 col-xs-6 tile_stats_count",
                                                                           children=[html.Span(className="count_top",
                                                                                               children=[html.I(className="fa fa-user"),
                                                                                                         'Total Users',
                                                                                                        ]), # end of Span

                                                                                     html.Div(className="count", children=[2500]),
                                                                                     html.Span(className="count_bottom",
                                                                                               children=[html.I(className="green", children=['4%']),
                                                                                                         'From last Week']),
                                                                                     ]), # end of tile_stats_count div

                                                        html.Div(className="col-md-3 col-sm-3 col-xs-6 tile_stats_count",
                                                                           children=[html.Span(className="count_top",
                                                                                               children=[html.I(className="fa fa-user"),
                                                                                                         'Total Users',
                                                                                                        ]), # end of Span

                                                                                     html.Div(className="count", children=[2500]),
                                                                                     html.Span(className="count_bottom",
                                                                                               children=[html.I(className="green", children=['4%']),
                                                                                                         'From last Week']),
                                                                                     ]), # end of tile_stats_count div

                                                        html.Div(className="col-md-3 col-sm-3 col-xs-6 tile_stats_count",
                                                                           children=[html.Span(className="count_top",
                                                                                               children=[html.I(className="fa fa-user"),
                                                                                                         'Total Users',
                                                                                                        ]), # end of Span

                                                                                     html.Div(className="count", children=[2500]),
                                                                                     html.Span(className="count_bottom",
                                                                                               children=[html.I(className="green", children=['4%']),
                                                                                                         'From last Week']),
                                                                                     ]), # end of tile_stats_count div
                                                        ]), # end of row tile_count

                                      html.Div(className='col-md-12 col-sm-12 col-xs-12',
                                               children=[html.Div(className="dashboard_graph",
                                                                  children=[html.Div(className="row x_title",
                                                                                     children=[html.Div(className="col-md-6",
                                                                                                        children=[html.H3(children=['Activity Monitor  ',
                                                                                                                                    html.Small('Summarizing activity for this period')
                                                                                                                                    ]),

                                                                                                        ]),
                                                                                               ]),
                                                                          html.Div(style={'width':'100%', 'margin-bottom':'20px'},
                                                                                   children=[html.Div(id="chart_plot_01", className="row-container",
                                                                                                      children=[html.Div(className='col-md-6 col-sm-6 col-xs-12',
                                                                                                                         id='col_one',
                                                                                                                         children=[line_graph]),
                                                                                                                html.Div(className='col-md-6 col-sm-6 col-xs-12',
                                                                                                                         id="col_two",
                                                                                                                         children=[bootstrap_table]),
                                                                                                               ]),

                                                                                            ]),

                                                                   ]), # END OF DASHBOARD-GRAPH
                                                         ]), #  end of dashboard-graph container

                                                         html.Div(className='col-md-12 col-sm-12 col-xs-12',
                                                                  children=[html.Div(className="dashboard_graph",
                                                                                     children=[html.Div(className="row x_title",
                                                                                                        children=[html.Div(className="col-md-6",
                                                                                                                           children=[html.H3(children=['Risk Map  ',
                                                                                                                                                       html.Small('Summarizing risk on a global scale')
                                                                                                                                                       ]),

                                                                                                                           ]),
                                                                                                                  ]),
                                                                                             html.Div(style={'width':'100%'},
                                                                                                      children=[html.Div(id="chart_plot_01", className="row-container",
                                                                                                                         children=[html.Div(className='col-md-6 col-sm-6 col-xs-12',
                                                                                                                                            style={'width':'48%', 'display':'inline-block'},
                                                                                                                                            children=[world_map]),
                                                                                                                                 html.Div(className='col-md-6 col-sm-6 col-xs-12',
                                                                                                                                          style={'width':'48%', 'display':'inline-block'},
                                                                                                                                          id="col_two",
                                                                                                                                          children=[bootstrap_table]),

                                                                                                                                  ]),

                                                                                                               ]),

                                                                                      ]), # END OF DASHBOARD-GRAPH
                                                                            ]), #  end of dashboard-graph container

                                ]), # end of 'right_col'

                    # html.Div(children=[message, html.Div(children=[dcc.Dropdown(id='dropdown', className='dropdown',
                    #                                                             options=[{'label': i, 'value': i} for i in ['option1', 'option2', 'option3']],
                    #                                                             value='option1',
                    #                                                              ),
                    #                                             ]), # end of dropdown div
                    #                   graph,]), # end of page_layout_div

    return page_layout


def someotherpage(pathname):
    ''' '''
    return html.P('hello world! I am "someotherpage"')
