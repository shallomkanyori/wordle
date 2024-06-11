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
INSTRUCTIONS = 'You may start guessing\n'
CONTINUE_STATEMENT = ' Would you like to continue (yes/no):'
EXIT_STATEMENT = '\n [white on green] Thanks for playing! [/]\n'
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

    while playing:
        console.print(INSTRUCTIONS, justify='center')

        word = choice(word_list)
        grid = Table.grid(padding=1)

        already_guessed = set()
        all_guessed = []

        while True:
            console.print(GUESS_STATEMENT, end='')
            guess = input("\u00A0").upper().strip()

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

        if guess != word:
            console.print(f'\n[red] WORDLE X/{TRIES}[/]')
            console.print(f'\n[green] Correct Word: {word}[/]')
        else:
            console.print(f'\n[green] WORDLE {len(already_guessed)}/{TRIES}[/]\n')

        console.print(CONTINUE_STATEMENT, end='')
        keep_playing = input("\u00A0").upper().strip()
        while keep_playing != 'YES' and keep_playing != 'NO':
            console.print(CONTINUE_STATEMENT, end='')
            keep_playing = input("\u00A0").upper().strip()

        if keep_playing == 'YES':
            console.print('')
            playing = True
        else:
            console.print(EXIT_STATEMENT, justify='center')
            playing = False


if __name__ == '__main__':
    console = Console(width=45)

    console.print(WELCOME_MESSAGE, justify='center')

    game(console)
