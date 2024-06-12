#!/usr/bin/env python3
"""Main module for the Wordle clone"""
from rich.console import Console
from rich.table import Table
from rich.padding import Padding

from random import choice
import enchant
import readline

from words import word_list
from utils import Util

WELCOME_MESSAGE = f'\n[white on blue] WELCOME TO WORDLE [/]\n'
GUESS_STATEMENT = ' Enter your guess:'
INSTRUCTIONS = ('Guess the word!\n'
                '[white on green]Green[/] is a correctly placed letter.\n'
                '[white on yellow]Yellow[/] is an incorrectly placed letter.\n'
                '[white on grey37]Grey[/] is an incorrect letter.\n'
                'Type exit to quit the game\n')
START_MESSAGE = 'You may start guessing\n'
CONTINUE_STATEMENT = ' Would you like to continue (yes/no):'
EXIT_STATEMENT = ' Would you like to quit (yes/no):'
EXIT_MESSAGE = '\n [white on green] Thanks for playing! [/]\n'
TRIES = 6

d = enchant.Dict("en_US")


def check_guess(guess, answer):
    """Checks a given guess"""

    # frequency count for each letter
    answer_counts = {c: answer.count(c) for c in answer}

    guessed = [''] * len(guess)

    # First pass: Correct placements
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed[i] = Util.correct_place(letter)
            answer_counts[letter] -= 1

    # Second pass: Incorrect placements
    for i, letter in enumerate(guess):
        if guessed[i] == '':
            if letter in answer and answer_counts.get(letter, 0) > 0:
                guessed[i] = Util.correct_letter(letter)
                answer_counts[letter] -= 1
            else:
                guessed[i] = Util.incorrect_letter(letter)

    return guessed


def game(console):
    """Game loop

    Args:
        console: Rich console.
    """

    playing = True

    console.print(INSTRUCTIONS, justify='center')

    while playing:
        console.print(START_MESSAGE, justify='center')

        word = choice(word_list)
        grid = Table.grid(padding=1)

        already_guessed = set()
        all_guessed = []

        while True:
            console.print(GUESS_STATEMENT, end='')
            guess = input("\u00A0").upper().strip()

            if guess == 'EXIT':
                playing = False
                break

            while True:
                if len(guess) != 5:
                    console.print('[red] Please enter a 5-letter word\n[/]',
                                  justify='center')

                elif guess in already_guessed:
                    console.print("[red] You've already guessed this word!\n[/]",
                                  justify='center')

                elif not d.check(guess):
                    console.print('[red] Word not found\n[/]',
                                  justify='center')
                else:
                    break

                console.print(GUESS_STATEMENT, end='')
                guess = input("\u00A0").upper().strip()

            already_guessed.add(guess)
            guessed = check_guess(guess, word)
            grid.add_row(*guessed)

            console.print(Padding(grid, (1, 0)), justify='center')

            if guess == word or len(already_guessed) == TRIES:
                break

        if not playing:
            # Player typed exit or quit
            console.print(f'\n[green] Correct Word: {word}[/]')

            exit = Util.prompt(console, EXIT_STATEMENT, ['YES', 'NO'])
            if exit == 'YES':
                console.print(EXIT_MESSAGE, justify='center')
                playing = False
            else:
                console.print('')
                playing = True
        else:

            if guess != word:
                console.print(f'\n[red] WORDLE X/{TRIES}[/]')
                console.print(f'\n[green] Correct Word: {word}[/]')
            else:
                console.print(f'\n[green] WORDLE {len(already_guessed)}/{TRIES}[/]\n')

            keep_playing = Util.prompt(console, CONTINUE_STATEMENT,
                                       ['YES', 'NO'])
            if keep_playing == 'YES':
                console.print('')
                playing = True
            else:
                console.print(EXIT_MESSAGE, justify='center')
                playing = False


if __name__ == '__main__':
    console = Console(width=45)

    console.print(WELCOME_MESSAGE, justify='center')

    game(console)
