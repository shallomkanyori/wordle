#!/usr/bin/env python3
"""Main module for the Wordle clone"""
from rich.console import Console
from random import choice
from words import word_list
from utils import Util

WELCOME_MESSAGE = f'\n[white on blue] WELCOME TO WORDLE [/]\n'
INSTRUCTIONS = 'You may start guessing\n'
ALLOWED_GUESSES = 6

if __name__ == '__main__':
    console = Console()
    word = choice(word_list)
    console.print(WELCOME_MESSAGE)
    console.print(INSTRUCTIONS)
