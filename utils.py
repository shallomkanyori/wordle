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
