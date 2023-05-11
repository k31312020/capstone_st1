import streamlit as st
import dataset
import matplotlib.pyplot as plt
import numpy as np
import utils
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def render_documentation():
    st.subheader('5. Predict rank from total subscriptions', anchor='9')

    st.write('''<div style="text-align: justify;">We try to predict the rank of channels using subscribers in this section
    using the rank and subscribers columns from the dataset. Two scenarios were analysed for this prediction because
    there was a huge difference in the subscriptions for top ranked channels. This created discontinuities in the training
    data, decreasing the strength of the model. The first model uses all the channels without removing the discontinuities
     while the second model skips the top 100 channels for better prediction. </div></br>
    <div style="text-align: justify;">
    As we need to plot and prepare data two times we create a reusable function called "plot_predictions" (line 1) for creating
    the polynomial regression model, fitting, predicting and plotting. Similarly a reusable function called "prepare data" (line 26) 
    is created to clean and collect training and test data. A parameter called skipIndex which has a default value of 0 can
    be passed to this function. Based on the skipIndex the prepare_data function will skip all rows with indexes less than
    the skipIndex (Note: This only works if the dataset is arranged in descending order of rank, for the current analysis
    the dataset was pre-sorted in this order before downloading).</div></br>
    <div style="text-align: justify;">
    We can see that the first chart has a r_square of 0.74 and the line of best fit appears linear for the highest subscriber
    value because of the huge gap in values as mentioned earlier. However, the prediction becomes much better when the outliers
    are removed in the second plot resulting in a high r_sqaure value of 0.98.</div></br>
    ''', unsafe_allow_html=True)


    st.code('''def plot_predictions(training_data, test_data):
  model = LinearRegression()
  training_data[dataset.SUBSCRIBERS_COL] = np.array(training_data[dataset.SUBSCRIBERS_COL]).reshape(-1,1)

  training_subs_ploy = PolynomialFeatures(degree=2, include_bias=False).fit_transform(training_data[dataset.SUBSCRIBERS_COL])

  test_subs_ploy = PolynomialFeatures(degree=2, include_bias=False).fit_transform(np.array(test_data[dataset.SUBSCRIBERS_COL]).reshape(-1,1))

  model.fit(training_subs_ploy, training_data[dataset.RANK_COL])

  r_square = model.score(training_subs_ploy, training_data[dataset.RANK_COL])

  st.text(f'r-square {r_square}')

  predicted_ranks = model.predict(test_subs_ploy)

  fig, ax = plt.subplots()

  ax.plot(test_data[dataset.SUBSCRIBERS_COL], predicted_ranks, color='b')
  ax.scatter(test_data[dataset.SUBSCRIBERS_COL], test_data[dataset.RANK_COL], color='r')
  ax.set_xlabel('views') 
  ax.grid(True, which="both")
  ax.set_ylabel('rank')
  st.pyplot(fig)

def prepare_data(skipIndex=0):
  training_data = dict(subscribers = [], rank = [])
  test_data = dict(subscribers = [], rank = [])
  for index, channel in dataset.most_subscribed_channels.iterrows():
    if index < skipIndex:
       continue
    if (index%2 == 0):
        test_data[dataset.RANK_COL].append(int(channel[dataset.RANK_COL]))
        test_data[dataset.SUBSCRIBERS_COL].append(utils.string_to_int(channel[dataset.SUBSCRIBERS_COL]))
    else:
        training_data[dataset.RANK_COL].append(int(channel[dataset.RANK_COL]))
        training_data[dataset.SUBSCRIBERS_COL].append(utils.string_to_int(channel[dataset.SUBSCRIBERS_COL]))
        
  return training_data, test_data

def predict_rank_from_subscriptions():
  plot_predictions(*prepare_data())

def predict_rank_from_subscriptions_removed_outlier():
#   skip the top 100 channels
  plot_predictions(*prepare_data(100))
    ''', line_numbers=True)

def plot_predictions(training_data, test_data, title):
  model = LinearRegression()
  training_data[dataset.SUBSCRIBERS_COL] = np.array(training_data[dataset.SUBSCRIBERS_COL]).reshape(-1,1)

  training_subs_ploy = PolynomialFeatures(degree=2, include_bias=False).fit_transform(training_data[dataset.SUBSCRIBERS_COL])

  test_subs_ploy = PolynomialFeatures(degree=2, include_bias=False).fit_transform(np.array(test_data[dataset.SUBSCRIBERS_COL]).reshape(-1,1))

  model.fit(training_subs_ploy, training_data[dataset.RANK_COL])

  r_square = model.score(training_subs_ploy, training_data[dataset.RANK_COL])

  st.text(f'r-square {r_square}')

  predicted_ranks = model.predict(test_subs_ploy)

  fig, ax = plt.subplots()
  ax.set_title(title)
  ax.plot(test_data[dataset.SUBSCRIBERS_COL], predicted_ranks, color='b')
  ax.scatter(test_data[dataset.SUBSCRIBERS_COL], test_data[dataset.RANK_COL], color='r')
  ax.set_xlabel('views') 
  ax.grid(True, which="both")
  ax.set_ylabel('rank')
  st.pyplot(fig)

def prepare_data(skipIndex=0):
  training_data = dict(subscribers = [], rank = [])
  test_data = dict(subscribers = [], rank = [])
  for index, channel in dataset.most_subscribed_channels.iterrows():
    if index < skipIndex:
       continue
    if (index%2 == 0):
        test_data[dataset.RANK_COL].append(int(channel[dataset.RANK_COL]))
        test_data[dataset.SUBSCRIBERS_COL].append(utils.string_to_int(channel[dataset.SUBSCRIBERS_COL]))
    else:
        training_data[dataset.RANK_COL].append(int(channel[dataset.RANK_COL]))
        training_data[dataset.SUBSCRIBERS_COL].append(utils.string_to_int(channel[dataset.SUBSCRIBERS_COL]))
        
  return training_data, test_data

def predict_rank_from_subscriptions():
  plot_predictions(*prepare_data(), 'Predicting rank from subscribers including all channels')

def predict_rank_from_subscriptions_removed_outlier():
#   skip the top 100 channels
  plot_predictions(*prepare_data(100), 'Predicting rank from subscribers by removing top 100 channels')