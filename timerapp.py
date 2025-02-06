import streamlit as st
import time
from playsound import playsound

st.title("10-Second Timer")

# Initialize session state if not already done
if 'time_left' not in st.session_state:
    st.session_state.time_left = 10
    st.session_state.running = False
    st.session_state.last_click_time = 0
    st.session_state.paused = False

# Function to play a sound when the timer ends
def play_sound():
    # Use st.audio for browser playback of audio
    st.audio("316839__lalks__alarm-02-long.wav", format="audio/wav")




# Function to start or restart the timer
def start_timer():
    st.session_state.running = True
    st.session_state.paused = False
    while st.session_state.running and st.session_state.time_left > 0:
        time.sleep(1)
        st.session_state.time_left -= 1
        placeholder.markdown(f"<h1 style='text-align: center; font-size: 72px;'>{st.session_state.time_left} seconds left</h1>", unsafe_allow_html=True)
        if not st.session_state.running:
            break
    if st.session_state.time_left == 0:
        play_sound()

# Function to stop the timer
def stop_timer():
    st.session_state.running = False
    st.session_state.paused = True

# Function to reset and restart the timer
def reset_timer():
    st.session_state.time_left = 10
    start_timer()

placeholder = st.empty()
placeholder.markdown(f"<h1 style='text-align: center; font-size: 72px;'>{st.session_state.time_left} seconds left</h1>", unsafe_allow_html=True)

# Style for circular buttons
st.markdown("""
    <style>
    div.stButton > button {
        width: 150px;
        height: 150px;
        font-size: 20px;
        border-radius: 50%;
        background-color: blue;
        color: white;
        border: none;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background-color: darkblue;
    }
    </style>
""", unsafe_allow_html=True)

# Buttons for controlling the timer
col1, col2 = st.columns(2)

# Start / Reset button
with col1:
    if st.button("Start / Reset"):
        reset_timer()

# Stop / Resume button
with col2:
    if st.button("Stop / Resume"):
        if st.session_state.running:
            stop_timer()
        else:
            start_timer()
