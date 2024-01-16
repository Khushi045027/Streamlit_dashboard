import streamlit as st
import pandas as pd
import plotly.express as px

# Sample DataFrame (replace this with your actual DataFrame 'df')
df = pd.read_csv("Youtube_data.csv")

# Convert 'published_at' to datetime with the specified format
df['published_at'] = pd.to_datetime(df['published_at'], format='%d-%m-%Y')

# Extract year from 'published_at'
df['year'] = df['published_at'].dt.year

# Streamlit app
st.title("Video Analytics Dashboard")

# Dropdown for column selection
selected_column = st.selectbox("Select Column", ['view_count', 'like_count', 'comment_count'])

# Line chart
st.plotly_chart(px.line(df, x='published_at', y=selected_column, title=f'{selected_column} Over Time'))

# Bar chart
st.plotly_chart(px.bar(df, x='published_at', y=selected_column, title=f'{selected_column} Over Time'))

# Scatter plot
st.plotly_chart(px.scatter(df, x='published_at', y=selected_column, color='year',
                            title=f'{selected_column} Scatter Plot Over Time'))

# Pie chart (year-wise distribution)
st.plotly_chart(px.pie(df, names='year', title=f'Year-wise Distribution'))
