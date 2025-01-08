# Wordhunt iMessage Game Solver 🎮🧩
Welcome to Wordhunt Solver – the tool to dominate your iMessage Wordhunt games! This app is quite capable of finding every possible word combination, and achieving scores of over 200,000 if the time allows 🙌

## What is Wordhunt?
If you're unfamiliar with the Wordhunt game in iMessage, it's a fast-paced puzzle where you’re given a grid of random letters. The challenge? Find as many words as you can by connecting adjacent letters, either vertically, horizontally, or diagonally. The longer and more complex the words, the higher your score.

## How Does the App Work?
This app uses a combination of a **Trie** data structure and **recursive backtracking** to rack up points insanely fast. Here’s a breakdown of how it all works:

### 1. Parsing the Dictionary
We start by parsing a dictionary.txt file that contains a list of valid words. This dictionary is loaded into a Trie data structure.

The Trie is a tree-like structure that stores words in such a way that we can quickly check if a given string is a valid word. It’s super fast and efficient, making it perfect for this kind of word search puzzle. ✨

### 2. User Input for the Grid
Next, you’ll input your **4x4** Wordhunt grid from left to right, top to bottom. The app takes this input, and is ready to start searching for words within the grid.

### 3. Recursive Backtracking Search
Now, here’s where the magic happens! 🔮

The app starts a recursive backtracking algorithm to find all possible words in the grid. Here’s how it works:
- Starting from each letter in the grid, we look at all adjacent tiles (up, down, left, right, and diagonally).
- For each tile, the app builds possible words by moving through the grid and checking if each word exists in the **Trie**.
- If it’s a valid word, both the string and the tile coordinates of each character are saved to a `solutions` hashmap. If not, it backtracks and tries the next path.
  
This continues until all valid words are found!

### 4. Automated Gameplay Using Screen Mirroring
Once all the words are found, it’s time to play the game for you! 🎮

Using Apple’s Screen Mirroring Tool (released with macOS 15, Sequoia), the app automates the entire game process:
- It maps the tile coordinates of each word in the `solutions` hashmap to mouse cursor coordinates.
- The app clicks through the grid, finding each letter and selecting the correct tiles to form each word.
  
This means you can sit back and watch as your score skyrockets within seconds! 💥

## How to use it:
### 1. Install the App
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
Press `Enter`, and bring the IOS screen mirror window into focus. Sit back and enjoy watching your score climb! 📈 (The script can be cancelled at any time with the `Esc` key)

## Demo
<img src="https://github.com/user-attachments/assets/b81d7014-fb2a-4dfd-953c-a54624e1336f" width="600" />


