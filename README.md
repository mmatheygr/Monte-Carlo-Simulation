# Monte Carlo simulation
## Metadata
- Student name: Mauricio Mathey
- Project name: Monte carlo simulation

## Synopsis

#### Installing and importing

Installing
- !pip install -e .

Importing
- import montecarlo
- Once installed there's no need to call each class because when importing the package it imports all the classes

#### Die class

Create a die
- unfair_coin = die(['H', 'T'])

Change weight of one of the faces
- unfair_coin.changew('H',5)

Roll die five times
- unfair_coin.roll(5)

Show results of the roll
- unfair_coin.show()

#### Game class

Create a game
- unfair_game([unfair_coin])

Play a game 10 times
- unfair_game.play(10)

Show results
- unfair_game.show() - This will show the results in wide format
- unfair_game.show(False) - This will show the results in nattow format

#### Analyzer class

Create analyzer object
- unfairgame_analyzer = analyzer(unfair_game)

Analyze jackpot - Jackpot means having all the faces the same
- unfairgame_analyzer.jackpot()

Analyze combo - Combo means checking the permutations and counting them
- unfairgame_analyzer.combo()

Analyze face counts by play - It means counting how many times each face appeared in each play
- unfairgame_analyzer.face_counts()

## API description

#### Die class
A die has N sides, or “faces”, and W weights, and can be rolled to select a face. 
W defaults to 1.0 for each face but can be changed after the object is created.
Note that the weights are just numbers, not a normalized probability distribution.
The die has one behavior, which is to be rolled one or more times.
Note that what we are calling a “die” here can be any discrete random variable
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
- show: returns a DataFrame with the faces as column 0 and the weights as column 1


#### Game class
A game consists of rolling of one or more dice of the same kind one or more times. 
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
- object: allows you to access the list of dies you have passed.

#### Analyzer class
An analyzer takes the results of a single game and computes various
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
- counts_df: stores the result, as a DataFrame, of the face counts by roll, where the rolls are the index and the faces are the columns

## Manifest
- LICENSE: contains the license of the package
- README: file you're currently reading, contains all the help you may need. More detailed than the docstrings.
- Scenarios: 3 scenarios used to test the correct function of the packages
- montecarlo_tests: unit testing of the package
- setup: required file for installation
- test_results: results of the unit testing
- Final_project: document containing all the previous documents and information (except the license, readme, and installation related documents)
- montecarlosim
  - init: required for the installation
  - montecarlo: main file of the package, contains the classes
