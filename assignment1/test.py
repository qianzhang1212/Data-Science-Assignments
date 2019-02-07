# -*- coding: utf-8 -*-
"""
Created on Sat Feb 02 16:00:20 2019

@author: ZQ
"""
import sys


def create_sent_dict(sentiment_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

        Args:
            sentiment_file (string): The name of a tab-separated file that contains
                                     all terms and scores (e.g., the AFINN file).

        Returns:
            dicitonary: A dictionary with schema d[term] = score
    """
    scores = {}

    afinnfile = open(sentiment_file, 'r')
    scores = {}
    for line in afinnfile:
        term, score = line.split('\t')
        scores[term] = score

    afinnfile.close()

    return scores


sentiment_file = "AFINN-111.txt"


sent_scores = create_sent_dict(sentiment_file)

for term in sent_scores.keys():
    words = term.split()
    if len(words)>=2:
        print(len(words))
        print(term)