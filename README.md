# 🎯 Number Wizard

Welcome to **Number Wizard**, an engaging and interactive number-guessing game built using **Streamlit**. Test your guessing skills with different difficulty levels, track your attempts, and compete with yourself!

---

## 🚀 Features

- **Dynamic Difficulty Levels**: Choose between Easy (10 attempts) and Hard (5 attempts).
- **Interactive Gameplay**: Real-time feedback on guesses—too high, too low, or correct!
- **Seamless Restart**: Play as many times as you want with the reset functionality.
- **User-Friendly Interface**: Built with a clean and intuitive UI using Streamlit.

---

## 📸 Screenshots

### 1. Home Screen
![Home Screen](https://github.com/nishnarudkar/Number_wizard/blob/main/screenshots/home_screen.png)  
*Choose your difficulty level and start the game.*

### 2. Gameplay in Progress
![Gameplay](https://github.com/nishnarudkar/Number_wizard/blob/main/screenshots/gameplay_in_progress.png)  
*Guess the number and get instant feedback.*

### 3. Game Over
![Game Over](https://github.com/nishnarudkar/Number_wizard/blob/main/screenshots/gamewin.png)  
*Celebrate your win or restart for another try.*

---

## 🛠️ Technologies Used

- **Python**: Core logic and functionality.
- **Streamlit**: Web application framework for building interactive UIs.
- **Random**: For generating a random target number.

---

## 📖 How to Play

1. Launch the application.
2. Select your difficulty:
   - **Easy**: You get 10 attempts to guess the number.
   - **Hard**: You get 5 attempts to guess the number.
3. Enter your guess in the input box and click **Submit Guess**.
4. Receive feedback:
   - **Too Low**: Your guess is below the target number.
   - **Too High**: Your guess exceeds the target number.
   - **Correct**: 🎉 You guessed it!
5. Track your remaining attempts and adjust your guesses accordingly.
6. If you run out of attempts, restart the game and try again!

---

## 💻 Installation and Usage

### Prerequisites

- Python 3.7 or higher installed on your system.

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/nishnarudkar/number-wizard.git
   cd number-wizard
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run main.py
   ```

4. Open the URL displayed in the terminal (e.g., `http://localhost:8501`) in your browser to play the game.

---

## 📦 Folder Structure

```
Number-Wizard/
│
├── main.py              # Main Streamlit application
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
├── screenshots/        # Folder for screenshots
```

---

## 🌟 Future Enhancements

- Add a leaderboard to track high scores.
- Implement custom difficulty levels (e.g., user-defined ranges or attempts).
- Add visualizations for guessing patterns.
- Introduce a timer to challenge players to guess faster.
- Enhance UI with animations or themed designs.

---

## 🤝 Contribution Guidelines

We welcome contributions to make this project even better! Follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your forked repository:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## 🧑‍💻 Author

**Your Name**  
- GitHub: [nishnarudkar](https://github.com/nishnarudkar)  
- LinkedIn: [NishantNarudkar](https://www.linkedin.com/in/nishant-narudkar-1b5225238/)  

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as you like.
