import streamlit as st
import functions as tf

def get_heat():
    pass

st.title("CPI Air Welding")

#Selection boxes:
st.selectbox('Machine: ', ("Machine 1", "Machine 2", "Machine 3(Down)", "Machine 4"), key='machine')
st.selectbox("Material: ", ("1055", "1365", "2051", "4090", "vinyl"), key='material')

col1, col2 = st.columns(2)
with col1:
    st.selectbox("Seam or Tape:", ("Seam","Tape"), key="seamtape")
with col2:
    st.selectbox("Heat or Speed: ", ('Heat','Speed'), key="heatbox")


#session state variables:
ssmachine = st.session_state['machine']
ssmaterial = st.session_state['material']
ssseamtape = st.session_state['seamtape']
ssheatbox = st.session_state['heatbox']

ss = st.session_state

#machine 1
# get speed setting:
if ssmachine == "Machine 1" and ssheatbox == "Speed" and ssmaterial == "1055" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speed1055_2(heat))



# get heat setting:
elif ssmachine == "Machine 1" and ssheatbox == "Heat" and ssmaterial == "1055" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heat1055_2(speed))

# get speed setting:
elif ssmachine == "Machine 1" and ssheatbox == "Speed" and ssmaterial == "1365" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speed1365_2(heat))



# get heat setting:
elif ssmachine == "Machine 1" and ssheatbox == "Heat" and ssmaterial == "1365" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heat1365_2(speed))

# get speed setting:
elif ssmachine == "Machine 1" and ssheatbox == "Speed" and ssmaterial == "2051" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speed2051_2(heat))



# get heat setting:
elif ssmachine == "Machine 1" and ssheatbox == "Heat" and ssmaterial == "2051" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heat2051_2(speed))

# get speed setting:
elif ssmachine == "Machine 1" and ssheatbox == "Speed" and ssmaterial == "4090" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speed4090_2(heat))



# get heat setting:
elif ssmachine == "Machine 1" and ssheatbox == "Heat" and ssmaterial == "4090" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heat4090_2(speed))


# get speed setting:
elif ssmachine == "Machine 1" and ssheatbox == "Speed" and ssmaterial == "vinyl" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speedvinyl_2(heat))



# get heat setting:
elif ssmachine == "Machine 1" and ssheatbox == "Heat" and ssmaterial == "vinyl" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heatvinyl_2(speed))


#machine 2


# get speed setting:
if ssmachine == "Machine 2" and ssheatbox == "Speed" and ssmaterial == "1055" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speed1055_2(heat))



# get heat setting:
elif ssmachine == "Machine 2" and ssheatbox == "Heat" and ssmaterial == "1055" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heat1055_2(speed))

# get speed setting:
elif ssmachine == "Machine 2" and ssheatbox == "Speed" and ssmaterial == "1365" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speed1365_2(heat))



# get heat setting:
elif ssmachine == "Machine 2" and ssheatbox == "Heat" and ssmaterial == "1365" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heat1365_2(speed))

# get speed setting:
elif ssmachine == "Machine 2" and ssheatbox == "Speed" and ssmaterial == "2051" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speed2051_2(heat))



# get heat setting:
elif ssmachine == "Machine 2" and ssheatbox == "Heat" and ssmaterial == "2051" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heat2051_2(speed))

# get speed setting:
elif ssmachine == "Machine 2" and ssheatbox == "Speed" and ssmaterial == "4090" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speed4090_2(heat))



# get heat setting:
elif ssmachine == "Machine 2" and ssheatbox == "Heat" and ssmaterial == "4090" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heat4090_2(speed))


# get speed setting:
elif ssmachine == "Machine 2" and ssheatbox == "Speed" and ssmaterial == "vinyl" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speedvinyl_2(heat))



# get heat setting:
elif ssmachine == "Machine 2" and ssheatbox == "Heat" and ssmaterial == "vinyl" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heatvinyl_2(speed))

# machine 4
# get speed setting:
if ssmachine == "Machine 4" and ssheatbox == "Speed" and ssmaterial == "1055" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speed1055_2(heat))



# get heat setting:
elif ssmachine == "Machine 4" and ssheatbox == "Heat" and ssmaterial == "1055" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heat1055_2(speed))

# get speed setting:
elif ssmachine == "Machine 4" and ssheatbox == "Speed" and ssmaterial == "1365" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speed1365_2(heat))



# get heat setting:
elif ssmachine == "Machine 4" and ssheatbox == "Heat" and ssmaterial == "1365" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heat1365_2(speed))

# get speed setting:
elif ssmachine == "Machine 4" and ssheatbox == "Speed" and ssmaterial == "2051" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speed2051_2(heat))



# get heat setting:
elif ssmachine == "Machine 4" and ssheatbox == "Heat" and ssmaterial == "2051" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heat2051_2(speed))

# get speed setting:
elif ssmachine == "Machine 4" and ssheatbox == "Speed" and ssmaterial == "4090" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speed4090_2(heat))



# get heat setting:
elif ssmachine == "Machine 4" and ssheatbox == "Heat" and ssmaterial == "4090" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heat4090_2(speed))


# get speed setting:
elif ssmachine == "Machine 4" and ssheatbox == "Speed" and ssmaterial == "vinyl" and ssseamtape == "Seam":
    st.text_input(label="Heat", key="heat", value=float(0))
    heat = float(ss["heat"])
    st.text("Speed:")
    st.info(tf.get_speedvinyl_2(heat))



# get heat setting:
elif ssmachine == "Machine 4" and ssheatbox == "Heat" and ssmaterial == "vinyl" and ssseamtape == "Seam":
    st.text_input(label="Speed", key="speed", value=float(0))
    speed = float(ss["speed"])
    st.text("Heat:")
    st.info(tf.get_heatvinyl_2(speed))

st.subheader("This is a Tool/Guideline. Always check your weld. It is still under development. Adding new features soon! Have to Calibrate machine 1 an 4")

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