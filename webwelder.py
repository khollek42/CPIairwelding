import streamlit as st
import functions as tf



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

try:
    #Seaming

    #machine 1
    # get speed setting:
    if ssmachine == "Machine 1" and ssheatbox == "Speed" and ssmaterial == "1055" and ssseamtape == "Seam":
        st.text_input(label="Heat", key="heat", value=float(0))
        heat = float(ss["heat"])
        st.text("Speed:")
        st.info(tf.get_speed1055_1(heat))



    # get heat setting:
    elif ssmachine == "Machine 1" and ssheatbox == "Heat" and ssmaterial == "1055" and ssseamtape == "Seam":
        st.text_input(label="Speed", key="speed", value=float(0))
        speed = float(ss["speed"])
        st.text("Heat:")
        st.info(tf.get_heat1055_1(speed))

    # get speed setting:
    elif ssmachine == "Machine 1" and ssheatbox == "Speed" and ssmaterial == "1365" and ssseamtape == "Seam":
        st.text_input(label="Heat", key="heat", value=float(0))
        heat = float(ss["heat"])
        st.text("Speed:")
        st.info(tf.get_speed1365_1(heat))



    # get heat setting:
    elif ssmachine == "Machine 1" and ssheatbox == "Heat" and ssmaterial == "1365" and ssseamtape == "Seam":
        st.text_input(label="Speed", key="speed", value=float(0))
        speed = float(ss["speed"])
        st.text("Heat:")
        st.info(tf.get_heat1365_1(speed))

    # get speed setting:
    elif ssmachine == "Machine 1" and ssheatbox == "Speed" and ssmaterial == "2051" and ssseamtape == "Seam":
        st.text_input(label="Heat", key="heat", value=float(0))
        heat = float(ss["heat"])
        st.text("Speed:")
        st.info(tf.get_speed2051_1(heat))



    # get heat setting:
    elif ssmachine == "Machine 1" and ssheatbox == "Heat" and ssmaterial == "2051" and ssseamtape == "Seam":
        st.text_input(label="Speed", key="speed", value=float(0))
        speed = float(ss["speed"])
        st.text("Heat:")
        st.info(tf.get_heat2051_1(speed))

    # get speed setting:
    elif ssmachine == "Machine 1" and ssheatbox == "Speed" and ssmaterial == "4090" and ssseamtape == "Seam":
        st.text_input(label="Heat", key="heat", value=float(0))
        heat = float(ss["heat"])
        st.text("Speed:")
        st.info(tf.get_speed4090_1(heat))



    # get heat setting:
    elif ssmachine == "Machine 1" and ssheatbox == "Heat" and ssmaterial == "4090" and ssseamtape == "Seam":
        st.text_input(label="Speed", key="speed", value=float(0))
        speed = float(ss["speed"])
        st.text("Heat:")
        st.info(tf.get_heat4090_1(speed))


    # get speed setting:
    elif ssmachine == "Machine 1" and ssheatbox == "Speed" and ssmaterial == "vinyl" and ssseamtape == "Seam":
        st.text_input(label="Heat", key="heat", value=float(0))
        heat = float(ss["heat"])
        st.text("Speed:")
        st.info(tf.get_speedvinyl_1(heat))



    # get heat setting:
    elif ssmachine == "Machine 1" and ssheatbox == "Heat" and ssmaterial == "vinyl" and ssseamtape == "Seam":
        st.text_input(label="Speed", key="speed", value=float(0))
        speed = float(ss["speed"])
        st.text("Heat:")
        st.info(tf.get_heatvinyl_1(speed))


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
        st.info(tf.get_speed1055_4(heat))


    # get heat setting:
    elif ssmachine == "Machine 4" and ssheatbox == "Heat" and ssmaterial == "1055" and ssseamtape == "Seam":
        st.text_input(label="Speed", key="speed", value=float(0))
        speed = float(ss["speed"])
        st.text("Heat:")
        st.info(tf.get_heat1055_4(speed))

    # get speed setting:
    elif ssmachine == "Machine 4" and ssheatbox == "Speed" and ssmaterial == "1365" and ssseamtape == "Seam":
        st.text_input(label="Heat", key="heat", value=float(0))
        heat = float(ss["heat"])
        st.text("Speed:")
        st.info(tf.get_speed1365_4(heat))



    # get heat setting:
    elif ssmachine == "Machine 4" and ssheatbox == "Heat" and ssmaterial == "1365" and ssseamtape == "Seam":
        st.text_input(label="Speed", key="speed", value=float(0))
        speed = float(ss["speed"])
        st.text("Heat:")
        st.info(tf.get_heat1365_4(speed))

    # get speed setting:
    elif ssmachine == "Machine 4" and ssheatbox == "Speed" and ssmaterial == "2051" and ssseamtape == "Seam":
        st.text_input(label="Heat", key="heat", value=float(0))
        heat = float(ss["heat"])
        st.text("Speed:")
        st.info(tf.get_speed2051_4(heat))



    # get heat setting:
    elif ssmachine == "Machine 4" and ssheatbox == "Heat" and ssmaterial == "2051" and ssseamtape == "Seam":
        st.text_input(label="Speed", key="speed", value=float(0))
        speed = float(ss["speed"])
        st.text("Heat:")
        st.info(tf.get_heat2051_4(speed))

    # get speed setting:
    elif ssmachine == "Machine 4" and ssheatbox == "Speed" and ssmaterial == "4090" and ssseamtape == "Seam":
        st.text_input(label="Heat", key="heat", value=float(0))
        heat = float(ss["heat"])
        st.text("Speed:")
        st.info(tf.get_speed4090_4(heat))



    # get heat setting:
    elif ssmachine == "Machine 4" and ssheatbox == "Heat" and ssmaterial == "4090" and ssseamtape == "Seam":
        st.text_input(label="Speed", key="speed", value=float(0))
        speed = float(ss["speed"])
        st.text("Heat:")
        st.info(tf.get_heat4090_4(speed))


    # get speed setting:
    elif ssmachine == "Machine 4" and ssheatbox == "Speed" and ssmaterial == "vinyl" and ssseamtape == "Seam":
        st.text_input(label="Heat", key="heat", value=float(0))
        heat = float(ss["heat"])
        st.text("Speed:")
        st.info(tf.get_speedvinyl_4(heat))



    # get heat setting:
    elif ssmachine == "Machine 4" and ssheatbox == "Heat" and ssmaterial == "vinyl" and ssseamtape == "Seam":
        st.text_input(label="Speed", key="speed", value=float(0))
        speed = float(ss["speed"])
        st.text("Heat:")
        st.info(tf.get_heatvinyl_4(speed))

    st.subheader("This is a Tool/Guideline. Always check your weld. It is still under development. Adding new features soon! Have to Calibrate machine 1 and 4")
except ValueError:
    st.exception("Wrong input. Type in a number.")





#st.session_state