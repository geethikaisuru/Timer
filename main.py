import streamlit as st
import time
import pygame

st.set_page_config(
    layout="centered",
    initial_sidebar_state="auto",
    page_icon="⏳",
    page_title="Hack Like a Girl Timer"
)

# Initialize Pygame Mixer
pygame.mixer.init()

# Function to play the ticking sound
def play_ticking_sound():
    tick_sound = pygame.mixer.Sound("tick.wav")
    tick_sound.play()

# Function to play the "Time-up" sound
def play_time_up_sound():
    time_up_sound = pygame.mixer.Sound("Time-up.wav")
    time_up_sound.play()
    while pygame.mixer.get_busy():  # Wait until the sound finishes playing
        time.sleep(0.1)

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
