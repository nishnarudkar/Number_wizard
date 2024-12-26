import random
import streamlit as st

# Initialize session state variables
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "max_attempts" not in st.session_state:
    st.session_state.max_attempts = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Easy (10 attempts)"  # Default difficulty

# Reset the game
def reset_game():
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Title and description
st.title("🎯 Number Guessing Game")
st.subheader("Welcome to the Number Guessing Game!")
st.write("I'm thinking of a number between **1 and 100**. Can you guess it?")

# Difficulty selection
difficulty_choice = st.radio("Choose a difficulty level:", ["Easy (10 attempts)", "Hard (5 attempts)"], index=0 if st.session_state.difficulty == "Easy (10 attempts)" else 1)
if difficulty_choice != st.session_state.difficulty:
    st.session_state.difficulty = difficulty_choice
    st.session_state.max_attempts = 10 if difficulty_choice == "Easy (10 attempts)" else 5
    reset_game()
    st.success(f"You switched to {'Easy' if st.session_state.max_attempts == 10 else 'Hard'} mode! You have {st.session_state.max_attempts} attempts.")

# Display current mode
st.write(f"🎮 You are playing on **{'Easy' if st.session_state.max_attempts == 10 else 'Hard'}** mode with {st.session_state.max_attempts} attempts.")

# Input for the guess
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input")
    if st.button("Submit Guess"):
        if guess == st.session_state.number:
            st.success(f"🎉 Congratulations! You guessed the number **{st.session_state.number}** correctly!")
            st.session_state.game_over = True
        else:
            st.session_state.attempts += 1
            if st.session_state.attempts >= st.session_state.max_attempts:
                st.error(f"❌ You've run out of attempts! The number was **{st.session_state.number}**.")
                st.session_state.game_over = True
            else:
                if guess < st.session_state.number:
                    st.warning("Your guess is **too low**. Try again!")
                else:
                    st.warning("Your guess is **too high**. Try again!")
                st.info(f"You have **{st.session_state.max_attempts - st.session_state.attempts}** attempts remaining.")

# Reset Button
if st.session_state.game_over:
    if st.button("Play Again"):
        reset_game()

st.write("Thank you for playing! 🎮")
