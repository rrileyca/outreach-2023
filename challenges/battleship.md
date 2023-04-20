# Battleship
Your assignment is to make a battleship game. This is a multi-part challenge. If you complete the first part,
move on to the second and so on. If you don't know what the battleship game is, 
[read here](https://en.wikipedia.org/wiki/Battleship_(game)).

## Part 1
Your game should do the following:
1. Accept `input()` from the terminal. Ask the user for an `x` coordinate and a `y` coordinate.
2. Once the battleship is "placed", the terminal prompts for Player 2 to guess where the ship is by asking
for the `x` and `y` coordinates of the ship.
3. If the guess is wrong, the LED pixel should light up `red`. If the guess is right, the LED lights up `green` and the
board stays lit for `5` seconds.

## Part 2
Congratulations on creating your game - but someone has asked for a new feature! 

- When a guess is 1 pixel away from the battleship, the pixel should now light up blue. Diagonal counts!

## Part 3
Now people want more battleships! 

- Your game should now accept **up to** `256` battleships! 
- The game should allow for any number of battleships to be entered by Player 1 before Player 2 starts guessing them. 
- Once Player 1 has entered all the coordinates, they should be able to type `done` to start the game.

*Hint! You're going to want to use a `list`!* 