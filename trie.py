class Trie:
    def __init__(self) -> None:
        self.root = {}
        self.delimiter = "*"

    def contains(self, word: str) -> bool:
        pointer = self.root
        word += self.delimiter
        for char in word:
            if char not in pointer:
                return False
            pointer = pointer[char]
        return True

    def insert(self, word: str) -> None:
        if self.contains(word):
            return
        pointer = self.root
        word += self.delimiter
        for char in word:
            if char not in pointer:
                pointer[char] = {}
            pointer = pointer[char]
