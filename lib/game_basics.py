#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from lib.letter_utils import LetterUtils


class GameBasics(object):
    """
    Handle the basic functions the board will need.
    """
    def __init__(self):
        """
        Set up required variables and settings.
        """
        self.lutils = LetterUtils()

    def generate_board(self, size=5):
        """
        Generate the board.

        :param size: Int of the board size.
        :return: The board object.
        """
        total_letters = size * size
        grid = dict()

    def generate_letter_list(self, total_letters)
        """
        Generate the list of letters to populate the grid.

        :param total_letters: Int of the total number of letters to gen.
        :return: List of the letters:
        """
        total_vowels = total_letters / 4
        letters = list()

        for x in range(1, total_vowels + 1):
            letters.append(self.lutils.get_vowel())

        for x in range(1, total_letters - total_vowels + 1):
            letters.append(self.lutils.get_letter())

        random.shuffle(letters)
        return letters
