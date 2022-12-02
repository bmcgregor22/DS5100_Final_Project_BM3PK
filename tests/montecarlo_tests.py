import unittest
import pandas as pd
import numpy as np
from montecarlo import Die, Game, Analyzer

class MonteCarloTestSuite(unittest.TestCase):
    '''
    This test suite executes unit tests to verify that all class methods are working as designed.
    '''
    def test_0_create_die(self):
        '''
        Unit test to test the initializer method for the Die Class.
        Verify that a data frame was intialized correcty based on an array of faces and default weights
        '''
        #create a test die with 6 faces, all six sides are initiaized with a weight of 1.0
        test1 = Die(pd.array(data=[1,2,3,4,5,6]))
        print ("Printing Die Object")
        print (test1.die_df)

        #create a  data frame with identical values for face and weight
        test_data={
                    'face':[1,2,3,4,5,6],
                    'weight':[1.0,1.0,1.0,1.0,1.0,1.0]
        }
        test_df=pd.DataFrame(test_data)
        test_df.set_index('face', inplace=True)

        message="Test Result is False"
        print ("Printing the test die based on test data ")
        print (test_df)

        # check to see if the data frames are equal
        self.assertTrue(pd.DataFrame.equals(test1.die_df,test_df), message)

    def test_1_create_die(self):
        '''
        Unit test to test the initializer method for the Die Class.
        Verify that weights are set to 1 upon object creation for every face of the die.
        '''
        #create a test die
        test1 = Die(pd.array(data=[1,2,3,4,5,6]))
        print (test1.die_df)

        #test
        message = "The test result is false"

        # check to see if any weights are not equal to 1.0
        if  any(test1.die_df.loc[:,'weight']) != 1.0 :
            test_value = True
        else:
            test_value = False
        self.assertFalse(test_value, message)

    def test_2_change_die_weight(self):
        '''
        Unit test to test method change_weight for the Die class.
        Create a die change its weight passing an integer and
        '''
        #create a test die
        test1 = Die(pd.array(data=[1,2,3,4,5,6]))
        print ("Printing the die before changing weight")
        print (test1.die_df)

        #change the weight of the first face to 3
        test1.change_weight(1,3)

        #test that the resulting weight is a float
        expected = 3.0

        #extract the weight based on the value of the first face
        test_value = test1.die_df.loc[1,'weight']

        self.assertEqual(test_value, expected)
        print ("Printing the die after weight of first face is changed")
        print (test1.die_df)

    def test_3_roll_die(self):
        '''
        Unit test to test the roll_die() method of the Die Class.
        Create a test tie and roll it 10 times. Verify that the resulting outcomes produces 10 results.
        '''
        #create a test die
        test1 = Die(pd.array(data=[1,2,3,4,5,6]))
        print (test1.die_df)
        #roll die 10 times
        outcomes = test1.roll_die(10)
        print ("Printing Outcomes :" + str(outcomes))

        # test
        message = "The test result is false"

        # check to see if 10 results were generated
        self.assertTrue(len(outcomes)==10, message)


    def test_4_show_die(self):
        """
        Unit test to test that the show_die method returns expected results.
        Create a test die with default weights, change the weights and then show that the die reflects all faces and weights (including changes)
        """
        #create a six sided test die
        test1 = Die(pd.array(data=[1,2,3,4,5,6]))
        print (test1.die_df)

        #change weights of three faces of the die
        test1.change_weight(1,2)
        test1.change_weight(2,3)
        test1.change_weight(3,4)

        #test results are a set of tuples with expected results of the die, three dies change weights
        expected = [(1,2),(2,3),(3,4),(4,1),(5,1),(6,1)]

        #create a list of tuples of faces and weights from show die method
        df = test1.show_die()
        test_value = list(zip(df.reset_index().face, df.weight))

        #compare the set of tuples to check they are equal
        self.assertEqual(test_value, expected)
        print (test1.die_df)

    def test_5_create_game(self):
        """
         Unit test to test if a game object was initialized correctly from the Game class.
         Create a game with three indentical die and verify that three die objects exist
        """
        # create three 6 sided die
        sides = [1,2,3,4,5,6]
        myDie1 = Die(sides)
        myDie2 = Die(sides)
        myDie3 = Die(sides)

        # create list of three test tie
        test_die = [myDie1, myDie2, myDie3]

        # initialize a game object of three die and check the number of die objects
        test_game = Game(test_die)
        test = len(test_game.die_objects)

        expected = 3
        self.assertEqual(test,expected)

    def test_6_play_game(self):
        """
        Unit test to verify the result of the play method of the Game class.
        Create a game of 2 die and roll them 5 time verify the results includes a 10 element data frame.
        """
        # create two 6 sided die
        sides = [1,2,3,4,5,6]
        myDie1 = Die(sides)
        myDie2 = Die(sides)

        # create list of two test tie
        test_die = [myDie1, myDie2]

        # initialize a game object of two die
        test_game = Game(test_die)

        #conduct the test
        test_game.play(5)
        test_results = test_game._game_results
        print("printing the test results\n"+ str(test_results))

        test=test_results.size

        #a 10 element data frame is expected from the game results
        expected = 10

        self.assertEqual(test,expected)

    def test_7_show(self):
        """
        Unit test to verify the results of the show method for specifying the Narrow format option
        Play a game and check the resulting data frame size for a narrow format.
        """
         # create two 6 sided die
        sides = [1,2,3,4,5,6]
        myDie1 = Die(sides)
        myDie2 = Die(sides)

        # create list of two test tie
        test_die = [myDie1, myDie2]

        # initialize a game object of two die
        test_game = Game(test_die)

        #conduct the test
        test_game.play(5)
        test_results = test_game.show('N')
        print("printing the test results\n"+ str(test_results))
        test=test_results.size

        #a 10 element data frame is expected from the game results
        expected = 10

        self.assertEqual(test,expected)

    def test_8_analyzer(self):
        """
        Unit test to verify the result of the analyzer object initialization
        """
        # create two 6 sided die
        sides = [1,2,3,4,5,6]
        myDie1 = Die(sides)
        myDie2 = Die(sides)

        # create list of two test tie
        test_die = [myDie1, myDie2]

        # initialize a game object of two die
        test_game = Game(test_die)
        test_game.play(5)

        #conduct the test - check the size of the data frame
        test_analysis = Analyzer(test_game)
        test= test_analysis.game_results_data_n.size

        #a 10 element data frame is expected from the game results
        expected = 10

        self.assertEqual(test,expected)

    def test_9_face_counts_per_roll(self):
        """
        Unit test to verify face counts per role method produces correct results
        """
        # create two 6 sided die
        sides = [1,2,3,4,5,6]
        myDie1 = Die(sides)
        myDie2 = Die(sides)

        # create list of two test tie
        test_die = [myDie1, myDie2]

        # initialize a game object of two die
        test_game = Game(test_die)
        test_game.play(5)

        #generate the analyzer object
        test_analysis = Analyzer(test_game)
        test= test_analysis.face_counts_per_roll().size

        message="Test Failed"
        #check to see that the method returned a populated dataframe
        self.assertTrue(test > 0, message)

    def test_10_jackpot(self):
        """
        Unit test to verify jackpot return an integer
        """
        # create two 6 sided die
        sides = [1,2,3,4,5,6]
        myDie1 = Die(sides)
        myDie2 = Die(sides)

        # create list of two test tie
        test_die = [myDie1, myDie2]

        # initialize a game object of two die
        test_game = Game(test_die)
        test_game.play(5)

        #generate the analyzer object
        test_analysis = Analyzer(test_game)

        message="Test Failed"
        #check to see that the method returned a populated dataframe
        self.assertTrue(isinstance(test_analysis.jackpot(), int), message)

    def test_11_combo(self):
        """
        Unit test to verify combo returns a populated dataframe
        """
        # create two 6 sided die
        sides = [1,2,3,4,5,6]
        myDie1 = Die(sides)
        myDie2 = Die(sides)

        # create list of two test tie
        test_die = [myDie1, myDie2]

        # initialize a game object of two die
        test_game = Game(test_die)
        test_game.play(5)

        #generate the analyzer object
        test_analysis = Analyzer(test_game)
        test=test_analysis.combo().size

        message="Test Failed"
        #check to see that the method returned a populated dataframe
        self.assertTrue(test > 0, message)



if __name__ == '__main__':
    unittest.main(verbosity=3)
