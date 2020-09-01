
# README: NCI Take Home

## Take-home Prompt

Code interview question: Work with the programing language you are most familiar with. 
 
1. Create a card game which supports 3 of the operations below. 
Shuffle cards in the deck: randomly mix the cards in the card deck, and return a whole deck of cards with a mixed order 
2. Get a card from the top of the deck: get one card from top of the card deck, return a card, and if there is no card left in the deck return error or exception.  
3. Sort cards: take a list of color as parameter and sort the card in that color order. Numbers should be in ascending order.   i.e. If the deck has a card contains with following order  (red, 1), (green, 5), (red, 0), (yellow, 3), (green, 2) 
Sort cards([yellow, green, red]) will return the cards with following order (yellow, 3), (green, 0), (green, 5), (red, 0), (red, 1)  
4. Determine winners: 2 players play the game. They will draw 3 cards by taking turns. 
Whoever has the high score wins the game. (color point calculation, red = 3, yellow =2, green = 1) the point is calculated by color point * number in the card.   
  
Testing: Create test cases to test the above operations. 
 
Please put the code in an online repository and provide the link before the interview: github, gitlab, etc. 

## Documentation

### Assumptions from prompt
The prompt is very short, leaving room for some assumptions. In this section I enumerate assumptions/clarifications I've made about the game and specification.

1. Each player will take a turn, in serial fashion, drawing from the top of the deck. 
2. The number value in each card can only be the integers 1-10.
3. Each player gets a fixed amount of 'moves', 3, in the vanilla case.  
4. The example game in the prompt is just a special case of the 'Color Card game'. This assumption requires that the implementation should easily support different variants of this game. Concretely,  
   1. Adding new color/color combination should be easy. A developer should be able to easily add new Cards to the game (blue = 4), (orange = 7)
   2. Changing point calculation  should be easy. A developer should be able to easily create a variant where points = 8*color_point *number_of_card
   3. The number of players should easily be modified. A developer should be able to easily create a 5 person game variant.
5. The default deck has all possible combinations of color and number value. e.g. If there are 3 colors (red, yellow, green) and the max number val is 10, by default the deck size will be 30. One for each combination.
6. The user/dev can't request a deck of cards $<$ the number of possible combinations. An error will be thrown in this case
7.  In the case that the user/dev requests a deck of cards $>$ possible combinations, each card combinations must be present at least once.

###  Implementation Details

This implementation uses the Flyweight design pattern for the card objects to maximize efficiency. Because of the 'immutable nature' of `Card`, only one instance for each unique (color, number) combination needs to be created.


