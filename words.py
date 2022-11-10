""" words module which retrives and prints list of words from URL

Usage:
    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """ Fetch list of words from URL.
    
    Args:
        url:the URL of UTF-8 text document.
    
    Return:
        a list of strings containing the words from the document.

    """
    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_items(items):
    """ Prints list of words form passed colletions.
    
    Args:
        items:list of words.
    
    Return:
        a list of strings containing the words from the document.

    """
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == "__main__":
    main(sys.argv[1])  # http://sixty-north.com/c/t.txt
