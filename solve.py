from collections.abc import Generator
from typing import Tuple, Dict, List
from trie import Trie
from pynput.mouse import Controller, Button
from pynput import keyboard
import time


# loop through each letter in the matrix
# for each letter, start a backtracking function called find_paths()
# find paths will iterate through all possible neighbors (-1,-1) - (1,1)
# As it appends each char it will check its value agaist the dictionary trie and update the pointer
# each time it encounters a '*' character -> add the current word to the solutions list and continue on the path
# If at any point, the newest char is not in the pointer map, clean up the current path
# Once done finding solutions, app shall iterate through each word (an array of coordinates)
# For each coordinate, use a hashmap to get a mouse coordinate
# If index is FIRST, move then mouseDOWN, otherwise ONLY move (mouse will be down)
# If index is last, move then mouseUP


grid = None
grid_size = 4
dictionary = None
solutions = {}
stop_game = False


def get_dictionary() -> Trie:
    dictionary = Trie()
    with open("dictionary.txt") as f:
        for word in f:
            word = word.strip()
            dictionary.insert(word)
    return dictionary


def get_adjacent_cells(r: int, c: int) -> Generator[Tuple[int, int], None, None]:
    for delta_r in range(-1, 2, 1):
        for delta_c in range(-1, 2, 1):
            if delta_r == delta_c == 0:
                continue
            new_r = r + delta_r
            new_c = c + delta_c
            if 0 <= new_r < grid_size and 0 <= new_c < grid_size:
                yield (new_r, new_c)


def search(
    r: int, c: int, word: List[str], path: List[Tuple[int, int]], pointer: Dict
) -> None:
    char = grid[r][c]
    word.append(char)
    path.append((r, c))
    pointer = pointer[char]

    if "*" in pointer:
        del pointer["*"]
        if len(word) > 2:
            solutions["".join(word)] = path.copy()

    grid[r][c] = None

    for new_r, new_c in get_adjacent_cells(r, c):
        if grid[new_r][new_c] is not None and grid[new_r][new_c] in pointer:
            search(new_r, new_c, word, path, pointer)
    word.pop()
    path.pop()
    grid[r][c] = char


def generate_coordinate_map() -> Dict[tuple, tuple]:
    top_left = (76, 400)  # set these with a calibrate function eventually
    top_right = (245, 400)
    bottom_left = (76, 568)

    x_increment = (top_right[0] - top_left[0]) / 3
    y_increment = (bottom_left[1] - top_left[1]) / 3

    coordinates = {}
    for r in range(grid_size):
        for c in range(grid_size):
            x = top_left[0] + x_increment * r
            y = top_left[1] + y_increment * c
            coordinates[(c, r)] = (x, y)
    return coordinates

def on_press(key):
    global stop_game
    if key == keyboard.Key.esc:
        stop_game = True


def play_game(paths) -> None:
    time.sleep(5)
    mouse = Controller()
    coordinate_map = generate_coordinate_map()

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    for path in paths:
        for i, tile in enumerate(path):
            if stop_game:
                print("You pressed Esc. Stopping...")
                mouse.release(Button.left)
                return
            
            coord = coordinate_map[tile]
            mouse.position = coord
            time.sleep(0.05)

            if i == 0:
                mouse.press(Button.left)
                time.sleep(0.05)
        mouse.release(Button.left)


def solve():
    global grid
    global solutions
    global dictionary
    solutions = {}

    dictionary = get_dictionary()

    chars = input("Enter Letters (ノ^_^)ノ: ")

    while len(chars) < 16:
        chars = chars + input(f"Not enough letters ¯\_(ツ)_/¯: {chars}")

    gridStr = chars[:16].upper()

    grid = [list(gridStr[i : i + 4]) for i in range(0, 16, 4)]

    for x in range(grid_size):
        for y in range(grid_size):
            search(x, y, [], [], dictionary.root)

    words = sorted(solutions.keys(), key=len, reverse=True)
    paths = sorted(solutions.values(), key=len, reverse=True)

    print(words)
    print(len(words))
    play_game(paths)

    input("Press enter to go again")
    solve()


solve()
