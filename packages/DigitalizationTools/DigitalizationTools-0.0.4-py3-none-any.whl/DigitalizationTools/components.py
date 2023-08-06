import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
from typing import Optional, Union

card_style = {'width':"100%", 'textAlign':'center'}

menu_font1 = {"color":"#FFFFFF", "fontWeight":"bold", 'font-size':'20px'}
menu_font2 = {"color":"#FFFFFF", 'font-size':'16px'}

card_title = {"color":"#080808", "fontWeight":"bold", 'font-size':'20px'}

left_column_style = {'margin-left': '0.0em','margin-right': '0.0em',}

notification_style = {"position": "fixed", "top": 30, "right": 10, "width": 350}

html_section_style = {"color":"#110ecc", 'textAlign':'center', "fontWeight":"bold", 
                    'font-size':'20px', 'margin-top': '1em', 'margin-bottom': '1em'}

input_style  = {'width':"100%", 'textAlign':'center'}

button_style0 = {'width':'100%', 'margin-bottom': '0.5em', 
                 'margin-top': '0.5em'}
radio_style = {'width':'100%', 'textAlign':'right', 'margin-top':'8px'}

dbc_color = {"blue": "primary", "grey": "secondary", "green": "success", "orange": "warning", 
            "red": "danger", "light blue": "info", "white": "light", "black": "dark"}

def button(buttonName:str, buttonID:str, color:str):
    botton_layout = dbc.Row(
                        children=[
                            dbc.Col(
                                dbc.Button(
                                    buttonName, 
                                    id=buttonID, 
                                    n_clicks=0, 
                                    color=color, 
                                    style=button_style0
                                ), 
                            width=12),
                        ], 
                    style=left_column_style)
    return botton_layout



def label_input_text(labelName:str, labelWidth:int, inputWidth:int, inputID:str,
                    defaultInputValue:Optional[str]=None):
    return dbc.Row(children=[
            dbc.Label(labelName, width=labelWidth),
            dbc.Col(
                dcc.Input(
                    type="text", 
                    id=inputID, 
                    value=defaultInputValue, 
                    style=card_style
                ), 
            width=inputWidth)
        ], style=left_column_style)



def label_input_number(labelName:str, labelWidth:int, inputWidth:int, inputID:str,
                    miniValue:Optional[Union[float, int]]=None, 
                    maxValue:Optional[Union[float, int]]=None,
                    stepValue:Optional[Union[float, int]]=None,
                    defaultInputValue:Optional[Union[float, int]]=None):
    return dbc.Row(children=[
            dbc.Label(labelName, width=labelWidth),
            dbc.Col(
                dcc.Input(
                    type="number", 
                    id=inputID, 
                    value=defaultInputValue,
                    min=miniValue,
                    max=maxValue,
                    step=stepValue,
                    style=card_style
                ), 
            width=inputWidth)
        ], style=left_column_style)


def label_Textarea(labelName:str, inputID:str, defaultInputValue:Optional[str]=None):

    layout = dbc.Row(children=[
                dbc.Label(labelName, width=12),
                dbc.Col(dbc.Textarea(id=inputID), width=12, ),
            ], style=left_column_style)
    return layout




def card(cardHeader: str, content: list ):
    content_layout = []
    for i in content:
        content_layout.append(i)
    return dbc.Card([
                dbc.CardHeader(cardHeader, 
                    style={'font-weight': 'bold', 
                    'font-size':'20px'}),
                dbc.CardBody(content_layout),
            ], )



def table(columnName:list, columnType:list, tableID:str, editable:bool,
        row_deletable:bool, row_selectable:str, tableHeight:Optional[str]="400px", 
        dropdownContent:Optional[dict]={}):
    '''
    columnType: text, numeric
    dropdownContent = {'column name': [list of items]}
    '''
    # check if dropdown key in columnName
    if dropdownContent == {}:
        dropdown = {}
        columns = []
        for i in range(len(columnName)):
            columns.append({'id':columnName[i],'name':columnName[i], 'type': columnType[i]})
    else:
        dropdownKeys = list(dropdownContent.keys())
        
        for i in range(len(dropdownKeys)):
            if dropdownKeys[i] not in columnName:
                return "dropdown colume name is not defined correctly."
        
        dropdown = {}
        for i in range(len(dropdownKeys)):
            dropdown[dropdownKeys[i]] = {'options': [{'label': i, 'value': i} for i in set(dropdownContent[dropdownKeys[i]])]}
        
        columns = []
        for i in range(len(columnName)):
            for j in range(len(dropdownKeys)):
                if dropdownKeys[j] == columnName[i]:
                    columns.append({'id':columnName[i],'name':columnName[i], 'type': columnType[i], 'presentation': 'dropdown'})
                else:
                    columns.append({'id':columnName[i],'name':columnName[i], 'type': columnType[i]})

    columns.append({'id':'id','name':'id', 'type': 'text'})
    
    table_layout =  dash_table.DataTable(
                        id=tableID,
                        data= [],
                        sort_action='native',
                        filter_action='native',
                        editable=editable,
                        row_deletable=row_deletable,
                        row_selectable=row_selectable,
                        columns=columns,
                        fixed_rows={'headers': True},
                        style_cell_conditional=[
                            # {'if': {'column_id': 'time'}, 'width': '50%', 'textAlign': 'center', 'textOverflow': 'ellipsis',},
                            # {'if': {'column_id': 'lod'},'width': '50%', 'textAlign': 'center'},
                            {'if':{'column_id': 'id',},'display':'None',},
                        ],
                        style_data_conditional=[
                            {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'},
                            {'if':{'column_id': 'id',},'display':'None',},
                        ],
                        style_header_conditional=[
                            {'if':{'column_id': 'id',},'display':'None',},
                        ],
                        style_header={
                            'backgroundColor': 'rgb(230, 230, 230)',
                            'fontWeight': 'bold'
                        },
                        style_cell={
                            'font-size': '13px',
                        },
                        style_table={
                            'overflowY': 'auto',
                            'overflowX': 'auto',
                            'margin-top': '0.5em',
                            'padding-bottom': '0.5em',
                            'height': tableHeight
                        },
                        css=[{"selector":".dropdown", "rule": "position: static"}],
                        dropdown=dropdown,
                    )
                  
    return table_layout


def dropdownMenu(dropdownName:str, dropdownID:str, labelWidth:int, dropdownWidth:int,
                options:Optional[list]=[]):
    dropdown_layout = dbc.Row(children=[
                            dbc.Label(dropdownName, width=labelWidth),
                            dbc.Col(dcc.Dropdown(id=dropdownID, options=options, value=None, 
                                    optionHeight=50, style=card_style), width=dropdownWidth),
                        ], style=left_column_style)
    return dropdown_layout


def upload(uploadID:str):
    upload_field = dbc.Row(children=[
                    dcc.Upload(id=uploadID,
                        children=html.Div(['Drag and drop or select a ',
                                            html.A('file')]),
                        style={'width': '100%',
                                'height': '60px',
                                'lineHeight': '60px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin': '1px',
                                'margin-bottom': '15px', },
                        multiple=False, )
                    ], style=left_column_style)
    
    return upload_field


def notification(noticeText:str, headerText:str, iconType:str, duration:int, dismissable:bool):
    notice = dbc.Toast(noticeText, header=headerText, icon=iconType, duration=duration, dismissable=dismissable, style=notification_style,)
    return notice


def spinner(htmlID:str):
    spinner_layout = dbc.Row(children=[
                        dbc.Spinner(html.Div(id=htmlID))
                    ], style=left_column_style)
    return spinner_layout


def multi_tabs(tabLayout:list, labelList:list):
    tabs = [dcc.Tab(tabLayout[i], label=labelList[i]) for i in range(len(labelList))]
    layout = html.Div([dcc.Tabs(tabs)])
    return layout

def radio_select(radioLabel:str, radioID:str, radioItemsLabel:list, radioItemsValue:list,  labelWidth:int, radioWidth:int):
    options = []
    for i in range(len(radioItemsValue)):
        options.append({'label': radioItemsLabel[i], 'value': radioItemsValue[i]})

    layout = dbc.Row(children=[
                dbc.Label(radioLabel, width=labelWidth),
                dbc.Col(dbc.RadioItems(
                            options=options,
                            value=radioItemsValue[0],
                            id=radioID,
                            labelCheckedStyle={
                                'color': 'green',
                                'width': '100%'
                            },
                            inline=True,
                            style=radio_style,
                            ), width=radioWidth,),
            ], style=left_column_style)
    return layout


def insert_image(app, imgLocation:str, height:int):
    layout  =   dbc.Row(
                    children=[
                        html.Img(
                            src=app.get_asset_url(imgLocation), 
                            style={'height': f'{height}px', 'object-fit': 'scale-down', 'Align': 'center'}),
                    ]
                )
    return layout