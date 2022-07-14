# -*- coding: utf-8 -*-
"""
Final project for DS 5100

@author: Mauricio Mathey
@userID: qwa2uc
"""
### Import packages
import pandas as pd
import numpy as np

### Class die
class die:
    '''A die has N sides, or “faces”, and W weights, and can be rolled to select a face.
    W defaults to 1.0 for each face but can be changed after the object is created.
    Note that the weights are just numbers, not a normalized probability distribution.
    The die has one behavior, which is to be rolled one or more times.
    Note that what we are calling a “die” here can be any discrete random variable,
    associated with a stochastic process, such as using a deck of cards or flipping
    a coin or speaking a language. Our probability model for such variable is, however,
    very simple – since our weights apply to only to single events, we are assuming that
    the events are independent. This makes sense for coin tosses but not for language use.

    Available methods:
    - changew: to change the weight of one face
    - roll: to roll the die N times
    - show: to show the current die faces and weights

    Parameters:
    - Initializing parameter: a list which should represent the die faces
    - changew(side, weight): side should be a value (number or string) that exists in the die, weight must be a number (integer or float)
    - roll(rolls = None): rolls should be an integer value, it defaults to 1 if not present
    - show(): doesn't take any input

    Return values:
    - sides: gives you the faces of the die
    - weights: gives you the weights of the faces
    - roll: returns a list containing the face obtained in each roll
    - show: returns a DataFrame with the faces as column 0 and the weights as column 1'''
    def __init__(self, sides):
        self.sides = sides
        self.weights = [1]*len(self.sides)
        self.__die = pd.DataFrame({'side': self.sides, 'weight': self.weights})
    
    def changew(self, side, weight):
        '''Allows to change the weight of a side, it takes to arguments, the first
        one is the side and the second one is the weight which should be a number.'''
        if side in self.sides:
            if (type(weight) == float) or (type(weight) == int):
                self.__die.loc[self.__die['side'] == side, 'weight'] = weight
            else:
                print("Weights must be a number")
        else:
            print("Specified side is not defined")
    
    def roll(self, rolls = None):
        '''Allows to roll the dice, you only specify the number of rolls, if not
        specified it defaults to 1.'''
        number_rolls = 1 if rolls is None else rolls
        _roll_results = []
        for i in range(1, number_rolls + 1):
            result = self.__die.side.sample(weights = self.__die.weight).values[0]
            _roll_results.append(result)
        return _roll_results
    
    def show(self):
        '''Displays the die sides and weights, no aditional input needed.'''
        return self.__die
    
### Class game
class game:
    '''A game consists of rolling of one or more dice of the same kind one or more times. 
    Each game is initialized with one or more of similarly defined dice (Die objects).
    By “same kind” and “similarly defined” we mean that each die in a given game has
    the same number of sides and associated faces, but each die object may have its own weights.
    The class has a behavior to play a game, i.e. to rolls all of the dice a given number of times.
    The class keeps the results of its most recent play.

    Available methods:
    - play: allows you to play N games
    - show: shows you the result of the last game played, it can display the results in wide or narrow form 

    Parameters:
    - Initializing parameter: it receives a list of dies to play on
    - play(rolls): rolls should be an integer number and it defines the number of times you want to play the game
    - show(wide): wide receives a boolean input (True/False). If True, or missing, it will return the game play results in wide format, if False it will return them in narrow form.

    Return values:
    - object: allows you to access the list of dies you have passed.'''
    def __init__(self, object):
        self.object = object
        
    def play(self, rolls):
        '''Allows to rolls the objects, just need to specify the number of rolls.'''
        self.__game_results = pd.DataFrame([])
        for i in range(0, len(self.object)):
            self.__game_results[i] =  self.object[i].roll(rolls)
    
    def show(self, wide = None):
        '''Allows to show the results of the game. It has an optional input
        which is True or False. If True it shows the results in wide format, if
        False it shows the results in narrow format. It defaults to True.'''
        self.wide = True if wide is None else False
        if self.wide:
            return(self.__game_results)
        else:
            return(self.__game_results.unstack(fill_value = 0).T)
        
### Class analyzer
class analyzer:
    '''An analyzer takes the results of a single game and computes various
    descriptive statistical properties about it. These properties results are
    available as attributes of an Analyzer object.

    Available methods:
    - jackpot: Identifies the number of times all the faces are the same. No input needed.
    - combo: You get the combination of faces obtained during the rolls. No input needed.
    - face_counts: You get the face counts for each roll. No input needed.

    Parameters:
    - Initializing parameter: it receives a game object as input
    - jackpot, combo, and face_counts don't take any input parameters

    Return values:
    - analyze: gives you the game object that is to be analyzed
    - data_type: saves the type of face the die has (number or string)
    - jackpot_play: stores the results of in which plays you got a jackpot
    - number: stores the result of how many jackpots you got
    - combos: stores the result, as a DataFrame, of the permutations of faces and how common they were (count)
    - counts_df: stores the result, as a DataFrame, of the face counts by roll, where the rolls are the index and the faces are the columns'''
    def __init__(self, results):
        self.analyze = results.show()
        self.data_type = type(self.analyze.iloc[0,0])
        self.jackpot_play = []

    def jackpot(self):
        '''Identifies the number of times all the faces are the same. No input needed.'''
        number = 0
        for i in range(0, self.analyze.shape[0]):
            length_row = len(set(self.analyze.iloc[i,:]))
            if length_row == 1:
                play = [i, self.analyze.iloc[i,0]]
                self.jackpot_play.append(play)
                number += 1
        self.jackpot_play = pd.DataFrame(self.jackpot_play)
        self.jackpot_play.columns = ['Play', 'Side']
        self.jackpot_play.set_index('Play', inplace = True)
        return number
    
    def combo(self):
        '''You get the combination of faces obtained during the rolls.
        No input needed'''
        column_names = list(self.analyze.columns)
        combos = pd.DataFrame(self.analyze.groupby(column_names).size())
        combos = combos.rename(columns = {0:'Counts'})
        combos.sort_values(by = 'Counts', ascending = False, inplace = True)
        return combos
    
    def face_counts(self):
        '''You get the face counts for each roll. No input needed.'''
        counts_df = pd.DataFrame(self.analyze.unstack(fill_value = 0).T).reset_index(level = 0)
        counts_df = pd.crosstab(counts_df.index, counts_df.iloc[:,1])
        return counts_df