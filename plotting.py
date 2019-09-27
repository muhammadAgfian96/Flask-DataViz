import plotly
import plotly.graph_objects as go
import plotly.express as px
import json
import preprocessing



def plot_hist_mpg():
    df = preprocessing.all_data()
    fig = px.histogram(df, x="mpg", marginal="rug", hover_data=df.columns)

    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def plot_hist_hp():
    df = preprocessing.all_data()
    fig = px.histogram(df, x="horsepower", marginal="rug", hover_data=df.columns)
    
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json