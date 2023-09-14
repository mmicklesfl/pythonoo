import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    
    def __init__(self, path):
        """Initialize the WordFinder with a path to a file containing words."""
        self.words = self.read_words(path)
        print(f"{len(self.words)} words read")

    def read_words(self, path):
        """Read words from the given file and return a list of words."""
        with open(path, 'r') as file:
            words = [line.strip() for line in file]
        return words

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)
    
wf = WordFinder("words.txt")

print(wf.random())
print(wf.random())
print(wf.random())


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary, excluding comments and blank lines."""

    def read_words(self, path):
        """Read words from the given file, excluding comments and blank lines, and return a list of words."""
        with open(path, 'r') as file:
            words = [line.strip() for line in file if line.strip() and not line.startswith("#")]
        return words

swf = SpecialWordFinder("words.txt")

print(swf.random())
print(swf.random())
print(swf.random())