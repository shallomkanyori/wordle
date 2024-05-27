#!/usr/bin/env python3
"""Main module for the Wordle clone"""
from rich.console import Console
from random import choice
from words import word_list
from utils import Util

WELCOME_MESSAGE = f'\n[white on blue] WELCOME TO WORDLE [/]\n'
GUESS_STATEMENT = 'Enter your guess: '
INSTRUCTIONS = 'You may start guessing\n'
TRIES = 6


def check_guess(guess, answer):
    """Checks a given guess"""

    guessed = []

    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed.append(Util.correct_place(letter))
        elif letter in answer:
            guessed.append(Util.correct_letter(letter))
        else:
            guessed.append(Util.incorrect_letter(letter))

    return ' '.join(guessed)


def game(console, word):
    """Game loop

    Args:
        console: Rich console.
        word (str): The word to guess.
    """

    playing = True
    already_guessed = set()
    all_guessed = []

    while playing:
        guess = input(GUESS_STATEMENT).upper()

        while True:
            if len(guess) != 5:
                console.print('[red]Please enter a 5-letter word!!\n[/]')
            elif guess in already_guessed:
                console.print("[red]You've already guessed this word!!\n[/]")
            else:
                break

            guess = input(GUESS_STATEMENT).upper()

        already_guessed.add(guess)
        guessed = check_guess(guess, word)
        all_guessed.append(guessed)

        console.print('')
        console.print(*all_guessed, sep='\n\n', justify='center')
        console.print('')

        if guess == word or len(already_guessed) == TRIES:
            playing = False

    if guess != word:
        console.print(f'\n[red]WORDLE X/{TRIES}[/]')
        console.print(f'\n[green]Correct Word: {word}[/]')
    else:
        console.print(f'\n[green]WORDLE {len(already_guessed)}/{TRIES}[/]\n')


if __name__ == '__main__':
    console = Console(width=35)
    word = choice(word_list)

    console.print(WELCOME_MESSAGE, justify='center')
    console.print(INSTRUCTIONS, justify='center')

    game(console, word)
