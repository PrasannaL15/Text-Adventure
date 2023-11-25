import json
import argparse
# load json file loop.map in ython


class GameEngine():



    def __init__(self, world_map):
        self.world_map = world_map
        self.start = world_map[0]
        self.inventory_array = []
        self.location = self.start
        self.verb_list = ['go', 'get', 'look', 'quit','inventory']
        self.single_word_verbs = ['look', 'quit','inventory']
        self.verb_msg_map = {'go':'somewhere', 'get':'something'}

    def play(self):
        
        self.describe_room()
            
        while True:
            user_choice = ' '
            try:
                user_choice = input('What would you like to do? ').lower()
            except EOFError or KeyboardInterrupt:
                print("Use 'quit' to exit.")
                continue
            choice_array = user_choice.split(' ', 1)
            verb = choice_array[0]
            
            if len(choice_array) > 1:
                noun = choice_array[1]
            else:
                noun = None

            
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
        print('>',self.location['name'])
        print('')
        print(self.location['desc'])

        if 'items' not in self.location:
            self.location['items'] = []

        if len(self.location['items']) > 0:
            print('')
            print('Items: '+' '.join([x for x in self.location['items']]))
        
        print('')
        print('Exits: '+' '.join([x for x in self.location['exits']]))
        print('')
        

    def print_sorry_verb(self, verb):
        print(f"Sorry, you need to '{verb}' {self.verb_msg_map[verb]}.")   

    def handle_input(self, verb, noun):

        match verb:
            case 'go':
                return self.go(noun)
            case 'get':
                return self.get(noun)
            case 'look':
                return 
            case 'quit':
                print('Goodbye!')
                quit()
            case 'inventory':
                return self.inventory()
            
            case _:
                print('Unknown verb {}'.format(verb))
        
    def go(self, direction):
        if direction not in self.location['exits']:
            print(f"There's no way to go {direction}.")
            return 'continue'

        world_map_index = self.location['exits'][direction]
        self.location = world_map[world_map_index]
        print('You go '+direction,end='.\n\n')
        
    def inventory(self):
        if(len(self.inventory_array) == 0):
            print("You're not carrying anything.")
            return 'continue'
        print('Inventory:'+'\n  '.join([x for x in self.inventory_array]))
        return 'continue'

    def get(self, item):
        is_item_in_room = item in self.location['items']

        if is_item_in_room:
            print('You pick up the {}'.format(item))
            self.inventory_array.append(item)
            self.location['items'].remove(item)
        else:
            print(f"There's no {item} anywhere.")
        
        return 'continue'



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Adventure game')
    parser.add_argument('mapfile', help='Map file to load')

    args = parser.parse_args()




    with open(args.mapfile) as f:
        world_map = json.load(f)
    game = GameEngine(world_map)
    game.play()