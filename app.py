import streamlit as st

st.write("てすと")

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

import plotly.graph_objects as go
from PIL import Image

st.title("wwwwww")
st.caption("なぁにこれぇ")
st.write("markdownも使える")

answer = st.button('Say hello')

if answer == True:
     st.write('Why hello there')
else:
     st.write('Goodbye')
    
data = {
    'lat': np.random.randn(100) / 100 + 35.68,
    'lon': np.random.randn(100) / 100 + 139.75,
}
map_data = pd.DataFrame(data)
# 地図に散布図を描く
st.map(map_data)


animals = ['giraffes', 'orangutans', 'monkeys','???','null']
populations = [20, 14, 23,54,-1]

fig = go.Figure(data=[go.Bar(x=animals, y=populations)])

fig.update_layout(
    xaxis = dict(
        tickangle = 0,
        title_text = "Animal",
        title_font = {"size": 20},
        title_standoff = 25),
    yaxis = dict(
        title_text = "Populations",
        title_standoff = 25),
    title ='Title')

# streatlimで表示するために
st.plotly_chart(fig, use_container_width=True)

code='''

st.plotly_chart(fig, use_container_width=True)
'''

st.code(code,language="Python")

img=Image.open("images/dog.jpg")
st.image(img, width=400)
