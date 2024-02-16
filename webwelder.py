import streamlit as st
import functions as tf

def get_heat():
    pass

st.title("CPI Air Welding")
st.title("Still In development: adding features and functions soon!")
#Selection boxes:
st.selectbox('Machine: ', ("Machine 1", "Machine 2", "Machine 3", "Machine 4"), key='machine')
st.selectbox("Material: ", ("955", "1055", "1365", "2051", "4090", "vinyl"), key='material')
st.selectbox("Heat or Speed: ", ('Heat','Speed'), key="heatbox")

#session state variables:
ssmachine = st.session_state['machine']
ssmaterial = st.session_state['material']
ssheatbox = st.session_state['heatbox']


if ssmachine == "Machine 1" and ssheatbox == "Speed":
    st.text_input(label="speed", key="speed", value=float(0))



#st.text_input(label="speed", key="speed", value=float(0))



#speed = sl.session_state["speed"]
#speed = float(speed)
#got_heat = tf.hmaterial1055_3test2(speed)

#st.info(tf.hmaterial1055_3test2(speed))

#st.text_input(label="heat", key="heat", value=float(0))

#heat = sl.session_state["heat"]
#heat = float(heat)

#st.info(tf.smaterial1055_3test2(heat))



#st.session_state