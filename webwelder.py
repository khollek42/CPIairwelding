import streamlit as st
import functions as tf
import base64


#sets local background img
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


set_png_as_page_bg('background.png')


col1, col2 = st.columns([.2,.8])
with col1:
    st.image("cpilogo.png")
with col2:
    st.title("Air Welding")

#Selection boxes:
st.selectbox('Machine: ', ("Machine 1", "Machine 2", "Machine 3", "Machine 4"), key='machine')
st.selectbox("Material: ", ("1055", "1365", "2051", "4090", "vinyl"), key='material')

col3, col4 = st.columns(2)
with col3:
    st.selectbox("Seam or Tape:", ("Seam","Tape"), key="seamtape")
with col4:
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
        st.selectbox("Wheel Size", ["1 in", "2 in"], key="wheel_size")
        if st.session_state["wheel_size"] == "1 in":
            st.text_input(label="Heat", key="heat", value=float(0))
            heat = float(ss["heat"])
            st.text("Speed:")
            st.info(tf.get_speed1055_2(heat))
        elif st.session_state["wheel_size"] == "2 in":
            st.text_input(label="Heat", key="heat", value=float(0))
            heat = float(ss["heat"])
            st.text("Speed:")
            st.info(tf.get_speed1055_2_2(heat))




    # get heat setting:
    elif ssmachine == "Machine 2" and ssheatbox == "Heat" and ssmaterial == "1055" and ssseamtape == "Seam":
        st.selectbox("Wheel Size", ["1 in", "2 in"], key="wheel_size")
        if st.session_state["wheel_size"] == "1 in":
            st.text_input(label="Speed", key="speed", value=float(0))
            speed = float(ss["speed"])
            st.text("Heat:")
            st.info(tf.get_heat1055_2(speed))
        elif st.session_state["wheel_size"] == "2 in":
            st.text_input(label="Speed", key="speed", value=float(0))
            speed = float(ss["speed"])
            st.text("Heat:")
            st.info(tf.get_heat1055_2_2(speed))



    # get speed setting:
    elif ssmachine == "Machine 2" and ssheatbox == "Speed" and ssmaterial == "1365" and ssseamtape == "Seam":
        st.selectbox("Wheel Size", ["1 in", "2 in"], key="wheel_size")
        if st.session_state["wheel_size"] == "1 in":
            st.text_input(label="Heat", key="heat", value=float(0))
            heat = float(ss["heat"])
            st.text("Speed:")
            st.info(tf.get_speed1365_2(heat))
        elif st.session_state["wheel_size"] == "2 in":
            st.text_input(label="Heat", key="heat", value=float(0))
            heat = float(ss["heat"])
            st.text("Speed:")
            st.info(tf.get_speed1365_2_2(heat))



    # get heat setting:
    elif ssmachine == "Machine 2" and ssheatbox == "Heat" and ssmaterial == "1365" and ssseamtape == "Seam":
        st.selectbox("Wheel Size", ["1 in", "2 in"], key="wheel_size")
        if st.session_state["wheel_size"] == "1 in":
            st.text_input(label="Speed", key="speed", value=float(0))
            speed = float(ss["speed"])
            st.text("Heat:")
            st.info(tf.get_heat1365_2(speed))
        elif st.session_state["wheel_size"] == "2 in":
            st.text_input(label="Speed", key="speed", value=float(0))
            speed = float(ss["speed"])
            st.text("Heat:")
            st.info(tf.get_heat1365_2_2(speed))


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
        st.selectbox("Wheel Size", ["1 in", "2 in"], key="wheel_size")
        if st.session_state["wheel_size"] == "1 in":
            st.text_input(label="Heat", key="heat", value=float(0))
            heat = float(ss["heat"])
            st.text("Speed:")
            st.info(tf.get_speed4090_2(heat))
        if st.session_state["wheel_size"] == "2 in":
            st.text_input(label="Heat", key="heat", value=float(0))
            heat = float(ss["heat"])
            st.text("Speed:")
            st.info(tf.get_speed4090_2_2(heat))


    # get heat setting:
    elif ssmachine == "Machine 2" and ssheatbox == "Heat" and ssmaterial == "4090" and ssseamtape == "Seam":
        st.selectbox("Wheel Size", ["1 in", "2 in"], key="wheel_size")
        if st.session_state["wheel_size"] == "1 in":
            st.text_input(label="Speed", key="speed", value=float(0))
            speed = float(ss["speed"])
            st.text("Heat:")
            st.info(tf.get_heat4090_2(speed))
        if st.session_state["wheel_size"] == "2 in":
            st.text_input(label="Speed", key="speed", value=float(0))
            speed = float(ss["speed"])
            st.text("Heat:")
            st.info(tf.get_heat4090_2_2(speed))


    # get speed setting:
    elif ssmachine == "Machine 2" and ssheatbox == "Speed" and ssmaterial == "vinyl" and ssseamtape == "Seam":
        st.selectbox("Wheel Size", ["1 in", "2 in"], key="wheel_size")
        if st.session_state["wheel_size"] == "1 in":
            st.text_input(label="Heat", key="heat", value=float(0))
            heat = float(ss["heat"])
            st.text("Speed:")
            st.info(tf.get_speedvinyl_2(heat))
        if st.session_state["wheel_size"] == "2 in":
            st.text_input(label="Heat", key="heat", value=float(0))
            heat = float(ss["heat"])
            st.text("Speed:")
            st.info(tf.get_speedvinyl_2_2(heat))

    # get heat setting:
    elif ssmachine == "Machine 2" and ssheatbox == "Heat" and ssmaterial == "vinyl" and ssseamtape == "Seam":
        st.selectbox("Wheel Size", ["1 in", "2 in"], key="wheel_size")
        if st.session_state["wheel_size"] == "1 in":
            st.text_input(label="Speed", key="speed", value=float(0))
            speed = float(ss["speed"])
            st.text("Heat:")
            st.info(tf.get_heatvinyl_2(speed))
        if st.session_state["wheel_size"] == "2 in":
            st.text_input(label="Speed", key="speed", value=float(0))
            speed = float(ss["speed"])
            st.text("Heat:")
            st.info(tf.get_heatvinyl_2_2(speed))

    # machine 3
    # get speed setting:
    if ssmachine == "Machine 3" and ssheatbox == "Speed" and ssmaterial == "1055" and ssseamtape == "Seam":
        st.text_input(label="Heat", key="heat", value=float(0))
        heat = float(ss["heat"])
        st.text("Speed:")
        st.info(tf.get_speed1055_3(heat))


    # get heat setting:
    elif ssmachine == "Machine 3" and ssheatbox == "Heat" and ssmaterial == "1055" and ssseamtape == "Seam":
        st.text_input(label="Speed", key="speed", value=float(0))
        speed = float(ss["speed"])
        st.text("Heat:")
        st.info(tf.get_heat1055_3(speed))

    # get speed setting:
#    elif ssmachine == "Machine 3" and ssheatbox == "Speed" and ssmaterial == "1365" and ssseamtape == "Seam":
#        st.text_input(label="Heat", key="heat", value=float(0))
#        heat = float(ss["heat"])
#        st.text("Speed:")
#        st.info(tf.get_speed1365_3(heat))



    # get heat setting:
#    elif ssmachine == "Machine 3" and ssheatbox == "Heat" and ssmaterial == "1365" and ssseamtape == "Seam":
#        st.text_input(label="Speed", key="speed", value=float(0))
#        speed = float(ss["speed"])
#        st.text("Heat:")
#        st.info(tf.get_heat1365_3(speed))

    # get speed setting:
#    elif ssmachine == "Machine 3" and ssheatbox == "Speed" and ssmaterial == "2051" and ssseamtape == "Seam":
#        st.text_input(label="Heat", key="heat", value=float(0))
#        heat = float(ss["heat"])
#        st.text("Speed:")
#        st.info(tf.get_speed2051_3(heat))



    # get heat setting:
#    elif ssmachine == "Machine 3" and ssheatbox == "Heat" and ssmaterial == "2051" and ssseamtape == "Seam":
#        st.text_input(label="Speed", key="speed", value=float(0))
#        speed = float(ss["speed"])
#        st.text("Heat:")
#        st.info(tf.get_heat2051_3(speed))

    # get speed setting:
#    elif ssmachine == "Machine 3" and ssheatbox == "Speed" and ssmaterial == "4090" and ssseamtape == "Seam":
#        st.text_input(label="Heat", key="heat", value=float(0))
#        heat = float(ss["heat"])
#        st.text("Speed:")
#        st.info(tf.get_speed4090_3(heat))



    # get heat setting:
#    elif ssmachine == "Machine 3" and ssheatbox == "Heat" and ssmaterial == "4090" and ssseamtape == "Seam":
#        st.text_input(label="Speed", key="speed", value=float(0))
#        speed = float(ss["speed"])
#        st.text("Heat:")
#        st.info(tf.get_heat4090_3(speed))


    # get speed setting:
    elif ssmachine == "Machine 3" and ssheatbox == "Speed" and ssmaterial == "vinyl" and ssseamtape == "Seam":
        st.text_input(label="Heat", key="heat", value=float(0))
        heat = float(ss["heat"])
        st.text("Speed:")
        st.info(tf.get_speedvinyl_3(heat))



    # get heat setting:
    elif ssmachine == "Machine 3" and ssheatbox == "Heat" and ssmaterial == "vinyl" and ssseamtape == "Seam":
        st.text_input(label="Speed", key="speed", value=float(0))
        speed = float(ss["speed"])
        st.text("Heat:")
        st.info(tf.get_heatvinyl_3(speed))

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

    st.subheader("This is a Tool/Guideline. Always check your weld. It is still under development. Adding new features soon! ")
except ValueError:
    st.exception("Wrong input. Type in a number.")





#st.session_state