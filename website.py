
from dash import Dash, html, dcc,Input,Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import re

app = Dash(__name__)

# we will use the df we have filtered out from the graph ipynb
main_df = pd.read_csv('main_df.csv')
time_df = pd.read_csv('time_df.csv')
# since csv folders do not have a datetime dtype => need to convert it here into dtype for the main_df
# converting time df back into the original set whereby time is the index
temp_df = pd.DataFrame({'time': pd.to_datetime(time_df['time']),
                        'total_lots': time_df['total_lots'],
                        'lots_avail': time_df['lots_avail'],
                        'lots_taken': time_df['lots_taken']})

time_df = temp_df.set_index('time')

def time_day_locater(day,start_time,end_time): # to find the time
    day = time_df.loc[day]
    time = day.between_time(start_time,end_time) # it uses the time df
    return time
def day_locater(day): # to find the day
    # it just uses a normal indexed df with time as one of the columns
    day = main_df.loc[main_df['time'].str.contains(day,flags = re.I,regex = True)]
    return day
#filter that filters  out the dataframe
def final_filter(selected_df): 
    if len(selected_df.index) > 1:
        return selected_df.iloc[-1]
    elif len(selected_df.index) == 0:
        print("error, no values found within this time frame")
    
    else:
        return selected_df.iloc[0]

def bar_producer(day): # produces the bar graph
    fig = px.bar(day_locater(day), x ="time",
                 y = "lots_taken",
                 color = "lots_taken",
                 color_continuous_scale = "bluyl",
                labels = {"lots_taken": "Lots Taken",
                         "time": "Time" },)
    fig.add_hrect(y0=0,y1 = 74, line_width = 0, fillcolor = "green", opacity = 0.2)
    fig.add_hrect(y0 = 74, y1 = 95, line_width = 0, fillcolor = "yellow",opacity = 0.2,annotation_text = "70% Capacity") # opacity levels
    fig.add_hrect(y0 = 95, y1 = 105, line_width = 0, fillcolor = "red", opacity = 0.2, annotation_text = "90% Capacity") # opacity levels
    fig2 = px.line(day_locater(day),x = "time" , y = "lots_taken")
    fig2.update_traces(line_color = 'green') # color traces!
    fig.add_trace(fig2.data[0])
    fig.update_layout(
        font = dict(
            family = "Courier New, monospace"
        ),
        title = {
            'text': f'Date: {day}',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        yaxis_range = [0,105]
    )
    return fig

def pie_producer(day,start_time,end_time):
    given_df = time_day_locater(day,start_time,end_time) #function that filters specific val (on top)
    frame_converter = final_filter(given_df)[1:].to_list() #converts into the row that we are going to plot
    indv_df = pd.DataFrame({"test":frame_converter,"names": ["Lots Available", "Lots Taken"]}) # segments into a new df

    fig = px.pie(indv_df,values = "test", # real plotting
            names = "names",
            hole = .3,
            color_discrete_sequence = px.colors.sequential.Blugrn,
            hover_data = ['names'],)
    fig.update_traces(
        textposition = 'inside',
        textinfo = 'percent+label',
    )
    fig.update_layout(
        font = dict(
            family = "Courier New, Courier, monospace"
        ),
        title = {
            'text': f'Lots from {start_time} to {end_time}',
            'y': 0.9,
            'x': 0.5,
            'yanchor': 'top'
        }
    )
    return fig

#getting all the unique dates from then csv that we have made
#this dashboard should be working!

# the time_list that we will be producing
time_List = ['00:00:00',
 '01:00:00',
 '02:00:00',
 '03:00:00',
 '04:00:00',
 '05:00:00',
 '06:00:00',
 '07:00:00',
 '08:00:00',
 '09:00:00',
 '10:00:00',
 '11:00:00',
 '12:00:00',
 '13:00:00',
 '14:00:00',
 '15:00:00',
 '16:00:00',
 '17:00:00',
 '18:00:00',
 '19:00:00',
 '20:00:00',
 '21:00:00',
 '22:00:00',
 '23:00:00']

time_column = pd.to_datetime(main_df["time"])
test = time_column.dt.normalize() 
dates = test.astype(str).unique().tolist()


#the real app layout
app.layout = html.Div(children=[
    html.Div([
        html.H1(id = "name"),
        html.Img(src = 'assets/logo.png'),
        html.P("A dashboard that utilises PeekingDuck to monitor parking lots", id = "paragraph"), # needs to be passed in an assets folder for it to work!
        html.Label("Select Day", id = "day"),
        dcc.Dropdown(dates,value ='2022-03-10',
        id = 'date_dropdown'),
        html.Label("Start Time", id = "time_start"),
        dcc.Dropdown(time_List,value = '00:00:00',id = 'pietime_start'),
        html.Label("End Time", id = "time_end"),
        dcc.Dropdown(time_List, value = '10:00:00', id = 'pietime_end'),
        html.Br(),
        html.Div([
            html.Label("About:",id = 'legend-label'),
            html.P("ParkingVision is a concept which hopes to cut down costs of traditional surveilience by leveraging the use of the peekingduck pipeline.",id = "about_info")
            ]
        ),
        html.Br()], id = 'left-container'),
    html.Div([
        html.Div([
            html.Iframe(src = "https://www.youtube.com/embed/O91ugk_N1pY",
        style={"height": "470px", "width": "65%"}, id = 'video_frame'),
        dcc.Graph(id = 'pie_chart')
        ], id = 'video-container')
        ,
        html.Div([
            dcc.Graph(
        id='example-graph')
        ], id = 'graph-container') 
    ], id = 'right-container')
])

@app.callback(
    Output('example-graph','figure'), # links back to output
    Input(component_id = 'date_dropdown', component_property = 'value') #links to dcc dropdown
)
def update_output(value): #links to the bar date
    figure_test = go.Figure(data = bar_producer(value))
    return figure_test

@app.callback(
    Output("pie_chart","figure"),
    Input("date_dropdown","value"),
    Input("pietime_start","value"),
    Input("pietime_end","value")
)

def pie_generator(date_dropdown,pietime_start,pietime_end):
    figure = go.Figure(data = pie_producer(date_dropdown,pietime_start,pietime_end))
    return figure
if __name__ == '__main__':
    app.run_server(debug=True)