# Python Adventure Game

## Overview
This Python-based text-adventure game employs an Object-Oriented Programming (OOP) design, allowing players to explore a virtual world, interact with elements, manage inventory, and solve puzzles via a command-line interface.

### Implemented Features
1. **Abbreviations for Verbs, Directions, and Items:** Supports shorthand inputs for streamlined gameplay.
2. **Help Verb:** Provides command guidance for players.
3. **Directions as Verbs:** Allows directional words as verbs for movement.
4. **Drop Verb:** Enables item removal from the inventory.

## Installation
Ensure Python 3 is installed on your system.

1.  Clone the repository:

    ```bash
    git clone https://github.com/your-username/adventure-game.git
    cd adventure-game
    ```
2.  Run the game by executing the following command in the terminal:

    ```bash
    python3 adventure.py [map name]
    ```
    Replace [map name] with the desired map file.

## Gameplay Instructions
- The game is structured using an Object-Oriented approach, making it modular and easy to extend or modify.
- Use commands to interact:
    - Abbreviations for verbs, directions, and items are supported.
    - Available commands: 'go [direction]', 'get [item]', 'drop [item]', 'look', 'inventory', 'help', 'quit'.
    - Directions can be used as verbs for movement (e.g., 'north').
    - 'help' provides command guidance.
    - 'inventory' lists collected items.
    - 'look' revisits the room's description.
    - 'quit' exits the game.

## OOP and Modularity
- **Object-Oriented Design:** The code is structured using classes, providing a modular approach for managing game elements, interactions, and actions.
- **Modularity:** Different aspects of the game are organized into classes, making it easier to maintain, extend, and debug.

## Testing
### Test Approach
Describe the testing methodology used to validate the game's functionality, including abbreviations, help command usability, directional verbs, and item dropping.

### Known Issues
No

## Implemented Extensions
### Abbreviations for Verbs, Directions, and Items
- **Description:** Supports shorthand inputs for verbs, directions, and items to streamline player interactions.
- **Usage Example:** 'g n' for 'go north', 'd k' for 'drop key'.

### Help Verb
- **Description:** Offers guidance by displaying available commands and their functionalities for players.
- **Usage:** Enter 'help' to access the command guide.

### Directions as Verbs
- **Description:** Allows using directional words as verbs for movement within the game world.
- **Usage Example:** 'north' to move in the north direction.

### Drop Verb
- **Description:** Enables players to drop items from their inventory to interact with the environment.
- **Usage Example:** 'drop sword' to remove the sword from the inventory.


# Example Gameplay with loop.map
    Run Command 

    ```
    python .\adventure.py .\loop.map
    ```

    Gameplay Output

    ```
    > A white room

    You are in a simple room with white walls.

    Exits: north east

    What would you like to do? go west
    There's no way to go west.
    What would you like to do? go
    Sorry, you need to 'go' somewhere.
    What would you like to do? go north
    You go north.

    > A blue room

    This room is simple, too, but with blue walls.

    Exits: east south

    What would you like to do? go south
    You go south.

    > A white room

    You are in a simple room with white walls.

    Exits: north east

    What would you like to do? GO EAST
    You go east.

    > A red room

    This room is fancy. It's red!

    Items: rose

    Exits: north west

    What would you like to do? 
    
    ```


