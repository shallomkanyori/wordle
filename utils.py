#!/usr/bin/env python3
"""Utility functions class"""


class Util:
    """Utility methods"""

    @staticmethod
    def correct_place(letter):
        """Returns a styled string for a letter placed correctly"""
        return f'[bold white on green] {letter} [/]'

    @staticmethod
    def correct_letter(letter):
        """Returns a styled string for a letter placed incorrectly"""
        return f'[bold white on yellow] {letter} [/]'

    @staticmethod
    def incorrect_letter(letter):
        """Returns a styled string for an incorrect letter"""
        return f'[bold white on grey39] {letter} [/]'

    @staticmethod
    def prompt(console, prompt_msg, valid):
        """Returns user input to a prompt after validating

        Args:
            console: Rich console.
            prompt_msg (str): The prompt message.
            valid (list of str):  Valid options for the input.
        """
        usr_input = ''

        while usr_input not in valid:
            console.print(prompt_msg, end='')
            usr_input = input("\u00A0").upper().strip()

        return usr_input
