import streamlit as st

st.write("Ok, let's see something fun...")
if st.button('Click me'):
    st.image('data/xkcd.png')
if st.button('Show more'):
    st.video('data/battle.mov')
