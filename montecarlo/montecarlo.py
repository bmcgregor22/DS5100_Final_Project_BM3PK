import pandas as pd
import numpy as np

class Die():
    """
    This class define method for a die object, which represents a variety of random variables
    The constructor takes a array object of faces as an argument.

    Attributes:
    -----------
    self.die_obj - the data defining an instance of die as a data frame
    self.faces - an array object of faces established an instance creation. The array may be an array of strings or an array of numbers.  The array cannot have any duplicate values.

    Methods:
    -----------
    init_(self, faces) - initializes the class taking an array of faces as an argument. A array of a faces is passed as an argument. The array may be an array of strings or numbers.
    change_weight(self, a_side, a_weight) - changes the weight of one of the sides of the die
    roll_die(self, num_rolls=1) - rolls an instance of a die the number of times specfied by num_rolls
    show_die(self) - displays the die's current defintion of faces and weights
    """

    def __init__(self, faces):
        """
        This is the initializer method for class Die. It creates an instance of the die with the specified number of faces. By default, all sides are initially assigned a weight=1.
        """

        #save the values in the array as a unique set of values
        self.faces=np.unique(faces)

        #create a die object data frame and initialize all weightd to 1
        self.die_df=pd.DataFrame({'face':self.faces, 'weight':1.0})


    def change_weight(self, a_face, a_weight):
        """
        This method changes the weight of one of the sides of the die to the specified weight.

        arg[1] specifies  the face that is to be changed
        arg[2] specified the weight that the face will be changed
        """

        self.face=a_face
        self.weight=a_weight

        #check to see that the provided side is defined for the die object.
        if self.face in self.die_df.set_index('face').index:

            #update the value of weight in the data frame to the weight given by the argument
            self.die_df.loc[self.die_df['face'] == self.face, ['weight']] = self.weight


        else :
            #if the face does not exist in the array then exit
            raise Exception("Value for face not in the face array. Must specify a valid value for face")

        #verify that the value passes as a_weight can be converted to a float
        try:
            float(a_weight)
        except:

            # if the conversion to float fails, then exit
            raise Exception("Invalid argument specificed for weight. Weight must be of type integer or float.")



    def roll_die(self, num_rolls=1):
        """
        Method to roll the die by a specified number of times. The default number of rolls is 1. The method returns a list of outcomes of the each roll.
        """

        self.num_rolls = num_rolls
        outcomes = []


        for i in range(self.num_rolls):
            result = self.die_df.face.sample(weights=self.die_df.weight).values[0]
            outcomes.append(result)
        return outcomes


    def show_die(self):
        """
        Method to show the current set of die faces and weights, reflecting any changes to weights. Returns the die object as a panda dataframe.
        """

        return self.die_df

class Game():
    """
    A class representing a game. A game consists of rolling one or more die of the same kind one or more times. In a given game, each die has the same number of sides and set of faces,
    but each die may have different weights.

    Attributes
    ----------
    self.die_objects - a list of die objects created by the Die class, defined with same number of sides and set of faces.

    Methods
    ---------
     __init__(self,l_die_objects) - intializer method to create the game instance using a list of already instantiated die objects

    play(self, num_rolls) - rolls reach die the number of times specified by the argument num_rolls

    show_results(self, format="W') - displays the results of the game in wide format by default. For narrow format, specify format='N'

    """

    def __init__(self, l_die_objects):
        """
        Create the game instance based on a list of die objects
        """

        #initialize the game with a list of similarily defined  die objects.
        self.die_objects = l_die_objects

    def play(self,num_rolls):
        """
        Rolls each of the die objects the num_rolls number of times.

        _game_results - private data frame to store results

        """

        #pass in the number of times the dice should be rolled
        self.num_rolls = num_rolls

        #create a data frame to store the game results and set the first column as the Roll Number
        self._game_results = pd.DataFrame({'Roll Number':range(1, self.num_rolls+1)})


        #for each die object, call the roll_die method and roll the number of times specified by num_rolls
        for i in range(len(self.die_objects)):

            #get a list of the results of each die object rolled the specified number of rolls
            results = self.die_objects[i].roll_die(self.num_rolls)

            #create a column for results for each die and concatenate it to the data frame in wide format
            self.results = pd.Series(results, name=i+1)
            self._game_results=pd.concat([self._game_results, self.results],axis=1)

        #make the roll number the named index for the data frame
        self._game_results.set_index(['Roll Number'],inplace=True)

        #rename the column axis with descriptive label
        self._game_results.rename_axis(columns="Die Number", inplace=True)


    def show(self, format='W'):
        """
        Displays the result of the data frame in narrow or wide format. Wide format is the default. The argument is
        specified as  W for wide, or N for narrow.

        Wide format will have a single column index with the roll number, and each die number as a column
        Narrow format will have a two-column index with the roll number and die number, and a single column for the face
        rolled

        _game_results_narrow - private dataframe to store the narrow format with two column index

        """

        self.format = format
        if self.format == 'W':

            return self._game_results

        elif self.format =='N':

            #convert to a narrow format
            _game_results_narrow = self._game_results.stack().to_frame('Face Rolled')

            return _game_results_narrow
        else:
            raise TypeError("Invalid argument specificed for format. Format argument expect 'N' or 'W'. ")


class Analyzer():
    """
    Analyzes the results of a game and produces various statistics about the game such as the number of jackpots and combinations

    Attributes
    ---------
    face_counts_per_roll_df - a dataframe storing the count of the  number of faces per roll

    jackpot - the number of jackpots rolled

    jackpot_df - an data frame storing the number of jackpots

    combo_df = a dataframe storing the distinct combinations rolled and their counts


    Methods
    ---------
    __init__ (self, a_game_object) - constructor method based on being passed a game object

    face_counts_per_roll(self) - method to compute how many times a given face is rolled in each event.

    jackpot(self) - method to compute the number of jackpots in a game

    combo(self) - method to compute the number of distinct combinations produced in a game

    """

    def __init__(self, a_game_object):
        """
        Creates an instance of the Analyzer class provided the game results.

        Arg1 - a game object instance
        """

        #store the dataframe results in the narrow and wide format
        self.game_results_data_n = a_game_object.show('N')
        self.game_results_data_w = a_game_object.show()



    def face_counts_per_roll(self):
        """
        Computes how many times a given face is rolled in each event. Returns the results in a data frame face_counts_per_roll_df.
        """

        self.face_counts_per_roll_df = \
        self.game_results_data_n.\
        groupby(['Roll Number','Face Rolled']).\
        value_counts().\
        reset_index(name='Counts')

        return self.face_counts_per_roll_df


    def jackpot(self):
        """
        Compute the number of jackpots (rolls with the all the faces of the same value). Returns the number of jackpots rolled.
        """

        #use apply function to compute the lengths of each set, sets with length 1 are jackpots
        jackpot_df= self.game_results_data_w.apply(lambda x: len(set(x)), axis=1).\
        to_frame("jackpot")

        #filter data frame to just the sets of length 1 = these are the jackpots
        jackpot_df=jackpot_df[jackpot_df['jackpot']==1]

        #length of the data frame is the number of jackpots in game
        jackpot = len(jackpot_df)

        return jackpot


    def combo(self):
        """
        Computes the number of distinct combinatinos. Returns the combo_df dataframe.
        """

        combo_df = self.game_results_data_w.apply(lambda x: x.sort_values().squeeze(), axis=1).\
        value_counts().to_frame('n')

        return combo_df
