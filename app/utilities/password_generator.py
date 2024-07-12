import nltk
import secrets
import string

nltk.download('words')
from nltk.corpus import words

def generate_password():
    word_list = words.words()
    word = secrets.choice(word_list)
    numbers = ''.join(secrets.choice(string.digits) for i in range(2))
    special_chars = ''.join(secrets.choice('@_*#&$_-') for i in range(2))
    password = word + numbers + special_chars
    return password