import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Sample DataFrame (replace this with your actual DataFrame 'df')
# df = ...

# Convert 'published_at' to datetime with the specified format
df['published_at'] = pd.to_datetime(df['published_at'], format='%d-%m-%Y')

# Extract year from 'published_at'
df['year'] = df['published_at'].dt.year

# Title of the Streamlit app
st.title("Video Analytics Dashboard")

# Dropdown for selecting the metric
selected_column = st.selectbox("Select a metric:", ['view_count', 'like_count', 'comment_count'])

# Line chart
line_chart_fig = px.line(df, x='published_at', y=selected_column, title=f'{selected_column} Over Time')
st.plotly_chart(line_chart_fig)

# Bar chart
bar_chart_fig = px.bar(df, x='published_at', y=selected_column, title=f'{selected_column} Over Time')
st.plotly_chart(bar_chart_fig)

# Scatter plot
scatter_plot_fig = px.scatter(df, x='published_at', y=selected_column, color='year',
                              title=f'{selected_column} Scatter Plot Over Time')
st.plotly_chart(scatter_plot_fig)

# Donut chart (year-wise distribution)
donut_chart_fig = px.pie(df, names='year', hole=0.4, title=f'Year-wise Distribution (Donut Chart)')
st.plotly_chart(donut_chart_fig)

# Bubble plot
bubble_plot_fig = px.scatter(df, x='published_at', y='duration', size='like_count', color='year',
                             title='Bubble Plot: Duration vs View Count (Bubble Size: Like Count)')
st.plotly_chart(bubble_plot_fig)

# Box plot (distribution of 'view_count' for each year)
box_plot_fig = px.box(df, x='year', y='view_count', title='Box Plot: Distribution of View Count for Each Year')
st.plotly_chart(box_plot_fig)

# Time series plot
time_series_plot_fig = px.line(df, x='published_at', y='view_count', title='Time Series Plot: View Count Over Time')
st.plotly_chart(time_series_plot_fig)

# Heatmap (correlation matrix)
correlation_matrix = df[['view_count', 'like_count', 'comment_count']].corr()
heatmap_fig = go.Figure(data=go.Heatmap(z=correlation_matrix.values,
                                        x=correlation_matrix.columns,
                                        y=correlation_matrix.columns,
                                        colorscale='Viridis'))
heatmap_fig.update_layout(title='Correlation Heatmap')
st.plotly_chart(heatmap_fig)
