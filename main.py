import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dataset
import timeline
import categories_distribution
import views_subscriptions
import video_view_ratio
import predict_subscribers
import predict_rank


st.title('Capstone Project ST1')

# setup side bar
st.sidebar.title('Sections')
st.sidebar.markdown('''[Dataset: Most subscribed youtube channels](#1)</br></br>
[Modules used for the project](#2)</br></br>
[Reading the dataset](#3)</br></br>
[This analysis tries to answer the following questions](#4)</br></br>
[1. Timeline for number of channels started](#5)</br></br>
[2. Channel categories distribution](#6)</br></br>
[3. Views and Subscriptions vs Rank](#7)</br></br>
[4. Predicting subscribers from views](#8)</br></br>
[5. Predict rank from total subscriptions](#9)</br></br>
[6. Average views per video](#10)</br></br>
[References](#11)''', unsafe_allow_html=True)

st.header('Dataset: Most subscribed youtube channels', anchor='1')

st.markdown('[kaggle dataset link](https://www.kaggle.com/datasets/surajjha101/top-youtube-channels-data)')
st.markdown('Maintained by: [surajjha101](https://www.kaggle.com/surajjha101)')

st.dataframe(dataset.most_subscribed_channels)

st.write('#')

st.subheader('Modules used for the project', anchor='2')

st.code('''streamlit
pandas
numpy
matplotlib
sklearn''')

st.subheader('Reading the dataset', anchor='3')

st.text('''The dataset was read using read_csv function in pandas 
and stored in a variable called "most_subscribed_channels"''')
        
st.code('''most_subscribed_channels = pd.read_csv('most_subscribed_youtube_channels.csv')''')

st.write('')

st.subheader('This analysis tries to answer the following questions:', anchor='4')
st.markdown('''1. How may top channels were started over the years?
2. How many unique categories are there and what are the top categories?
3. How does views and subscriptions change with decreasing channel rank?
4. Can we predict total subscribers from total views for channels?
5. Can we predict channel rank from total number of subscribers?
6. Is there a common pattern in the average views per video ratio for channels?''')

st.write('#')

timeline.render_documentation()
timeline.plot_total_channels_timeline()

categories_distribution.render_documentation()
categories_distribution.plot_categories_distribution()

views_subscriptions.render_documentation()
views_subscriptions.plot_views_and_subscriptions_vs_rank()

predict_subscribers.render_documentation()
predict_subscribers.predict_subscribers_from_views()

predict_rank.render_documentation()
predict_rank.predict_rank_from_subscriptions()
predict_rank.predict_rank_from_subscriptions_removed_outlier()

video_view_ratio.render_documentation()
video_view_ratio.plot_views_to_videos_ratio()


st.write('')

st.subheader('References', anchor='11')

st.markdown('''1. https://realpython.com/linear-regression-in-python/
2. https://matplotlib.org/cheatsheets/_images/cheatsheets-1.png
3. https://docs.streamlit.io/library/cheatsheet
4. https://www.analyticsvidhya.com/blog/2021/10/everything-you-need-to-know-about-linear-regression/''')