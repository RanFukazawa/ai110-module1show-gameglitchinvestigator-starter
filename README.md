# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Check the main screen or the sidebar to confirm difficulty (default: Normal, range 1–100, 8 attempts) — change it via the dropdown if desired
2. Enter a guess (e.g., 50) — game returns "Too High" or "Too Low" and updates the score
3. Narrow down with the next guess (e.g., 25) — game returns "Too Low"
4. Continue guessing; score updates after each attempt (correct guess awards points, wrong guess deducts)
5. If stuck, expand "Developer Debug Info" to see the secret number, attempt count, guess history, and current score
6. Game ends when the correct number is guessed or all attempts are used up
7. Click "New Game" to reset the state, clear history, and start a fresh round

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
================================ test session starts ===============================
collected 14 items                                                                                                                                                                                   
tests/test_game_logic.py::test_winning_guess PASSED                            [  7%]
tests/test_game_logic.py::test_guess_too_high PASSED                           [ 14%]
tests/test_game_logic.py::test_guess_too_low PASSED                            [ 21%]
tests/test_game_logic.py::test_hint_says_go_lower_when_too_high PASSED         [ 28%]
tests/test_game_logic.py::test_hint_says_go_higher_when_too_low PASSED         [ 35%]
tests/test_game_logic.py::test_win_on_first_attempt_gives_90 PASSED            [ 42%]
tests/test_game_logic.py::test_win_on_fifth_attempt_gives_50 PASSED            [ 50%]
tests/test_game_logic.py::test_win_score_never_drops_below_10 PASSED           [ 57%]
tests/test_game_logic.py::test_wrong_guess_too_high_deducts_5 PASSED           [ 64%]
tests/test_game_logic.py::test_wrong_guess_too_low_deducts_5 PASSED            [ 71%]
tests/test_game_logic.py::test_score_accumulates_correctly_over_game PASSED    [ 78%]
tests/test_game_logic.py::test_easy_range PASSED                               [ 85%]
tests/test_game_logic.py::test_normal_range PASSED                             [ 92%]
tests/test_game_logic.py::test_hard_range PASSED                               [100%]

================================= 14 passed in 0.02s ================================

```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
