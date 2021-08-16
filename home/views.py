from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
# Create your views here.

def home(requests):
    # def scatter():
    #     return None
    #
    # context = {
    #     'simpleGraph': scatter()
    # }

    return render(requests, 'home/welcome.html')
