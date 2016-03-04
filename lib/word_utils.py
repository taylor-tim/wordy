#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class WordUtils(object):
    """
    Utility methods for handling word processes.
    """

    @staticmethod
    def get_dictionary_words():
        """
        Get the list of words in the dictionary.
        Strip out the proper nouns first.

        :return: Set of the words.
        """
        with open('/usr/share/dict/words') as os_list:
            word_list = os_list.readlines()

        word_list = [s for s in word_list if not re.search(r'([A-Z])', s)]

        return set(word_list)

    def set_to_none(self, word_grid, row, col):
        """
        Simple reusable method to set an item in the word grid to None,
        signifying it's been used.

        :param word_grid: The word grid.
        :param row: The row of the item to set to None.
        :param col: The column of the item to set to None.
        :return: the word_grid with the updated item.
        """
        word_grid.get('row{}'.format(row))['col{}'.format(col)] = None
        return word_grid
        
    def _get_potential_rows(self, word_grid, current_row):
        """
        Get a list of the dicts for valid rows to check for next letters.
        
        :param word_grid: The working word grid.
        :param current_row: Int of the row the current letter is on.
        :return: List of the rows from word grid to check.
        """
        potential_rows = list()

        if current_row - 1 > 0:
            potential_rows.append(current_row - 1)

        if current_row + 1 <= len(word_grid.keys()):
            potential_rows.append(current_row + 1)

        potential_rows.append(current_row)
        potential_rows.sort()

        return potential_rows

    def check_row(self, row, current_col):
        """
        Check the row for available characters.

        :param current_row: Dict of the current row being checked.
        :param current_col: Int of the col for the current char.
        :return: Returns the letter and it's col position (or None).
        """
        max_col = len(row.keys())
        prev_col = current_col - 1
        next_col = current_col + 1

        if row.get('col{}'.format(prev_col)) is not None:
            return row.get('col{}'.format(prev_col)), prev_col

        elif current_col == max_col:
            return None, None

        elif row.get('col{}'.format(next_col)) is not None:
            return row.get('col{}'.format(next_col)), next_col

        else:
            return None, None

    def get_next_letter(self, word_grid, current_row, current_col):
        """
        Get the next valid letter to check.

        :param word_grid: The word grid to check.
        :param current_row: The int of the row current letter is in.
        :param current_col: The int of the col current letter is in.
        :return: [Next available letter, the row it's in, the column it's in] or None, the grid.
        """
        potential_rows = self._get_potential_rows(word_grid, current_row)

        for row_num in potential_rows:
            row = word_grid.get('row{}'.format(row_num))
            letter, col = self.check_row(row, current_col)

            if letter is not None:
                word_grid = self.set_to_none(word_grid, row_num, col)
                return letter, row, col, word_grid

        return None, None, None, word_grid









