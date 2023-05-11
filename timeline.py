import streamlit as st
import dataset
import matplotlib.pyplot as plt
import numpy as np

def render_documentation():
    st.write('')

    st.subheader('1. Timeline for number of channels started', anchor='5')

    st.write('''<div style="text-align: justify;">To find out how many channels were started each year 
    first we initialize a timeline dictionary (line 2)
    . Then we loop over the dataframe (line 3), adding the 
    started year to the timeline dictionary (line 6-7) 
    if it is not found in the dictionary. If it is in the timeline dictionary (line 4) 
    the count for that year is increased by one (line 5)</div>
    ''', unsafe_allow_html=True)
    st.write('')         
    st.write('''<div style="text-align: justify;">We can see from the timeline that the number of top channels 
    has gradually increased over time and has peaked in 2014 followed by 
    a steep decline in the following years. This shows that we may not have a large volume of upcoming top 
    creaters on youtube.</div>
    ''', unsafe_allow_html=True)

    st.code('''def plot_total_channels_timeline():
    timeline_data = {}
    for i, channel in dataset.most_subscribed_channels.iterrows():
        if channel[dataset.STARTED_COL] in timeline_data:
        timeline_data[channel[dataset.STARTED_COL]] += 1
        else:
        timeline_data[channel[dataset.STARTED_COL]] = 1

    x, y = zip(*timeline_data.items())
    fig, ax = plt.subplots()
    ax.set_xlabel('Year')
    ax.set_ylabel('Total channels started')
    ax.set_xticks(np.arange(min(x), max(x)+1, 2))
    ax.set_xlim(2004, 2023)
    ax.bar(x,y, color='red')
    st.pyplot(fig)''', line_numbers=True)

def plot_total_channels_timeline():
  timeline_data = {}
  for i, channel in dataset.most_subscribed_channels.iterrows():
    if channel[dataset.STARTED_COL] in timeline_data:
      timeline_data[channel[dataset.STARTED_COL]] += 1
    else:
      timeline_data[channel[dataset.STARTED_COL]] = 1

  x, y = zip(*timeline_data.items())
  fig, ax = plt.subplots()
  ax.set_xlabel('Year')
  ax.set_ylabel('Total channels started')
  ax.set_xticks(np.arange(min(x), max(x)+1, 2))
  ax.set_xlim(2004, 2023)
  ax.bar(x,y, color='red')
  st.pyplot(fig)