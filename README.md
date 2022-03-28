# AdaGrams

## Skills Assessed

- Following directions and reading comprehension
- Reading tests
- Using git to maintain code
- Manipulating and processing data in lists and strings
- Practicing pair-programming techniques

## Goal

An [anagram](https://en.wikipedia.org/wiki/Anagram) is a word or phrase formed by rearranging the letters of a different word or phrase. In this project you and your partner will be creating _Adagrams_, a game in which a player is given a random set of letters and must make an anagram using those letters.  Each submitted word will score points.

While working on _Adagrams_, it may help to think of a physical metaphor for this game, such as other common word games like _Scrabble_ or _Bananagrams_. These games all feature a _pool_ of letter _tiles_ that the player _draws_ from.

In this version of _Adagrams_, we will only be working with the English alphabet.

![an image of a pile of letter tiles](images/letter-tiles.jpeg)

## Pair Programming

Utilize good pair programming practices. Refer to articles from the [Agile Alliance](http://guide.agilealliance.org/guide/pairing.html), the [Agile Institute](http://powersoftwo.agileinstitute.com/2015/02/benefits-of-pair-programming-revisited.html), and the lesson in Learn titled Intro to Pair Programming from Approaching a Problem if you need a refresher for some best practices. Switch _driver_ and _navigator_ roles often. When there is uncertainty or confusion, step away from the keyboard and discuss, plan, and document on paper or whiteboard before continuing.

## One-Time Project Setup

Follow these directions once, a the beginning of your project:

*Only one member of the team should complete the following two steps steps:*

1. In Github, click on the "Fork" button in github and fork the repository to your Github account.  This will make a copy of the project in your github account. 

![Fork Button](images/fork.png)

2. In Github, add the other member(s) of your team as collaborators to the repository. Do this by a The student who forked the respository should first choosing **Settings** from the top menu bar, then **Manage access** from the left navigation, and finally **Invite teams or people**.

You can find detailed instructions [here](https://help.github.com/articles/inviting-collaborators-to-a-personal-repository/).

![Settings](images/settings.png)

<img src="images/manage-access.png" alt="Manage access" width="250"/>

![Invite teams or people](images/invite.png)

The member(s) who are invite will need to accept the invitation either by accepting an email invitation or accepting the invitation in Github.

Both members of the team will be working from the same forked repository.  Be sure to follow proper git protocol from the Intro to Git topic in Learn.

*Each member of the pair should complete the following steps:*

3. Navigate to your projects folder named `projects`

```bash
$ cd ~/Developer/projects
```

4. "Clone" (download a copy of this project) into your projects folder. This command makes a new folder called `adagrams-py`, and then puts the project into this new folder.  Make sure you are cloning from your copy of the project and not the class version (ada-cX).

```bash
$ git clone ...
```

Use `ls` to confirm there's a new project folder

5. Move your location into this project folder

```bash
$ cd adagrams-py
```

6. Create a virtual environment named `venv` for this project:

```bash
$ python3 -m venv venv
```

7. Activate this environment:

```bash
$ source venv/bin/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

8. Install dependencies once at the beginning of this project with

```bash
# Must be in activated virtual environment
$ pip install -r requirements.txt
```

Summary of one-time project setup:

One person:
- [X] Fork the project respository
- [X] Invite team members to the respository

All team members:
- [ ] `cd` into your `projects` folder
- [ ] Clone the project onto your machine
- [ ] `cd` into the `adagrams-py` folder
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependencies with `pip`

## Project Development Workflow

1. When you want to begin work on this project, ensure that your virtual environment is activated:

```bash
$ source venv/bin/activate
```

2. Run the game and play test your current wave.  Replace the word `wave` below with the wave number (ie, 1, 2, 3 or 4):

```bash
# Must be in activated virtual environment
$ python main.py wave
```

3. Use play-testing wth your partner to guide your development.

4. Use tests to verify your functions after thoroughly play-testing. See instructions for running tests in the section below.

5. Use git to commit your work regularly!  Commit between each wave.

```bash
# Add your current work
$ git add .
$ git commit -m "meaningful message explaining your commit"
```

6. Consider switching driver/navigator rolls. Make sure the current driver pushes using `git push` and the new driver pulls using `git pull`.

7. Move on to the next wave!

8. When you are finished working for the day, deactivate your environment with deactivate or closing the Terminal tab/window

```bash
$ deactivate
```

## Details About How to Run Tests

1. Find the test file that contains the test you want to run.

   - Check the `tests` folder, and find the test file you want to run
   - In that test file, read through each test case


2. Run the tests for your specific wave

```bash
# Must be in activated virtual environment
$ pytest tests/test_wave_01.py
```

3. Run all tests that exist in this project with:

```bash
# Must be in activated virtual environment
$ pytest
```

4. If you want to see any `print` statements print to the console, add `-s` to the end of any `pytest` command:

```bash
# Must be in activated virtual environment
$ pytest -s
```

## Project Write-Up: How to Complete and Submit


The goal of this project is to write code in `game.py` so each of the functions meet the requirements outlined in the Project Directions below. 

Go through the waves one-by-one and build the features of this game.

You will use play-testing and unit tests to drive your development.

At submission time, no matter where you are, submit the project via Learn.

In addition to submitting your Pull Request, submit a reflection the the pair programming reflection prompt.


## Project Directions

### Setup a Pair Plan

First, come up with a "plan of action" for how you want to work as a pair. Discuss your learning style, how you prefer to receive feedback, and one team communication skill you want to improve with this experience.

We recommend spending at least a portion of the time pair programming and working collaboratively from the same machine.  Zoom and screen sharing or [VSCode Live Share](https://code.visualstudio.com/learn/collaboration/live-share) are good tools to consider.  Some teams will choose to pair program and work collaboratively from the same machine for the entire project.  Some teams will choose to divide a portion of the work and combine their code using git. 

### Get Familiar

Take time to read through the Wave 1 implementation requirements and the tests for wave 1. Write down your questions, and spend some time going through your understanding of the requirements and tests with your pair. Make sure you both can run `$ pytest` and see the tests fail.

If, after you and your pair have taken some time to think through the problem and would like direction for how to dissect the problem, or if you need clarity on the terms/vocabulary we used in this project, you can check out [a small hint we've provided](./project_docs/hints.md).

### Wave 1: draw_letters

Your first task is to build a hand of 10 letters for the user. To do so, implement the function `draw_letters` in `game.py`. This method should have the following properties:

- No parameters
- Returns an list of ten strings
  - Each string should contain exactly one letter
  - These represent the hand of letters that the player has drawn
- The letters should be randomly drawn from a pool of letters
  - This letter pool should reflect the distribution of letters as described in the table below
  - There are only 2 available `C` letters, so `draw_letters` cannot ever return more than 2 `C`s
  - Since there are 12 `E`s but only 1 `Z`, it should be 12 times as likely for the user to draw an `E` as a `Z`
- Invoking this function should **not** change the pool of letters
  - Imagine that the user returns their hand to the pool before drawing new letters

#### Distribution of Letters

letter_pool = ["a", "a", "a", "a", "b", "b', "c"]

pool_index = random integer in the range(len(letter_pool))

| Letter : Qty. | Letter : Qty. |
|:------:|:-----:|
| A : 9  | N : 6 |
| B : 2  | O : 8 |
| C : 2  | P : 2 |
| D : 4  | Q : 1 |
| E : 12 | R : 6 |
| F : 2  | S : 4 |
| G : 3  | T : 6 |
| H : 2  | U : 4 |
| I : 9  | V : 2 |
| J : 1  | W : 2 |
| K : 1  | X : 1 |
| L : 4  | Y : 2 |
| M : 2  | Z : 1 |

**Note:** Making sure that the drawn letters match the rules of the letter pool can be straightforward or very difficult, depending on how you build the data structure for the letter pool. It is worth spending some time with your partner to think carefully about this.


### Wave 2: use_available_letters

Next, you need a way to check if an input word (a word a player submits) only uses characters that are contained within a collection (or hand) of drawn letters. Essentially, you need a way to check if the word is an anagram of some or all of the given letters in the hand.

To do so, implement the function called `uses_available_letters` in `game.py`. This function should have the following properties:

- Has two parameters:
   - `word`, the first parameter, describes some input word, and is a string
   - `letter_bank`, the second parameter, describes an array of drawn letters in a hand. You can expect this to be an array of ten strings, with each string representing a letter
- Returns either `True` or `False`
- Returns `True` if every letter in the `input` word is available (in the right quantities) in the `letter_bank`
- Returns `False` if not; if there is a letter in `input` that is not present in the `letter_bank` or has too much of compared to the `letter_bank`

### Wave 3: score_word

Now you need a function returns the score of a given word as defined by the Adagrams game.

Implement the function `score_word` in `game.py`. This method should have the following properties:

- Has one parameter: `word`, which is a string of characters
- Returns an integer representing the number of points
- Each letter within `word` has a point value. The number of points of each letter is summed up to represent the total score of `word`
- Each letter's point value is described in the table below
- If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points

#### Score chart

|Letter                        | Value|
|:----------------------------:|:----:|
|A, E, I, O, U, L, N, R, S, T  |   1  |
|D, G                          |   2  |
|B, C, M, P                    |   3  |
|F, H, V, W, Y                 |   4  |
|K                             |   5  |
|J, X                          |   8  |
|Q, Z                          |   10 |

### Wave 4: get_highest_word_score

After several hands have been drawn, words have been submitted, checked, scored, and played, you need a way to find the highest scoring word. This function looks at the list of `word_list` and calculates which of these words has the highest score, applies any tie-breaking logic, and returns the winning word in a special data structure.

Implement a function called `get_highest_word_score` in `game.py`. This method should have the following properties:

- Has one parameter: `word_list`, which is a list of strings
- Returns a tuple that represents the data of a winning word and it's score.  The tuple must contain the following elements:
  - index 0 ([0]): a string of a word
  - index 1 ([1]): the score of that word
- In the case of tie in scores, use these tie-breaking rules:
    - prefer the word with the fewest letters...
    - ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
    - If the there are multiple words that are the same score and the same length, pick the first one in the supplied list




