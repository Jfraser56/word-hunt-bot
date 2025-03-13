# Wordhunt Bot 🎮🧩
Welcome to my Wordhunt Bot – A friend of mine loves this game and would consistenly crush me each time we'd play. Her scores ranged from 15,000 - 30,000, while I could barely get over 10,000. 

One day while practicing leetcode, I was learning about the **Trie** data structure and how it can be used to search strings by prefixes. I then had an idea... I could create a bot, that not only finds all possible word solutions in a given Wordhunt grid, but could also programatically play the game for me and achieve scores of up to 200,000. 🙌

## What is Wordhunt?
If you're unfamiliar with Wordhunt, it's an iMessage word game where you’re given a grid of random letters, and have one minute to find as many words as you can. You create words by connecting adjacent letters, either vertically, horizontally, or diagonally. The longer and more complex the words, the higher your score.

## How Does the Program Work?
It uses a combination of a **Trie** data structure and **recursive backtracking** to rack up points really fast. Here’s a breakdown of how it works:

### 1. Parsing the Dictionary
We start by parsing a dictionary.txt file that contains a list of valid words. This dictionary is loaded into a Trie data structure.

The Trie is a tree-like structure that stores words in such a way that we can quickly check if a given string is a valid word. Like I said before, it’s super fast and efficient too, making it perfect for this kind of application. ✨

### 2. User Input for the Grid
Next, you’ll input your **4x4** Wordhunt grid from left to right, top to bottom. The script takes this input, and is ready to start searching for words within the grid.

### 3. Recursive Backtracking Search
The script starts a recursive backtracking algorithm to find all possible words in the grid. Here’s the idea:
- Starting from each letter in the grid, we look at all adjacent tiles (up, down, left, right, and diagonally).
- For each tile, the script builds possible words by moving through the grid and checking if each word exists in the **Trie**.
- If it’s a valid word, both the string and the tile coordinates of each character are saved to a `solutions` hashmap. If not, it backtracks and attempts the next path.
  
This continues until it reaches the last tile in the grid, and therefore no more combinations are left.

### 4. Automated Gameplay Using Screen Mirroring
Once all the words are found, I thought it would be cool if the script would actually play the game for you. 🎮

Using Apple’s Screen Mirroring Tool (released with macOS 15, Sequoia), the program automates the entire game process:
- It maps the tile coordinates of each word in the `solutions` hashmap to mouse cursor coordinates.
- It then clicks and drags through the grid, selecting the correct tiles to form valid solutions.

## How to use it:
### 1. Clone the Repo
Make sure you have Python 3.x installed. Clone this repository to your local machine:
```
git clone https://github.com/jfraser56/Word-Hunt-Bot.git
cd Word-Hunt-Bot
```
Create your virtual env, and install required dependencies
```
python3 -m venv myenv
pip install -r requirements.txt
```
### 2. Prepare the bot
Connect your IOS Device via screen mirroring - (TODO) if this is your first time running the bot,execute the calibrate script and follow the instructions on the cli with:
```
python3 ./calibrate.py
```
### Let the bot work!
Run the solve.py script and start your Wordhunt game. The bot will ask that you enter all the letters seen on the grid into the cli from left to right, top to bottom.
```
(myenv) MacBookPro:wordhunt-bot JohnDoe$ python3 ./solve.py
Enter Letters (ノ^_^)ノ: <grid letters here> 
```
Press `Enter`, and bring the IOS screen mirror window into focus. Sit back and enjoy confusing your competition with impossibly high scores. 🤖 (The script can be cancelled at any time with the `Esc` key)

## Demo
<img src="https://github.com/user-attachments/assets/b81d7014-fb2a-4dfd-953c-a54624e1336f" width="600" />


