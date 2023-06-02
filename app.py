import streamlit as st

import numpy as np
import pandas as pd

st.title("My first app")

st.markdown(
"""
## Header 2
The following is a list:
- item 1
- item 2
- item 3

**Some bold text!**
"""
)

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})


# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

if st.checkbox('Show dataframe'):
    head_df

'The code for my bike is...'
st.secrets['my_bike_lock_code']
