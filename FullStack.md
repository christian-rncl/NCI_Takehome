# CardGame - FullStack Example

## Situation

You posted gameplay footage of your CardGame implementation online and it's now gone viral on TikTok! You decide to create a web version of the CardGame called 'CardGame.io' where a player is matched with a random player. Matched players play the classic cardgame and the winner is given a point. The global leaderboard is then updated.


## Behavior Driven Development

1. Given:<br>
    Someone just saw the viral TikTok and is curious about CardGame.io

    Event:<br>
    The user visits the webpage

    Result:<br>
    The user sees a landing page about our game and is prompted to register with a username


2. Given:<br>
    A new user just found the website and is not registered

    Event:<br>
        The user registers for an account with a `username` and `password`

    Result:<br>
        If the the `username` is not unique, then the user is prompted to try again with a different name. Otherwise the user is added to the leaderboard with 0 games and 0 wins and 0 losses under their belt. The message "User created" is displayed if they succeed.


3. Given:<br>
   A registered user visits the website

   Event:<br>
   The registered user logs in.

   Result:<br>
   The user is shown the top 100 leaderboard, their spot on the leaderboard, their score and a button that says "play a game"

4. Given:<br>
   A registered user is logged in

   Event:<br>
   The registered user clicks the "play a game" button.

   Result:<br>
   A session is created for a user with a unique link. The user can share this link with another registered user. If the registered user follows the link they are brought into the game

5. Given:<br>
    A player is in a match made game

    Event:<br>
    The player presses "draw!"

    Result:<br>
    3 cards are dealt to the player. The cards are seen by both players in a match. The scores are tallied and the winner is displayed with a message saying "`username` won!!!" The wins/losses score for each person is added to the database.

## Implementation/Server Interactions

### Behavior 1:
    client --> GET / --> server
    client <-- 200 index.html <-- server

### Behavior 2:

Security considerations: use hashing/salt/pepper for at rest storage
Make sure to use SSL for in transit security

    client -->  POST {'name':username, 'password':password} --> server

If the username exists

    client <-- 409 {'message': Please try again}  <-- server

Otherwise

    client <-- 200 {'message': User Created}  <-- server

While adding user information to `Players` database with hashed/salted/peppered password

### Behavior 3
Create a template page for a user as described in this behavior , called `userpage`. The page contains a table displaying displaying `Players` table with columns ['Name', 'Score'] oredered by Ascending score, Ascending Name

    client <-- 200 userpage <-- server

### Behavior 4
Create a unique string as the game id. Expose the game session at URI:

    cardgame.io/game/UNIQUE_STRING

Render a template as described in Behavior #4 for the response. Use socket.io websockets to enable user interaction

### Behavior 5
Create a unique string as the game id. Expose the game session at URI:

    cardgame.io/game/UNIQUE_STRING

Render a template as described in Behavior #4 for the response. Use socket.io websockets to enable user interaction (render the same page/information for both users)

Server interaction when a user presses "draw!!" button:

    client --> GET cardgame.io/game/draw --> server
    client <-- 200 {['(red,3), (green,1), ('yellow,9)']} <-- server

Where the response object is a random card combination as described in the classic card game description


## Model

## REST endpoints

## View

## Stack


