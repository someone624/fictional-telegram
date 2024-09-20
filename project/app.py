import streamlit as st
import time
import numpy as np
import pandas as pd

st.title('hello world')
time.sleep(5)
st.title('pip install streamlit')
time.sleep(5)
st.title('streamlit hello')

st.write('Hello, World')

name = st.text_input('Enter your name:')
st.write(f'Hello, {name}!')

st.text_input('Enter your text here:')
st.slider('Pick a number', 0, 100)

st.image('assets/example_image.png', caption='Example Image')

data = pd.read_csv('data/example_data.csv')
st.write('Here is some example data:')
st.dataframe(data)

x = np.linspace(0, 10, 100)
y = np.sin(x)

data = pd.DataFrame({
    'x': x,
    'y': y
})

st.line_chart(data.set_index('x'))
