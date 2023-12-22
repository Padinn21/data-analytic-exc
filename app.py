import numpy as np
import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt 
import plotly.express as px

df_day = pd.read_csv('day.csv')

st.title('Dashboard From Bike-Sharing Dataset')

col1, col2 = st.columns(2)
with col1:
    total_cas = df_day['casual'].sum()
    st.metric('Total Casual Customer', value=total_cas)

with col2:
    total_reg = df_day['registered'].sum()
    st.metric('Total Registered Customer', value=total_reg)

month = df_day['mnth'].value_counts()
fig = px.bar(df_day, 
             x =month.index, 
             y =month.values,
             color =month.index,
             title = 'Total bike rental by month',
             text_auto = '.2s',
             width = 750,
             height = 500)

fig.update_layout(
    xaxis_title = 'month',
    yaxis_title = 'Values',
    title_x= 0.35,
    showlegend = True)

fig.update_traces(
    textposition='outside')

st.plotly_chart(fig)

col3, col4 = st.columns(2)
with col3:
    weekend = df_day['workingday'].value_counts()

    fig = px.pie(
    weekend,
    values = weekend.values,
    names = weekend.index,
    title = 'comparison working vs holiday',
    width=300,
    height=400)

    fig.update_layout(
    title_x = 0.10
)

    fig.update_traces(textposition='inside', 
                  textinfo='percent+label')

    st.plotly_chart(fig)

with col4:
    user_counts = pd.DataFrame({
    'user_type': ['casual', 'registered'],
    'count': [df_day['casual'].sum(), df_day['registered'].sum()]
})

    fig = px.bar(user_counts, 
             x='user_type', 
             y='count',
             color='user_type',
             barmode='group',
             title='Comparison between Users Type',
             text='count',
             text_auto= '.2s',
             width=350,
             height=400)

    fig.update_layout(
    xaxis_title='User Type',
    yaxis_title='Count',
    showlegend=True,
    title_x = 0.10
)

    fig.update_traces(
    textposition='outside'
)
    st.plotly_chart(fig)






