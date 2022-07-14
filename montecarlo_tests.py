# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 09:02:07 2022

@author: Mauricio
"""

import unittest
from montecarlosim.montecarlo import die
from montecarlosim.montecarlo import game
from montecarlosim.montecarlo import analyzer

class MontecarloTestSuite(unittest.TestCase):
    
    def test_changew_show(self):
    #The assumption here is that if the die is not correctly created I would not
    #be able to change the weight, therefore I am not testing for the creation of the
    #die. Furthermore, to test the correct change of weight I also need to test that
    #show is working so I can reference the cell and validate that the weight was changed,
    #this is why I'm also including the show test in this function.
        die1 = [1,2,3,4,5]
        test1 = die(die1)
        test1.changew(1,5)
        
        expected_value = 5
        real_value = test1.show().iloc[0,1]
        self.assertEqual(real_value, expected_value)
        
    def test_roll(self):
        #Roll do need an independent testing to verify tht it is working correctly.
        die1 = [1,2,3,4,5]
        test2 = die(die1)
        
        self.assertEqual(len(test2.roll(5)), 5)
    
    def test_play_show(self):
        #A similar logic is followed here, if the object is being created correctly
        #then I would be able to load it onto the game class and to test that it has been
        #correctly interpreted I test play. If play works, then I can be sure that the
        #basics are correct.
        die1 = die([1,2,3,4,5])
        dies_test = [die1,die1]
        test3 = game(dies_test)
        test3.play(5)
        
        self.assertEqual(len(test3.show().index), 5)
    
    def test_jackpot(self):
        #Jackpot, combo, and face counts do need their own testing functions, which
        #is what I did from this moment onwards
        die1 = die([1,2,3,4,5])
        dies_test = [die1,die1]
        test4a = game(dies_test)
        test4a.play(100)
        
        expected_type = type(analyzer(test4a).jackpot())
        
        self.assertTrue(expected_type == int)
    
    def test_combo(self):
        die1 = die([1,2,3,4,5])
        dies_test = [die1,die1]
        test5a = game(dies_test)
        test5a.play(100)
        test5b = analyzer(test5a)
        
        self.assertFalse(test5b.combo().empty)
    
    def test_face_count(self):
        die1 = die([1,2,3,4,5])
        dies_test = [die1,die1]
        test6a = game(dies_test)
        test6a.play(5)
        test6b = analyzer(test6a)
        
        self.assertFalse(test6b.face_counts().empty)

if __name__ == '__main__':
    
    unittest.main(verbosity=3)
