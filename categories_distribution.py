
import streamlit as st
import dataset
import matplotlib.pyplot as plt
import numpy as np


def render_documentation():
    st.write('')

    st.subheader('2. Channel categories distribution', anchor='6')

    st.write('''<div style="text-align: justify;">Each channel has one or more categories separated
    by the '&' symbol. For this plot, all the categories are extrated into a dictionary and the duplicates
    are counted using the unique function in numpy. First we initialize a categories list (line 2). 
    Then we loop over the dataframe (line 3) where "i" is the index.</div></br>
    <div style="text-align: justify;">
    The category for each channel is split into a list using the split function of the string by
    passing the "&" delimiter as the argument (line 4). Some values from the category column were not in string format
    so "str" function is used to convert them to a string (line 4). Trailing spaced are stripped from the sub
    categories and each sub category is converted to lowercase for uniformity (line 4). All the sub categories 
    are stored in the sub_categoires list (line 4).</div></br>
    <div style="text-align: justify;">
    Using numpy append the categories list and sub categories list are joined and assigned back to 
    from a new categories list (line 5). Next, we extract the unique categories
    using the unique function from numpy along with the corresponding list of duplicate count, using the 
    return_count flag set to True (line 6). As it was difficult to fit all the categories on the 
    same chart, the argsort function from numpy was used to get the top ten recurring categories by sorting 
    the unique categories_count list in descending order (line 8) Colors were generated using the 
    get_cmap function from the pyplot module (line 10)</div></br>
    <div style="text-align: justify;">
    From the pie chart it is evident that atleast 40% of the top channels fall in the music and entertainment category. 
    Some of the other major categories are people, blogs, gaming and comedy.
    </div>
    ''', unsafe_allow_html=True)

    st.code('''def plot_categories_distribution():
    categories = []
    for i, channel in dataset.most_subscribed_channels.iterrows():
        sub_categories = [sub_category.strip().lower() for sub_category in str(channel[dataset.CATEGORY_COL]).split('&')]
        categories = np.append(categories, sub_categories)
    categories, categories_count = np.unique(categories, return_counts=True)

    categories_count_desc_index = np.argsort(-categories_count)[:10]
    
    colors = plt.get_cmap('Reds')(np.linspace(0.9, 0.1, len(categories)))

    fig, ax = plt.subplots()
    ax.pie(categories_count[categories_count_desc_index], 
        colors=colors, 
        labels=categories[categories_count_desc_index], 
        autopct='%1.1f%%',
        radius=2,
        labeldistance=1.03,
        pctdistance=0.8,
        wedgeprops={"width": 1,"linewidth": 1, "edgecolor": "white"}
    )

    categories_markdown = ''
    for category in categories:
        # removing nan as is not a valid category
        categories_markdown += '<button style="{color:blue;}">' + category + '</button>' if category != 'nan' else ''

    st.text(f'There are {len(categories) - 1} unique categories.') 
    st.text('The distribution of the channels into the top ten plotted below.')
    st.markdown(categories_markdown, unsafe_allow_html=True)

    st.pyplot(fig)
    ''', line_numbers=True)


def plot_categories_distribution():
    categories = []
    for i, channel in dataset.most_subscribed_channels.iterrows():
        sub_categories = [sub_category.strip().lower() for sub_category in str(
            channel[dataset.CATEGORY_COL]).split('&')]
        categories = np.append(categories, sub_categories)
    categories, categories_count = np.unique(categories, return_counts=True)

    categories_count_desc_index = np.argsort(-categories_count)[:10]

    colors = plt.get_cmap('Reds')(np.linspace(0.9, 0.1, len(categories)))

    fig, ax = plt.subplots()
    ax.pie(categories_count[categories_count_desc_index],
           colors=colors,
           labels=categories[categories_count_desc_index],
           autopct='%1.1f%%',
           radius=2,
           labeldistance=1.03,
           pctdistance=0.8,
           wedgeprops={"width": 1, "linewidth": 1, "edgecolor": "white"}
           )

    categories_markdown = ''
    for category in categories:
        # removing nan as is not a valid category
        categories_markdown += '<button style="{color:blue;}">' + \
            category + '</button>' if category != 'nan' else ''

    st.text(f'There are {len(categories) - 1} unique categories.')
    st.text('The distribution of the channels into the top ten plotted below.')
    st.markdown(categories_markdown, unsafe_allow_html=True)

    st.pyplot(fig)
