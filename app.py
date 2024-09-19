import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

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

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
st.pyplot(plt)
