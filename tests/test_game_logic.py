from logic_utils import check_guess, update_score, get_range_for_difficulty


# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_says_go_lower_when_too_high():
    # Bug was: hint said "Go HIGHER" when guess was above secret
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_hint_says_go_higher_when_too_low():
    # Bug was: hint said "Go LOWER" when guess was below secret
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


# --- update_score ---

def test_win_on_first_attempt_gives_90():
    # 100 - 10 * 1 = 90; bug was +1 off-by-one giving 80
    score = update_score(0, "Win", 1)
    assert score == 90

def test_win_on_fifth_attempt_gives_50():
    score = update_score(0, "Win", 5)
    assert score == 50

def test_win_score_never_drops_below_10():
    # attempt 10+: 100 - 100 = 0, but floor is 10
    score = update_score(0, "Win", 15)
    assert score == 10

def test_wrong_guess_too_high_deducts_5():
    # Bug was: even attempts added +5 instead of deducting
    score = update_score(50, "Too High", 2)
    assert score == 45

def test_wrong_guess_too_low_deducts_5():
    score = update_score(50, "Too Low", 3)
    assert score == 45

def test_score_accumulates_correctly_over_game():
    # 4 wrong guesses then win on attempt 5
    score = 0
    for attempt in range(1, 5):
        score = update_score(score, "Too Low", attempt)   # -5 each = -20
    score = update_score(score, "Win", 5)                 # + 50
    assert score == 30


# --- get_range_for_difficulty ---

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_hard_range():
    # Bug: Hard was returning (1, 50) instead of a tighter range
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 50
