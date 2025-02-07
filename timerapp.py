import streamlit as st
import time

st.title("10-Second Timer")

# Initialize session state if not already done
if 'time_left' not in st.session_state:
    st.session_state.time_left = 10
    st.session_state.running = False
    st.session_state.last_click_time = 0
    st.session_state.paused = False
    st.session_state.play_sound = False  # Initialize play_sound here

# Function to play a sound when the timer ends
def play_sound():
    st.session_state.play_sound = True  # Set the flag to play audio

# Function to start or restart the timer
def start_timer():
    st.session_state.running = True
    st.session_state.paused = False
    st.session_state.play_sound = False  # Reset sound trigger
    while st.session_state.running and st.session_state.time_left > 0:
        time.sleep(1)
        st.session_state.time_left -= 1
        placeholder.markdown(
            f"<h1 style='text-align: center; font-size: 72px;'>{st.session_state.time_left} seconds left</h1>",
            unsafe_allow_html=True
        )
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
placeholder.markdown(
    f"<h1 style
