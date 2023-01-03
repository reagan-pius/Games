# Games


## The Rock Paper Scissors
This is my third attempt at the game. It fixes the issue of some players micing up cases while choosing an action
If the player enters a move that is a combination of lower and uppercase letters, such as "pAper",
the current version of the code will not recognize it as a valid move. This is because the lower() function will only convert uppercase letters to lowercase,
and will not affect lowercase letters.

To handle input that is a combination of lower and uppercase letters,
you can use the lower() function on both the player's input and the list of possible choices, like shown above

## The Hangman!
