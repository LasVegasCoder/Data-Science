# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:04:20 2017

@author: Prince Adeyemi
"""

import random


def majority_vote(votes):
    """Calculate and select majority vote from a list of votes"""
    
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] =  1
            
    #Choose a winner
    winner = []
    max_count = max(vote_counts.values())
    #loop over vote and count
    for vote, count in vote_counts.items():
        if count == max_count:ype
            winner.append(vote)
            
    return random.choice(winner)
