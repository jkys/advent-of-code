"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""
from utils import get_input_file

VALID_SYMBOLS = ['-', '*', '/', '#', '&', '=', '$', '%', '@', '+']
GEAR_PART = '*'


"""
Keep the previous line, current line, and next line stored. Save the index of where each symbol exists. 
Take the -1, current, and +1 position of the symbol

run through each of the lines and check to see if there is a digit there, keep going backwards or forward applicable until no more digits.

"""

def number_is_adjacent_to_previous_symbal(index: int, previous_symbols: set) -> bool:
    return index in previous_symbols or index -1 in previous_symbols or index + 1 in previous_symbols

def symbol_is_adjacent_to_previous_number(index: int, previous_numbers: dict) -> bool:
    return index in previous_numbers or index -1 in previous_numbers or index + 1 in previous_numbers

def number_exists_in_area(line: str):
    for character in line:
        if character.isdigit():
            return True
    return False

def get_numbers_from_area(index: int, line: str) -> list[int]:
    print('Index: ' + str(index) + ', line=' + line)
    if line[index].isdigit():
        current_location = index
        start_location = None
        print('Running Loop1...')
        try:
            while line[current_location].isdigit():
                print(line[current_location])
                start_location = current_location
                current_location -= 1
        except:
            pass

        current_location = index
        end_location = None
        print('Running Loop2...')
        try:
            while line[current_location].isdigit():
                end_location = current_location
                current_location += 1
        except:
            pass

        print('Start=' + str(start_location) + ',End=' + str(end_location))
        print('Which is number=' + line[start_location : end_location  + 1])
        return [int(line[start_location : end_location + 1])]
        

    else:
        numbers = []
        if line[index - 1].isdigit():
            current_location = index - 1
            start_location = None
            end_location = current_location
            try: 
                while line[current_location].isdigit():
                    start_location = current_location
                    current_location -= 1
            except:
                pass
            numbers.append(int(line[start_location : end_location + 1]))
        
        if line[index + 1].isdigit():
            current_location = index + 1
            start_location = current_location
            end_location = None
            try:
                while line[current_location].isdigit():
                    end_location = current_location
                    current_location += 1
            except:
                pass
            numbers.append(int(line[start_location : end_location + 1]))
        return numbers



def symbol_snake(index: int, lines: str) -> list[int]:
    """Identifies and parses the numbers surrounding a symbol

    Handles checks to ensure IndexError's do not occur

    Args:
      index (int): The current index of a symbol 
      lines (list[str]): The previous, current, and next lines

    Returns:
      List of numbers which exist surrounding the symbol
    """
    print(lines)
    surrounding_numbers = []
    for line in lines:
        if number_exists_in_area(line[index - 1 : index + 2]):
            print('Looking in: ' + line[index - 1 : index + 2])
            numbers = get_numbers_from_area(index, line)
            print('Numbers=' + str(numbers))
            surrounding_numbers.extend(numbers)
    print('SurroundNumbers=' + str(surrounding_numbers))
    return surrounding_numbers

def part_one(schematics: list[str]):
    counter = 0
    numbers = []
    for line_number in range(0, len(schematics) - 1):
        print('Line Number: ' + str(line_number))
        counter += 1

        for index, character in enumerate(schematics[line_number]):
            if character in VALID_SYMBOLS:
                print('FoundSymbol: ' + character)
                if line_number == 0:
                    numbers.extend(symbol_snake(index, schematics[line_number : line_number + 2]))
                elif line_number == len(schematics) - 1:
                    numbers.extend(symbol_snake(index, schematics[line_number - 1 : line_number]))
                else:
                    numbers.extend(symbol_snake(index, schematics[line_number - 1 : line_number + 2]))
    print('EndAllBeAll: ' + str(numbers))

    answer = 0
    for number in numbers:
        answer += number
    print('Answer:' + str(answer))

def part_two(schematics: list[str]):
    counter = 0
    gears = []
    for line_number in range(0, len(schematics) - 1):
        print('Line Number: ' + str(line_number))
        counter += 1

        for index, character in enumerate(schematics[line_number]):
            if character == GEAR_PART:
                print('FoundSymbol: ' + character)
                numbers = []
                if line_number == 0:
                    numbers.extend(symbol_snake(index, schematics[line_number : line_number + 2]))
                elif line_number == len(schematics) - 1:
                    numbers.extend(symbol_snake(index, schematics[line_number - 1 : line_number]))
                else:
                    numbers.extend(symbol_snake(index, schematics[line_number - 1 : line_number + 2]))
                if len(numbers) == 2:
                    gears.append(numbers[0] * numbers[1])


    print('EndAllBeAll: ' + str(gears))

    answer = 0
    for gear in gears:
        answer += gear
    print('Answer:' + str(answer))


if __name__ == "__main__":
    INPUT_FILE = get_input_file('day-3.txt')
    lines = [line.strip() for line in open(INPUT_FILE)]
    # part_one(lines)
    part_two(lines)