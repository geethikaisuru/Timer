import streamlit as st
import time
import base64
from streamlit.components.v1 import html

st.set_page_config(
    layout="centered",
    initial_sidebar_state="auto",
    page_icon="⏳",
    page_title="Hack Like a Girl Timer"
)

# Function to convert sound file to base64 for browser playback
def sound_to_base64(sound_file):
    with open(sound_file, "rb") as f:
        audio_data = f.read()
        return base64.b64encode(audio_data).decode()

# Function to play the sound using JavaScript without displaying the audio player
def play_audio_in_browser(audio_data):
    audio_js = f"""
    <script>
        var audio = new Audio("data:audio/wav;base64,{audio_data}");
        audio.play();
    </script>
    """
    html(audio_js, height=0)  # Ensure no visual component is displayed

# Main Streamlit app
def main():
    st.title("Hack Like a Girl Countdown ⏳✨ ")
    st.write("Set the duration for your timer below:")

    # Input for duration in minutes
    minutes = st.number_input("Duration (in minutes):", min_value=0, max_value=120, step=1, value=1)

    if st.button("Start Timer"):
        # Convert minutes to seconds
        total_seconds = int(minutes * 60)

        # Create a placeholder for updating the countdown
        countdown_placeholder = st.empty()

        # Start countdown
        for remaining in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            time_str = f"{mins:02}:{secs:02}"

            # Always show enlarged countdown
            countdown_placeholder.markdown(
                f"""
                <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
                    <h1 style="font-size: 10rem; color: #333;">{time_str}</h1>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Play the ticking sound in the browser without showing the player
            if remaining > 0:  # Play only for each tick, not when time is up
                tick_audio_data = sound_to_base64("tick.wav")
                play_audio_in_browser(tick_audio_data)

            # Wait exactly one second
            time.sleep(1)

        # Notify when the countdown is over
        countdown_placeholder.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
                <h1 style="font-size: 10rem; color: #333;">00:00</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Play the "Time-up" sound in the browser without showing the player
        time_up_audio_data = sound_to_base64("Time-up.wav")
        play_audio_in_browser(time_up_audio_data)

        st.success("Time's up!")
        st.balloons()

if __name__ == "__main__":
    main()
