import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Sample DataFrame (replace this with your actual DataFrame 'df')
df = pd.read_csv("Youtube_data.csv")

# Title of the Streamlit app
st.title("Video Analytics Dashboard")

# Check if the 'year' column is numeric and has no missing values
if df['year'].dtype == 'int64' and not df['year'].isnull().any():
    # Slicer for selecting the year
    selected_year = st.slider("Select a year:", min_value=int(df['year'].min()), max_value=int(df['year'].max()), value=(int(df['year'].min()), int(df['year'].max())))
    
    # Filter the DataFrame based on selected year
    filtered_df = df[(df['year'] >= selected_year[0]) & (df['year'] <= selected_year[1])]

    # Dropdown for selecting the metric
    selected_column = st.selectbox("Select a metric:", ['view_count', 'like_count', 'comment_count'])

    # Line chart
    line_chart_fig = px.line(filtered_df, x='year', y=selected_column, title=f'{selected_column} Over Time')
    st.plotly_chart(line_chart_fig)

    # Bar chart
    bar_chart_fig = px.bar(filtered_df, x='year', y=selected_column, title=f'{selected_column} Over Time')
    st.plotly_chart(bar_chart_fig)

    # Scatter plot
    scatter_plot_fig = px.scatter(filtered_df, x='year', y=selected_column, color='year',
                                  title=f'{selected_column} Scatter Plot Over Time')
    st.plotly_chart(scatter_plot_fig)

    # Donut chart (year-wise distribution)
    donut_chart_fig = px.pie(filtered_df, names='year', hole=0.4, title=f'Year-wise Distribution (Donut Chart)')
    st.plotly_chart(donut_chart_fig)

    # Bubble plot
    bubble_plot_fig = px.scatter(filtered_df, x='year', y='duration', size='like_count', color='year',
                                 title='Bubble Plot: Duration vs View Count (Bubble Size: Like Count)')
    st.plotly_chart(bubble_plot_fig)

    # Box plot (distribution of 'view_count' for each year)
    box_plot_fig = px.box(filtered_df, x='year', y='view_count', title='Box Plot: Distribution of View Count for Each Year')
    st.plotly_chart(box_plot_fig)

    # Heatmap (correlation matrix)
    correlation_matrix = filtered_df[['view_count', 'like_count', 'comment_count']].corr()
    heatmap_fig = go.Figure(data=go.Heatmap(z=correlation_matrix.values,
                                            x=correlation_matrix.columns,
                                            y=correlation_matrix.columns,
                                            colorscale='Viridis'))
    heatmap_fig.update_layout(title='Correlation Heatmap')
    st.plotly_chart(heatmap_fig)
else:
    st.error("The 'year' column must be numeric and have no missing values for the app to work.")
