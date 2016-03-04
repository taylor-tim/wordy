#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("/home/nerd/dev/boggley/")

import json
import unittest

from lib.word_utils import WordUtils

class TestWordUtils(unittest.TestCase):

    def setUp(self):
        self.wutils = WordUtils()
        with open('tests/word_grid_data.json') as infile:
            json_grid = infile.read()
        self.word_grid = json.loads(json_grid)

    def test_get_dictionary_words(self):
        words = WordUtils.get_dictionary_words()
        self.assertTrue(len(words) > 300000)

    def test_set_to_none(self):
        word_grid = self.wutils.set_to_none(self.word_grid, 1, 1)
        self.assertEqual(word_grid.get('row1').get('col1'), None)

    def test__get_potential_rows(self):
        low_row = self.wutils._get_potential_rows(self.word_grid, 1)
        self.assertTrue(low_row == [1,2]) 
        mid_row = self.wutils._get_potential_rows(self.word_grid, 3)
        self.assertTrue(mid_row == [2,3,4]) 
        high_row = self.wutils._get_potential_rows(self.word_grid, 5)
        self.assertTrue(high_row == [4,5]) 

    def test_full_check_row(self):
        row = self.word_grid.get('row1')

        left_col = self.wutils.check_row(row, 1)
        self.assertEqual(('b', 2), left_col)

        mid_col = self.wutils.check_row(row, 3)
        self.assertEqual(('b', 2), mid_col)

        right_col = self.wutils.check_row(row, 5)
        self.assertEqual(('d', 4), right_col)

    def test_none_in_check_row(self):
        row = {'col1': None, 'col2': 'b', 'col3': None, 'col4': 'd', 'col5': 'e'}

        none_col = self.wutils.check_row(row, 2)
        self.assertEqual((None, None), none_col)

        right_col = self.wutils.check_row(row, 4)
        self.assertEqual(('e', 5), right_col)
   
    def test_get_next_letter(self):
       print "something:"  


if __name__ == '__main__':
    unittest.main()
