import random
import re
import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords

stops = set(stopwords.words('english'))

def random_synonym(word: str) -> str:
    synonyms = set()

    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.add(l.name())
            
    if synonyms:
        return random.choice(list(synonyms)).replace("_", " ")
    else:
        return word

def shipofthesaurus(ship: str) -> str:    
    ship = re.findall(r"[\w]+|[\s]+|[^\w]", ship.strip())
    new_ship = []
    for board in ship:
        if board.isalpha() and len(board) > 1 and board not in stops:
            new_board = random_synonym(board)
            if board != new_board and board.isupper():
                new_board = new_board.upper()
            elif board != new_board and board[0].isupper():
                new_board = new_board.capitalize()
        else:
            new_board = board
        new_ship.append(new_board)
    new_ship = "".join(new_ship)
    return new_ship