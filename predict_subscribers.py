import streamlit as st
import dataset
import matplotlib.pyplot as plt
import numpy as np
import utils
from sklearn.linear_model import LinearRegression

def render_documentation():
    st.write('')

    st.subheader('4. Predicting subscribers from views', anchor='8')

    st.write('''<div style="text-align: justify;">We use linear regression to find the best fit line
    for estimating the total subscribers from views for a channel</div></br>
    <div style="text-align: justify;">
    Inorder to develop and test the dataset properly we divide the data into two dictionaries, training_data and
    test_data (line 2-3). Each dictionary consist of subscribers, views and rank list. We loop through the dataset (line 4)
    and if the number of views are greater than zero (line 5), all the even rows are added to the test dictionary (line 6-9)
    and all the odd rows are added to the training dictionary (line 10-13)</div></br>
    <div style="text-align: justify;">
    The views traning data is then converted to a two dimensional numpy array (line 15). A model is initialized (line 19) and the training data
    is fitted to the model (line 20). The R square value is calculated and printed (line 22-24). Subscribers are predicted
    for the training data based on the model (line 26). A line plot is used to represent the predicted subscribers (line 30)
    and a scatter plot is used to represent the actual subscribers for the test data (line 31).
    </div></br>
    <div style="text-align: justify;">
    The upper bound of the chart was changed to 40 billion as the majority of data was concentrated in this range. This regression
    model has a r square value of 0.63, which means 63% of total subscribers variance can be explained by the total views for 
    the channels. Compared to the dense scattered volume of the actual data, this model may not be suitable for predicting
    total subscribers from total views for channels.
    </div>
    ''', unsafe_allow_html=True)

    st.code('''def predict_subscribers_from_views():
    training_data = dict(subscribers = [], views = [], rank = [])
    test_data = dict(subscribers = [], views = [], rank = [])
    for index, channel in dataset.most_subscribed_channels.iterrows():
        if (utils.string_to_int(channel[dataset.VIEWS_COL]) > 0):
            if (index%2 == 0):
                test_data[dataset.RANK_COL].append(channel[dataset.RANK_COL])
                test_data[dataset.SUBSCRIBERS_COL].append(utils.string_to_int(channel[dataset.SUBSCRIBERS_COL]))
                test_data['views'].append(utils.string_to_int(channel[dataset.VIEWS_COL]))
            else:
                training_data[dataset.RANK_COL].append(channel[dataset.RANK_COL])
                training_data[dataset.SUBSCRIBERS_COL].append(utils.string_to_int(channel[dataset.SUBSCRIBERS_COL]))
                training_data['views'].append(utils.string_to_int(channel[dataset.VIEWS_COL]))

    training_data['views'] = np.array(training_data['views']).reshape((-1, 1))

    #linear regression

    model = LinearRegression()
    model.fit(training_data['views'], training_data[dataset.SUBSCRIBERS_COL])

    r_square = model.score(training_data['views'], training_data[dataset.SUBSCRIBERS_COL])

    print(f'r-square {r_square}')

    predicted_subscribers = model.predict(np.array(test_data['views']).reshape(-1,1))

    st.text(f'r-square {r_square}')

    ax.plot(test_data['views'], predicted_subscribers, color='b')
    ax.scatter(test_data['views'], test_data['subscribers'], color='r')
    ax.set_xlabel('views') 
    ax.set_xlim(0, 40000000000)
    ax.set_ylabel('subscribers')
    st.pyplot(fig)
    ''', line_numbers=True)

def predict_subscribers_from_views():
  training_data = dict(subscribers = [], views = [], rank = [])
  test_data = dict(subscribers = [], views = [], rank = [])
  for index, channel in dataset.most_subscribed_channels.iterrows():
    if (utils.string_to_int(channel[dataset.VIEWS_COL]) > 0):
        if (index%2 == 0):
          test_data[dataset.RANK_COL].append(channel[dataset.RANK_COL])
          test_data[dataset.SUBSCRIBERS_COL].append(utils.string_to_int(channel[dataset.SUBSCRIBERS_COL]))
          test_data['views'].append(utils.string_to_int(channel[dataset.VIEWS_COL]))
        else:
          training_data[dataset.RANK_COL].append(channel[dataset.RANK_COL])
          training_data[dataset.SUBSCRIBERS_COL].append(utils.string_to_int(channel[dataset.SUBSCRIBERS_COL]))
          training_data['views'].append(utils.string_to_int(channel[dataset.VIEWS_COL]))

  training_data['views'] = np.array(training_data['views']).reshape(-1, 1)

  #linear regression

  model = LinearRegression()
  model.fit(training_data['views'], training_data[dataset.SUBSCRIBERS_COL])

  r_square = model.score(training_data['views'], training_data[dataset.SUBSCRIBERS_COL])

  st.text(f'r-square {r_square}')

  predicted_subscribers = model.predict(np.array(test_data['views']).reshape(-1,1))

  fig, ax = plt.subplots()

  ax.plot(test_data['views'], predicted_subscribers, color='b')
  ax.scatter(test_data['views'], test_data['subscribers'], color='r')
  ax.set_xlabel('views') 
  ax.grid(True, which="both")
  ax.set_xlim(0, 40000000000)
  ax.set_ylabel('subscribers')
  st.pyplot(fig)