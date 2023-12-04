"""
-- Day 2: Cube Conundrum ---
You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""
from utils import get_input_file

RED, GREEN, BLUE = 'red', 'green', 'blue'

CUBE_COUNT = {
    RED: 12,
    GREEN: 13,
    BLUE: 14
}

class GameRound:
    red = 0
    green = 0
    blue = 0

    def __init__(self, round_values: list[tuple]):
        for round_value in round_values:
            if RED in round_value[0]:
                self.red = int(round_value[1])
            
            if GREEN in round_value[0]:
                self.green = int(round_value[1])
            
            if BLUE in round_value[0]:
                self.blue = int(round_value[1])
    
    def is_valid_game(self) -> bool:
        return self.red <= CUBE_COUNT[RED] and self.green <= CUBE_COUNT[GREEN] and self.blue <= CUBE_COUNT[BLUE]

    def get_cube_power(self) -> bool:
        return self.red * self.green * self.blue
    
    def __str__(self):
        return 'RED: {red}, GREEN: {green}, BLUE: {blue}'.format(red=self.red, green=self.green, blue=self.blue)

class Game:
    rounds: list[GameRound] = []
    def __init__(self, rounds: list[GameRound]):
        self.rounds = rounds
    
    def get_game_power(self) -> int:
        red, green, blue = 0, 0, 0
        for round in self.rounds:
            red = round.red if round.red > red else red
            blue = round.blue if round.blue > blue else blue
            green = round.green if round.green > green else green
        return red * green * blue

    def is_valid_game(self) -> bool:
        return all([round.is_valid_game() for round in self.rounds])

def parse_game_id(game_log: str) -> int:
    return int(game_log[len('Game '):game_log.index(':')])

def get_game_rounds(game_log: str) -> list[str]:
    game_rounds_raw = game_log[game_log.index(':') + 1:]
    game_rounds_split = game_rounds_raw.split(';')
    return game_rounds_split

def parse_round_values(round_data: list[str]) -> list[tuple]:
    data = round_data.split(',')
    round_values = []
    for datum in data:
        datum = datum.lstrip()
        datum = datum.rstrip()
        value = ()
        if RED in datum:
            value = (RED, datum[:datum.index(RED) -1])
        elif GREEN in datum:
            value = (GREEN, datum[:datum.index(GREEN) -1])
        elif BLUE in datum:
            value = (BLUE, datum[:datum.index(BLUE) -1])
        else:
            raise ValueError('Unexpected value type within datum=' + datum)
        round_values.append(value)

    return round_values

def parse_round_data(rounds: list[str]) -> list[GameRound]:
    round_data = []
    for round in rounds:
        round_values = parse_round_values(round)
        game_round = GameRound(round_values)
        round_data.append(game_round)
    return round_data
    

def part_one(input_file: str):
    with open(input_file) as game_logs:
        count = 0
        for game_log in game_logs:
            game_log = game_log.strip()
            game_id = parse_game_id(game_log)
            game_rounds = get_game_rounds(game_log)
            game_data = parse_round_data(game_rounds)
            game = Game(game_data)
            if game.is_valid_game():
                count += game_id

        print(count)

def part_two(input_file: str):
    with open(input_file) as game_logs:
        count = 0
        for game_log in game_logs:
            game_log = game_log.strip()
            game_id = parse_game_id(game_log)
            game_rounds = get_game_rounds(game_log)
            game_data = parse_round_data(game_rounds)
            game = Game(game_data)
            count += game.get_game_power()

        print(count)

if __name__ == "__main__":
    INPUT_FILE = get_input_file('day-2.txt')
    part_one(INPUT_FILE)
    part_two(INPUT_FILE)