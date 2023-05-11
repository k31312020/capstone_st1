import streamlit as st
import dataset
import matplotlib.pyplot as plt
import numpy as np
import utils

def render_documentation():
    st.subheader('3. Views and Subscriptions vs Rank', anchor='7')

    st.write('''<div style="text-align: justify;">This plot can be done using a line graph for the subscribers as
    the dataset is arranged in the descending order of subscribers. Scatter plot can be used for views as the total 
    number of views for each channel significantly vary from the others. </div></br>
    <div style="text-align: justify;">
    We cannot directly use the data from dataframe as the value in the columns for views and subscribers were recorded
    as a formatted string separated by commas. To clean these columns we need to initialize views and subscribers list (line3-4).
    Next we iterate through the dataframe rows, converting the value of views and subscribers for each channel 
    into an integer (line7-8) by removing comma separation using the "string_to_int" function from "utils" module.</div></br>
    <div style="text-align: justify;">
    As these two colums have large varying values, the values are scaled down to a range of 0 to 100 as a percentage of the 
    maximum. To achieve this, the maximum for views and subscribers are determined (line9-10). The map function 
    to iterate over each value for a channel with the help of a "map_to_hundred" helper function along with the corresponding
    maximum for the column (line 13 - 14).</div></br>
    <div style="text-align: justify;">
    From this plot we can see that the graph of subscribers vs rank is asymptotical, while the graph of views is highly varying
    across channels. We can also see that the graph of views follows along the similar slope as the subscribers graph.
    </div>
    ''', unsafe_allow_html=True)


    st.code('''def plot_views_and_subscriptions_vs_rank():
    rank = []
    views = []
    subscribers = []
    for i, channel in dataset.most_subscribed_channels.iterrows():
        rank.append(channel[dataset.RANK_COL])
        views.append(int(channel[dataset.VIEWS_COL].replace(',','')))
        subscribers.append(int(channel[dataset.SUBSCRIBERS_COL].replace(',','')))
    max_views = np.amax(views)
    max_subscribers = np.amax(subscribers)
    def map_to_hundred(value, max):
        return value * 100/max
    views = [*map(map_to_hundred, views, [max_views]*len(views))]
    subscribers = [*map(map_to_hundred, subscribers, [max_subscribers]*len(subscribers))]
    fig, ax = plt.subplots()
    colors = plt.get_cmap('Reds')(np.linspace(1, 0.7, 2))
    ax.scatter(dataset.most_subscribed_channels[dataset.RANK_COL], views, s = 5, color='b')
    ax.plot(dataset.most_subscribed_channels[dataset.RANK_COL], subscribers, color='r')
    ax.legend()
    ax.set_ylim(0, 100)
    ax.grid(True, which="both")
    ax.set_xlabel('rank') 
    ax.set_ylabel('views & subscriptions')
    fig.set_figheight(6)
    fig.set_figwidth(10)
    st.pyplot(fig)
    ''', line_numbers=True)

def plot_views_and_subscriptions_vs_rank():
  views = []
  subscribers = []
  for i, channel in dataset.most_subscribed_channels.iterrows():
    views.append(utils.string_to_int(channel[dataset.VIEWS_COL]))
    subscribers.append(utils.string_to_int(channel[dataset.SUBSCRIBERS_COL]))
  max_views = np.amax(views)
  max_subscribers = np.amax(subscribers)
  views = [*map(utils.fit_value, [100]*len(views), views, [max_views]*len(views))]
  subscribers = [*map(utils.fit_value, [100]*len(views), subscribers, [max_subscribers]*len(subscribers))]
  fig, ax = plt.subplots()
  ax.scatter(dataset.most_subscribed_channels[dataset.RANK_COL], views, s = 5, color='b')
  ax.plot(dataset.most_subscribed_channels[dataset.RANK_COL], subscribers, color='r')
  ax.legend()
  ax.set_ylim(0, 100)
  ax.grid(True, which="both")
  ax.set_xlabel('rank') 
  ax.set_ylabel('views & subscriptions')
  fig.set_figheight(6)
  fig.set_figwidth(10)
  st.pyplot(fig)