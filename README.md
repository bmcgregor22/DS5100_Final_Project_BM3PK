# Monte Carlo Simulator 
# Bruce McGregor

## Synopsis:
See the following notes on hoo to use this package.

### Installation  
Use the package manager pip to install montecarlo
```bash
pip install .
```
### Importing
```python
from montecarlo import Die, Game, Analyzer
```
### Creating Dice Objects

```python
#Create a die with sides based on a array of string or numbers

sides = ['H','T']
coin=Die(sides)

sides =[1,2,3,4,5,6]
fair_die=Die(sides)
```

### Playing games
```python
#setup a game 

#specify number of die in game
n_dice = 3

#specify the number of rolls per die in a game
n1 = 1000

#create a set of die for the game
game_1_1_dice=([fair_die for i in range(n_dice)])

##create the game object based on the set of die
game_1_1 = Game(game_1_1_dice)

#play the game
game_1_1.play(n1)

#show the game results in a wide format table
game_1_1.show()

#show the game results in a narrow format table
game_1_1.show('N')

```

### Analyzing Games
Monte Carlo enables analysis of game results to calculate the number of jackpots and the combinations that are generated.
Game results can be displayed in a wide and narrow format.
```python
#create an analysis of the game
game_1_1_analysis = Analyzer(game_1_1)

#compute the jackpots
jp_1_1 = game_1_1_analysis.jackpot()

#combute the combinations
jp_1_1 = game_1_1_analysis.combo()

#compute the face counts per roll
jp_1_1 = game_1_1_analysis.face_counts_per_roll()
```

## API Description


### List of Classes and Public Methods
#### Class Die
```python
    """
    This class define method for a die object, which represents a variety of random variables
    The constructor takes a array object of faces as an argument.

    Attributes:
    -----------
    self.die_obj - the data defining an instance of die as a data frame
    self.faces - an array object of faces established an instance creation. The array may be an array of strings or an array of numbers.  The array cannot have any duplicate values.

    Methods:
    -----------
    change_weight(self, a_side, a_weight) - changes the weight of one of the sides of the die
    
    roll_die(self, num_rolls=1) - rolls an instance of a die the number of times specfied by num_rolls
    
    show_die(self) - displays the die's current defintion of faces and weights
    """
```

#### Methods of the Class Die
    def change_weight(self, a_face, a_weight):
        """
        This method changes the weight of one of the sides of the die to the specified weight.

        arg[1] specifies  the face that is to be changed
        arg[2] specified the weight that the face will be changed
        """
        
    def roll_die(self, num_rolls=1):
        """
        Method to roll the die by a specified number of times. The default number of rolls is 1. The method returns a list of outcomes of the each roll.
        """
        Return Value: outcomes
        
    def show_die(self):
        """
        Method to show the current set of die faces and weights, reflecting any changes to weights. Returns the die object, die_df, as a panda dataframe.
        """
        
        Return Value: die_df




#### Class Game
```python
    """
    A class representing a game. A game consists of rolling one or more die of the same kind one or more times. In a given game, each die has the same number of sides and set of faces,
    but each die may have different weights.

    Attributes
    ----------
    self.die_objects - a list of die objects created by the Die class, defined with same number of sides and set of faces.

    Methods
    ---------
    play(self, num_rolls) - rolls reach die the number of times specified by the argument num_rolls

    show_results(self, format="W') - displays the results of the game in wide format by default. For narrow format, specify format='N'

    """
```

#### Methods of the Class Game
```python

    def play(self,num_rolls):
        """
        Rolls each of the die objects the num_rolls number of times.

        """
        
    def show(self, format='W'):
        """
        Displays the result of the data frame in narrow or wide format. Wide format is the default. The argument is
        specified as  W for wide, or N for narrow.

        Wide format will have a single column index with the roll number, and each die number as a column
        Narrow format will have a two-column index with the roll number and die number, and a single column for the face rolled

        """
```
        
#### Class Analyzer 
  
```python
"""
    This is the docstring for the Analyzer class.  Analyzes the results of a game and produces various statistics about the game
    such as the number of jackpots and combinations

    Attributes
    ---------
    face_counts_per_roll_df - a dataframe storing the count of the  number of faces per roll

    jackpot_df - an dataframe storing the number of jackpots
    
    jackpot - the number of jackpots rolled

    combo_df = a dataframe storing the distinct combinations rolled and their counts


    Methods
    ---------

    face_counts_per_roll(self) - method to compute how many times a given face is rolled in each event.

    jackpot(self) - method to compute the number of jackpots in a game

    combo(self) - method to compute the number of distinct combinations produced in a game

    """

```

#### Methods of the Analyzer Class
```python

    def face_counts_per_roll(self):
        """
        Computes how many times a given face is rolled in each event. Returns the results in a data frame face_counts_per_roll_df.
        """
        
    def jackpot(self):
        """
        Compute the number of jackpots (rolls with the all the faces of the same value). Returns the number of jackpots rolled.
        """
        
    def combo(self):
        """
        Computes the number of distinct combinatinos. Returns the combo_df dataframe.
        """  
        
```
