import streamlit as st
import time
import simpleaudio as sa

st.set_page_config(
    layout="centered",
    initial_sidebar_state="auto",
    page_icon="⏳",
    page_title="Hack Like a Girl Timer"
)

# Function to play the ticking sound
def play_ticking_sound():
    tick_sound = sa.WaveObject.from_wave_file("tick.wav")
    play_obj = tick_sound.play()
    #play_obj.wait_done()  # Ensure the sound plays completely before moving on

# Function to play the "Time-up" sound
def play_time_up_sound():
    time_up_sound = sa.WaveObject.from_wave_file("Time-up.wav")
    play_obj = time_up_sound.play()
    play_obj.wait_done()

# Main Streamlit app
def main():
    st.title("Hack Like a Girl ⏳✨ ")
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

            # Play the ticking sound for each second
            play_ticking_sound()

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

        # Play the "Time-up" sound
        play_time_up_sound()

        st.success("Time's up!")
        st.balloons()

if __name__ == "__main__":
    main()
