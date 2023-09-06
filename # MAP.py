# MAP
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
import plotly.express as px

data = pd.read_csv("C:\\Users\\ETI\\Downloads\\Country_clean (1).csv")
df = data.fillna(value=0)

a = list(df["Latitude of Capital"])
b = list(df["Longitude of Capital"])

for i in range(len(a)):
    if a[i]=="unknown":
        a[i]=0.52
    else:
        x = a[i].replace(" ",".")
        s = x.replace(x[-1],'')
        a[i]=float(s[:len(s)-1])

for i in range(len(b)):
    if b[i]=="unknown":
        b[i]=166.9
    else:
        y = b[i].replace(" ",".")
        t = y.replace(y[-1],'')
        b[i]=float(t[:len(t)-1])


lat = st.selectbox(
    'Which latitude?',
     a)

long = st.selectbox(
    'Which longitude?',
     b)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [lat, long],
    columns=['lat', 'lon'])

st.map(map_data)