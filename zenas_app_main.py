# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests
import pandas

cnx = st.connection("snowflake")
session = cnx.session()

st.title('My Parents New Helathy Dinner')
