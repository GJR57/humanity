import streamlit as st
import pandas as pd

filepath = 'data/data_rse-western-collection.xlsx'
data = pd.read_excel(filepath, sheet_name='data')
st.dataframe(data, hide_index=True)
