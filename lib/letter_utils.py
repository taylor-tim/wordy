#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class LetterUtils(object):
    """
    Handle the utilities for letter manipulation.
    """

    def __init__(self):
        """
        Set up the required variables and sets.
        """
        self.albet = self.get_alphabet()
        self.vowels = ["a", "e", "i", "o", "u"]
        self.consonants = self.get_consonants()

    def get_alphabet(self):
        """
        Get the alphabet.
    
        :return: List of the alphabet.
        """
        albet = list()
        for x in xrange(ord('a'), ord('z')+1):
            albet.append(chr(x))
        return albet

    def get_consonants(self):
        """
        Get the consonants.
        """
        cons = set(self.albet).difference(set(self.vowels))
        return list(cons)

    def get_letter(self):
        """
        Get a randomized letter.

        :return: Letter object for use.
        """
        return random.choice(self.albet)

    def get_vowel(self):
        """
        Get a randomized vowel.

        :return: Vowel object for use.
        """
        return random.choice(self.vowels)

    def get_consonant(self):
        """
        Get a randomized consonant.

        :return: Consonant object for use.
        """
        return random.choice(self.consonants)

class Letter(object):
    """
    Letter object to handle the various properties you'd want to invoke from the letter.
    """
    def __init__(self, letter):
        """
        Set up the attributes.
        """
        self.letter = letter
#        self.repres = iono, figure this out
        self.viable_start = True
