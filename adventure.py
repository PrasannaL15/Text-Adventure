import json
import argparse
# load json file loop.map in ython


class GameEngine():

    '''
    The GameEngine class represents the game engine for a text adventure game.
    It handles the game logic, player input, and game state.

    Attributes:
    - world_map (list): The list of rooms in the game world.
    - start (dict): The starting room of the game.
    - inventory_array (list): The list of items in the player's inventory.
    - location (dict): The current location of the player.
    - verb_list (list): The list of valid verbs for player actions.
    - single_word_verbs (list): The list of verbs that do not require a noun.
    - verb_msg_map (dict): The mapping of verbs to their corresponding messages.

    Methods:
    - play(): Starts the game and handles player input.
    - describe_room(): Prints the description of the current room.
    - print_sorry_verb(verb): Prints a message indicating that the verb requires a noun.
    - find_anything_in_dict(item, input_dict): Finds matching items in a dictionary.
    - find_anything_in_list(item, input_list): Finds matching items in a list.
    - handle_input(verb, noun): Handles player input and performs the corresponding action.
    - go(direction): Moves the player to the specified direction.
    - drop(item): Drops an item from the player's inventory.
    - inventory(): Displays the player's inventory.
    - get(item): Picks up an item from the current room.
    - help(): Displays the list of available verbs for the player.
    '''

    def __init__(self, world_map):
        self.world_map = world_map
        self.start = world_map[0]
        self.inventory_array = []
        self.location = self.start
        self.verb_list = ['go', 'get', 'look',
                          'quit', 'inventory', 'help', 'drop']
        self.single_word_verbs = ['look', 'quit', 'inventory', 'help']
        self.verb_msg_map = {'go': 'somewhere',
                             'get': 'something', 'drop': 'something'}

    def __init__(self, world_map):
        self.world_map = world_map
        self.start = world_map[0]
        self.inventory_array = []
        self.location = self.start
        self.verb_list = ['go', 'get', 'look',
                          'quit', 'inventory', 'help', 'drop']
        self.single_word_verbs = ['look', 'quit', 'inventory', 'help']
        self.verb_msg_map = {'go': 'somewhere',
                             'get': 'something', 'drop': 'something'}

    def play(self):

        self.describe_room()

        while True:
            user_choice = ' '
            try:
                user_choice = input('What would you like to do? ').lower()
            except EOFError:
                print("Use 'quit' to exit.")
                continue
            choice_array = user_choice.split(' ', 1)
            verb = choice_array[0]

            if len(choice_array) > 1:
                noun = choice_array[1].rstrip()
            else:
                noun = None

            potential_verbs = self.find_anything_in_list(verb, self.verb_list)

            if len(potential_verbs) > 1:
                last_verb = self.verb_list[potential_verbs.pop()]
                verbs = [self.verb_list[i] for i in potential_verbs]
                print('Did you want to use ' +
                      ', '.join([x for x in verbs])+' or '+last_verb+'?')
                continue
            elif len(potential_verbs) == 1:
                verb = self.verb_list[potential_verbs[0]]
            elif len(potential_verbs) == 0:
                direction = self.find_anything_in_dict(
                    verb, self.location['exits'])
                if len(direction) == 1:
                    verb = 'go'
                    noun = direction[0]
                elif len(direction) > 1:
                    last_direction = direction.pop()
                    directions = [direction[i] for i in range(len(direction))]
                    print('Did you want to go ' +
                          ', '.join([x for x in directions])+' or '+last_direction+'?')
                    continue

            if verb not in self.verb_list:
                print('Unknown verb {}'.format(verb))
                continue

            if verb == 'look':

                self.describe_room()
                continue

            if noun is None and verb not in self.single_word_verbs:
                self.print_sorry_verb(verb)
                continue

            # print(verb, noun)
            output = self.handle_input(verb, noun)

            if output == 'continue':
                continue

            self.describe_room()

    def describe_room(self):
        print('>', self.location['name'])
        print('')
        print(self.location['desc'])

        if 'items' not in self.location:
            self.location['items'] = []

        if len(self.location['items']) > 0:
            print('')
            print('Items: '+', '.join([x for x in self.location['items']]))

        print('')
        print('Exits: '+' '.join([x for x in self.location['exits']]))
        print('')

    def print_sorry_verb(self, verb):
        print(f"Sorry, you need to '{verb}' {self.verb_msg_map[verb]}.")

    def find_anything_in_dict(self, item, input_dict):
        match_index = []
        assert type(
            input_dict) == dict, f"Maybe you want to use find_anything_in_{type(input_dict).__name__} instead of find_anything_in_dict()"
        for i in input_dict:

            if item == i:
                return [i]
            if item in i:
                match_index.append(i)
        # print(match_index)
        return match_index

    def find_anything_in_list(self, item, input_list):
        # print(input_list)
        assert type(
            input_list) == list, f'maybe you want to use find_anything_in_{type(input_list).__name__} instead of find_anything_in_list() '

        match_index = []
        for i in input_list:

            if item == i:
                return [input_list.index(i)]
            if item in i:
                match_index.append(input_list.index(i))
        return match_index

    def look(self):
        '''
        The look method prints the description of the current room.
        '''
        self.describe_room()
        return 'continue'

    def quit(self):
        '''
        The quit method exits the game.
        '''
        print('Goodbye!')
        quit()

    def handle_input(self, verb, noun):

        match verb:
            case 'go':
                return self.go(noun)
            case 'get':
                return self.get(noun)
            case 'look':
                return self.look()
            case 'drop':
                return self.drop(noun)
            case 'quit':
                return self.quit()
            case 'inventory':
                return self.inventory()
            case 'help':
                return self.help()
            case _:
                print('Unknown verb {}'.format(verb))

    def go(self, direction):
        '''
        The go method moves the player to the specified direction.
        '''
        direction_matches = self.find_anything_in_dict(
            direction, self.location['exits'])
        if len(direction_matches) > 1:
            last_direction = direction_matches.pop()
            # print(direction_matches,last_direction)
            print('Did you want to go ' +
                  ', '.join([x for x in direction_matches])+' or '+last_direction+'?')
            return 'continue'
        if direction not in self.location['exits']:
            print(f"There's no way to go {direction}.")
            return 'continue'

        world_map_index = self.location['exits'][direction]
        self.location = world_map[world_map_index]
        print('You go '+direction, end='.\n\n')

    def drop(self, item):
        '''
        The drop method drops an item from the player's inventory.
        '''
        inventory_items = self.inventory_array
        item_index = self.find_anything_in_list(item, inventory_items)
        is_item_in_inventory = len(item_index) > 0
        if is_item_in_inventory:
            if len(item_index) > 1:
                last_item = inventory_items[item_index.pop()]
                items = [inventory_items[i] for i in item_index]
                print('Did you want to drop the ' +
                      ', '.join([x for x in items])+' or the '+last_item+'?')
                return 'continue'
            item_index = item_index[0]
            print('You drop the {}.'.format(inventory_items[item_index]))
            self.location['items'].append(inventory_items[item_index])
            inventory_items.pop(item_index)
        else:
            print(f"You're not carrying {item}.")

        return 'continue'

    def inventory(self):
        '''
        The inventory method displays the player's inventory.
        '''

        if (len(self.inventory_array) == 0):
            print("You're not carrying anything.")
            return 'continue'
        print('Inventory:\n  '+'\n  '.join([x for x in self.inventory_array]))
        return 'continue'

    def get(self, item):
        '''
        The get method picks up an item from the current room.
        '''
        location_items = self.location['items']
        item_index = self.find_anything_in_list(item, location_items)
        is_item_in_room = len(item_index) > 0
        if is_item_in_room:
            if len(item_index) > 1:
                last_item = location_items[item_index.pop()]
                items = [location_items[i] for i in item_index]
                print('Did you want to get the ' +
                      ', '.join([x for x in items])+' or the '+last_item+'?')
                return 'continue'
            item_index = item_index[0]
            print('You pick up the {}.'.format(location_items[item_index]))
            self.inventory_array.insert(0, location_items[item_index])
            location_items.pop(item_index)
        else:
            print(f"There's no {item} anywhere.")

        return 'continue'

    def help(self):
        '''
        The help method displays the list of available verbs for the player.
        '''

        print('You can use the following verbs to interact with this amazing world:')
        print(f"{'Verb':10} {'Noun':12} {'Description'}")
        print(f"{'-'*10:10} {'-'*12:12} {'-'*50}")
        for verb in self.verb_list:

            verb_msg = '{'+self.verb_msg_map[verb] + \
                '}' if verb in self.verb_msg_map else ''

            method = getattr(self, verb, None)
            verb_doc_string = ''
            if method:
                if method.__doc__:
                    verb_doc_string = method.__doc__.strip()

            print(f'{verb:10} {verb_msg:12} {verb_doc_string}')
        return 'continue'


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Adventure game')
    parser.add_argument('mapfile', help='Map file to load')

    args = parser.parse_args()

    with open(args.mapfile) as f:
        world_map = json.load(f)
    game = GameEngine(world_map)
    game.play()
