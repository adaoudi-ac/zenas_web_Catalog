# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')

# connect to snowflake
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
cnx = st.connection("snowflake")
session = cnx.session()

# run a snowflake query and put it all in a var called my_catalog
session.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

# put the dafta into a dataframe
df = pandas.DataFrame(my_catalog)

# temp write the dataframe to the page so I Can see what I am working with
# streamlit.write(df)
# put the first column into a list
color_list = df[0].values.tolist()

# print(color_list)
# Let's put a pick list here so they can pick the color
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

# We'll build the image caption now, since we can
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'
#st.stop()

