# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

<!-- What did the game look like the first time you ran it?
1.  After winning the game within the expected attempts left, I clicked to start the new game and it allowed me to input new number but did not run. 
    - broken, state not refreshed?
    - history not cleared after clicking start new game
2. The attempts incremented by 1 after correctly guessing in the first attempt, which supposed to be decrementing by 1.
    - This was seen when 
3. The hints were backward, it said go higher when the secret number was lower than the guess number and vice versa when guessing lower, it said guess lower.
4. Unclear about the scoring system/calculation. When I could not guess the secret number within the limited attempts, the final score was -5, and when I guessed the secret number at one attempt, it gave me 70.
5. Wrong range (range not matching with the main screen) shown in the setting side bar.
    - When playing for the first time, the attempts left shown in the main screen is actually one time fewer than the actual attempts the player can play and the count followed that. -> side bar shows Attempts left: 8 (for Normal), but main screen shows Attempts left: 7 and can only guess for 7 times (missing one more attempt) -> Inside the "Developer Debug Info", Attempts: 1 is the default, so this needs to be changed to 0.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards"). -->

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Correct guess on first attempt, then click "Start New Game" | Game resets fully: new secret number, cleared history, functional input | Input field appeared but guesses did nothing; game state not refreshed, history not cleared | none |
| Correct guess on first attempt | Attempts left decrements by 1 (e.g., 7 → 6) | Attempts left incremented by 1 (e.g., 7 → 8) | none |
| Guess a number higher than the secret number (e.g., guess 70, secret is 40) | Display "Too High — guess lower" | Displayed "Too Low — guess higher" (hints were backwards) | none |
| Fail to guess within all attempts; also guess correctly on first try | Reasonable score reflecting performance (e.g., 0 for loss, high positive for quick win) | Score of -5 on loss; score of 70 on first-attempt win — scoring logic unclear/miscalculated | none |
| Start game on Normal difficulty | Sidebar shows "Attempts left: 8"; main screen also shows 8 available attempts | Sidebar showed "Attempts left: 8" but main screen showed "Attempts left: 7" and only allowed 7 guesses (Developer Debug Info defaulted Attempts to 1 instead of 0) | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude Code as my primary AI tool throughout this project. I relied on it to help identify the root causes of bugs, suggest fixes, and explain why certain parts of the code were behaving unexpectedly. It acted as a collaborative partner rather than just a code generator, helping me think through the logic step by step.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One example of a correct AI suggestion was fixing the backwards hint logic. Claude identified that the comparison in the hint function had the return strings swapped — it was returning "Too Low" when the guess was above the secret number, and vice versa. The fix was straightforward: swap the return values in the if-else block. I verified it by running the app and playing the game multiple times with intentionally high and low guesses to confirm the hints matched the actual secret number.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

There was no outright incorrect suggestion during this project, but I noticed that Claude tended to fix bugs one at a time rather than addressing all related issues in a single pass. For example, after fixing the hint logic, the attempts counter bug still remained and needed a separate prompt to resolve. This taught me that I could not assume a single fix would resolve the entire system — I had to actually run the app and play through it after each change to catch what was still broken. It reinforced that AI assistance works best as an iterative loop with hands-on testing, not a one-shot solution.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

Since the app never crashes outright — it keeps running even when logic is wrong — I couldn't rely on error messages alone to confirm a fix. My main method was to manually play the game after each change: making guesses that should trigger each hint direction, winning on the first attempt to check the score, and switching difficulties to verify the range. A bug was only considered fixed when the game behaved exactly as expected across multiple test scenarios, not just the single case I had changed.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

I ran the pytest suite in `tests/test_game_logic.py`, which covered `check_guess`, `update_score`, and `get_range_for_difficulty`. One test that stood out was `test_hint_says_go_lower_when_too_high` — it directly targeted the backwards hint bug by asserting that guessing 60 when the secret is 50 returns a message containing "LOWER". Running this test before the fix would have failed, and passing it after the fix gave me confidence that the logic was corrected. The score accumulation test (`test_score_accumulates_correctly_over_game`) was also useful because it simulated a full game sequence and revealed whether the scoring compounded correctly across multiple attempts.

- Did AI help you design or understand any tests? How?

Yes, I asked Claude to generate test cases and it produced tests that covered the core bugs I had identified during manual play. However, I noticed that Claude could only write meaningful tests for bugs I had already described in my prompts — it had no way to anticipate issues I hadn't mentioned yet. This showed me that AI is effective at translating known problems into test code, but the responsibility of discovering what needs to be tested still falls on the developer through hands-on exploration.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

In most apps, clicking a button triggers only one specific function. In Streamlit, every user interaction — clicking a button, submitting a guess, changing a dropdown — causes the entire Python script to re-execute from top to bottom. This is called a "rerun." The problem is that any regular variable (like `score = 0` or `attempts = 8`) gets reset to its initial value on every rerun, which would wipe out the player's progress after each guess. Session state (`st.session_state`) solves this by acting like a persistent dictionary that survives across reruns for the duration of a user's session. That's why this game stores everything important — the secret number, the score, the attempt count, the guess history — inside `st.session_state` instead of plain variables. I also discovered separately that Streamlit has a hot-reload feature that automatically reflects code changes without restarting the server, though I had been manually restarting it throughout the project before I learned about that.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

One habit I want to carry forward is documenting bugs as I find them — recording which function or line is affected, what the broken behavior was, and adding a comment explaining how it was fixed. This project showed me that bugs in logic-heavy code can be subtle and easy to forget once they're resolved. Having that paper trail made it much easier to write tests later and to explain my fixes clearly. It also gave me a record I could hand to AI with enough context to get useful suggestions without re-explaining everything from scratch.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time, before I point out specific problems I found manually, I would first ask the AI to read through the code independently and identify any logic issues it can spot on its own. In this project I led every conversation by describing a bug I had already found, which meant the AI was always reacting to my findings rather than contributing its own. Combining AI's static code analysis with my hands-on playtesting would likely surface bugs faster and from more angles.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project taught me that AI-generated code can look and run perfectly fine on the surface while hiding logic bugs that only show up through actual use. You cannot trust that a program is correct just because it runs without crashing — you have to manually exercise the features to find the places where the behavior silently diverges from what was intended.
