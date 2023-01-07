import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import graphviz as graphviz
import streamlit as st

# create a sidear with some attributes
#st.sidebar().title("This is a sidebar Title")
# "with" notation
with st.sidebar:
    st.title("The sidebar title")
    st.file_uploader('Upload a pic')
    cont1 = st.container()
    cont1.write("Some Container Text - One")
    cont1.write("Some Container Text - Two")
    cont1.text_area('DescriptionOne')
    rand=np.random.normal(1, 2, size=20)
    fig, ax = plt.subplots()
    ax.hist(rand, bins=15)
    st.pyplot(fig)

    
    st.graphviz_chart('''
        digraph {
            Big_shark -> Tuna
            Tuna -> Mackerel
            Mackerel -> Small_fishes
            Small_fishes -> Shrimp
        }
    ''')

st.write("Hello ,let's learn how to build a streamlit app alone")

st.title ("This is the app title")

st.header("This is the markdown")

st.markdown("This is the header")

st.subheader("This is the subheader")

st.caption("This is the caption")

st.code("!pip install something \nimport something as so\nX * so.Dosomething(2021)")

st.latex(r'''\Sigma ( a+a r^1+a r^2+a r^3) ''')
st.latex(r'''\Gamma ( g + 9 r^3 + a r^2 + g r^3) ''')

df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.line_chart(df[['x']])


df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.bar_chart(df)

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))


st.balloons()
st.progress(10)
with st.spinner('Wait for it...'):
    time.sleep(10)

isCheck = st.checkbox('yes')
st.write(f"Selection : {0}", isCheck)

st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')




st.caption("SuryaNamaskar Posures - Image")
st.image("./resources/Namaskar.jpg")

st.write("\n\n")
st.caption("Thoughts - Audio")
st.audio("./resources/audio.m4a")

st.write("\n\n")
st.caption("Tutorial - Video")
st.video("https://youtu.be/EpmnOTr7E2c")
