Prasanna Limaye plimaye@stevens.edu

GitHub URL : https://github.com/PrasannaL15/Text-Adventure

Hours spent on project : 50

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

I created test.py which compares the expected output with the actual output received from the terminal

### Known Issues

No

### issue or bug solved

I faced a challenge in making code modular so that I can keep the original functionality while implementing the extensions

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

## A Map which implements all features ([my_map.map](my_map.map))

# Example Gameplay with loop.map

1.  Run Command

    ```
    python .\adventure.py .\my_map.map
    ```

2.  Gameplay Output

    ```
    > Hidden Leaf Village

    You are in the heart of the Hidden Leaf Village, surrounded by towering trees and ninja structures.

    Items: shuriken, medicinal herbs, ninja scroll

    Exits: north east south west

    What would you like to do? go north
    You go north.

    > Training Grounds

    This vast area is designated for ninja training, with open fields and various obstacle courses.

    Items: throwing knives, training dummy, smoke bomb

    Exits: south west

    What would you like to do? g s
    Did you want to use go or get?
    What would you like to do? go s
    Did you want to go south or west?
    What would you like to do? south
    You go south.

    > Hidden Leaf Village

    You are in the heart of the Hidden Leaf Village, surrounded by towering trees and ninja structures.

    Items: shuriken, medicinal herbs, ninja scroll

    Exits: north east south west

    What would you like to do? help
    You can use the following verbs to interact with this amazing world:
    Verb       Noun         Description
    ---------- ------------ --------------------------------------------------
    go         {somewhere}  The go method moves the player to the specified direction.
    get        {something}  The get method picks up an item from the current room.
    look                    The look method prints the description of the current room.
    quit                    The quit method exits the game.
    inventory               The inventory method displays the player's inventory.
    help                    The help method displays the list of available verbs for the player.
    drop       {something}  The drop method drops an item from the player's inventory.
    What would you like to do? look
    > Hidden Leaf Village

    You are in the heart of the Hidden Leaf Village, surrounded by towering trees and ninja structures.

    Items: shuriken, medicinal herbs, ninja scroll

    Exits: north east south west

    What would you like to do? get shuri
    You pick up the shuriken.
    What would you like to do? go south
    You go south.

    > Marketplace

    A bustling marketplace where villagers and ninjas gather to buy and sell goods.

    Items: rare herbs, ninja tools, souvenirs

    Exits: north east

    What would you like to do? get rare
    You pick up the rare herbs.
    What would you like to do? inv
    Inventory:
    shuriken
    rare herbs
    What would you like to do? drop shuriken
    You drop the shuriken.
    What would you like to do? look
    > Marketplace

    A bustling marketplace where villagers and ninjas gather to buy and sell goods.

    Items: ninja tools, souvenirs, shuriken

    Exits: north east

    What would you like to do? d r
    You drop the rare herbs.
    What would you like to do? quit
    Goodbye!
    PS C:\Users\limay\OneDrive\Desktop\GitHub\Text-Adventure>

    ```
