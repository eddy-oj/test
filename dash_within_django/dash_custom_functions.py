import dash_html_components as html

import os
import pandas as pd



def makeDashHTMLTable(df, verbose_col_names, tableClass='ey-table'):
    '''Description: Creates an html table for use in Dash. The function indicates whether a datatype is categorical
                    or numerical, consequently assigning a class to that html component which can be styled by class
                    (e.g. left aligned for categorical and center for numeric)'''
    # get data types of df:
    data_types_dict = df.dtypes.to_dict()

    html_table = []

    # create table headers
    html_row = []
    for col in df.columns:
        if data_types_dict[col] == object:
            className = 'categoricalTableCell'
        else:
            className = 'numericalTableCell'
        html_row.append(html.Th(verbose_col_names[col], className=className))
    html_table.append(html.Tr(html_row))

    # create the table cells
    for index, row in df.iterrows():
        html_row= []
        for col in df.columns:
            # look up the data type in the data_types_dict, which will be used to style the table
            if data_types_dict[col] == object:
                className = 'categoricalTableCell'
            else: # assume it is
                className = 'numericalTableCell'
            html_row.append(html.Td(row[col], className=className))
        html_table.append(html.Tr(html_row))

    return html.Table(html_table, className=tableClass)

def makeBootStrapTable(df, verbose_col_names, tableClass='table table-hover'):

    '''Description: Creates an html table for use in Dash. The function indicates whether a datatype is categorical
                    or numerical, consequently assigning a class to that html component which can be styled by class
                    (e.g. left aligned for categorical and center for numeric)'''

    # get data types of df:
    data_types_dict = df.dtypes.to_dict()

    html_table = []

    # create table headers
    html_row = []

    for col in df.columns:
        if data_types_dict[col] == object:
            className = 'categoricalTableCell'
        else:
            className = 'numericalTableCell'

        html_row.append(html.Th(verbose_col_names[col], className=className))
    html_table.append(html.Thead(html_row))

    # create the table cells
    html_body = []
    for index, row in df.iterrows():
        html_row= []
        for col in df.columns:
            # look up the data type in the data_types_dict, which will be used to style the table
            if data_types_dict[col] == object:
                className = 'categoricalTableCell'
            else: # assume it is
                className = 'numericalTableCell'
            html_row.append(html.Td(row[col], className=className))
        html_body.append(html.Tr(html_row))

    html_table.append(html.Tbody(html_body))

    Dash_table = html.Table(html_table, className=tableClass)

    return Dash_table

def wrap_bootstrap_table(DashTable, title='Table Summary', subtitle='Hover mouse to highlight row'):

    wrapper = html.Div(className='Dash-table-container',
                       children=[html.Div(className='x_panel',
                                          children=[html.Div(className='x_title',
                                                             children=[html.H2(children=[title, html.Small(subtitle),
                                                                                        ]),
                                                                       html.Div(className='clearfix'),
                                                                      ]), # end of x_title
                                                    html.Div(className='x_content',
                                                             children=[DashTable]) # end of x_content
                                                   ]), # end of x_panel
                               ])
    return wrapper

def currency_formatter(value):

    # convert to millions:
    if len(str(value).split('.')[0]) > 6:
        value = str(value / 1000000)
        #print("printing new value: %s" %(value))
        suffix = 'm'
        decimal_places = 2

    # convert to thousands:
    elif len(str(value).split('.')[0]) > 4:
        value = str(value / 1000)
        suffix = 'k'
        decimal_places = 0

    # leave alone:
    else:
        value = str(value)
        suffix =''
        decimal_places = 0

    # further formatting
    splitted_val = value.split('.')
    integer = splitted_val[0]

    if len(splitted_val) > 1:
        if decimal_places > 0:
            decimals = splitted_val[1][:2]
            number = integer + '.' + decimals

        else:
            number = integer
    else:
        number = integer

    value = "£" + number + suffix

    return value


def loadDemoData(filePath, encoding='utf-8'):

    # load data - temporarily for TAAF demo:
    # read current directory and load summary table:
    cwd = os.getcwd()
    print("The current working directory: %s" %(cwd))
    cwd = cwd+'/dash_within_django/static/dash_within_django/data/'
    df = pd.read_csv(cwd + filePath, encoding=encoding)

    return df
