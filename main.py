#!/usr/bin/env python3
"""Main module for the Wordle clone"""
from rich.console import Console
from random import choice
from words import word_list
from utils import Util

WELCOME_MESSAGE = f'\n[white on blue] WELCOME TO WORDLE [/]\n'
GUESS_STATEMENT = 'Enter your guess'
INSTRUCTIONS = 'You may start guessing\n'
ALLOWED_GUESSES = 6


def check_guess(guess, answer):
    """Checks a given guess"""

    guessed = []

    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += Util.correct_place(letter)
        elif letter in answer:
            guessed += Util.correct_letter(letter)
        else:
            guessed += Util.incorrect_letter(letter)

    return ''.join(guessed)


if __name__ == '__main__':
    console = Console()
    word = choice(word_list)
    console.print(WELCOME_MESSAGE)
    console.print(INSTRUCTIONS)
